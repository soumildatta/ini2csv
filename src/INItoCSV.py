# Author: Soumil Datta
from fileinput import filename
from typing import Dict, List
import os
import sys

masterHeaderList = ['INIFileName']

# Make a pass through all files adding to the master header list
def getMasterHeaderListFromINI(fileList: List[str]) -> List[str]:
    for inputFile in fileList:
        with open(inputFile) as currentFile:
            for line in currentFile:
                key = line.split("=")[0].strip()
                if not key in masterHeaderList:
                    masterHeaderList.append(key)
    return masterHeaderList


# Returns a string list of the values in a specified ini file
def getValueDictFromINI(filename: str) -> Dict[str, str]:
    fileDict = {}
    with open(filename) as inputFile:
        for line in inputFile:
            entry = line.split('=')
            key = entry[0].strip()
            value = entry[1].strip()
            fileDict[key] = value
    return fileDict


# Adds the proper commas and spaces to a list of strings
def formatCSVLine(list: List[str]) -> str:
    string = list[0]
    for i in range(1, len(list)):
        string += f", {list[i]}"
    return string


# Uses the key, value dictionary to check against the masterHeaderList and output the string
def processValueDictToString(filename: str, valueDict: Dict[str, str]) -> str:
    string = filename
    for i in range(1, len(masterHeaderList)):
        key = masterHeaderList[i]
        # add nothing if value does not exist for key
        string += f", {valueDict.get(key, '')}"
    return string


# Write entries for each file into the output CSV file
def writeToCSV(outputFile: str, fileList: List[str]):
    with open(outputFile, 'w') as outputFile:
        outputFile.write(formatCSVLine(getMasterHeaderListFromINI(fileList)))
        outputFile.write('\n')

        for inputFile in fileList:
            # Get the filename for the first column
            filename = inputFile.split('/')[1]
            valueDict = getValueDictFromINI(inputFile)
            outputFile.write(processValueDictToString(filename, valueDict))
            outputFile.write('\n')

# Process a folder of .ini files into an output .csv file
def process_folder(folder_name: str, output_filename: str):
    files = [f'{folder_name}/{file}' for file in os.listdir(folder_name)]
    writeToCSV(output_filename, files)

# Process a list of .ini files into an output .csv file
def process_files(file_names: List[str], output_filename: str):
    writeToCSV(output_filename, file_names)