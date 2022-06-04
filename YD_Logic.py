##                                  YD Logic

##              It is where all the logic and event handling of the
##                          Youtube Video Downloader goes

# Imports
import helper_funcs, os
from PyQt5 import QtCore, QtGui, QtWidgets
from pytube import YouTube

class YDMainWindow(QtWidgets.QMainWindow):
    """Main Window of the YVD."""

    def __init__(self, yt_downloader):
        """Initialize this YVD Main Window."""

        # Call the parents constructor
        super(YDMainWindow, self).__init__()

        # Save the URL of the Youtube Video
        self.__videoURL = ""

        # Save where the video will be downloaded
        self.__saveFolder = ""

        # Save the Youtube Downloader Object
        self.__yt_downloader = yt_downloader

    def __check_for_download(self, inputToCheck):
        """Checks user input is appropiate for download"""

        # Get the text for every Text Input PyQt5 Widget
        self.__videoURL = inputToCheck["URL"].toPlainText().strip()
        self.__saveFolder = inputToCheck["Location"].toPlainText().strip()

        # Check the given URL is valid            
        if not helper_funcs.check_valid_URL(self.__videoURL):
            helper_funcs.show_error("Youtube Link Error", "The given link does not correspond to an avaliable Youtube video.")
            return False
        
        # Check the given path is valid (If a path was given)
        elif not helper_funcs.check_valid_path(self.__saveFolder):
            helper_funcs.show_error("Saving Location Error", "The given folder does not exist in your system.")
            return False

        # All checks have been successful by this point, so return True for sucessful
        else:
            return True
        

    def browse_system(self, textEdit):
        """Browse the user's folder system."""
        self.__saveFolder = QtWidgets.QFileDialog.getExistingDirectory(self,
                                                                       'Select video folder:',
                                                                       os.getcwd(),
                                                                       QtWidgets.QFileDialog.ShowDirsOnly)
        # Write the folder location on the location Text Edit
        textEdit.setText(self.__saveFolder)
        

    def download_operations(self, givenWidgets):
        """Check if user input is valid for download and proceed to download the video."""

        # Check the input the user entered is appropiate
        if self.__check_for_download(givenWidgets) and not (self.__yt_downloader.is_downloading or self.__yt_downloader.is_paused):
            
            # Display the Quit and the Pause Buttons
            givenWidgets["Cancel"].show()
            givenWidgets["Pause"].show()

            # Hide the download Button
            givenWidgets["Download"].hide()
            

    def cancel_operations(self, givenWidgets):
        """Cancel downloading the Youtube Video by user request"""

        # Hide this button and the pause button
        givenWidgets["Cancel"].hide()
        givenWidgets["Pause"].hide()

        # Show the download Button
        givenWidgets["Download"].show()

    def pause_or_resume(self, givenWidgets):
        """Pause or resume to download as indicated by the user."""

        # Change the text of the button
        if givenWidgets["Pause"].text() == "Pause":
            givenWidgets["Pause"].setText("Resume")

        else:
            givenWidgets["Pause"].setText("Pause")
        
        
        
