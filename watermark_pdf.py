import PyPDF2

data=PyPDF2.PdfReader('result.pdf')

wtrmark=PyPDF2.PdfReader('wtr.pdf')

output=PyPDF2.PdfWriter('')

for num in range(len(data.pages)):
	page=data.pages[num]
	page.merge_page(wtrmark.pages[0])
	output.add_page(page)
output.write('new_pdf.pdf')
print('process executed')
