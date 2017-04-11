import os, pprint, re


# Identify folders containing music files
Dirs = []
nD = os.listdir('/mnt/nd')
for a in nD:
    b = os.path.join('/mnt/nd/' + a)
    if os.path.isdir(b) == True:
        Dirs.append(b)
    else:
        continue
    
sDir = []
for subD in Dirs:
    e = os.listdir(subD)
    for f in e:
        if f.endswith('.mp3' or '.flac' or '.m4a' or '.wma'):
            sDir.append(subD)

muDir = list(set(sDir))
#pprint.pprint(muDir)


# Match music folders in New Downloads to folders in Music library
# THIS DON'T WORK

Af = re.compile(r'^[0-9A-Fa-f]{1}')
Go = re.compile(r'^[G-Og-o]{1}')
Pz = re.compile(r'^[P-Zp-z]{1}')

for g in muDir:
    h = g.replace('/mnt/nd/', '')
    print(h)



# 
