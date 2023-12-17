import os

container = []
for file in os.listdir("../Daily Short Sale Volume"):
    if ".html" in file:
        container.append(file)

container.sort()

for i in container:
    print(f'<div class="daily-short-sale-volume-container"><a href="Daily%20Short%20Sale%20Volume/STOCK/{i.replace(" ","%20")}" class="rectangle-fill"><img src="LOGO/STOCKS/{i.split(" Daily")[0]}.svg" alt="{i.split(" Daily")[0]} logo">{i.split(" Daily")[0]}</a><br></div>')