import re

url_list=["https://github.com/arpitkumar482/myappsample.git","https://github.com/arpitkumar482/sample2.git"]
for url in url_list:
    list_urltags = url.split('/')[-1:][0][:-4]
    foldername = list_urltags
    print(foldername)
