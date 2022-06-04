###                                                                             Main File

###                                            The whole Tkinter Youtube Downloader runs here

# Imports
from tkinter import *
from YT_Frame import YT_Frame
from YT_Downloader import YT_Downloader

def main():
    """Execute the whole Tkinter Youtube Downloader."""

    # Create Tk window
    root = Tk()

    # Change default title
    root.title("Prototype Youtube Downloader")

    # Initiate a Youtube Downloader Object
    yt_downloader = YT_Downloader()

    # Create an instance of the Youtube Frame to use
    yt_frame = YT_Frame(root, yt_downloader)

    # Place the Frame in the first row and column
    yt_frame.grid(row = 0, column = 0)

    # Run mainloop
    root.mainloop()


# Only run main() if the file is directly invoked
if __name__ == "__main__":
    main()
