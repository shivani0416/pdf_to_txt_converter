from flask import Flask, render_template, request
import PyPDF2

# Summarization
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

app = Flask(__name__)

def summarize_text(text, sentence_count=5):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, sentence_count)
    return " ".join(str(sentence) for sentence in summary)

@app.route("/", methods=["GET", "POST"])
def index():
    extracted_text = ""
    summary = ""
    if request.method == "POST":
        pdf_file = request.files["file"]
        reader = PyPDF2.PdfReader(pdf_file)
        for page in reader.pages:
            extracted_text += page.extract_text()

        # summarize the extracted text
        summary = summarize_text(extracted_text, sentence_count=5)

    return render_template("index.html", extracted_text=extracted_text, summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
