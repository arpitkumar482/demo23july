
import os
import re
from git.repo.base import Repo
url_list=["https://github.com/arpitkumar482/myappsample.git","https://github.com/arpitkumar482/sample2.git"]
root_path=r"C:\Users\arpit.kumar\Desktop\backup5"

for url in url_list:
    foldername = re.findall(".+\/(.+)\.git",url)[0]
    folderpath = root_path+'\\'+foldername
    os.mkdir(folderpath)
    Repo.clone_from(url,folderpath)
    print("Repo cloned in :"+folderpath)
print("Clone Completed")
