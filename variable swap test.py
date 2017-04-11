import os, shutil

# Creates list of .mkv, .mp4, and .avi files in New Downloads
fullPath = []
onlyFile = []

for dirPath, subDirs, fileNames in os.walk("/mnt/nd"):
    for e in fileNames:
        if e.endswith('.txt'):
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
    else:
        per2Space.append(x)

# Creates list of folders in TV and Movies
tvnmDir = []
for folder in os.listdir('/mnt/tvnm'):    
    tvnmDir.append(folder)

# pprint.pprint(per2Space)


# Moves files to matching folder name


sp2Per = []
for x in per2Space:
    for y in tvnmDir:
        if x[:8] == y[:8]:
            z = x.replace(' ', '.')
            sp2Per.append(z)
            #a = z.replace('.mkv', '')
            

fPath = []
for p in os.listdir('/mnt/nd'):
    for r in sp2Per:
        if p[:18] == r[:18]:
            fPath.append(os.path.join('/mnt/nd/', p, r))

for i in fPath:
    print(i)
            

'''
            try:
                e = os.path.join('/mnt/nd', a, z)
                shutil.move(e, os.path.join('/mnt/tvnm', y))
            except(FileNotFoundError, shutil.Error):
                pass
            try:
                b = os.path.join('/mnt/nd', a + '[rarbg]', z)
                shutil.move(b, os.path.join('/mnt/tvnm', y))            
            except(FileNotFoundError, shutil.Error):
                pass
            try:
                d = os.path.join('/mnt/nd', a + '[ettv]', z)
                shutil.move(d, os.path.join('/mnt/tvnm', y))             
            except(FileNotFoundError, shutil.Error):
                pass
'''
            
# Delete Empty folders 
      
for l in os.listdir('/mnt/nd'):
    mt = os.path.join('/mnt/nd/' + l)
    if os.path.isdir(mt) == True:
        if not os.listdir(mt):
            os.rmdir(mt)

