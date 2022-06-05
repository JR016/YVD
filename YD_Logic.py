##                                                                  YD Logic

##                                      It is where all the logic and event handling of the
##                                              Youtube Video Downloader goes

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

        # Save the name of the vide file
        self.__videoName = ""

        # Save the Youtube Downloader Object
        self.__yt_downloader = yt_downloader

    def browse_system(self, textEdit):
        """Browse the user's folder system."""
        self.__saveFolder = QtWidgets.QFileDialog.getExistingDirectory(self,
                                                                       'Select video folder:',
                                                                       os.getcwd(),
                                                                       QtWidgets.QFileDialog.ShowDirsOnly)
        # Write the folder location on the location Text Edit
        textEdit.setText(self.__saveFolder)

    def __check_for_download(self, inputToCheck):
        """Checks user input is appropiate for download"""

        # Get the text for every Text Input PyQt5 Widget
        self.__videoURL = inputToCheck["URL"].toPlainText().strip()
        self.__saveFolder = inputToCheck["Location"].toPlainText().strip()
        self.__videoName = inputToCheck["Name"].toPlainText().strip()

        # Check the given URL is valid            
        if not helper_funcs.check_valid_URL(self.__videoURL):
            helper_funcs.show_error("Youtube Link Error", "The given link does not correspond to an avaliable Youtube video.")
            return False
        
        # Check the given path is valid (If a path was given)
        elif not helper_funcs.check_valid_path(self.__saveFolder):
            helper_funcs.show_error("Saving Location Error", "The given folder does not exist in your system.")
            return False

        # Check the user gave a name for its video file
        elif len(self.__videoName) == 0:
            helper_funcs.show_error("Video Name Error", "No name was provided for the video to be downloaded.")
            return False

        # All checks have been successful by this point, so return True for sucessful
        else:
            return True      

    def download_operations(self, givenWidgets):
        """Check if user input is valid for download and proceed to download the video."""

        # Check the input the user entered is appropiate
        if self.__check_for_download(givenWidgets):

            # Show the appropiate wdigets when there is a download
            self.__on_download(givenWidgets)

            # Get the entire name for the file to download
            complete_filename = os.path.join(self.__saveFolder, self.__videoName) + ".mp4"

            # Give to the downloader relevant widgets to manage on the downloading process
            downloading_widgets = {
                "Download"     : givenWidgets["Download"],
                "Cancel"         : givenWidgets["Cancel"],
                "Pause"          : givenWidgets["Pause"],
                "ProgressBar" : givenWidgets["ProgressBar"]}

            # Set the text of the Pause Button always to pause before any download
            if self.__yt_downloader.is_paused:
                givenWidgets["Pause"].setText("Resume")

            else:
                givenWidgets["Pause"].setText("Pause")

            # Start the download
            self.__yt_downloader.start_download(self.__videoURL,
                                                complete_filename,
                                                downloading_widgets)

    def cancel_operations(self, givenWidgets):
        """Cancel downloading the Youtube Video by user request"""

        # Show the appropiate widgets when there is no download
        self.__off_download(givenWidgets)

        # Pop up to the user the download progress will be discarded
        helper_funcs.show_info("Download cancelled", "Your download progress will be eliminated.")

        # Cancel the download
        self.__yt_downloader.cancel_download()

    def pause_or_resume(self, givenWidgets):
        """Pause or resume to download as indicated by the user."""

        # Change the text of the button
        if givenWidgets["Pause"].text() == "Pause":
            givenWidgets["Pause"].setText("Resume")

        else:
            givenWidgets["Pause"].setText("Pause")

        # Pause or Resume the download
        self.__yt_downloader.pause_resume_download()

    def __on_download(self, widgets):
        """Control which widgets to show while a download is going on."""

        # Hide the Download Button
        widgets["Download"].hide()

        # Show the Cancel and Pause Buttons as well as the ProgressBar
        widgets["Cancel"].show()
        widgets["Pause"].show()
        widgets["ProgressBar"].show()
        widgets["ProgressBar"].setValue(0)

    def __off_download(self, widgets):
        """Control which widgets to show while there is not a download going on."""

        # Show the Download Button
        widgets["Download"].show()

        # Hide the Cancel and Pause Buttons as well as the ProgressBar
        widgets["Cancel"].hide()
        widgets["Pause"].hide()
        widgets["ProgressBar"].hide()
        
