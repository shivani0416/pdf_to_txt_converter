from flask import Flask, render_template, request
import PyPDF2

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    extracted_text = ""
    if request.method == "POST":
        if "file" not in request.files:
            return "No file part in request"
        pdf_file = request.files["file"]
        if pdf_file.filename == "":
            return "No selected file"

        reader = PyPDF2.PdfReader(pdf_file)
        for page in reader.pages:
            extracted_text += page.extract_text()

    return render_template("index.html", extracted_text=extracted_text)

if __name__ == "__main__":
    app.run(debug=True)
