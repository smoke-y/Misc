ignoreDirs     = [".git", ".vs", "bin"]
acceptFilesExt = ["c", "cc", "cpp", "h", "hh", "hpp", "py"]

import os
from sys import argv

if(len(argv) < 2):
    print("Provide root dir")
    quit()
    
folderPath = argv[1]
all_files = []
total = 0

for root, dirs, files in os.walk(folderPath):
    shouldCont = False
    for i in ignoreDirs:
        if i in root: shouldCont = True
    if shouldCont: continue
    for file in files:
        shouldConsider = False
        for a in acceptFilesExt:
            if file.endswith(a): shouldConsider = True
        if shouldConsider == False: continue
        filePath = os.path.join(root, file)
        print(filePath, end='')
        f = open(filePath)
        lineCount = len(f.readlines())
        print(":", lineCount)
        total += lineCount

print("Total:", total)
