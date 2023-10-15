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

google_links = '''
https://drive.google.com/open?id=1lanxC42yShAgosW9_qCnWnEIomfrAxrC&usp=drive_copy
https://drive.google.com/open?id=1mvslFTJwvFXoN-w035GWgeCYMkfFci_J&usp=drive_copy
https://drive.google.com/open?id=1JBBi6eAa7C63d0yLTuJEyzk5oMtqsdmD&usp=drive_copy
https://drive.google.com/open?id=1tENblBq8idVqMOn9if3-Lk0Cn5agwxDd&usp=drive_copy
https://drive.google.com/open?id=1mjzfsdDsYHm-M5jQ42xu4MYMhSMkJ-T9&usp=drive_copy
https://drive.google.com/open?id=1qM3RgO8-KXD4_v-WGMT5GoMYjf8zxczY&usp=drive_copy
https://drive.google.com/open?id=1LdoRU6i24hoJG7--JNZtMfyfjuQ5hXwV&usp=drive_copy
https://drive.google.com/open?id=1NcEGdkr5bPDVMBJQDK4BhMiR6xWiFvg6&usp=drive_copy
https://drive.google.com/open?id=12ZJ4XgJZvw7ovYFKsLwGj9o8XcGilgbi&usp=drive_copy
https://drive.google.com/open?id=1jr-WuJ5Qk3Ccj4B8Isx9t-snDH3hwmhl&usp=drive_copy
https://drive.google.com/open?id=1Z07Nh52AGB00kD3Jo2UeWd0uEGkJsxqJ&usp=drive_copy
https://drive.google.com/open?id=1SLWAVMG7TDgJh2Glr6zNPeTvUDL-7sc9&usp=drive_copy
https://drive.google.com/open?id=1797BRm-VlqA9bPyEiOQLxWm9I7DApBtG&usp=drive_copy
https://drive.google.com/open?id=1BNHO-RAoFcOvq5WHiizQNBy5xElhhAEY&usp=drive_copy
https://drive.google.com/open?id=1K8dPRq0HdhuvuGA4gPZ9pc78klez7iuy&usp=drive_copy
https://drive.google.com/open?id=1aidZJqW58y7ELv8pCFBgnIyPM1Oe-lm0&usp=drive_copy
https://drive.google.com/open?id=1OB1xPzSyN2G6qFR_-KazufozkU_hy_Zc&usp=drive_copy
https://drive.google.com/open?id=1xaIspJQFSe3jSuZMRQotiKlW1aIVZ9Ff&usp=drive_copy
https://drive.google.com/open?id=12gDFqVJAhwJiIbB_I-6EYuDCOP9jXpyx&usp=drive_copy
https://drive.google.com/open?id=1YHbwNsGWfAFi8Nvdcr-dG_yXEucEXyAQ&usp=drive_copy
https://drive.google.com/open?id=16zwvSzBgrCokU0RsH67bpi_ISWZlgibD&usp=drive_copy
https://drive.google.com/open?id=1YBlYIuNouBhQwkxTH-UclYv1jSmblQQy&usp=drive_copy
https://drive.google.com/open?id=16KzwQA19yn4QZaxmMvTZvDU9cawq73de&usp=drive_copy
https://drive.google.com/open?id=1iOiqN2Csl8kwIp3uTrLpXRNZhYBb0tYh&usp=drive_copy
https://drive.google.com/open?id=1lo83KHtLmvIxVK3zN2oEtDryWORvgwKQ&usp=drive_copy
https://drive.google.com/open?id=14f43MCZNphyISjp6RJdskNb2AD2dqotK&usp=drive_copy
https://drive.google.com/open?id=1lk8gJa2DOT28Z3LLfPkzGQ4_0hwjYgWw&usp=drive_copy
https://drive.google.com/open?id=1mEtXc-JdfVpBksInV0H9PpomUJPasdAh&usp=drive_copy
https://drive.google.com/open?id=1N0a0zWlliudJiGYmCA4_WniGbDVevvHE&usp=drive_copy
https://drive.google.com/open?id=1jtWc0A8pIn_-NgrR2NJgtr56m3jVhY6v&usp=drive_copy
https://drive.google.com/open?id=1IDJBxaz2zUG5Q63RsqcLAJx0ptWqX_TF&usp=drive_copy
https://drive.google.com/open?id=125e5HCq9HE4NjLREi1TgwHkKxMe4-tIk&usp=drive_copy
https://drive.google.com/open?id=1OynrAl3gV9jyUOFT7g6rZaUkiQVapaJ1&usp=drive_copy
https://drive.google.com/open?id=1XejAn0RiTsv8WGXnjBkAWOBS53gCL1Iu&usp=drive_copy
https://drive.google.com/open?id=1nuUdmCTD1_EIUaJic9MizS1RBAAiQxiF&usp=drive_copy
https://drive.google.com/open?id=1C-bnpCNCdxhyVBrMYYi02jAW-D80bAxv&usp=drive_copy
https://drive.google.com/open?id=1gYFg51X7U_ZeaPgT5shwfE6N_YDV5mlJ&usp=drive_copy
https://drive.google.com/open?id=1pWHG4-U6z8-ezm9GenWdqCD0ao5sLwWi&usp=drive_copy
https://drive.google.com/open?id=13wi2Te322P3flKUy-_rpy48TyTqhSuqr&usp=drive_copy
https://drive.google.com/open?id=1Tg46TZ_0vQs10ETCbZdyEde-HMSiGcG6&usp=drive_copy
https://drive.google.com/open?id=16sSmv-jdievgD7vYBY-CHMswBKQRDvW4&usp=drive_copy
https://drive.google.com/open?id=1_KECpJC_rWJfWQoRw-ClZF_ey0mktes6&usp=drive_copy
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
