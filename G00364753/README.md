## GMIT H.DIP in Data Analytics
### Project for Applied Databases module

This repository contains all of the files pertaining to my project submission for the Applied Databases module of the GMIT H.DIP in Data Analysis program. The main body of work is in the `G00364753` folder. This README.md file is a guide to set up and run the project.

### G00364753 folder contents

The repository contains:
* `MySQL.txt ` - a plain text file containing my answers to section 4.1
* `Nomalisation.pdf` - a pdf file containg my answer to section 4.2
* `MongoDB.txt ` - a plain text file containing my answers to section 4.3
* `Python` - a folder containing my Python code for section 4.4
* this `README.md` file

### Dependancies

The dependencies for the Python Application are:
* Python 3
* pymysql
* pymongo

Installation details for `pymysql` can be found <a href="https://pypi.org/project/PyMySQL/#installation">here</a>.

Installation details for `pymongol` can be found <a href="https://api.mongodb.com/python/current/installation.html">here</a>.

### Instructions for running the software

The software can be downloaded and run on a machine as follows:

* Clone the repository with the following command
```
git clone https://github.com/shkyler/gmit-adb-project.git
```
Note that there are 3 files in the Python folder:
* `main.py` - this is the main file containing the UI functions
* `dbConnect.py` - this manages the connections to the MySql database
* `dbMongo.py` - this manages the connectinos to the MongoDB database

The project script can be run using the following command from the `\G00364753\Python` folder:
```
python main.py
```
