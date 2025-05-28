# Importing modules to read '.docx', '.txt' and '.pdf' files

import PyPDF2 # Actually, this is installed but not used in this script, just for reference purpose only
import docx
import pdfplumber

# This function reads the '.pdf' file using pdfplumber
# This takes the file-path as an argument
def read_pdf(file_path):
    """Reads text from a PDF file."""
    
    # Opens the pdf with pdfplumber by using path
    with pdfplumber.open(file_path) as pdf:
        # initializes an empty text variable to store string
        text = ""
        # It loops over through the pdf and extracts the text and appends to empty string variable 'text', and returns it.
        for page in pdf.pages:
            text += page.extract_text()
    return text

# This function reads the '.docx' file using docx 
# This takes the file-path as an argument
def read_docx(file_path):
    """Reads text from a DOCX file."""
    # Opens the pdf with docx by using path
    doc = docx.Document(file_path)
    # initializes an empty text variable to store string
    text = ""
    # It loops over through the pdf and extracts the text and appends to empty string variable 'text', and returns it.
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

# This function reads the '.txt' file in read mode with utf-8 encoding (UTF-8 is a character encoding standard used to represent Unicode 
# characters using one to four bytes)
# This takes the file-path as an argument
def read_txt(file_path):
    """Reads text from a TXT file."""
    # This reads entire contents of text file into a empty 'text' variable and returns it. 
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text
