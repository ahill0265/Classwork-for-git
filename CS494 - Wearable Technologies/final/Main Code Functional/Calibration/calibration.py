# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calibration.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
minBend = ""
maxBend = ""
state = 0

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1500, 1000)
        self.CalibrationText = QtWidgets.QLabel(Form)
        self.CalibrationText.setGeometry(QtCore.QRect(960, 110, 441, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(40)
        self.CalibrationText.setFont(font)
        self.CalibrationText.setStyleSheet("background-image: url(:/images/transparent.png);")
        self.CalibrationText.setAlignment(QtCore.Qt.AlignCenter)
        self.CalibrationText.setObjectName("CalibrationText")
        self.set_btn = QtWidgets.QPushButton(Form)
        self.set_btn.setGeometry(QtCore.QRect(800, 780, 251, 101))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(25)
        self.set_btn.setFont(font)
        self.set_btn.setStyleSheet("background-color: rgb(238, 17, 51);\n"
"background-image: url(:/images/transparent.png);\n"
"color: rgb(255, 255, 255);")
        self.set_btn.setObjectName("set_btn")
        self.exit_btn = QtWidgets.QPushButton(Form)
        self.exit_btn.setGeometry(QtCore.QRect(1200, 780, 251, 101))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(25)
        self.exit_btn.setFont(font)
        self.exit_btn.setStyleSheet("background-color: rgb(238, 17, 51);\n"
"background-image: url(:/images/transparent.png);\n"
"color: rgb(255, 255, 255);")
        self.exit_btn.setObjectName("exit_btn")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-50, -10, 1601, 1021))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("bend.JPG"))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(-50, -10, 1601, 1021))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("straight.JPG"))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.CalibrationLog = QtWidgets.QTextEdit(Form)
        self.CalibrationLog.setGeometry(QtCore.QRect(800, 450, 651, 311))
        self.CalibrationLog.setObjectName("CalibrationLog")
        self.CalibrationLog.setFontPointSize(16)
        self.curBendText = QtWidgets.QLabel(Form)
        self.curBendText.setGeometry(QtCore.QRect(860, 210, 591, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(40)
        self.curBendText.setFont(font)
        self.curBendText.setStyleSheet("background-image: url(:/images/transparent.png);")
        self.curBendText.setAlignment(QtCore.Qt.AlignCenter)
        self.curBendText.setObjectName("curBendText")
        self.maxBendText = QtWidgets.QLabel(Form)
        self.maxBendText.setGeometry(QtCore.QRect(860, 280, 591, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(40)
        self.maxBendText.setFont(font)
        self.maxBendText.setStyleSheet("background-image: url(:/images/transparent.png);")
        self.maxBendText.setAlignment(QtCore.Qt.AlignCenter)
        self.maxBendText.setObjectName("maxBendText")
        self.minBendText = QtWidgets.QLabel(Form)
        self.minBendText.setGeometry(QtCore.QRect(860, 350, 591, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(40)
        self.minBendText.setFont(font)
        self.minBendText.setStyleSheet("background-image: url(:/images/transparent.png);")
        self.minBendText.setAlignment(QtCore.Qt.AlignCenter)
        self.minBendText.setObjectName("minBendText")
        self.label_2.raise_()
        self.label.raise_()
        self.CalibrationText.raise_()
        self.set_btn.raise_()
        self.exit_btn.raise_()
        self.CalibrationLog.raise_()
        self.curBendText.raise_()
        self.maxBendText.raise_()
        self.minBendText.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.CalibrationText.setText(_translate("Form", "Calibration"))
        self.set_btn.setText(_translate("Form", "Set Value"))
        self.exit_btn.setText(_translate("Form", "Exercises"))
        self.curBendText.setText(_translate("Form", "Current Bend Value"))
        self.maxBendText.setText(_translate("Form", "Bend Value: "))
        self.minBendText.setText(_translate("Form", "Straight Value: "))
        self.CalibrationLog.append("Welcome to calibration! Please bend your leg as much as you can!")
        self.CalibrationLog.append("Then hit the 'Set Value' button.")

    def setCalibrate(self, Form, calibrateState, val):
        if calibrateState == 0:
            Form.maxBendText.setText("Bend Value: " + val)
            Form.CalibrationLog.append("Bend Value > " + val)
            Form.CalibrationLog.append("Nice! Next, straigthen your leg!")
            Form.label.hide()
        elif calibrateState == 1:
            Form.minBendText.setText("Straight Value: " + val)
            Form.CalibrationLog.append("Straight Value > " + val)
            Form.CalibrationLog.append("You're done with calibration!")
            Form.CalibrationLog.append("You can continue to exercises by clicking the exercise button.")
            Form.CalibrationLog.append("Or you can restart calibration again.")
            Form.label.show()
        elif calibrateState == 2:
            Form.minBendText.setText("Straight Value: " + val)
            Form.CalibrationLog.append("Straight Value > " + val)
            Form.CalibrationLog.append("Uh oh! You Straight Value is greater than your Bend Value!")
            Form.CalibrationLog.append("Please restart calibration again.")
            Form.label.show()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
