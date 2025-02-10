import google.generativeai as genai
from bs4 import BeautifulSoup

# Read Gemini API key from the text file
def get_gemini_api_key():
    try:
        with open("api.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        raise Exception("API key file not found. Please ensure 'api.txt' exists and contains the key.")

# Set the Gemini API key
genai.configure(api_key=get_gemini_api_key())

template = (
    "You are an AI assistant tasked with simplifying educational content. "
    "The user is asking: {parse_description}. "
    "Based on the educational link content: {dom_content}, follow these instructions:\n\n"
    "1. **Focus on the User's Need:** Answer their question simply and clearly. "
    "2. **Use Very Simple Words:** Make sure everyone can understand. "
    "3. **Explain in Steps:** Break your answer into easy-to-follow points. "
    "4. **Give Examples:** Show examples to help them understand better. "
    "5. **Avoid Complex Ideas:** Skip details that make it hard to follow. "
    "6. **Be Short and Clear:** Write each point in one short sentence."
)


def extract_code_from_dom(dom_content):
    """
    Extract code snippets from the DOM content using BeautifulSoup.
    Assumes that code blocks are inside <code> or <pre> tags.
    """
    soup = BeautifulSoup(dom_content, 'html.parser')
    
    # Find all code blocks in the DOM
    code_blocks = soup.find_all(['code', 'pre'])
    
    # Return the code content as a string
    return "\n".join([block.get_text() for block in code_blocks])

def parse_with_gemini(dom_chunks, parse_description):
    if not dom_chunks:
        return "Error: No content to process. Please provide valid DOM chunks."
    
    # Combine all dom_chunks into a single string for one-batch processing
    combined_content = " ".join(dom_chunks).strip()
    if not combined_content:
        return "Error: Combined content is empty. Please check the input data."
    
    # If the query contains "code", extract code content from the DOM
    if 'code' in parse_description.lower() or 'example' in parse_description.lower() or 'syntax' in parse_description.lower():
        extracted_code = extract_code_from_dom(combined_content)
        if extracted_code:
            combined_content = extracted_code  # Focus only on the code content
    
    # Format the single prompt with the combined content
    prompt = template.format(dom_content=combined_content, parse_description=parse_description)
    
    try:
        # Request content generation from Gemini model
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        
        # Extract and return the simplified text
        simplified_text = response.text.strip()
        
        # Check if the model returned a relevance warning
        if "out of topic" in simplified_text.lower():
            print("Warning: The query is unrelated to the content provided.")
        
        print("Parsed the entire content as one batch.")
        return simplified_text

    except Exception as e:
        print(f"Error processing content: {e}")
        return "Error occurred while processing the content."
