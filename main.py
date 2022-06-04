#                                   Main Script

#                       It is where the whole GUI is run

import YD_Logic, YD_UI, platform, helper_funcs, os
from PyQt5 import QtCore, QtGui, QtWidgets
from YT_Downloader import YT_Downloader

if __name__ == "__main__":
    import sys

    if platform.system() == "Windows":

        # Path to Youtube Icon
        YT_ICON = os.path.join("pics", "youtube.png")
        
        # Execute program only if OS is Windows
        app = QtWidgets.QApplication(sys.argv)

        # Give the YT Downloader to the main window
        yt_downloader = YT_Downloader()
        MainWindow = YD_Logic.YDMainWindow(yt_downloader)

        # Set the window icon
        MainWindow.setWindowIcon(QtGui.QIcon(YT_ICON))

        # Set Window icon in PyQt5
        ui = YD_UI.Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

    else:
        helper_funcs.show_error("OS Error", "The Youtube Video Downloader only works for Windows")
        
