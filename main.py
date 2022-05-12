#                                   Main Script

#                       It is where the whole GUI is run

import YD_Logic, YD_UI, platform, helper_funcs
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    import sys

    if platform.system() == "Windows":
        
        # Execute program only if OS is Windows
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = YD_Logic.YDMainWindow()
        ui = YD_UI.Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

    else:
        helper_funcs.show_error("OS Error", "The Youtube Video Downloader only works for Windows")
        
