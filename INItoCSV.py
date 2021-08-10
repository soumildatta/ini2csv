# Author: Soumil Datta
# Script lives inside Results/
import os

def getFileList(folderName: str) -> [str]:
    onlyfiles: [str] = [os.path.join(folderName, file) for file in os.listdir(folderName) if os.path.isfile(os.path.join(folderName, file)) and file.endswith(".INI")]
    return onlyfiles

def getHeaderListFromINI(filename: str, addFileName=True) -> [str]:
    headerList = []

    if addFileName:
        headerList = ['INIFileName']
    with open(filename) as inputFile:
        for line in inputFile:
            attribute = line.split("=")[0].strip()
            headerList.append(attribute)
    return headerList

def getValueListFromINI(filename: str) -> [str]:
    fileList = []
    with open(filename) as inputFile:
        for line in inputFile:
            attribute = line.split('=')[1].strip()
            fileList.append(attribute)
    return fileList

def formatCSVLine(list: [str]) -> str:
    string = list[0]
    for i in range(1, len(list)):
        string += f", {list[i]}"
    return string

def writeToCSV(folderName: str, outputFile: str, addFileName=True):
    fileList = getFileList(folderName)

    with open(outputFile, 'w') as outputFile:
        if addFileName:
            outputFile.write(formatCSVLine(getHeaderListFromINI(fileList[0])))
        else:
            outputFile.write(formatCSVLine(getHeaderListFromINI(fileList[0], False)))

        outputFile.write('\n')
        # for loop iterating through each file
        for inputFile in fileList:
            if addFileName:
                outputFile.write(inputFile.split('/')[1] + ', ')
            outputFile.write(formatCSVLine(getValueListFromINI(inputFile)))
            outputFile.write('\n')

if __name__ == "__main__":
    folderName = input('Folder Name: ')
    outputFileName = input('Ouput CSV filename: ')

    fileNameFlag = input('Add filename to csv? (y/n): ')
    if fileNameFlag == 'y':
        writeToCSV(folderName, outputFileName)
    elif fileNameFlag == 'n':
        writeToCSV(folderName, outputFileName, False)
    else:
        print('Invalid choice')
        exit(1)