def format_archive_html(fileName, googleLink):
  string = f"""
<!-- File Start -->
                  <div class="col-12 col-sm-6 col-md-4 col-lg-3 mb-4">
                     <div class="card">
                        <img src="{fileName[:-13]}_Covers/{fileName.replace('.pdf','.jpeg')}" alt="{fileName.replace('.pdf','.jpeg')}" class="card-img-top">
                        <div class="card-body text-center">
                           <h5 class="card-title">
                              {fileName[:-13].replace('_',' ')}<br></br>
                              <p>{fileName[-12:].replace('.pdf','')[:4]}-{fileName[-12:].replace('.pdf','')[4:6]}-{fileName[-12:].replace('.pdf','')[6:8]}</p>
                           </h5>
                           <a href="{googleLink}" class="btn btn-dark" style="margin-top: 10px; margin-bottom: -1px; background: black; border-width: 0px; background: white; color: #333333; border-width: 1px; border-color: #333333">
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-google" viewBox="0 0 16 16">
  <path d="M15.545 6.558a9.42 9.42 0 0 1 .139 1.626c0 2.434-.87 4.492-2.384 5.885h.002C11.978 15.292 10.158 16 8 16A8 8 0 1 1 8 0a7.689 7.689 0 0 1 5.352 2.082l-2.284 2.284A4.347 4.347 0 0 0 8 3.166c-2.087 0-3.86 1.408-4.492 3.304a4.792 4.792 0 0 0 0 3.063h.003c.635 1.893 2.405 3.301 4.492 3.301 1.078 0 2.004-.276 2.722-.764h-.003a3.702 3.702 0 0 0 1.599-2.431H8v-3.08h7.545z"/>
</svg>                              Preview
                           </a>
                           <br>
                           <a href="{googleLink.replace('open?','uc?export=download&')}" class="btn btn-dark" style="margin-top: 10px; margin-bottom: -1px; background: black; border-width: 0px">
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
"""
  print(string)

googleLinks = '''
https://drive.google.com/open?id=1w1CVx5XtdDF6FMgPr1rhyyb2et6W3DTM&usp=drive_copy
https://drive.google.com/open?id=1sm4OmT9ycBblVqOVIfAlS57WNT6DcD0E&usp=drive_copy
https://drive.google.com/open?id=1mmO2K7K6wfDkEzzzTLiWyXE1hOFMYKHB&usp=drive_copy
https://drive.google.com/open?id=1w7NaYM0epu7waEeW9hmS-QbW0nFqZ173&usp=drive_copy
https://drive.google.com/open?id=1xM7mxGCQyvEY5CGHj8gx7-VlUiGA4mCJ&usp=drive_copy
https://drive.google.com/open?id=1K0_SCCsCfavMmqLwWHg4BtWZCxpEOm1L&usp=drive_copy
https://drive.google.com/open?id=1oKO0l0PCmHlmgbTz-9D50WF4epkwUhJ2&usp=drive_copy
https://drive.google.com/open?id=1mMDF_VfvXz2_5Nj_-sqro2Vhaj_njSat&usp=drive_copy
https://drive.google.com/open?id=1XVhzxVaHg6ZzJaAsJyhml2cG1dm8nxO7&usp=drive_copy
https://drive.google.com/open?id=1xsKKCUNsJTPDY67xyUthdt0ko5wBeLEG&usp=drive_copy
https://drive.google.com/open?id=15I-xoa_hBCIAnUj43--1tBQAsRMqmt-_&usp=drive_copy
https://drive.google.com/open?id=1doRwQUhooZcQj0uTH-R2aC1DXvl2b0Ap&usp=drive_copy
https://drive.google.com/open?id=11WiEU29Gs133jDfqS4cvtVOb27-Z0LXP&usp=drive_copy
https://drive.google.com/open?id=1KFLRIdDw24Wpkyie9XTd_vDV77f4llWL&usp=drive_copy
https://drive.google.com/open?id=1R1-svua04wDvRsltqMRgu9KuwvCbR59s&usp=drive_copy
https://drive.google.com/open?id=1zsqOoXZ31rQyAmXq11awtRuBElhthfKl&usp=drive_copy
https://drive.google.com/open?id=1DxwMcqp8S50-_1o6SsgbGOzrGik_vnWU&usp=drive_copy
https://drive.google.com/open?id=1QgQEpYIAn3HdEBpmQbV0lqQxkESxCZUi&usp=drive_copy
'''.split('\n')[1:-1]

fileNames = '''
The_Wall_Street_Journal_20231021.pdf
The_Wall_Street_Journal_20231020.pdf
The_Wall_Street_Journal_20231019.pdf
The_Wall_Street_Journal_20231018.pdf
The_Wall_Street_Journal_20231017.pdf
The_Wall_Street_Journal_20231016.pdf
The_Wall_Street_Journal_20231014.pdf
The_Wall_Street_Journal_20231013.pdf
The_Wall_Street_Journal_20231012.pdf
The_Wall_Street_Journal_20231011.pdf
The_Wall_Street_Journal_20231010.pdf
The_Wall_Street_Journal_20231009.pdf
The_Wall_Street_Journal_20231007.pdf
The_Wall_Street_Journal_20231006.pdf
The_Wall_Street_Journal_20231005.pdf
The_Wall_Street_Journal_20231004.pdf
The_Wall_Street_Journal_20231003.pdf
The_Wall_Street_Journal_20231002.pdf
'''.split('\n')[1:-1]

for file, link in zip(fileNames, googleLinks):
  format_archive_html(file,link)
