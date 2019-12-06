from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class MyMessageBox(QWidget):

    def __init__(self):
        super(MyMessageBox,self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('提示')
        self.resize(200,100)
        total_layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        self.yesbutton = QPushButton('确认')
        self.yesbutton.clicked.connect(self.yesfunc)

        self.nobutton = QPushButton('取消')
        self.nobutton.clicked.connect(self.nofunc)

        self.info_lable = QLabel('你是否希望重新开始游戏?')

        button_layout.addWidget(self.yesbutton)
        button_layout.addWidget(self.nobutton)

        total_layout.addWidget(self.info_lable)
        total_layout.addLayout(button_layout)

        self.setLayout(total_layout)

    def yesfunc(self):
        print(self.sender().text())

    def nofunc(self):
        self.close()

app = QApplication(sys.argv)
mmb = MyMessageBox()
mmb.show()
sys.exit(app.exec_())