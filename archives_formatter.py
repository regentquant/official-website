# From Newest To Oldest
import os

file_names = [i.replace('jpeg','pdf') for i in '''
Barrons_20230102.jpeg
Barrons_20230109.jpeg
Barrons_20230116.jpeg
Barrons_20230123.jpeg
Barrons_20230130.jpeg
Barrons_20230206.jpeg
Barrons_20230213.jpeg
Barrons_20230220.jpeg
Barrons_20230227.jpeg
Barrons_20230306.jpeg
Barrons_20230313.jpeg
Barrons_20230320.jpeg
Barrons_20230327.jpeg
Barrons_20230403.jpeg
Barrons_20230410.jpeg
Barrons_20230417.jpeg
Barrons_20230424.jpeg
Barrons_20230501.jpeg
Barrons_20230508.jpeg
Barrons_20230515.jpeg
Barrons_20230522.jpeg
Barrons_20230529.jpeg
Barrons_20230605.jpeg
Barrons_20230612.jpeg
Barrons_20230619.jpeg
Barrons_20230627.jpeg
Barrons_20230703.jpeg
Barrons_20230710.jpeg
Barrons_20230717.jpeg
Barrons_20230724.jpeg
Barrons_20230731.jpeg
Barrons_20230807.jpeg
Barrons_20230814.jpeg
Barrons_20230821.jpeg
Barrons_20230828.jpeg
Barrons_20230904.jpeg
Barrons_20230909.jpeg
Barrons_20230918.jpeg
Barrons_20230925.jpeg
Barrons_20231002.jpeg
Barrons_20231009.jpeg
Barrons_20231016.jpeg
'''.split('\n')[1:-1]]

files = (sorted(file_names))
files.reverse()
file_names = files

google_links = '''
https://drive.google.com/open?id=1OOVqmLFTEPqB2bka0V9rUGyNbx5d6di0&usp=drive_copy
https://drive.google.com/open?id=16PPoOcHUWzJrxJESMypArvckkEm4N-0f&usp=drive_copy
https://drive.google.com/open?id=14GDggO9BmvMV1CSDQ7FbKMDSmWEM2-l_&usp=drive_copy
https://drive.google.com/open?id=1dDCsU56j_6AhZWWyg5AXLXSK_HhFJKl6&usp=drive_copy
https://drive.google.com/open?id=1lUy-YaGhKiHkEpmUGGBNev08JvoqJz1C&usp=drive_copy
https://drive.google.com/open?id=14gkyDHwMGjcLatTl1qvqAjpg1J1KTTxY&usp=drive_copy
https://drive.google.com/open?id=1ghzmfReYfn9lxyYIDe1pn_6JfL8zK9kH&usp=drive_copy
https://drive.google.com/open?id=1Zx0oTKVfjRVTagR2aHHRMh1PXzutAEDk&usp=drive_copy
https://drive.google.com/open?id=183ww2fIUCt5PpfeGHkyQuCj-Dsr7Rmss&usp=drive_copy
https://drive.google.com/open?id=1kERCE32d8Y5BfbaU6Mh0CpejNLRN4YrA&usp=drive_copy
https://drive.google.com/open?id=1RegyXCTe7bInSyNVUtbzhKkvA7On5q-5&usp=drive_copy
https://drive.google.com/open?id=1OH5pvuMX6-ESmGpajq_FgH0cfQ74ifKu&usp=drive_copy
https://drive.google.com/open?id=1j9b-x3XEe5T7wsMQw991SJvVaKjN229h&usp=drive_copy
https://drive.google.com/open?id=1NU0RVvYZXaGGwXFiN_BqTagGIjxeqioK&usp=drive_copy
https://drive.google.com/open?id=1V1B0Z4IuJfR0hQIucsp940Gyjd6qt88M&usp=drive_copy
https://drive.google.com/open?id=1_s_K9PFB_qj3Sq7KlGU_ClyXYNIufVkt&usp=drive_copy
https://drive.google.com/open?id=19OR84vl4_GbWUj02T23qW6gGMnmDVrH1&usp=drive_copy
https://drive.google.com/open?id=1SatIUTRCEnRjZTKYgkM3E9mKxWtw1E67&usp=drive_copy
https://drive.google.com/open?id=1aHbKWqYmw8VhiQUhyO5twtb9Q4-pfwXP&usp=drive_copy
https://drive.google.com/open?id=1kH3Q1RtrsR9mHcg55qCmwWEQJZK9vwIN&usp=drive_copy
https://drive.google.com/open?id=1C2RPUxfTWWgrSBxevH47AC7FCY_ZUAkr&usp=drive_copy
https://drive.google.com/open?id=1mfuWmJcRR3MT0e0aYne3Z6rj0KZBz21u&usp=drive_copy
https://drive.google.com/open?id=1JzW2Zbl2ZGfPWj-2lVbA0faYwrGiTRG-&usp=drive_copy
https://drive.google.com/open?id=16rtl-BvRMRCc4_2svyF7Sat_zCbmdIvJ&usp=drive_copy
https://drive.google.com/open?id=1HLmQe5D3n078QV07QlamYC5O-BYpLqhR&usp=drive_copy
https://drive.google.com/open?id=18VdcjJGrDOg87Bzdi7-6HfikxaxPwlnf&usp=drive_copy
https://drive.google.com/open?id=1BszAHf_F7oKdTrBGeqa2eCH39Kkdcu0_&usp=drive_copy
https://drive.google.com/open?id=1i5dOBuV2WBOgKHpX5eVFq-MFma6APwSI&usp=drive_copy
https://drive.google.com/open?id=1-d8WBFxSo0MvOxJqBUh_VMWy56fhxEsz&usp=drive_copy
https://drive.google.com/open?id=1kCHfixub-0SIf-eg4eGAH-qsyQEmf-uD&usp=drive_copy
https://drive.google.com/open?id=1j23lKQngZVqd2Yg1_LUGvk20ifmvRJ_P&usp=drive_copy
https://drive.google.com/open?id=19jTA6wAbXBKI0P6Fi1OVfS1EjqSRJ5aL&usp=drive_copy
https://drive.google.com/open?id=14b-gVDGJDTt8HsiwI5TTYi1bpHDVkdp1&usp=drive_copy
https://drive.google.com/open?id=1nIjQnuzdSJodMZibGEVzfW1K_kVSIIYi&usp=drive_copy
https://drive.google.com/open?id=1r6nB3Qv1mmntygmgMcXYX2tTytQQbLZz&usp=drive_copy
https://drive.google.com/open?id=1C2o9eVU5JTiiN9rhG2lNykxL_P_wO7I7&usp=drive_copy
https://drive.google.com/open?id=1iawjIYFi1oPWaPekniqyce-D11sGiv6E&usp=drive_copy
https://drive.google.com/open?id=1XOkDds0B0d3DIOCQyZJIjAT_-F-3JvAg&usp=drive_copy
https://drive.google.com/open?id=1EXM4HEE2gi1N1Nx_oVwoJ_Dyf9kln0vx&usp=drive_copy
https://drive.google.com/open?id=172ECpPMhw4SgRtK7cOtEzkIkXN1zVgdn&usp=drive_copy
https://drive.google.com/open?id=1Klzos3BWRvr42BkpkA7_nd5zRgbXt5-m&usp=drive_copy
https://drive.google.com/open?id=1F8ohjwBb3Nq7Yw-QKT6i5PCARM5WEgwa&usp=drive_copy
'''.split('\n')[1:-1]

for file_name, google_link in zip(file_names, google_links):

  print(f"""
                  <!-- File Start -->
                  <div class="col-12 col-sm-6 col-md-4 col-lg-3 mb-4">
                     <div class="card">
                        <img src="Barrons_Covers/{file_name.replace('.pdf','.jpeg')}" alt="{file_name.replace('.pdf','.jpeg')}" class="card-img-top">
                        <div class="card-body text-center">
                           <h5 class="card-title">
                              The Economist<br></br>
                              <p>2023-{file_name.split('Barrons_')[1].split('.jpeg')[0][4:6]}-{file_name.split('Barrons_')[1].split('.jpeg')[0][6:8]}</p>
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
