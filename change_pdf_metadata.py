from PyPDF2 import PdfReader, PdfWriter
import os

a = '知识星球搜索丽晶财经：https://t.zsxq.com/05MzFAuji'
b = 'www.regentquant.com'
metadata = b


directory = '/Users/curryyao/Downloads/metadata_change'

for file in os.listdir(directory):
	if file.endswith(".pdf"):  # Ensure the file is a PDF before processing
		original_file_path = os.path.join(directory, file)
		temp_file_path = os.path.join(directory, "temp.pdf")

		reader = PdfReader(original_file_path)  # Open the PDF file
		writer = PdfWriter()

		for page in reader.pages:  # Copy all pages from the original PDF to the new one
			writer.add_page(page)

		writer.add_metadata({
			'/Title': metadata,
			'/Author': metadata,
			'/Subject': metadata,
		})

		with open(temp_file_path, 'wb') as f:
			writer.write(f)  # Write the modified PDF to a temporary file

		os.remove(original_file_path)  # Delete the original file
		os.rename(temp_file_path, original_file_path)  # Rename the temporary file to the original file name


