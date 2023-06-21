# INItoCSV
![](https://img.shields.io/badge/python-3.9-lgreen)
</br></br>
 A simple utility that converts and combines a folder of .ini files with identical keys into one csv file. The keys of the .ini files become the headers of the csv file, and the values of each file become a row.

## Package Installation and Usage
INItoCSV is available on PyPI and can be installed using __pip__:
```
pip install initocsv
```

To use INItoCSV, the library needs to first be imported in your project:
```
import initocsv
```

### Included functions
INItoCSV has two main functions: `processFolder` and `processFiles`
Each of these functions take two arguments. `processFolder` takes in the __folder name__ and __output .csv file name__ as arguments. `processFiles` similarly takes __a list of file names__ and __output .csv file name__ as arguments.
```py
# Argument list
processFolder(folderName: str, outputFilename: str)
processFiles(fileNames: List[str], outputFilename: str)
```

## Use Case
Suppose you have a folder of .ini files, where each file contains data for one instance of an item. Each file thus represents one row in a .csv file, and each key in the file represents the headers in the .csv file. A folder of such .ini files can then be converted into a csv file and saved for ease of other pre-existing data-processing pipelines.