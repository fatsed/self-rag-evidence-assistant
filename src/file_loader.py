from pypdf import PdfReader
from docx import Document

def read_txt_file(uploaded_file):
    """
    Read text from an uploaded file.
    """
    return uploaded_file.read().decode('utf-8')

def read_pdf_file(uploaded_file):
    """
    Read text from an uploaded PDF file.
    """
    reader = PdfReader(uploaded_file)

    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + '\n'
    return text

def read_docx_file(uploaded_file):
    """
    Read text from an uploaded docx file.
    """
    document = Document(uploaded_file)
    text = ""

    for para in document.paragraphs:
        if para.text.strip():
            text += para.text + '\n'
    return text

def load_uploaded_files(uploaded_files):
    """
    Load text from multiple uploaded files.
    Supports PDF, TXT, and DOCX files.
    """
    documents = []

    for uploaded_file in uploaded_files:
        file_name = uploaded_file.name.lower()
        if file_name.endswith('.pdf'):
            text = read_pdf_file(uploaded_file)
        elif file_name.endswith('.docx'):
            text = read_docx_file(uploaded_file)
        elif file_name.endswith('.txt'):
            text = read_txt_file(uploaded_file)
        else:
            continue

        documents.append({
            'file_name': file_name,
            'text': text
        })
    return documents