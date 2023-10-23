links = '''
https://drive.google.com/open?id=121VPos4ewZi-xviz-sxa27vFdjXIONfi&usp=drive_copy
https://drive.google.com/open?id=1cV0XHgQROl-1PWG74ZfqiqR8HQL6ASRz&usp=drive_copy
https://drive.google.com/open?id=1heOrRhU8ZSTHezGyInExPzJh4YvAJLrX&usp=drive_copy
https://drive.google.com/open?id=1nzXaDhA_r4ozQFvLJf5N0Gmo-PaIkXc4&usp=drive_copy
https://drive.google.com/open?id=1quPg2mHrWS8-xbmXBLF8cXLQL79VeJ8s&usp=drive_copy
https://drive.google.com/open?id=1Zpx9cz-vu-pCHFzrApbUqAUivV5Oth0n&usp=drive_copy
https://drive.google.com/open?id=1oIarZbIOcSj1vr5pGFnU2kj7Gg1SCILr&usp=drive_copy
https://drive.google.com/open?id=1pcgVqkkjya0l739Dph3ob18IFPIVQHa9&usp=drive_copy
https://drive.google.com/open?id=17XZyys8WZ3yI2dycClENWYIkuPvuQMX3&usp=drive_copy
https://drive.google.com/open?id=1dkRQ9twq8eWKr-jI4DSI7C_4KPY2n_tQ&usp=drive_copy
https://drive.google.com/open?id=1rL3Gd0lVZCa_vwYfoTLRTom5bi6iTDtu&usp=drive_copy
https://drive.google.com/open?id=1iUx4rybLFCP5nX6CoATp2-krUNsn2zUk&usp=drive_copy
https://drive.google.com/open?id=1PoCyFszgvxoRTODmcatj26tnil5dSe4M&usp=drive_copy
https://drive.google.com/open?id=1wipRnSFNmtApAbiSh4x6AYyxp3zAeC3Q&usp=drive_copy
https://drive.google.com/open?id=17ZJi3JpBkTpExCN14_VqytNRTGL_4J4N&usp=drive_copy
'''.split('\n')[1:-1]

names = '''
fund_nav_report_weekly_edition_230828.pdf
fund_nav_report_weekly_edition_230829.pdf
fund_nav_report_weekly_edition_230830.pdf
fund_nav_report_weekly_edition_230901.pdf
fund_nav_report_weekly_edition_230905.pdf
fund_nav_report_weekly_edition_230906.pdf
fund_nav_report_weekly_edition_230908.pdf
fund_nav_report_weekly_edition_230911.pdf
fund_nav_report_weekly_edition_230912.pdf
fund_nav_report_weekly_edition_230914.pdf
fund_nav_report_weekly_edition_230915.pdf
fund_nav_report_weekly_edition_230922.pdf
fund_nav_report_weekly_edition_230929.pdf
fund_nav_report_weekly_edition_231006.pdf
fund_nav_report_weekly_edition_231020.pdf
'''.split('\n')[1:-1]

names.reverse()

for name, link in zip(names, links):
  date = name.split(".pdf")[-6:][0].replace("fund_nav_report_weekly_edition_","")
  print(f'<a href="{link.replace("open?","uc?export=download&")}">20{date[:2]}-{date[2:4]}-{date[4:6]}</a><br>')
