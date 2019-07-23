import os
root_path=r"C:\Users\arpit.kumar\Desktop\backup1"
folder=[11,22,33,44]
gh=folder

print(gh)
for i in gh:
    os.mkdir(os.path.join(root_path,str(i)))
