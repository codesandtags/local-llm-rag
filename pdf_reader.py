from pypdf import PdfReader

def read_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    all_text = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            all_text.append(text)
    return "\n".join(all_text)