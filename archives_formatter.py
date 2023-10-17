# From Newest To Oldest
import os

file_names = [i.replace('jpeg','pdf') for i in '''
Bloomberg_Businessweek_20230109.jpeg
Bloomberg_Businessweek_20230116.jpeg
Bloomberg_Businessweek_20230123.jpeg
Bloomberg_Businessweek_20230130.jpeg
Bloomberg_Businessweek_20230206.jpeg
Bloomberg_Businessweek_20230213.jpeg
Bloomberg_Businessweek_20230220.jpeg
Bloomberg_Businessweek_20230306.jpeg
Bloomberg_Businessweek_20230313.jpeg
Bloomberg_Businessweek_20230320.jpeg
Bloomberg_Businessweek_20230403.jpeg
Bloomberg_Businessweek_20230410.jpeg
Bloomberg_Businessweek_20230424.jpeg
Bloomberg_Businessweek_20230501.jpeg
Bloomberg_Businessweek_20230508.jpeg
Bloomberg_Businessweek_20230522.jpeg
Bloomberg_Businessweek_20230529.jpeg
Bloomberg_Businessweek_20230612.jpeg
Bloomberg_Businessweek_20230619.jpeg
Bloomberg_Businessweek_20230626.jpeg
Bloomberg_Businessweek_20230703.jpeg
Bloomberg_Businessweek_20230717.jpeg
Bloomberg_Businessweek_20230807.jpeg
Bloomberg_Businessweek_20230821.jpeg
Bloomberg_Businessweek_20230828.jpeg
Bloomberg_Businessweek_20230904.jpeg
Bloomberg_Businessweek_20230918.jpeg
Bloomberg_Businessweek_20231009.jpeg
Bloomberg_Businessweek_20231016.jpeg
'''.split('\n')[1:-1]]

files = (sorted(file_names))
files.reverse()
file_names = files

google_links = '''
https://drive.google.com/open?id=12qSPYMPLSVxYjmlTSiXkvJDLZbvkUC_F&usp=drive_copy
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

for file_name, google_link in zip(file_names, google_links):

  print(f"""
                  <!-- File Start -->
                  <div class="col-12 col-sm-6 col-md-4 col-lg-3 mb-4">
                     <div class="card">
                        <img src="Bloomberg_Businessweek_Covers/{file_name.replace('.pdf','.jpeg')}" alt="{file_name.replace('.pdf','.jpeg')}" class="card-img-top">
                        <div class="card-body text-center">
                           <h5 class="card-title">
                              Bloomberg Businessweek<br></br>
                              <p>2023-{file_name.split('week_')[1].split('.jpeg')[0][4:6]}-{file_name.split('week_')[1].split('.jpeg')[0][6:8]}</p>
                           </h5>
                           <a href="{google_link}" class="btn btn-primary" style="margin-top: 10px; margin-bottom: -1px; background: black; border-width: 0px; background: white; color: #333333; border-width: 1px; border-color: #333333">
                              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-book" viewBox="0 0 16 16">
                                 <path d="M1 2.828c.885-.37 2.154-.769 3.388-.893 1.33-.134 2.458.063 3.112.752v9.746c-.935-.53-2.12-.603-3.213-.493-1.18.12-2.37.461-3.287.811V2.828zm7.5-.141c.654-.689 1.782-.886 3.112-.752 1.234.124 2.503.523 3.388.893v9.923c-.918-.35-2.107-.692-3.287-.81-1.094-.111-2.278-.039-3.213.492V2.687zM8 1.783C7.015.936 5.587.81 4.287.94c-1.514.153-3.042.672-3.994 1.105A.5.5 0 0 0 0 2.5v11a.5.5 0 0 0 .707.455c.882-.4 2.303-.881 3.68-1.02 1.409-.142 2.59.087 3.223.877a.5.5 0 0 0 .78 0c.633-.79 1.814-1.019 3.222-.877 1.378.139 2.8.62 3.681 1.02A.5.5 0 0 0 16 13.5v-11a.5.5 0 0 0-.293-.455c-.952-.433-2.48-.952-3.994-1.105C10.413.809 8.985.936 8 1.783z"/>
                              </svg>
                              Preview
                           </a>
                           <br>
                           <a href="{google_link.replace('open?','uc?export=download&')}" class="btn btn-primary" style="margin-top: 10px; margin-bottom: -1px; background: black; border-width: 0px">
                              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-download" viewBox="0 0 16 16">
                                 <path d="M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5z"/>
                                 <path d="M7.646 11.854a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293V1.5a.5.5 0 0 0-1 0v8.793L5.354 8.146a.5.5 0 1 0-.708.708l3 3z"/>
                              </svg>
                              Download
                           </a>
                        </div>
                     </div>
                  </div>
                  <!-- File End -->
""".replace('btn-primary', 'btn-dark'))
