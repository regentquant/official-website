import pyperclip

d = pyperclip.paste().split('\n')
d = [i.replace('\r','') for i in d]
s=''
for i in d:
  s = f"{s}{i},"

print(s)
