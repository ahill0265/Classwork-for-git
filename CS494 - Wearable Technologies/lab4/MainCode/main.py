# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets, QtSerialPort
from pynput.keyboard import Key, Controller, Listener
import time
import pygame
import random

status = 0
lastTime = 0
currentString = []
currentWord = []
newLine = False
wordHistory = []

class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(900, 600))
        Form.setMaximumSize(QtCore.QSize(900, 600))
        Form.setAutoFillBackground(True)
        self.Home_Page = QtWidgets.QFrame(Form)
        self.Home_Page.setGeometry(QtCore.QRect(0, 40, 901, 561))
        self.Home_Page.setAutoFillBackground(True)
        self.Home_Page.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Home_Page.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Home_Page.setObjectName("Home_Page")
        self.SnakeButton = QtWidgets.QPushButton(self.Home_Page, clicked=self.goSnake)
        self.SnakeButton.setGeometry(QtCore.QRect(0, 20, 450, 500))
        self.SnakeButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Snake.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SnakeButton.setIcon(icon)
        self.SnakeButton.setIconSize(QtCore.QSize(450, 500))
        self.SnakeButton.setObjectName("SnakeButton")
        self.MorseButton = QtWidgets.QPushButton(self.Home_Page, clicked=self.goMorse)
        self.MorseButton.setGeometry(QtCore.QRect(450, 20, 450, 500))
        self.MorseButton.setAcceptDrops(False)
        self.MorseButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Morse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MorseButton.setIcon(icon1)
        self.MorseButton.setIconSize(QtCore.QSize(450, 500))
        self.MorseButton.setObjectName("MorseButton")
        self.Connect = QtWidgets.QPushButton(
            Form,
            text="Connect",
            checkable=True,
            toggled=self.on_toggled
        )
        self.Connect.setGeometry(QtCore.QRect(520, 0, 380, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Connect.setFont(font)
        self.Connect.setObjectName("Connect")
        self.Morse_Page = QtWidgets.QFrame(Form)
        self.Morse_Page.setEnabled(True)
        self.Morse_Page.setGeometry(QtCore.QRect(0, 40, 901, 561))
        self.Morse_Page.setAutoFillBackground(True)
        self.Morse_Page.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Morse_Page.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Morse_Page.setObjectName("Morse_Page")
        self.MorsePic = QtWidgets.QLabel(self.Morse_Page )
        self.MorsePic.setGeometry(QtCore.QRect(390, 0, 511, 561))
        self.MorsePic.setAutoFillBackground(False)
        self.MorsePic.setText("")
        self.MorsePic.setPixmap(QtGui.QPixmap("lab4_morsecode.png"))
        self.MorsePic.setScaledContents(True)
        self.MorsePic.setObjectName("MorsePic")
        self.CurrentInput_Box = QtWidgets.QTextEdit(self.Morse_Page, readOnly=True)
        self.CurrentInput_Box.setGeometry(QtCore.QRect(60, 100, 261, 51))
        self.CurrentInput_Box.setAutoFillBackground(False)
        self.CurrentInput_Box.setObjectName("CurrentInput_Box")
        self.CurrentInput_Text = QtWidgets.QLabel(self.Morse_Page)
        self.CurrentInput_Text.setGeometry(QtCore.QRect(60, 50, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(18)
        self.CurrentInput_Text.setFont(font)
        self.CurrentInput_Text.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentInput_Text.setObjectName("CurrentInput_Text")
        self.WordHistory_Text = QtWidgets.QLabel(self.Morse_Page)
        self.WordHistory_Text.setGeometry(QtCore.QRect(60, 320, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(18)
        self.WordHistory_Text.setFont(font)
        self.WordHistory_Text.setAlignment(QtCore.Qt.AlignCenter)
        self.WordHistory_Text.setObjectName("WordHistory_Text")
        self.WordHistory_Box = QtWidgets.QTextEdit(self.Morse_Page, readOnly=True)
        self.WordHistory_Box.setGeometry(QtCore.QRect(60, 370, 261, 131))
        self.WordHistory_Box.setAutoFillBackground(False)
        self.WordHistory_Box.setObjectName("WordHistory_Box")
        self.CurrentWord_Text = QtWidgets.QLabel(self.Morse_Page)
        self.CurrentWord_Text.setGeometry(QtCore.QRect(60, 190, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(18)
        self.CurrentWord_Text.setFont(font)
        self.CurrentWord_Text.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentWord_Text.setObjectName("CurrentWord_Text")
        self.CurrentWord_Box = QtWidgets.QTextEdit(self.Morse_Page, readOnly=True)
        self.CurrentWord_Box.setGeometry(QtCore.QRect(60, 240, 261, 51))
        self.CurrentWord_Box.setAutoFillBackground(False)
        self.CurrentWord_Box.setObjectName("CurrentWord_Box")
        self.Snake_Page = QtWidgets.QFrame(Form)
        self.Snake_Page.setEnabled(True)
        self.Snake_Page.setGeometry(QtCore.QRect(0, 40, 901, 561))
        self.Snake_Page.setAutoFillBackground(True)
        self.Snake_Page.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Snake_Page.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Snake_Page.setObjectName("Snake_Page")
        self.Home = QtWidgets.QPushButton(Form, clicked=self.goHome)
        self.Home.setGeometry(QtCore.QRect(0, 0, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Home.setFont(font)
        self.Home.setAutoFillBackground(False)
        self.Home.setObjectName("Home")
        self.Morse_Page.raise_()
        self.Connect.raise_()
        self.Snake_Page.raise_()
        self.Home.raise_()
        self.Home_Page.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.status = 0
        self.keyboard = Controller()

        self.serial = QtSerialPort.QSerialPort(
            'COM3',
            baudRate=QtSerialPort.QSerialPort.Baud115200,
            readyRead=self.receive
        )


    def receive(self):
        global lastTime, currentString, currentWord, wordHistory, newLine
        import MorseCode

        while self.serial.canReadLine():
            text = self.serial.readLine().data().decode()
            text = text.rstrip('\r\n')
            
            #Conditionals, Probably better to use switch statements in the future

            if text == '0':
                if status == 0:
                    self.keyboard.press(Key.up)
                    self.keyboard.release(Key.up)
                print("Up Key was Pressed")
                print(time.perf_counter() - lastTime)
                if lastTime == 0:
                    currentString.append('.')
                elif time.perf_counter() - lastTime > 2:
                    currentString.append('-')
                else:
                    currentString.append('.')
                # print(currentString)
                lastTime = time.perf_counter()

            elif text == '1':
                self.keyboard.press(Key.down)
                self.keyboard.release(Key.down)
                print("Down Key was Pressed")
                message = ''.join(currentString)
                print(message)
                currentWord.append(MorseCode.inputCode(message))
                self.CurrentWord_Box.clear()
                self.CurrentWord_Box.append(''.join(currentWord))
                currentString.clear()

                lastTime = time.perf_counter()
            elif text == '2':
                self.keyboard.press(Key.left)
                self.keyboard.release(Key.left)
                print("Left Key was Pressed")
            elif text == '3':
                self.keyboard.press(Key.right)
                self.keyboard.release(Key.right)
                print("Right Key was Pressed")
                self.CurrentWord_Box.clear()
                self.WordHistory_Box.append(''.join(currentWord))
                currentWord.clear()



            self.CurrentInput_Box.clear()
            self.CurrentInput_Box.append(''.join(currentString))

    def on_toggled(self, checked):
        self.Connect.setText("Disconnect" if checked else "Connect")
        if checked:
            if not self.serial.isOpen():
                if not self.serial.open(QtCore.QIODevice.ReadWrite):
                    self.Connect.setChecked(False)
        else:
            self.serial.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Connect.setText(_translate("Form", "Connect"))
        self.CurrentInput_Text.setText(_translate("Form", "Current Input:"))
        self.WordHistory_Text.setText(_translate("Form", "Word History:"))
        self.CurrentWord_Text.setText(_translate("Form", "Current Word:"))
        self.Home.setText(_translate("Form", "Home"))

    def goSnake(self):
        global status
        print("GO SNAKE")
        status = 1
        import jb_snake as jbSnake
        jbSnake.snake()

    def goHome(self):
        global status
        print("GO Home")
        status = 0
        self.Home_Page.raise_()

    def goMorse(self):
        global status
        print("Morse GO")
        status = 2
        self.Morse_Page.raise_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
