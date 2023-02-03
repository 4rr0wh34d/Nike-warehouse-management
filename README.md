# Final_capstone

## Table of Content
- Project Name
- Description
- Installation
- Usage
- Credits

## Project name :
inventory.py

## Description :
This project is a warehouse management system for Nike sporting company. It allows the user to manage the warehouse efficiently and saves delivery time.
The project consist of several functionalities including reading shoe data from the file, viewing shoe data, restocking shoe, searching for the shoeand adding new shoe details.The project is based on the concept of object oriented programming.

## Installation:
### For windows:
1. Firstly download and install a python interpreter from https://www.python.org/downloads/ . Select the correct OS before downloading.
2. Open up the command prompt and navigate to project folder and install the module name Tabulate using command  : `pip install modulate` 
   - Make sure to install pip first by downloading 'get-pip.py' files from https://bootstrap.pypa.io/get-pip.py 
   - open up command prompt and navigate to the folder where the above file is downloaded and run the command : `python get-pip.py`
3. Finally run the command `python inventory.py`
### For Linux:
Normally python comes bundled with linux. To check if python is installed on your system. Just open up your terminal and type
`python --version`

If python is not installed then follow the commands below to install python, pip and modulate module.

```
sudo apt-get update && apt-get upgrade -y
sudo apt-get install python3
sudo apt-get install python3-pip
sudo pip3 install modulate
```


Finally navigate to the file folder and type
`sudo python inventory.py`


## Usage:
The project is fairly simple and easy to use. Once all the installation is done. Simply navigate to a project folder either from your IDE or command Prompt.
If using command prompt, type python followed by the file name ie, > python inventory.py to execute the file and if using IDE simply click the run button on your IDE. 
- After running, the program provides you with a lists of menu to select from. To read a file from a computer simply enter 'r'(make sure you do have a file to read the inventory data on the same folder).

![File read](/read_file.jpg)
- To capture data from user simply follow the prompt and enter the details to be provided.
 
![Capture Input](/capture.jpg)
- To view a list of inventory simply type 'v' and enter.
 
![view All](/view_file.jpg)
- To restock shoe inventory simple enter 'rs'.
 
![Search shoe](/restock.jpg)
- Enter 's' to search for the shoe.

![Search Shoe](/search_shoe.jpg)
- To find the total value of each shoe enter 'tv'.
 
![Total Value](/read_file.jpg)
- Finally enter 'hq' to get the highest quantity shoe.
 
![Highest quantity](/read_file.jpg)

## Credits
Thanks to the lecturer,mentor and whole of hyperiondev team without whom this project would not have been possible.
