#!/usr/bin/env python
#Copying Picture from some folder to some folder :)
#Please read README.md in advance.
import os
from PIL import Image
from PIL.ExifTags import TAGS
import shutil
import sys

E_DateTag = 0x9003
TOKEN = "-"

def getArgs():
    print("getArgs()")
    if len(sys.argv)>1:
        FromDirPath = sys.argv[1]
        print("1_attribute")
        if len(sys.argv)>2:
            ToDirPath = sys.argv[2]
            print("2_attributes")
        else:
            ToDirPath = os.getcwd()
        Object = {"FromDirPath":FromDirPath,"ToDirPath":ToDirPath}
        return Object
    else:
        print("Lack of attributes!!!!!!")
        sys.exit()
def getDate(img):
    #Get Exif original date.
    try:
        exif = img._getexif()
        rawDateTime = exif[E_DateTag]
        rawDate = rawDateTime.split(" ")[0]
    except:
        print("Error!!")
    Date = rawDate.split(":")
    print("Tooked at "+Date[0]+"/"+Date[1]+"/"+Date[2])
    return Date

def loadPic(path):
    #Construct PIL.Image class.
    image = Image.open(path)
    return image

def listFiles(path):
    rawList = os.listdir(path)
    listDirs = []
    for name in rawList:
        #print(name)
        if ".jpg" or ".JPG" in name:
            listDirs.append(name)
    return listDirs
    #For Debug
    for txt in listDirs:
        print(txt)

def copyFile(name,fromWhere,targetWhere):
    fromPath = genFromPath(name,fromWhere)
    image = loadPic(fromPath)
    date = getDate(image)
    dir = genDir(date,TOKEN)
    targetPath = genToPath(dir,targetWhere)
    check_and_make(targetPath)
    shutil.copy2(fromPath,targetPath+"/"+name)
    print(name+" Copied!")

def check_and_make(targetPath):
    if os.path.isdir(targetPath):
        print("OK")
    else:
        os.mkdir(targetPath)
        print("Folder generated.")

def genDir(date,TOKEN):
    return date[0]+TOKEN+date[1]+TOKEN+date[2]
def genFromPath(dirName,fromPath):
    return fromPath + "/" + dirName
def genToPath(dirName,toPath):
    return toPath + "/" + dirName

def main():
    print("Hello...")
    Args = getArgs()
    print(Args["FromDirPath"])
    pathList = listFiles(Args["FromDirPath"])
    for imgName in pathList:
        copyFile(imgName,Args["FromDirPath"],Args["ToDirPath"])


#root stage
if __name__ == "__main__":
    main()
