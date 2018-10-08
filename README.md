# Desktop-Wallpaper-Changer

## Purpose

This python program automatically changes the desktop wallpaper daily. All you need to do is add `pybat0.bat` file to the startups folder. 

## Getting Started

### Windows
 1. Fire up a command prompt by typing "command prompt" on start menu.
 2. Set up a python virtual environment by issuing command on the cmd, `python -m venv venv`
 3. Then, activate the virtual environment: `venv\Scripts\activate` 
 4. Run: `pip install -r requirements.txt` to install the dependencies.
 5. To test if it works on your system, just run the program: `python sample1.py`
 6. Once you are happy, add this batch file to the Startups folder.
 7. The system will run it daily whenever the system starts, and the picture will be downloaded when there's internet connection.
 8. Then it will be kept as the desktop wallpaper.

### Working

The file will run on system boot and the image will be downloaded when the internet is connected.

### Limitations
#### Operating System
Windows Only

## Report an Issue:

If you come across a problem, create a new issue [here](https://github.com/amrs-tech/Desktop-Wallpaper-Changer/issues)
