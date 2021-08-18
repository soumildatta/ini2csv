# INItoCSV
![](https://img.shields.io/badge/python-3.9-green)
</br></br>
This is a simple utility script that converts a folder of .ini files with identical keys to a csv file. The keys of the .ini files becomes the header of the csv file, and the values of each file becomes a row.

## Usage
To run this script, open a terminal and type:   
```python INItoCSV.py <outputFileName> <list of files separated by spaces>```    
<br/>
Replace <outputFileName> with the output csv file name including the .csv extention. Here is an example run of the program with the correct arguments:     
```python INItoCSV.py convertedINI.csv file1.ini file2.ini file3.ini file4.ini```      
  <br/>
The addition of files as arguments can be simplified by letting bash expand the path for you with the use of \*. An example is shown below, where the .ini files are persent in a folder called "Test":    
```python INItoCSV.py convertedINI.csv Test/*.ini```    
Test/*.ini will expand to the path of each of the .ini file inside the "Test" folder. 
