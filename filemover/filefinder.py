import os
import os.path

for dirPath, dirNames, fileNames in os.walk("/mnt/nd"):
    for fileName in [f for f in fileNames if f.endswith(".mkv", ".mp4", ".avi")]:
        print os.path.join(dirPath, fileName)
