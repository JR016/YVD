##                                  YD Logic

##              It is where all the logic and event handling of the
##                          Youtube Video Downloader goes

# Imports
import helper_funcs
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

    def __check_for_download(self, inputToCheck):
        """Checks user input is appropiate for download"""

        # Get the text for every Text Input PyQt5 Widget
        self.__videoURL = inputToCheck["URL"].toPlainText()
        self.__saveFolder = inputToCheck["Location"].toPlainText()

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
                                                                       'Select project folder:',
                                                                       'C:\\Users',
                                                                       QtWidgets.QFileDialog.ShowDirsOnly)
        # Write the folder location on the location Text Edit
        textEdit.setText(self.__saveFolder)

    def download_operations(self, inputToCheck):
        """Check if user input is valid for download and proceed to download the video."""

        # Check the input the user entered is appropiate
        if self.__check_for_download(inputToCheck):
            pass
        
        
