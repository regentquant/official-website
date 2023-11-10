from PIL import Image
import pytesseract

# Load the image from file
img_path = 'Screenshot 2023-11-09 at 12.15.16 AM.png'
img = Image.open(img_path)

# Use tesseract to do OCR on the image
text = pytesseract.image_to_string(img)
text_list = text.split('\n\n')

lenth = len(text_list)
interval = 9

date_list = text_list[:int(interval)]
change = text_list[int(interval): int(interval*2)]
a = text_list[int(interval*2):int(interval*3)]
b = text_list[int(interval*3):int(interval*4)]
c = text_list[int(interval*4):int(interval*5)]
d = text_list[int(interval*5):int(interval*6)]
e = text_list[int(interval*6):int(interval*7)]

for z,zz,zzz,zzzz,zzzzz in zip(a,b,c,d,e):
  print(f"{z}\t{zz}\t{zzz}\t{zzzz}\t{zzzzz}")
