# PDF to Text Converter – Flask Web App

**PDF to Text Converter** is a lightweight Flask web application that allows users to upload PDF documents and instantly extract clean, readable text. It also generates a concise TextRank-based summary of the extracted content. This tool is ideal for document digitization, data preprocessing or NLP tasks and is easy to deploy on any cloud platform (AWS, Azure, GCP, Railway, Render, etc.).

---

## 🔧 Key Features

- **Instant Extraction** – Upload a PDF and get the full text within seconds  
- **Text Summarization** – Generates a short summary (TextRank-based) of the extracted content  
- **Clean & Modern UI** – Professional pastel themed interface with minimalist design  
- **Download Option** – Extracted text can be downloaded as a `.txt` file  
- **Cloud-Friendly** – Built with Flask; runs smoothly on any free cloud hosting

---

## 💡 Real Life Applications

- Digitizing contracts, invoices, research papers or scanned PDFs
- Pre-processing documents for Machine Learning / NLP pipelines
- Building resume-parsing or chatbot systems that use PDF inputs
- Data extraction in Enterprise document automation workflows

---

## 🚀 Tech Stack

| Component     | Used                         |
|---------------|------------------------------|
| Backend       | Python + Flask               |
| PDF Parsing   | PyPDF2                       |
| Summarization | Sumy / TextRank              |
| UI            | HTML / CSS (inline)          |
| Deploy        | AWS / GCP / Azure / Railway / Render |

---
## 📂 Project Structure

pdf_to_text_app/
│
├── app.py
├── requirements.txt
├── templates/
│ └── index.html
└── static/
└── (optional for CSS or logo)

## ⚙️ Installation & Usage

1. **Clone the Repository**


git clone <repository-url>
cd pdf_to_text_app
Install Dependencies

2. **Install Dependencies**
pip install -r requirements.txt
pip install sumy numpy

3. **Run the App**
python app.py

4. Open your browser and go to http://localhost:5000
Upload any PDF file to view the full extracted text and its short summary.
