# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ctof.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(24, 84, 355, 80))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.lineEdit_C = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_C.setObjectName("lineEdit_C")
        self.gridLayout.addWidget(self.lineEdit_C, 1, 0, 1, 1)
        self.lineEdit_F = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_F.setObjectName("lineEdit_F")
        self.gridLayout.addWidget(self.lineEdit_F, 1, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.myconnect()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "C_TO_F"))
        self.pushButton_2.setText(_translate("Form", "F_TO_C"))
        self.label.setText(_translate("Form", "摄氏度:"))
        self.label_2.setText(_translate("Form", "华氏度:"))

    def myconnect(self):
        self.pushButton.clicked.connect(self.myctof)
        self.pushButton_2.clicked.connect(self.myftoc)

    def myctof(self):
        # print('in ctof')
        #1 获取lineEdit_C中的值
        c_str = self.lineEdit_C.text()
        if not c_str:
            print('no valid input num')
            return
        else:
            c_num = float(c_str)
        # print(c_str)

        #2 转换为F
        f_num = c_num*9.0/5+32

        #3 放到lineEdit_F中
        self.lineEdit_F.setText("%.2f"%float(f_num))

    def myftoc(self):
        # print('in ftoc')
        f_str = self.lineEdit_F.text()
        if not f_str:
            print('no valid input num')
            return
        else:
            f_num = float(f_str)

        #2 转换为F
        c_num = (f_num-32)*5/9.0

        #3 放到lineEdit_F中
        self.lineEdit_C.setText("%.2f"%float(c_num))