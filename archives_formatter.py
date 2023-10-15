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
