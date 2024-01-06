import pyperclip
cover_name = "The_New_Yorker_20240101.jpeg"
google_link = "https://drive.google.com/open?id=1_z8OAeXD-BfPvp0yZ2Vf6f7CaaVr52Hj&usp=drive_copy"
date = f"{cover_name.split('.')[0].split('_')[-1][:4]}-{cover_name.split('.')[0].split('_')[-1][4:6]}-{cover_name.split('.')[0].split('_')[-1][6:8]}"
print(date)

if "Barrons" in cover_name:
    publisher = "Barron's"
elif "Bloomberg" in cover_name:
    publisher = "Bloomberg Businessweek"
elif "Economist" in cover_name:
    publisher = "The Economist"
elif "Yorker" in cover_name:
    publisher = "The New Yorker"

template = f'''    <!-- File Start -->
                <div class="col-12 col-sm-6 col-md-4 col-lg-3 mb-4">
                    <div class="card">
                        <img src="all-covers/{cover_name}" alt="{cover_name.replace('.jpeg','')}_Cover.jpeg"
                             class="card-img-top">
                        <div class="card-body text-center">
                            <h5 class="card-title">
                                {publisher}<br></br>
                                <p>{date}</p>
                            </h5>
                            <a href="{google_link}"
                               class="btn btn-dark"
                               style="margin-top: 10px; margin-bottom: -1px; background: black; border-width: 0px; background: white; color: #333333; border-width: 1px; border-color: #333333">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                     class="bi bi-book" viewBox="0 0 16 16">
                                    <path d="M1 2.828c.885-.37 2.154-.769 3.388-.893 1.33-.134 2.458.063 3.112.752v9.746c-.935-.53-2.12-.603-3.213-.493-1.18.12-2.37.461-3.287.811V2.828zm7.5-.141c.654-.689 1.782-.886 3.112-.752 1.234.124 2.503.523 3.388.893v9.923c-.918-.35-2.107-.692-3.287-.81-1.094-.111-2.278-.039-3.213.492V2.687zM8 1.783C7.015.936 5.587.81 4.287.94c-1.514.153-3.042.672-3.994 1.105A.5.5 0 0 0 0 2.5v11a.5.5 0 0 0 .707.455c.882-.4 2.303-.881 3.68-1.02 1.409-.142 2.59.087 3.223.877a.5.5 0 0 0 .78 0c.633-.79 1.814-1.019 3.222-.877 1.378.139 2.8.62 3.681 1.02A.5.5 0 0 0 16 13.5v-11a.5.5 0 0 0-.293-.455c-.952-.433-2.48-.952-3.994-1.105C10.413.809 8.985.936 8 1.783"/>
                                </svg>
                                Read Now
                            </a>
                            <br>
                            <a href="{google_link.replace('open?','uc?export=download&')}"
                               class="btn btn-dark"
                               style="margin-top: 10px; margin-bottom: -1px; background: black; border-width: 0px">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                     class="bi bi-download" viewBox="0 0 16 16">
                                    <path d="M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5z"/>
                                    <path d="M7.646 11.854a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293V1.5a.5.5 0 0 0-1 0v8.793L5.354 8.146a.5.5 0 1 0-.708.708l3 3z"/>
                                </svg>
                                Download
                            </a>
                        </div>
                    </div>
                </div>
                <!-- File End -->
                '''
import pyperclip
print(template)
pyperclip.copy(template)