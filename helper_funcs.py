##                              Helper Functions Script

##                         Contains functions that run when
##                  Certain events of the Youtube Video Downloader App
##                                  are triggered

# IMPORTS
import requests, os
from tkinter import *
from tkinter import messagebox
from pytube import YouTube

# CUSTOM FUNCTIONS
def show_error(title, error_message):
    """Show a GUI error message."""

    box = Tk() #Create Tkinter Window Object
    box.withdraw() #Hide Tkinter Window Object
    messagebox.showerror(title, error_message) #Show pop up
    box.destroy()

def check_valid_URL(link):
    """Checks link is a valid youtube URL."""

    if len(link) == 0:
        return False

    else:
    
        try:
            YouTube(link)

        except:
            return False

        else:
            return True

def check_valid_path(path):
    """Check the given path is valid for Windows."""

    # If the length of the given path is 0, assume it is the local folder
    if len(path) == 0:
        return True

    else:
        return os.path.isdir(path)

    
