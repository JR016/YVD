###                                                                         Youtube Downloader

###                                                 Manages how Youtube Videos are Downloaded

# Imports
import threading, os, helper_funcs
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

    def __download(self, yt_link, complete_vidName, relevant_widgets):
        """Download Youtube video from the provided URL."""

        try:

            print("Downloading")

            # Set the downloading state to True
            self.__downloading = True
            self.__is_complete = False
            self.__is_cancelled = False
            self.__is_paused = False

            # Create a local Youtube Object
            yt_object = YouTube(yt_link)

            # Create the Youtube stream to use
            yt_stream = yt_object.streams.get_highest_resolution()

            # Get the video file size
            self.__yt_size = yt_stream.filesize

            # Generate the download video
            with open(complete_vidName, "wb") as yt_vid:

                # Request an iterable stream obkect
                yt_iter_stream = request.stream(yt_stream.url)

                # Set the initial file size of the download video to zero
                self.__downloaded = 0

                # Set the while loop used to download the video
                while True:

                    # Cancel video download if user requires it
                    if self.__is_cancelled:
                        break

                    # Pause video download if user wants to
                    if self.__is_paused:
                        continue

                    # Get the next video chunk
                    else:
                        vid_chunk = next(yt_iter_stream, None)

                        # If there is a chunk, write it to the downloading video file
                        if self.__downloaded < self.__yt_size:
                            yt_vid.write(vid_chunk)

                            self.__downloaded += len(vid_chunk)

                            # Show the user the download progress
                            relevant_widgets["ProgressBar"].setValue(int(self.__downloaded / self.__yt_size * 100))
                            print(f"Percentage: {int(self.__downloaded / self.__yt_size * 100)}%")

                        else:
                            print("Download completed")
                            break
            

        except Exception as e:
            print(e)

        
        print("Outside the downloading loop")
        self.__downloading = False

        # Reset the download widgets to their "previous download" state
        relevant_widgets["Download"].show()
        relevant_widgets["Cancel"].hide()
        relevant_widgets["Pause"].hide()
        relevant_widgets["ProgressBar"].hide()

        # Alert to the user the download is complete

        if self.__is_cancelled:
            
            # Delete the download video as the user does not want it in his/her system
            try:
                os.remove(complete_vidName)

            except PermissionError:
                helper_funcs.show_warning("Cancelling Operations Warning", "Your download could not be properly cancelled" \
                                          + "\n\nIf you wish to cancel the download, please close this program and manually delete the download progress.")

        else:
            self.__is_complete = True
            helper_funcs.show_info("Download Complete", f"Your video was successfully downloaded at:\n{complete_vidName}")
            

    def start_download(self, yt_link, complete_vidName, relevantWidgets):
        """Start downloading the Youtube video."""

        print("Download started")

        # This code makes it possible for the download and the GUI to work together
        threading.Thread(target = self.__download,
                         args = (yt_link, complete_vidName, relevantWidgets, ),
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
        
