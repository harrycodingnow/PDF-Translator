import tkinter as tk
from tkinter import filedialog, messagebox
import os
from pdf2docx import Converter
from docx import Document
import openai
from translator import PDFTranslator
from converter import PDF2DOCX

def save_API():
    global APIkey
    APIkey = openaiAPI.get()
    print(APIkey)

def select_pdf():
    pdf2docx = PDF2DOCX()
    docx_file = pdf2docx.pdf2docx(filedialog, pdf_path_var)
    if docx_file:
        pdf_translator = PDFTranslator(APIkey)
        translated_docx_file = os.path.splitext(docx_file)[0] + ".docx"
        pdf_translator.translate_document(docx_file, translated_docx_file)
        translated_pdf_file = pdf2docx.docx2pdf(translated_docx_file)
        messagebox.showinfo("Success", f"Translated document saved as {translated_pdf_file}")

 
        


def open_file():
    docx_file = select_pdf()
    os.system(f'start {docx_file}')

def exit():
    root.destroy()


# Setting up the GUI
root = tk.Tk()
root.title("PDF Translator")

openaiAPI = tk.StringVar()
pdf_path_var = tk.StringVar()
save_path_var = tk.StringVar()

tk.Label(root, text="Enter your openai API: ").grid(row=0, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=openaiAPI, width=50).grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Enter", command=save_API).grid(row=0, column=2, padx=10, pady=5)

tk.Label(root, text="Select PDF File:").grid(row=1, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=pdf_path_var, width=50).grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=select_pdf).grid(row=1, column=2, padx=10, pady=5)

tk.Button(root, text="Exit", command=exit).grid(row=1, column=3, padx=10, pady=5)

root.mainloop()

