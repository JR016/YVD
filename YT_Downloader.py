###                                                                         Youtube Downloader

###                                                 Manages how Youtube Videos are Downloaded

# Imports
import threading, os
from pytube import YouTube, request

# Custom class to manage Youtube Video Downloads
class YT_Downloader(object):
    """Manages Youtube Video Downloads."""

    def __init__(self):
        """Initialize this TY_Downloader."""

        # Set states of download
        self.__is_complete = False
        self.__is_downloading = False
        self.__is_paused = False
        self.__is_cancelled = False

    def __download(self, yt_link, displayer = None):
        """Download Youtube video from the provided URL."""

        try:

            print("Downloading")

            # Create a local Youtube Object
            yt_object = YouTube(yt_link)

            # Create the Youtube stream to use
            yt_stream = yt_object.streams.get_highest_resolution()

            # Get the video file size
            self.__yt_size = yt_stream.filesize

            # Generate the download video
            with open("yt_vid.mp4", "wb") as yt_vid:

                # Set the downloading state to True
                self.__downloading = True
                self.__is_complete = False
                self.__is_cancelled = False
                self.__is_paused = False

                # Request an iterable stream obkect
                yt_iter_stream = request.stream(yt_stream.url)

                # Set the initial file size of the download video to zero
                self.__downloaded = 0

                displayer["text"] = "Download Progress: 0%"

                # Set the while loop used to download the video
                while True:

                    # Cancel video download if user requires it
                    if self.__is_cancelled:
                        displayer["text"] = "Download Cancelled"
                        break

                    # Pause video download if user wants to
                    if self.__is_paused:
                        displayer["text"] = "Download Paused"
                        continue

                    # Get the next video chunk
                    vid_chunk = next(yt_iter_stream, None)

                    # If there is a chunk, write it to the downloading video file
                    if vid_chunk:
                        yt_vid.write(vid_chunk)

                        self.__downloaded += len(vid_chunk)
                        if displayer != None:
                            displayer["text"] = f"Download Progress: {round(float(self.__downloaded / self.__yt_size) * 100, 2)}%"
                            
                        print(f"Bytes downloaded: {self.__downloaded}")
                        print(f"File size: {self.__yt_size}")

                    else:
                        print("Download completed")
                        displayer["text"] = "Download Completed"
                        break
            

        except Exception as e:
            print(e)

        
        print("Outside the downloading loop")
        self.__downloading = False
        self.__is_complete = True

        if self.__is_cancelled:
            
            # Delete the download video as the user does not want it in his/her system
            os.remove("yt_vid.mp4")

    def start_download(self, yt_link, displayer = None):
        """Start downloading the Youtube video."""

        print("Download started")
        #self.__download(yt_link, displayer)

        # This code makes it possible for the download and the GUI to work together
        threading.Thread(target = self.__download,
                         args = (yt_link, displayer, ),
                         daemon = True).start()

    def cancel_download(self):
        """Cancel downloading Youtube video"""

        print("Download cancelled")
        self.__is_cancelled = True

    def pause_resume_download(self):
        """Pause or resume download"""
        
        self.__is_paused = not self.__is_paused
        print(f"Download is paused {self.__is_paused}")

    @property
    def video_size(self):
        """Return the size of the youtube video."""
        return self.__yt_size

    @property
    def bytes_downloaded(self):
        """URL of the youtube video."""
        return self.__downloaded

    @property
    def is_complete(self):
        """Returns whether the download is complete or not."""
        return self.__is_complete

    @property
    def is_downloading(self):
        """Returns whether the download is going on or not."""
        return self.__is_downloading

    @property
    def is_paused(self):
        """Returns whether the download is paused or not."""
        return self.__is_paused

    @property
    def is_cancelled(self):
        """Returns whether the download is cancelled or not."""
        return self.__is_cancelled
        
