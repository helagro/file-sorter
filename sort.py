from env import SORT_RULES
import os
from helpers import mPrint


def sort(filepath):
    destination = getFolderDestination(filepath, 0)

    if(destination == "NONE"):
        return

    moveToFolder(filepath, destination)

def getFolderDestination(filepath, sortRuleI):
    if sortRuleI >= len(SORT_RULES):
        return "NONE"
    sortRule = SORT_RULES[sortRuleI]
    
    if anySortTypeMatches(filepath, sortRule):
        return sortRule.folderNm

    sortRuleI += 1
    return getFolderDestination(filepath, sortRuleI)

def anySortTypeMatches(filepath, sortRule):
    return extSortMatches(filepath, sortRule)

def extSortMatches(filepath, sortRule):
    extension = os.path.splitext(filepath)[1]
    
    for extMatch in sortRule.sortMathes:
        if(extension == extMatch):
            return True
    return False

def moveToFolder(filepath, folderpath):
    if (not os.path.isfile(filepath)):
        return

    filename = os.path.basename(filepath)
    newFilePath = folderpath + os.path.sep + filename
    vacantFilePath = getVacantFilePath(newFilePath)

    os.rename(filepath, vacantFilePath)

def getVacantFilePath(filePath):
    originalFilePathWithoutExtension = os.path.splitext(filePath)[0]
    extension = os.path.splitext(filePath)[1]
    i = 0

    while os.path.isfile(filePath):
        i += 1
        filePath = "{0}({1}){2}".format(originalFilePathWithoutExtension, i, extension)

    return filePath