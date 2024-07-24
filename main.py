#first paste your pdf in PdfConverter to convert

from pdf2docx import Converter

your_pdf= input("enter your pdf to convert: ")

pdf_path = your_pdf

docx_path="output.docx"

cv = Converter(pdf_file=pdf_path)

cv.convert(docx_filename=docx_path)

cv.close()


