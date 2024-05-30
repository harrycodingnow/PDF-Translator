from pdf2docx import Converter
from docx2pdf import convert
import spire.doc
from spire.doc.common import *
import os

class PDF2DOCX:

    def __init__(self):
        self.pdf_file_path = None
        self.docx_file = None

    def pdf2docx(self, filedialog, pdf_path_var):
        pdf_file_path = filedialog.askopenfilename(
            title="Select PDF File",
            filetypes=[("PDF Files", "*.pdf")]
        )
        self.pdf_file_path = pdf_file_path
        pdf_path_var.set(pdf_file_path)
        docx_file = os.path.splitext(pdf_file_path)[0] + "_translated" + ".docx"
        cv = Converter(pdf_file_path)
        cv.convert(docx_file)
        cv.close()
        self.docx_file = docx_file
        return docx_file
    
    def docx2pdf(self, translated_docx_file):
        translated_pdf_file = os.path.splitext(translated_docx_file)[0] + ".pdf"
        convert(translated_docx_file, translated_pdf_file)
        return translated_pdf_file
    


