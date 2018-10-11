import PyPDF2

pdf = 'EN-FINAL Table 9.pdf'

pdfFileObj = open(pdf, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(0)

print (pdfReader.numPages)
print (pageObj.extractText().encode('utf-8'))

print type(pageObj.extractText())



