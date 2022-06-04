from pytube import YouTube
import os

def on_complete(stream, filepath):
    print("Download complete")
    print(filepath)

def on_progress(stream, chunk, bytes_remaining):
    progress_string = f"{round( 100 - (bytes_remaining / stream.filesize * 100), 2)}%"
    print(progress_string)


video_object = YouTube("https://www.youtube.com/watch?v=NtzDjNhPZgU",
                       on_complete_callback = on_complete,
                       on_progress_callback = on_progress)

video_object.streams.get_highest_resolution().download(os.getcwd())
