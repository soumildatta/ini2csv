# Author: Soumil Datta
# Script lives inside Results/

import os

def getFileList(folderName: str) -> [str]:
    onlyfiles: [str] = [os.path.join(folderName, file) for file in os.listdir(folderName) if os.path.isfile(os.path.join(folderName, file)) and file.endswith(".INI")]
    return onlyfiles

def getHeaderListFromINI(filename: str) -> [str]:
    headerList = []
    with open(filename) as inputFile:
        for line in inputFile:
            attribute = line.split("=")[0].strip()
            headerList.append(attribute)
    return headerList

def formatCSVLine(list: [str]) -> str:
    string = list[0]
    for i in range(1, len(list)):
        string += f", {list[i]}"
    return string

def writeToCSV(folderName: str, outputFile: str):
    fileList = getFileList(folderName)

    with open(outputFile, 'w') as outputFile:
        outputFile.writelines(formatCSVLine(getHeaderListFromINI(fileList[0])))

if __name__ == "__main__":
    # folderName = input("Folder Name: ")
    folderName = "ConcurrentPoolScalability"
    # print(getFileList(folderName))
    # print(formatCSVLine(getHeaderListFromINI(f"{folderName}/NVIDIA GeForce RTX 3090^ConcurrentPoolScalability^USA-NY.CSR^128^1.INI")))
    writeToCSV(folderName, "test.csv")