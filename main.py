import streamlit as st
from scrape import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom_content,
)
from parse import parse_with_gemini  # Updated import to use Gemini API

# Streamlit UI
st.title("EduSimplify")
url = st.text_input("Enter Website URL")

# Initialize session state variables
if "dom_content" not in st.session_state:
    st.session_state.dom_content = None
if "parsing_status" not in st.session_state:
    st.session_state.parsing_status = "idle"  # idle, in_progress, completed, failed
if "parsing_result" not in st.session_state:
    st.session_state.parsing_result = None
if "error_message" not in st.session_state:
    st.session_state.error_message = None

# Step 1: Scrape the Website
if st.button("Scrape Website"):
    if url:
        st.write("Scraping the website...")

        # Scrape the website
        try:
            dom_content = scrape_website(url)
            body_content = extract_body_content(dom_content)
            cleaned_content = clean_body_content(body_content)

            # Store the DOM content in session state
            st.session_state.dom_content = cleaned_content

            # Reset parsing status after new content is scraped
            st.session_state.parsing_status = "idle"

            # Display the DOM content
            with st.expander("View DOM Content"):
                st.text_area("DOM Content", cleaned_content, height=300)

        except Exception as e:
            st.error(f"Failed to scrape the website: {str(e)}")

# Step 2: Parse the DOM Content
if st.session_state.dom_content:
    parse_description = st.text_area("Describe what you want to parse")

    if st.button("Parse Content"):
        if parse_description:
            # Set parsing in progress
            st.session_state.parsing_status = "in_progress"
            st.session_state.parsing_result = None  # Clear previous results
            st.session_state.error_message = None  # Clear previous errors

            # Parse the content
            try:
                dom_chunks = split_dom_content(st.session_state.dom_content)
                parsed_result = parse_with_gemini(dom_chunks, parse_description)

                # Update session state
                st.session_state.parsing_result = parsed_result
                st.session_state.parsing_status = "completed"
            except Exception as e:
                st.session_state.parsing_status = "failed"
                st.session_state.error_message = str(e)

    # Display feedback based on parsing status
    if st.session_state.parsing_status == "in_progress":
        st.info("Parsing the content... Please wait.")
    elif st.session_state.parsing_status == "completed":
        st.success("Parsing completed!")
        st.write(st.session_state.parsing_result)
    elif st.session_state.parsing_status == "failed":
        st.error(f"Parsing failed: {st.session_state.error_message}")
