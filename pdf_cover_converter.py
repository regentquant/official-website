import os
from pdf2image import convert_from_path

def convert_pdf_to_img(folder_path, output_folder):
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)
            images = convert_from_path(pdf_path, first_page=0, last_page=1)
            for i, image in enumerate(images):
                image.save(os.path.join(output_folder, f'{filename[:-4]}.png'), 'PNG')

# Example usage:
folder_path = '/Users/curryyao/Library/Mobile Documents/com~apple~CloudDocs/Regent Quant/metadata_pdf'
output_folder = '/Users/curryyao/Library/Mobile Documents/com~apple~CloudDocs/Git/official-website/Bloomberg_Businessweek_Covers'
convert_pdf_to_img(folder_path, output_folder)
