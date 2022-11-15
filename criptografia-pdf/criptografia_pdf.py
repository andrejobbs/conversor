from PyPDF2 import PdfFileWriter, PdfFileReader 

arquivo = PdfFileReader("285173966-aprendendo-python-pdf.pdf")
gravar=PdfFileWriter() 
for page in gravar.pages:
    gravar.add_page(page)

gravar.encrypt('ricardo007')

with open('arquivo-encriptado.pdf','wb') as e:
    gravar.write(e)
