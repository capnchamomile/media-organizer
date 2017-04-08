import os, shutil

os.chdir('/mnt/nd')

for dirName in os.listdir():
    if dirName.startswith('Stephen'):
        shutil.rmtree(dirName)
    elif dirName.startswith('Conan'):
        shutil.rmtree(dirName)
        #print(dirName)
