import os, re, shutil, pprint



# Creates list of .mkv, .mp4, and .avi files in New Downloads
fullPath = []
onlyFile = []
dirPath = ()
for dirPath, subDirs, fileNames in os.walk("/mnt/nd"):
    for e in fileNames:
        if e.startswith('RARBG.txt'):
            os.remove(os.path.join(dirPath, e))
        elif e.startswith('RARBG.com.txt'):
            os.remove(os.path.join(dirPath, e))
        elif e.endswith('.nfo'):
            os.remove(os.path.join(dirPath, e))
        else:
            continue
    for fileName in [f for f in fileNames if f.endswith(".mkv") or f.endswith(".avi") or f.endswith(".mp4")]:
        #fullPath.append(os.path.join(dirPath, fileName))
        onlyFile.append(fileName)

# Turns periods in filenames to spaces
per2Space = []

for x in onlyFile:
    if x.count('.') > 2:
        j = x.replace('.', ' ')
        per2Space.append(j)

# Creates list of folders in TV and Movies
tvnmDir = []
for folder in os.listdir('/mnt/tvnm'):    
    tvnmDir.append(folder)

# pprint.pprint(per2Space)


# Moves files to matching folder name

for x in per2Space:
    for y in tvnmDir:
        if x[:8] == y[:8]:
            print(os.path.join('/mnt/nd', x.replace(' ', '.')), os.path.join('/mnt/tvnm', y, x.replace(' ', '.')))
            



    
'''
for q in per2Space:
    if q[:8] == y[:8] for y in tvnmDir: 
        print(x)

#This isn't going to work    

# Strips extraneous characters for comparison 

for a in per2Space:
    set1 = []
    set1.append(a[:8])


for b in tvnmDir:
    set2 = []
    set2.append(b[:8])



for c[:8] in fullPath:
    if c[:8] in tvnmDir:
        print(os.stat(c))

'''
