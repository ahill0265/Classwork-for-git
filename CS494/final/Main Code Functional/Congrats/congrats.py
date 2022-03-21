# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'congrats.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1500, 1000)
        Form.setStyleSheet("background-image: url(:/images/congrats.jpg);")
        self.earned_1 = QtWidgets.QLabel(Form)
        self.earned_1.setGeometry(QtCore.QRect(1070, 240, 381, 271))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(30)
        self.earned_1.setFont(font)
        self.earned_1.setStyleSheet("background-image: url(:/images/transparent.png);")
        self.earned_1.setAlignment(QtCore.Qt.AlignCenter)
        self.earned_1.setWordWrap(True)
        self.earned_1.setObjectName("earned_1")
        self.home_btn = QtWidgets.QPushButton(Form)
        self.home_btn.setGeometry(QtCore.QRect(130, 650, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(20)
        self.home_btn.setFont(font)
        self.home_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(224, 22, 61);\n"
"background-image: url(:/images/transparent.png);")
        self.home_btn.setObjectName("home_btn")
        self.exercise_btn = QtWidgets.QPushButton(Form)
        self.exercise_btn.setGeometry(QtCore.QRect(130, 760, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(15)
        self.exercise_btn.setFont(font)
        self.exercise_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(224, 22, 61);\n"
"background-image: url(:/images/transparent.png);")
        self.exercise_btn.setObjectName("exercise_btn")
        self.exit_btn = QtWidgets.QPushButton(Form)
        self.exit_btn.setGeometry(QtCore.QRect(130, 870, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(20)
        self.exit_btn.setFont(font)
        self.exit_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(224, 22, 61);\n"
"background-image: url(:/images/transparent.png);")
        self.exit_btn.setObjectName("exit_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.earned_1.setText(_translate("Form", "You\'ve Earned Some Coupons for Chicken Joy!"))
        self.home_btn.setText(_translate("Form", "HOME"))
        self.exercise_btn.setText(_translate("Form", "KEEP EXERCISING"))
        self.exit_btn.setText(_translate("Form", "EXIT"))
import resources_rc_Congrats


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
