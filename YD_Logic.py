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

        # Save the current folder location
        self.__saveFolder = ""

    def browse_system(self, textEdit):
        """Browse the user's folder system."""
        self.__saveFolder = QtWidgets.QFileDialog.getExistingDirectory(self,
                                                                       'Select project folder:',
                                                                       'C:\\Users',
                                                                       QtWidgets.QFileDialog.ShowDirsOnly)
        # Write the folder location on the location Text Edit
        textEdit.setText(self.__saveFolder)
        
