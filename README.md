# EduSimplify

EduSimplify is a **Streamlit-based web application** designed to simplify educational content. It scrapes website data, extracts meaningful text, and processes it using the **Gemini API** to provide easy-to-understand summaries.

## 🚀 Features
- **Web Scraping**: Extracts content from a given website URL.
- **Content Cleaning**: Removes unnecessary HTML elements.
- **AI-Based Parsing**: Uses Gemini API to simplify and explain content.
- **Interactive UI**: Built with Streamlit for seamless user experience.
- **Expandable Content View**: Allows users to inspect raw extracted content.

---

## 🛠 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/EduSimplify.git
cd EduSimplify
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application
```bash
streamlit run app.py
```

---

## 📝 Usage

### 1️⃣ Scrape Website Content
- Enter the **website URL** in the input field.
- Click **"Scrape Website"** to extract content.
- View the **DOM Content** in the expander.

### 2️⃣ Parse the Content
- Enter a **description of what you want to parse**.
- Click **"Parse Content"** to process it using the **Gemini API**.
- View the **simplified output**.

---

## 💂️ Project Structure
```
EduSimplify/
│── scrape.py          # Web scraping & content extraction
│── parse.py           # Parsing logic with Gemini API
│── app.py             # Streamlit application
│── requirements.txt   # Required Python libraries
│── README.md          # Project Documentation
```

---

## 🔧 Future Improvements
- **OCR Integration**: Extracting text from images and flowcharts.
- **Real-time Chatbot**: Interactive Q&A based on scraped content.
- **Multilingual Support**: Content summarization in multiple languages.

---

## 🏆 Credits
Developed using **Python, Streamlit, and Gemini API**.

---

## 🐟 License
This project is licensed under the **MIT License**.
