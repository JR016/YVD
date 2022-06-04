###                                                                                                                                                 By Bit Script

###                                                                                                         Example code on how to download youtube videos by chunks
###                                                                                                                                                 using pytube

# Imports
import tkinter as tk
import threading
from pytube import YouTube, request

# Detect when the download is paused or canceled
is_paused = False
is_cancelled = False

def download_video(url):
    """Execute all required Youtube video download operations."""

    # State the global variables to use
    global is_paused, is_cancelled

    # Set states of interactive buttons when download starts
    download_button["state"] = "disabled"
    pause_button["state"] = "normal"
    cancel_button["state"] = "normal"

    # Try to download the Youtube video chunk by chunk
    try:
        # Show the download status
        progress["text"] = "Connecting ..."

        # Create the Youtube Object
        yt = YouTube(url)

        # Create the Youtube stream to use
        stream = yt.streams.get_highest_resolution()

        # Get the video total file size
        filesize = stream.filesize

        # Generate the downloaded video file
        with open("sample.mp4", "wb") as f:

            #  Reset the cancel and pause states
            is_paused = False
            is_cancelled = False

            # Request an iterable stream
            iter_stream = request.stream(stream.url)

            # Set the initial file size of the downloaded video to zero
            downloaded = 0

            # Set a loop to loop through all the video chunks until they are all downloaded
            while True:

                # Cancel video download if user wants it to
                if is_cancelled:
                    progress["text"] = "Download cancelled"
                    break

                # Pause video download if user wants it to
                if is_paused:
                    continue

                # Get the next video chunk
                chunk = next(iter_stream, None)

                # If there is a chunk, write it to the downloading video file
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    progress["text"] = f"Downloaded {downloaded}"

                # If there are no more chunks, download is completed and loop must be broken
                else:
                    progress["text"] = "Download completed"
                    break

        print("Done")

    # Catch error message and display it
    except Exception as e:
        print(e)


    # Set the button states to be ready for download
    download_button["state"] = "normal"
    pause_button["state"] = "disabled"
    cancel_button["state"] = "disabled"


def start_download():
    """Event to trigger when user clicks the 'Download' button."""
    threading.Thread(target = download_video,
                     args = (url_entry.get(), ), daemon = True).start()


def toggle_download():
    """Change pause/resume state Event."""

    # Change the value of the variable that manages the paused state
    global is_paused

    # Reverse the current value of the variable
    is_paused = not is_paused

    # Change the text in the pause/resume button
    pause_button["text"] = "Resume" if is_paused else "Pause"

def cancel_download():
    """Event to trigger when user clicks the 'Cancel' button."""
    global is_cancelled
    is_cancelled = True


# Create Tk Window
root = tk.Tk()
root.title("Youtube Downloader.")

# Set Widgets to Get the Video URL
tk.Label(root, text = "URL:").grid(row = 0, column = 0, sticky = "e")

url_entry = tk.Entry(root, width = 60)
url_entry.grid(row = 0, column = 1, columnspan = 2, padx = 10, pady = 10)

download_button = tk.Button(root, text = "Download", width = 20, command = start_download)
download_button.grid(row = 1, column = 2, sticky = "e", padx = 10, pady = (0,10))

pause_button = tk.Button(root, text = "Pause", width = 10, command = toggle_download, state = "disabled")
pause_button.grid(row = 2, column = 0)

progress = tk.Label(root)
progress.grid(row = 2, column = 1, sticky = "w")

cancel_button = tk.Button(root, text = "Cancel", width= 10, command = cancel_download, state = "disabled")
cancel_button.grid(row = 2, column = 2, sticky = "e")

# Call the mainloop of the Tk
root.mainloop()
            
