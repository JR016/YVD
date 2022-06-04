###                                                                             YT Frame

###                                                                 Tkinter Frame that will contain all
###                                                                 interactive widgets to download videos

# Imports
from tkinter import *

# Use OOP to configure yout own Tk frame
class YT_Frame(Frame):
    """Frame for the Tkinter Youtube Downloader."""

    def __init__(self, master, yt_downloader):
        """Instantiate this Youtube Downloader Frame."""

        # Call parent's constructor
        super(YT_Frame, self).__init__(master)

        # Save the Youtube Download Manager as a public attribute
        self.yt_downloader = yt_downloader

        # Save the master of this Tk frame
        self.master = master

        # Place widgets on screen
        self.build_UI()

    def build_UI(self):
        """Builds the widgets of this frame."""

        # Label that indicates the user to enter a Youtube URL
        Label(self, text = "Youtube Link").grid(row = 0, column = 0, sticky = "e")

        # Link entry widget
        self.yt_link = Entry(self, width = 60)
        self.yt_link.grid(row = 0, column = 1, columnspan = 2, padx = 10, pady = 10)

        # Download button
        self.download_btn = Button(self, text = "Download", width = 20, command = self.download_event)
        self.download_btn.grid(row = 1, column = 2, sticky = "e", padx = 10, pady = (0, 10))

        # Pause/Resume button
        self.pause_resume_btn = Button(self, text = "Pause", width = 10, command = self.pause_resume_event)
        self.pause_resume_btn.grid(row = 2, column = 0)

        # Show the download progress
        self.progress_label = Label(self)
        self.progress_label.grid(row = 2, column = 1, sticky = "w")

        # Cancel button
        self.cancel_btn = Button(self, text = "Cancel", width = 10, command = self.cancel_event)
        self.cancel_btn.grid(row = 2, column = 2, sticky = "e")

    def download_event(self):
        """Download Button Event Triggerer."""

        # Start the download
        self.yt_downloader.start_download(self.yt_link.get(), self.progress_label)

    def cancel_event(self):
        """Cancel Button Event Triggerer."""

        # Cancel the download
        self.yt_downloader.cancel_download()

    def pause_resume_event(self):
        """Pause/Resume Button Event Triggerer."""

        # Pause/Resume the download
        self.yt_downloader.pause_resume_download()

        # Change the text of the pause/resume button according to the paused state
        self.pause_resume_btn["text"] = "Resume" if self.yt_downloader.is_paused else "Pause"



            
    
