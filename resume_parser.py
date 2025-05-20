# copyright [2025] [Phat Nguyen Cong] (Github: https://github.com/paht2005)

import fitz  # PyMuPDF

def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    return "\n".join([page.get_text() for page in doc])
