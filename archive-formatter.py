string = """                                          <!-- File Start -->
                  <div class="col-12 col-sm-6 col-md-4 col-lg-3 mb-4">
                     <div class="card">
                        <img src="The_Economist_Covers/The_Economist_20231125.jpeg" alt="The_Economist_20231125.jpeg" class="card-img-top">
                        <div class="card-body text-center">
                           <h5 class="card-title">
                              The Economist<br></br>
                              <p>2023-11-25</p>
                           </h5>
                           <a href="https://drive.google.com/open?id=19SqlM8nvx1ziZBRZaHjy6Y4UAnQk8sUe&usp=drive_copy" class="btn btn-dark" style="margin-top: 10px; margin-bottom: -1px; background: black; border-width: 0px; background: white; color: #333333; border-width: 1px; border-color: #333333">
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-google" viewBox="0 0 16 16">
  <path d="M15.545 6.558a9.42 9.42 0 0 1 .139 1.626c0 2.434-.87 4.492-2.384 5.885h.002C11.978 15.292 10.158 16 8 16A8 8 0 1 1 8 0a7.689 7.689 0 0 1 5.352 2.082l-2.284 2.284A4.347 4.347 0 0 0 8 3.166c-2.087 0-3.86 1.408-4.492 3.304a4.792 4.792 0 0 0 0 3.063h.003c.635 1.893 2.405 3.301 4.492 3.301 1.078 0 2.004-.276 2.722-.764h-.003a3.702 3.702 0 0 0 1.599-2.431H8v-3.08h7.545z"/>
</svg>                              Preview
                           </a>
                           <br>
                           <a href="https://drive.google.com/uc?export=download&id=19SqlM8nvx1ziZBRZaHjy6Y4UAnQk8sUe&usp=drive_copy" class="btn btn-dark" style="margin-top: 10px; margin-bottom: -1px; background: black; border-width: 0px">
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


download_links = """https://drive.google.com/open?id=1huQrFLUCkyg_PbcjZqJhZSh-OwcmHUNK&usp=drive_copy""".split('\n')

file_names = """Bloomberg_Businessweek_20231211.jpeg""".split('\n')

file_names.sort()
file_names.reverse()

for file_name, download_link in zip(file_names, download_links):
    string = """                                          <!-- File Start -->
                  <div class="col-12 col-sm-6 col-md-4 col-lg-3 mb-4">
                     <div class="card">
                        <img src="The_New_Yorker_Covers/@replace_a" alt="@replace_a" class="card-img-top">
                        <div class="card-body text-center">
                           <h5 class="card-title">
                              Barron's<br></br>
                              <p>@replace_date</p>
                           </h5>
                           <a href="@replace_link_a" class="btn btn-dark" style="margin-top: 10px; margin-bottom: -1px; background: black; border-width: 0px; background: white; color: #333333; border-width: 1px; border-color: #333333">
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-google" viewBox="0 0 16 16">
  <path d="M15.545 6.558a9.42 9.42 0 0 1 .139 1.626c0 2.434-.87 4.492-2.384 5.885h.002C11.978 15.292 10.158 16 8 16A8 8 0 1 1 8 0a7.689 7.689 0 0 1 5.352 2.082l-2.284 2.284A4.347 4.347 0 0 0 8 3.166c-2.087 0-3.86 1.408-4.492 3.304a4.792 4.792 0 0 0 0 3.063h.003c.635 1.893 2.405 3.301 4.492 3.301 1.078 0 2.004-.276 2.722-.764h-.003a3.702 3.702 0 0 0 1.599-2.431H8v-3.08h7.545z"/>
</svg>                              Preview
                           </a>
                           <br>
                           <a href="@replace_link_b" class="btn btn-dark" style="margin-top: 10px; margin-bottom: -1px; background: black; border-width: 0px">
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
""".replace("@replace_a", file_name.replace(".pdf","jpeg")).replace("@replace_date", f"{file_name[15:].replace('.jpeg','')[:4]}-{file_name[15:].replace('.jpeg','')[4:6]}-{file_name[15:].replace('.jpeg','')[6:8]}").replace("@replace_link_a", download_link).replace("@replace_link_b",download_link.replace("open?","uc?export=download&"))
    print(string)
    print(f"")