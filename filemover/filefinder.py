import os, pprint, re, shutil

toMove = []

for dirPath, dirNames, fileNames in os.walk("/mnt/nd"):
    for fileName in [f for f in fileNames if f.endswith(".mkv") or f.endswith(".avi") or f.endswith(".mp4")]:
        toMove.append(os.path.join(dirPath, fileName)) 

# pprint.pprint(toMove)

fileRegex = re.compile(r'The\.Expanse.\w+', re.I)

for file in toMove:
    print(fileRegex.findall(file))


