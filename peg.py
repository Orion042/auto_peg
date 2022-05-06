#!/usr/bin/env python
import ffmpeg
import math
import sys
import argparse
import os, os.path

def show(endNumber : int) -> None:
    print("Start Number : 1")
    print("End Number : " + str(endNumber))

def userChoice() -> bool:

    user = input("Is the number oK ? [Y/N] --> ")

    if (user == "YES") or (user == "Yes") or (user == "Y") or (user == "y"):
        return True
    elif (user == "NO") or (user == "No") or (user == "no") or (user == "N") or (user == "n"):
        return False
    else:
        sys.exit()

def startConvert(startNumber: int,endNumber: int,beforeExtension: str,afterExtension: str) -> bool:

    show(endNumber)

    if(not userChoice()):
        startNumber = int(input("Please enter a starting number --> "))
        endNumber = int(input("Please enter a exit number --> "))

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
        user = input("Do you want to delete the original file ？ [Y/N] --> ")

        if (user == "YES") or (user == "Yes") or (user == "Y") or (user == "y"):
            os.remove(extension.input)
        else:
            pass
    else:
        print("The number of original files differs from the number of converted files．")


if __name__ == '__main__':
    main()