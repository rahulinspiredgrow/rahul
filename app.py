from flask import Flask, render_template, request, send_file
import os
from utils.pdf_extract import extract_text_from_pdf
from utils.translate import translate_hindi_to_english
from utils.summarize import summarize_text
from utils.pdf_generate import generate_pdf

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['pdf_file']
        if file.filename.endswith('.pdf'):
            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)

            hindi_text = extract_text_from_pdf(path)
            english_text = translate_hindi_to_english(hindi_text)

            hindi_summary = summarize_text(hindi_text, lang='hi')
            english_summary = summarize_text(english_text, lang='en')

            output_pdf_path = os.path.join(OUTPUT_FOLDER, 'translated_output.pdf')
            generate_pdf(hindi_text, english_text, output_pdf_path)

            return render_template('result.html',
                                   hindi=hindi_text,
                                   english=english_text,
                                   hin_summary=hindi_summary,
                                   eng_summary=english_summary,
                                   pdf_link='/download')
    return render_template('index.html')

@app.route('/download')
def download_pdf():
    return send_file('outputs/translated_output.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
