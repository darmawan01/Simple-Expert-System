# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Home import Ui_MainWindow
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):

    def messageBox(self,title,pesan):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(pesan)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()

    def loginCheck(self):

        user = self.tfUser.text()
        pas = self.tfPass.text()
        if user == str('sistem') and pas == str('pakar'):
            self.messageBox('Informations','Login SuccesFull, Welcome !! ')
            self.h = QtGui.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.h)
            self.h.show()
            Dialog.close()

        else :
            self.messageBox('Warning','Login Failed, Try again !! ')

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        # Dialog.resize(362, 224)
        Dialog.setFixedSize(326,222)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.tfUser = QtGui.QLineEdit(Dialog)
        self.tfUser.setGeometry(QtCore.QRect(100, 80, 171, 27))
        self.tfUser.setObjectName(_fromUtf8("tfUser"))
        self.tfPass = QtGui.QLineEdit(Dialog)
        self.tfPass.setGeometry(QtCore.QRect(100, 130, 171, 27))
        self.tfPass.setObjectName(_fromUtf8("tfPass"))
        self.btnLogin = QtGui.QPushButton(Dialog)
        self.btnLogin.setGeometry(QtCore.QRect(150, 170, 61, 27))
        self.btnLogin.setObjectName(_fromUtf8("btnLogin"))
        self.btnLogin.clicked.connect(self.loginCheck)
        self.btnBtl = QtGui.QPushButton(Dialog)
        self.btnBtl.setGeometry(QtCore.QRect(220, 170, 51, 27))
        self.btnBtl.setObjectName(_fromUtf8("btnBtl"))
        self.btnBtl.clicked.connect(self.close)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 60, 121, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 110, 81, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 361, 221))
        self.frame.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.frame.raise_()
        self.label.raise_()
        self.tfUser.raise_()
        self.tfPass.raise_()
        self.btnLogin.raise_()
        self.btnBtl.raise_()
        self.label_2.raise_()
        self.label_3.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def close(self):
        Dialog.close()
        
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Form Login", None))
        self.label.setText(_translate("Dialog", "Sig In", None))
        self.btnLogin.setText(_translate("Dialog", "Login", None))
        self.btnBtl.setText(_translate("Dialog", "Batal", None))
        self.label_2.setText(_translate("Dialog", "Username", None))
        self.label_3.setText(_translate("Dialog", "Password", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

