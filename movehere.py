import os, shutil

#yn = input("Click any button to run. Otherwise close the window")
here = os.getcwd()

for dir, sub_dirs, files in os.walk(here):
    for file in files:
        if os.path.isfile(file):
            print("LUL")
        else:    
            print(dir + file)
            shutil.move(dir + "/" + file, here)

folders = sorted(list(os.walk(here))[1:],reverse=True)
for folder in folders:
    print(folder)
    if len(folder[2]) == 0:
        print(str(folder))
        os.rmdir(folder[0])
    
