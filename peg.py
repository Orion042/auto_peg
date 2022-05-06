#!/usr/bin/env python
import ffmpeg
import math
import sys
import argparse
import os, os.path

def show(endNumber : int) -> None:
    print("開始番号 : 1")
    print("終了番号 : " + str(endNumber))

def userChoice() -> bool:

    user = input("番号は大丈夫でしょうか [Y/N] ? --> ")

    if (user == "YES") or (user == "Yes") or (user == "Y") or (user == "y"):
        return True
    elif (user == "NO") or (user == "No") or (user == "no") or (user == "N") or (user == "n"):
        return False
    else:
        sys.exit()

def startConvert(startNumber: int,endNumber: int,beforeExtension: str,afterExtension: str) -> bool:

    show(endNumber)

    if(not userChoice()):
        startNumber = int(input("開始番号を入力してください --> "))
        endNumber = int(input("終了番号を入力してください --> "))

    for i in range(startNumber,endNumber+1):
        
        countConvert=str(i).zfill(numberOfDigits)

        (
			ffmpeg
			.input('{}.' + beforeExtension.format(countConvert))
			.output('{}.' + afterExtension.format(countConvert))
			.run(quiet=True)
		)

        print("\r" + "Convert " + str(i) + " of " + str(endNumber),end="")
    
    finalNum = len([name for name in os.listdir(".") if os.path.isfile(name)])

    if (countAll * 2 == finalNum):
        return True
    else: 
        return False

def countImages() -> int:
    return len([name for name in os.listdir(".") if os.path.isfile(name)])


def checkCommand():
    parser = argparse.ArgumentParser()

    parser.add_argument("-i","--input",required=True, help="変更前拡張子を入力してください．", type=str)

    parser.add_argument("-o","--output",required=True, help="変更後拡張子を入力してください．", type=str)

    args = parser.parse_args()

    return (args)


def main() -> None:

    extension = checkCommand()

    global countAll

    countAll = countImages()

    global numberOfDigits

    numberOfDigits=int(math.log10(countAll)+1)

    finishConvert = startConvert(1,countAll,extension.input,extension.output)

    if (finishConvert):
        user = input("元のファイルは削除しますか？ [Y/N] --> ")

        if (user == "YES") or (user == "Yes") or (user == "Y") or (user == "y"):
            os.remove(extension.input)
        else:
            pass
    else:
        print("元のファイル数と変換後のファイル数が異なります．")


if __name__ == '__main__':
    main()