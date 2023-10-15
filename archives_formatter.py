# From Newest To Oldest
import os

file_names = '''
Barrons_20231016.pdf
Barrons_20230102.pdf
Barrons_20230109.pdf
Barrons_20230116.pdf
Barrons_20230123.pdf
Barrons_20230130.pdf
Barrons_20230206.pdf
Barrons_20230213.pdf
Barrons_20230220.pdf
Barrons_20230227.pdf
Barrons_20230306.pdf
Barrons_20230313.pdf
Barrons_20230320.pdf
Barrons_20230327.pdf
Barrons_20230403.pdf
Barrons_20230410.pdf
Barrons_20230417.pdf
Barrons_20230424.pdf
Barrons_20230501.pdf
Barrons_20230508.pdf
Barrons_20230515.pdf
Barrons_20230522.pdf
Barrons_20230529.pdf
Barrons_20230605.pdf
Barrons_20230612.pdf
Barrons_20230619.pdf
Barrons_20230627.pdf
Barrons_20230703.pdf
Barrons_20230710.pdf
Barrons_20230717.pdf
Barrons_20230724.pdf
Barrons_20230731.pdf
Barrons_20230807.pdf
Barrons_20230814.pdf
Barrons_20230821.pdf
Barrons_20230828.pdf
Barrons_20230904.pdf
Barrons_20230909.pdf
Barrons_20230918.pdf
Barrons_20230925.pdf
Barrons_20231002.pdf
Barrons_20231009.pdf
'''.split('\n')[1:-1]

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

number = 1

for file_name, google_link in zip(file_names, google_links):

	print(f"""
<!-- File {number} -->
<div class="col-12 col-sm-6 col-md-4 col-lg-3 mb-4">
    <div class="card">
        <img src="Barrons_Covers/{file_name.replace('.pdf','.jpeg')}" alt="{file_name.replace('.pdf','.jpeg')}" class="card-img-top">
        <div class="card-body text-center">
            <h5 class="card-title">{file_name.replace('.pdf','').replace('Barrons_',"Barron's ")}</h5>
            <a href="{google_link}" class="btn btn-primary" style="margin-top: 10px; margin-bottom: -1px; background: black; border-width: 0px">Download</a>
        </div>
    </div>
</div>
""")
	number = number + 1
