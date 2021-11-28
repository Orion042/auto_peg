#!/usr/bin/env python
import ffmpeg
import math
import sys
import argparse
import os, os.path

def show(endNumber : int):
    print("開始番号 : 1")
    print("終了番号 : " + endNumber)

def userChoice() -> bool:

    user = input("番号は大丈夫でしょうか [Y/N] ? --> ")

    if (user == "YES") or (user == "Yes") or (user == "Y") or (user == "y"):
        return True
    elif (user == "NO") or (user == "No") or (user == "no") or (user == "N") or (user == "n"):
        return False

def startConvert(startNumber: int,endNumber: int,beforeExtension: str,afterExtension: str) -> bool:

    show(endNumber)

    if(not userChoice()):
        startNumber = int(input("開始番号を入力してください -->"))
        endNumber = int(input("終了番号を入力してください -->"))
    
    for i in range(startNumber,endNumber+1):
            #countConvert=str(i)
            countConvert = str(i).zfill(numberOfDigits)
            
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

def countImages() -> int:
    return len([name for name in os.listdir(".") if os.path.isfile(name)])


def checkCommand():
    parser = argparse.ArgumentParser()

    parser.add_argument("--i", help="変更前拡張子を入力してください．", type=str)

    parser.add_argument("--o", help="変更後拡張子を入力してください．", type=str)

    args = parser.parse_args()

    return (args)


def mainProgram():

    extension = checkCommand()

    #extension.i は変更前の拡張子情報

    #extension.o は変更後の拡張子情報

    global countAll

    countAll = countImages()

    global numberOfDigits

    numberOfDigits=int(math.log10(countAll)+1)

    #startConvert(0,10,extension.i,extension.o)


if __name__ == '__main__':
    mainProgram()