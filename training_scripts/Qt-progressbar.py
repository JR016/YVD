# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from pytube import YouTube
import sys, time, os, threading

class Example(QWidget):
        """Progressbar Example Window."""

        def __init__(self):
                super().__init__()
                self.initUI()

        def on_complete(self, stream, filepath):
                print("Download complete")
                print(filepath)

        def on_progress(self, stream, chunk, bytes_remaining):
               progress_string = int( 100 - (bytes_remaining / stream.filesize * 100))
               self.pbar.setValue(progress_string)

        def initUI(self):

                self.pbar = QProgressBar(self)
                self.pbar.setGeometry(30, 40, 200, 25)

                # Generate a multi threading object for the download
                download_thread = threading.Thread(target = self.doAction,
                                                   args = (),
                                                   daemon = True)

                self.btn = QPushButton("Start", self)
                self.btn.move(40, 80)
                self.btn.clicked.connect(lambda : download_thread.start())

                self.setGeometry(300, 300, 280, 170)
                self.setWindowTitle("PyQt Progress Bar")
                self.show()

        def doAction(self):
                video_object = YouTube("https://www.youtube.com/watch?v=NtzDjNhPZgU",
                        on_complete_callback = self.on_complete,
                        on_progress_callback = self.on_progress)

                video_object.streams.get_highest_resolution().download(os.getcwd())

if __name__ == "__main__":

        App = QApplication(sys.argv)
        window = Example()
        sys.exit(App.exec())
