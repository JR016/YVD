#                                   Main Script

#                       It is where the whole GUI is run

import YD_Logic, YD_UI
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = YD_Logic.YDMainWindow()
    ui = YD_UI.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
