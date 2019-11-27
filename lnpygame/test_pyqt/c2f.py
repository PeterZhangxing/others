import sys
from PyQt5.QtWidgets import QApplication,QWidget

from ctof import Ui_Form


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mw = QWidget()

    myui = Ui_Form()

    myui.setupUi(mw)

    mw.show()

    sys.exit(app.exec_())