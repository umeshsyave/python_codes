
from PyPDF2 import PdfMerger
import sys

inputs=sys.argv[1:]

merger = PdfMerger()

for pdf in inputs:
	merger.append(pdf)

merger.write("cert.pdf")
merger.close()
print('process executed')

