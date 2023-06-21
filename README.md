# INI2CSV
![](https://img.shields.io/badge/python-3.9-lgreen)
</br></br>
 A simple utility that converts and combines a folder of .ini files with identical keys into one csv file. The keys of the .ini files become the headers of the csv file, and the values of each file become a row.

## Package Installation and Usage
ini2csv is available on PyPI and can be installed using __pip__:
```
pip install ini2csv
```

To use ini2csv, the library needs to first be imported in your project:
```
import ini2csv
```

### Included functions
ini2csv has two main interface functions: `process_folder` and `process_files`
Each of these functions take two arguments. `process_folder` takes in the __folder name__ and __output .csv file name__ as arguments. `process_files` similarly takes __a list of file names__ and __output .csv file name__ as arguments.
```py
# Argument list
process_folder(folder_name: str, output_filename: str)
process_files(file_names: List[str], output_filename: str)
```

## Use Case
Suppose you have a folder of .ini files, where each file contains data for one instance of an item. Each file thus represents one row in a .csv file, and each key in the file represents the headers in the .csv file. A folder of such .ini files can then be converted into a csv file and saved for ease of other pre-existing data-processing pipelines.