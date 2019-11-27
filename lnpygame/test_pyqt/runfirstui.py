import sys
from PyQt5.QtWidgets import QApplication,QMainWindow

from mytest import Ui_MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mw = QMainWindow()

    myui = Ui_MainWindow()

    myui.setupUi(mw)

    mw.show()

    sys.exit(app.exec_())