import pyperclip
from PIL import Image
import pytesseract

# Load the image from file
img_path = 'IMG_FFB1FE9CC995-1.jpeg'
img = Image.open(img_path)

# Use tesseract to do OCR on the image
text = pytesseract.image_to_string(img)
text_list = text.split('\n\n')

lenth = len(text_list)
interval = 11

date_list = text_list[:int(interval)]
change = text_list[int(interval): int(interval*2)]
a = text_list[int(interval*2):int(interval*3)]
b = text_list[int(interval*3):int(interval*4)]
c = text_list[int(interval*4):int(interval*5)]
d = text_list[int(interval*5):int(interval*6)]
e = text_list[int(interval*6):int(interval*7)]
a.reverse()
b.reverse()
c.reverse()
d.reverse()
e.reverse()

for z,zz,zzz,zzzz,zzzzz in zip(a,b,c,d,e):
  print(f"{z}\t{zz}\t{zzz}\t{zzzz}\t{zzzzz}")

print(f"")

fs = ''

for i in e:
  if "B" in i:
    i = i.replace("I","")
    if "+" in i:
      string = (int(float(i.replace("B","").replace("+",""))*1000000000))
      fs = f"{fs}{string}\n"
    elif "-" in i:
      string = (int(float(i.replace("B","").replace("-",""))*-1000000000))
      fs = f"{fs}{string}\n"

  elif "M" in i:
    i = i.replace("I","")
    if "+" in i:
      string = (int(float(i.replace("M", "").replace("+", "")) * 1000000))
      fs = f"{fs}{string}\n"

    elif "-" in i:
      string = (int(float(i.replace("M", "").replace("-", "")) * -1000000))
      fs = f"{fs}{string}\n"


  elif "K" in i:
    i = i.replace("I","")
    if "+" in i:
      string = (int(float(i.replace("K", "").replace("+", "")) * 1000))
      fs = f"{fs}{string}\n"

    elif "-" in i:
      string = (int(float(i.replace("K", "").replace("-", "")) * -1000))
      fs = f"{fs}{string}\n"


  else:
    print(i)

pyperclip.copy(fs)

print(fs)
