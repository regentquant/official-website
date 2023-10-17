# From Newest To Oldest
import os

file_names = '''
The_Economist_20230902.pdf
The_Economist_20230909.pdf
The_Economist_20230916.pdf
The_Economist_20230923.pdf
The_Economist_20230930.pdf
The_Economist_20231007.pdf
The_Economist_20231014.pdf
'''.split('\n')[1:-1]

files = (sorted(file_names))
files.reverse()
file_names = files

google_links = '''
https://drive.google.com/open?id=1CY9qhE61Fqk6KVyaMYYDY1gp46tGsgb3&usp=drive_copy
https://drive.google.com/open?id=1nn9AL1VLyuRvWxxC5dD2DewLVWYTGbwH&usp=drive_copy
https://drive.google.com/open?id=1IoHdIfevyE7JEKk4jr3C6tSZyJJIR7eA&usp=drive_copy
https://drive.google.com/open?id=1xb0vIA_qAeE6ezzMSKukX4-pWwaM5u-h&usp=drive_copy
https://drive.google.com/open?id=1Oe_jY3OirhFbAMhPJZv_ZrpKxoaQf17b&usp=drive_copy
https://drive.google.com/open?id=1TvyVd6MSViyqgMpS63fkxaqWixfc4fFr&usp=drive_copy
https://drive.google.com/open?id=1nCvcx0RIctbz-5Q7udMCZ894NWT4MZE8&usp=drive_copy
'''.split('\n')[1:-1]

number = 1

for file_name, google_link in zip(file_names, google_links):

	print(f"""
<div class="col-12 col-sm-6 col-md-4 col-lg-3 mb-4">
   <div class="card">
      <img src="The_Economist_Covers/{file_name.replace('.pdf','.jpeg')}" alt="{file_name.replace('.pdf','.jpeg')}" class="card-img-top">
      <div class="card-body text-center">
         <h5 class="card-title">
            The Economist<br></br>
            <p>{file_name.split('Economist_')[1].replace('.pdf','')}</p>
         </h5>
         <a href="{google_link}" class="btn btn-primary" style="margin-top: 10px; margin-bottom: -1px; background: black; border-width: 0px">Download</a>
      </div>
   </div>
</div>
""")
	number = number + 1
