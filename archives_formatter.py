# From Newest To Oldest
import os

file_names = '''
Bloomberg_Businessweek_20230123.pdf
Bloomberg_Businessweek_20230109.pdf
Bloomberg_Businessweek_20230116.pdf
Bloomberg_Businessweek_20230130.pdf
Bloomberg_Businessweek_20230206.pdf
Bloomberg_Businessweek_20230213.pdf
Bloomberg_Businessweek_20230220.pdf
Bloomberg_Businessweek_20230306.pdf
Bloomberg_Businessweek_20230313.pdf
Bloomberg_Businessweek_20230320.pdf
Bloomberg_Businessweek_20230403.pdf
Bloomberg_Businessweek_20230410.pdf
Bloomberg_Businessweek_20230424.pdf
Bloomberg_Businessweek_20230501.pdf
Bloomberg_Businessweek_20230508.pdf
Bloomberg_Businessweek_20230522.pdf
Bloomberg_Businessweek_20230529.pdf
Bloomberg_Businessweek_20230612.pdf
Bloomberg_Businessweek_20230619.pdf
Bloomberg_Businessweek_20230626.pdf
Bloomberg_Businessweek_20230703.pdf
Bloomberg_Businessweek_20230717.pdf
Bloomberg_Businessweek_20230807.pdf
Bloomberg_Businessweek_20230821.pdf
Bloomberg_Businessweek_20230828.pdf
Bloomberg_Businessweek_20230904.pdf
Bloomberg_Businessweek_20230918.pdf
Bloomberg_Businessweek_20231009.pdf
'''.split('\n')[1:-1]

files = (sorted(file_names))
files.reverse()
file_names = files

google_links = '''
https://drive.google.com/open?id=1ifH7Cy13zWuYNbCtHE71CJWYFzYACE20&usp=drive_copy
https://drive.google.com/open?id=1Do1FMZ6GpQ6VJclCpH4PljnnLV7fdpLf&usp=drive_copy
https://drive.google.com/open?id=144wDPqhlDa9q2ikVFnq8qih9J7ePu5hc&usp=drive_copy
https://drive.google.com/open?id=1HzccO5tSLa-IdHg7PoT0gCIb2N7P4VPW&usp=drive_copy
https://drive.google.com/open?id=1tl8kDFBC6-ekheUrbImsUlfH0wVz9u_2&usp=drive_copy
https://drive.google.com/open?id=1_tP2aI__PRAj_M0joo8-6eOFKsV6Zw3k&usp=drive_copy
https://drive.google.com/open?id=1VNvRWTUtq22F99gsm6WWMWSPmebur4Kw&usp=drive_copy
https://drive.google.com/open?id=16DoKKFulE0O3_XwtQnQhDyzkOjsVJmfo&usp=drive_copy
https://drive.google.com/open?id=1F82rLJAugXvGKComa51Tlvv0xPrO9KbW&usp=drive_copy
https://drive.google.com/open?id=1U1JbZu6tnDrXZ76e41tNL4bxQOIwVkEP&usp=drive_copy
https://drive.google.com/open?id=1yxvUSVHAG-eAPNKheimIUIcE5acFCrrq&usp=drive_copy
https://drive.google.com/open?id=1wolf__9K6e3j6lHBzqq8ySauewEfYqVn&usp=drive_copy
https://drive.google.com/open?id=1-WRxmgAqhwpx-3Da1nxs3qzL9BCwNgk1&usp=drive_copy
https://drive.google.com/open?id=1K-EnufNVRitaYk8xZZROaGtLxch1-fCC&usp=drive_copy
https://drive.google.com/open?id=1Irb8NEZfRVqDrFZnBDcGIsN37L3bFcbN&usp=drive_copy
https://drive.google.com/open?id=12_gw7__JN5ttki3rmP_HcJM-Fg7ztizs&usp=drive_copy
https://drive.google.com/open?id=1oqodBbtQulBU8dwqUuNIqSOcmIznZ41f&usp=drive_copy
https://drive.google.com/open?id=1yVICgwKO2BJ2qZQmYICeU1pBmG04AHVW&usp=drive_copy
https://drive.google.com/open?id=1GZgIwPuWtHbsQj7IjfbglOajNj6_W2oA&usp=drive_copy
https://drive.google.com/open?id=1xb5odJwil93zJXeXaDRqBlRNAtYgdqlv&usp=drive_copy
https://drive.google.com/open?id=1ngL3WDQbzlxNf8ZaAv9Gzm3G4vAXoV-4&usp=drive_copy
https://drive.google.com/open?id=1_zqR38BVhSoOJckNEUTU4a7gfholaGyX&usp=drive_copy
https://drive.google.com/open?id=1x7HMJxwckbUuD1D6zbxW66cBDLMNb8d5&usp=drive_copy
https://drive.google.com/open?id=1F-R0GVGSvpLuGsTL1gaY4f89SgSp_I72&usp=drive_copy
https://drive.google.com/open?id=12ArMCcK5--k5OHiMqlF3U1fWhEqcdIap&usp=drive_copy
https://drive.google.com/open?id=1539xOPyUj7S4gaHvs1tak_PQf7Kq7Pqd&usp=drive_copy
https://drive.google.com/open?id=1C0nEu13Q3M5VwyzbaNRMrWjNe6yPr0Gp&usp=drive_copy
https://drive.google.com/open?id=19oqifYIjUpwcvXmbJ4ge48u07yqEIUkY&usp=drive_copy
'''.split('\n')[1:-1]

number = 1

for file_name, google_link in zip(file_names, google_links):

	print(f"""
<!-- File {number} -->
<div class="col-12 col-sm-6 col-md-4 col-lg-3 mb-4">
    <div class="card">
        <img src="Bloomberg_Businessweek_Covers/{file_name.replace('.pdf','.jpeg')}" alt="{file_name.replace('.pdf','.jpeg')}" class="card-img-top">
        <div class="card-body text-center">
            <h5 class="card-title">{file_name.replace('.pdf','').replace('Bloomberg_Businessweek_',"Bloomberg Businessweek ")}</h5>
            <a href="{google_link}" class="btn btn-primary" style="margin-top: 10px; margin-bottom: -1px; background: black; border-width: 0px">Download</a>
        </div>
    </div>
</div>
""")
	number = number + 1
