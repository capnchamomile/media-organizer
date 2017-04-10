import os, re, shutil

# Creates list of .mkv, .mp4, and .avi files in New Downloads
fullPath = []
onlyFile = []
for dirPath, subDirs, fileNames in os.walk("/mnt/nd"):
    for fileName in [f for f in fileNames if f.endswith(".mkv") or f.endswith(".avi") or f.endswith(".mp4")]:
        fullPath.append(os.path.join(dirPath, fileName))
        onlyFile.append(fileName)

# Turns periods in filenames to spaces

for x in fullPath:
    per2Space = []
    j = x.replace('.', ' ')
    per2Space.append(j)

# Creates list of folders in TV and Movies

for folder in os.listdir('/mnt/tvnm'):
    tvnmDir = []
    tvnmDir.append(folder)



#This isn't going to work    
'''
# Strips extraneous characters for comparison 
set1 = []
for a in per2Space:
    set1.append(a[:8])

set2 = []
for b in tvnmDir:
    set2.append(b[:8])



for c[:8] in fullPath:
    if c[:8] in tvnmDir:
        print(os.stat(c))

'''
