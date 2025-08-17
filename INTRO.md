# PDF to Text Converter – Flask Web App

**PDF to Text Converter** is a lightweight Flask web application that allows users to upload PDF documents and instantly extract plain, readable text. It’s ideal for document digitization, data preprocessing or NLP tasks and is easy to deploy on any cloud platform (AWS, Azure, GCP, Railway, Render, etc.).

---

## 🔧 Key Features

- **Instant Extraction** – Upload a PDF and get the text within seconds
- **Clean and Simple UI** – Professional pastel themed user interface
- **Cloud-Friendly** – Built with Flask; runs smoothly on any free cloud hosting
- **Download Option** – Extracted text can be downloaded as a `.txt` file

---

## 💡 Real Life Applications

- Digitizing contracts, invoices, research papers or scanned PDFs
- Pre-processing documents for Machine Learning / NLP pipelines
- Building resume-parsing or chatbot systems that use PDF inputs
- Data extraction in Enterprise document automation workflows

---

## 🚀 Tech Stack

| Component | Used |
|----------|---------------------------|
| Backend  | Python + Flask            |
| PDF Parsing | PyPDF2                |
| UI       | HTML / CSS (inline)       |
| Deploy   | Compatible with AWS, GCP, Azure, Railway, Render |

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

```bash
git clone <repository-url>
cd pdf_to_text_app
Install Dependencies


pip install -r requirements.txt
Run the App


python app.py
Open your browser and go to http://localhost:5000
Upload any PDF file and the extracted text will be shown instantly.

