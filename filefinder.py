import os, pprint, re, shutil

# Creates list of .mkv, .mp4, and .avi files in New Downloads
fullPath = []
onlyFile = []
for dirPath, dirNames, fileNames in os.walk("/mnt/nd"):
    for fileName in [f for f in fileNames if f.endswith(".mkv") or f.endswith(".avi") or f.endswith(".mp4")]:
        fullPath.append(os.path.join(dirPath, fileName))
        onlyFile.append(fileName)

# Turns periods in filenames to spaces
per2Space = []
for x in onlyFile:
    j = x.replace('.', ' ')
    per2Space.append(j)
    

# pprint.pprint(onlyFile)

# REGEX TO FIND FILES 

fileRegex = re.compile(r'The\.Expanse.\w*', re.I)

#for file in onlyFile:
#    print(fileRegex.findall(file))    

# Creates list of folders in TV and Movies
tvnmDir = []
for folder in os.listdir('/mnt/tvnm'):
    tvnmDir.append(folder)

pprint.pprint(set(tvnmDir) & set(noSpace))

