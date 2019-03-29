[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](Python_Scripts/LICENSE)
# Python_Scripts
Python Scripts That I Make Now And Then To Help Me With Various Tasks.<br/>

## Python Module Updater
The [module_updater.py](Python_Scripts/src/module_updater.py) detects all your python modules that are outdated including the pip and updates them automatically.
### Usage
To put it into action you type <code>python module_updater.py</code>.<br/>
Once you have type the specified command it updates all the outdated modules. You can see the outdated modules in the "modulesToBeUpdated.txt" file.

## Fibonacci Calculator
The [fibonacci.py](Python_Scripts/src/fibonacci.py) calculates the fibonacci of a given number.
### Usage
If you want to see the fibonnaci number of a random number you type <code>python fibonacci.py [desired number]</code>.<br/>
If you want to see the entire fibonnaci sequence until the fibonacci number of your desired number you can type <code>python fibonacci.py [desired number] -f</code>.<br/>
For help you can type <code>python fibonacci.py -h</code>

## Create Folders
The [create_folder.py](Python_Scripts/src/create_folders.py) creates folders in the given path and names them either by numbers either by custom names, given by the user.

### Usage
You can call the script by typing in the cmd <code>python create_folders.py [--outputDirectory OUTPUTDIRECTORY] [-num, --numeric]</code>.<br/>
The "--outputDirectory" argument is necessary because is the path that the new folders will be created.<br/>
The "--numeric", or "-num" for short, is optional. You can use it in order to create numeric folders.<br/>
If you want to give custom names to the folders, just ignore it.<br/>
For help you can type <code>python create_folders.py -h</code>
