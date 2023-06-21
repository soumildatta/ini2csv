# Author: Soumil Datta
from typing import Dict, List
import os
import sys

masterHeaderList = ['INIFileName']

def _getMasterHeaderListFromINI(fileList: List[str]) -> List[str]:
    '''Make a pass through all files adding to the master header list'''
    for inputFile in fileList:
        with open(inputFile) as currentFile:
            for line in currentFile:
                key = line.split("=")[0].strip()
                if not key in masterHeaderList:
                    masterHeaderList.append(key)
    return masterHeaderList


def _getValueDictFromINI(filename: str) -> Dict[str, str]:
    '''Returns a string list of the values in a specified ini file'''
    fileDict = {}
    with open(filename) as inputFile:
        for line in inputFile:
            entry = line.split('=')
            key = entry[0].strip()
            value = entry[1].strip()
            fileDict[key] = value
    return fileDict


def _formatCSVLine(list: List[str]) -> str:
    '''Adds the proper commas and spaces to a list of strings'''
    string = list[0]
    for i in range(1, len(list)):
        string += f", {list[i]}"
    return string


def _processValueDictToString(filename: str, valueDict: Dict[str, str]) -> str:
    '''Uses the key, value dictionary to check against the masterHeaderList and output the string'''
    string = filename
    for i in range(1, len(masterHeaderList)):
        key = masterHeaderList[i]
        # add nothing if value does not exist for key
        string += f", {valueDict.get(key, '')}"
    return string

def _write_to_csv(outputFile: str, fileList: List[str]):
    '''Writes entries for each file into the output CSV file'''
    with open(outputFile, 'w') as outputFile:
        outputFile.write(_formatCSVLine(_getMasterHeaderListFromINI(fileList)))
        outputFile.write('\n')

        for inputFile in fileList:
            # Get the filename for the first column
            filename = inputFile.split('/')[1]
            valueDict = _getValueDictFromINI(inputFile)
            outputFile.write(_processValueDictToString(filename, valueDict))
            outputFile.write('\n')

def process_folder(folder_name: str, output_filename: str):
    '''Processes a folder of .ini files into an output .csv file'''
    files = [f'{folder_name}/{file}' for file in os.listdir(folder_name)]
    _write_to_csv(output_filename, files)

def process_files(file_names: List[str], output_filename: str):
    '''Process a list of .ini files into an output .csv file'''
    _write_to_csv(output_filename, file_names)