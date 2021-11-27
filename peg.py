#!/usr/bin/env python
import ffmpeg
import math
import sys
import os, os.path

def startConvert(startNumber: int,endNumber: int,beforeExtension: str,afterExtension: str) -> bool:
    
    for i in range(startNumber,endNumber+1):
            #countConvert=str(i)
            countConvert = str(i).zfill(p)
            print(countConvert)
            (
                ffmpeg
                .input('{}.' + beforeExtension.format(countConvert))
                .output('{}.' + afterExtension.format(countConvert))
                .run()
            )

    finalNum = len([name for name in os.listdir(".") if os.path.isfile(name)])

    if (countAll * 2 == finalNum):
        return True
    else: 
        return False

def mainProgram():

    countAll = len([name for name in os.listdir(".") if os.path.isfile(name)])
    p=int(math.log10(countAll)+1)

    startConvert(0,10,"webp","jpg")


if __name__ == '__main__':
    mainProgram()