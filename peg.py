#!/usr/bin/env python
import ffmpeg
import math
import sys
import argparse
import os, os.path

def show(startNumber : int, endNumber : int) -> None:
    print("Start Number : " + str(startNumber))
    print("End Number : " + str(endNumber))

def userChoice() -> bool:

    user = input("Is the number ok ? [Y/N] --> ")

    if (user.lower() == "yes") or (user.lower() == "y"):
        return True
    elif (user.lower() == "no") or (user.lower() == "n"):
        return False
    else:
        print("Error")
        sys.exit()

def renameFile(extension):
    files = os.listdir(".")
    files.sort(key=os.path.getmtime, reverse=False)

    before_images_num = 0

    renameFile = []
    file_type = extension.input

    for _ ,name in enumerate(files):
        if name.endswith(file_type):
            renameFile.append(name)
            before_images_num += 1
    
    checkFileLength = len(renameFile)

    maxRank = int(math.log10(checkFileLength)+1)

    cnt = 1

    for renamed in renameFile:
        i = str(cnt)
        file_num = i.zfill(maxRank)
        os.rename(renamed, file_num + "." + extension.input)
        cnt += 1
    
    return before_images_num

def startConvert(startNumber: int,endNumber: int,beforeExtension: str,afterExtension: str,before_images_num: int) -> bool:
    
    show(1, countAll)

    if(not userChoice()):
        startNumber = int(input("Please enter a Start number --> "))
        endNumber = int(input("Please enter a End number --> "))

    for i in range(startNumber,endNumber+1):
        
        countConvert=str(i).zfill(numberOfDigits)

        (
			ffmpeg
			.input('{0}.{1}'.format(countConvert, beforeExtension))
			.output('{0}.{1}'.format(countConvert, afterExtension))
			.run(quiet=True)
		)

        print("\r" + "Converting " + str(i) + " of " + str(endNumber),end="")
    print("")

    files = os.listdir(".")
    files.sort(key=os.path.getmtime, reverse=False)

    after_images_num = 0

    file_type = (beforeExtension, afterExtension)

    for _ ,name in enumerate(files):
        if name.endswith(file_type):
            after_images_num += 1

    if (before_images_num * 2 == after_images_num):
        return True
    else: 
        return False

def countImages(extension) -> int:
    files = os.listdir(".")
    files.sort(key=os.path.getmtime, reverse=False)

    images_num = 0

    file_type = extension.input

    for _ ,name in enumerate(files):
        if name.endswith(file_type):
            images_num += 1
    return images_num


def checkCommand():
    parser = argparse.ArgumentParser()

    parser.add_argument("-i","--input", default="png", type=str, help="変更前拡張子を入力してください．")

    parser.add_argument("-o","--output", default="jpg", type=str, help="変更後拡張子を入力してください．")

    args = parser.parse_args()

    return (args)


def main() -> None:

    extension = checkCommand()

    global countAll

    before_images_num = renameFile(extension)

    countAll = countImages(extension)

    global numberOfDigits

    numberOfDigits=int(math.log10(countAll)+1)

    finishConvert = startConvert(1,countAll,extension.input,extension.output,before_images_num)

    print("done")

    # if (finishConvert):
    #     user = input("Do you want to delete the original file ？ [Y/N] --> ")

    #     if (user.lower() == "yes") or (user.lower() == "y"):
    #         os.remove("*." + extension.input)
    #         print("done")
    #     else:
    #         print("done")
    #         pass
    # else:
    #     print("The number of original files differs from the number of converted files.")


if __name__ == '__main__':
    main()