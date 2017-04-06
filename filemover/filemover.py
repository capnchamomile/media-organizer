import os, re, pprint

# get list of only folders in New Downloads
rawDir = []

ndCont = os.listdir('/mnt/nd') # new downloads contents 

for dirName in ndCont:
        if os.path.isdir(os.path.join('/mnt/nd', dirName)):
                rawDir.append(dirName)
                
        
#pprint.pprint('Folders\n' + str(rawDir))

# get list of only files in New Downloads
rawFiles = []

for fileName in ndCont:
        if os.path.isfile(os.path.join('/mnt/nd', fileName)):
                rawFiles.append(fileName)
                
        
# pprint.pprint('\nFiles \n' + str(rawFiles))

# TODO: List contents of subfolders 

#subFolders = os.listdir(str(rawDir))
#print(subFolders) 

for subDir in rawDir:
	subs = os.listdir(subDir)


# TODO: match files to names of folders



# TODO: match season # to folder name

