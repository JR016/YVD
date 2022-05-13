##                                  YD Logic

##              It is where all the logic and event handling of the
##                          Youtube Video Downloader goes

# Imports
import helper_funcs, os
from PyQt5 import QtCore, QtGui, QtWidgets

class YDMainWindow(QtWidgets.QMainWindow):
    """Main Window of the YVD."""

    def __init__(self):
        """Initialize this YVD Main Window."""

        # Call the parents constructor
        super(YDMainWindow, self).__init__()

        # Save the URL of the Youtube Video
        self.__videoURL = ""

        # Save where the video will be downloaded
        self.__saveFolder = ""

        # Downloading status of the App
        self.__is_downloading = False

        # Pause status of the app
        self.__is_paused = False

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
        if self.__check_for_download(givenWidgets) and not (self.__is_downloading or self.__is_paused):

            # Set the downloading status to True
            self.__is_downloading = True
            
            # Display the Quit and the Pause Buttons
            givenWidgets["Cancel"].show()
            givenWidgets["Pause"].show()
            

    def cancel_operations(self, givenWidgets):
        """Cancel downloading the Youtube Video by user request"""

        # If there is a download, stop it
        if self.__is_downloading:

            # Hide this button and the pause button
            givenWidgets["Cancel"].hide()
            givenWidgets["Pause"].hide()

            # Set the downloading state to False
            self.__is_downloading = False

    def pause_or_resume(self, givenWidgets):
        """Pause or resume to download as indicated by the user."""

        # Change the text of the button
        if givenWidgets["Pause"].text() == "Pause":
            givenWidgets["Pause"].setText("Resume")
            self.__is_downloading = False
            self.__is_pause = True

        else:
            givenWidgets["Pause"].setText("Pause")
            self.__is_downloading = True
            self.__is_pause = False
        
        
        
