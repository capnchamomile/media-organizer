import os, re, shutil, pprint



# Creates list of .mkv, .mp4, and .avi files in New Downloads
fullPath = []
onlyFile = []
dirPath = ()
for dirPath, subDirs, fileNames in os.walk("/volume1/New Downloads"):
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
for folder in os.listdir('/volume1/TV and Movies'):    
    tvnmDir.append(folder)

# pprint.pprint(per2Space)


# Moves files to matching folder name

for x in per2Space:
    for y in tvnmDir:
        if x[:8] == y[:8]:
            z = x.replace(' ', '.')
            a = z.replace('.mkv', '')
            try:
                shutil.move(os.path.join('/volume1/New Downloads', a + '[rarbg]', z), os.path.join('/volume1/TV and Movies', y))           
            except FileNotFoundError:
                pass

for d in tvnmDir:
    if not os.listdir(d):
        print(d)
    

