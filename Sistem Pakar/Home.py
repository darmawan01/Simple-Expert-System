# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Home.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

from Diagnosa import Ui_Diagnosa
from Penyakit import Ui_Penyakit
from Gejala import Ui_Gejala
from Tentang import Ui_Tentang

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

class Ui_MainWindow(object):

    def diagnosa(self):
        self.a = QtGui.QDialog()
        self.ui = Ui_Diagnosa()
        self.ui.setupUi(self.a)
        self.a.show()

    def penyakit(self):
        self.b = QtGui.QDialog()
        self.ui = Ui_Penyakit()
        self.ui.setupUi(self.b)
        self.b.show()

    def gejala(self):
        self.c = QtGui.QDialog()
        self.ui = Ui_Gejala()
        self.ui.setupUi(self.c)
        self.c.show()

    def tentang(self):
        self.d = QtGui.QDialog()
        self.ui = Ui_Tentang()
        self.ui.setupUi(self.d)
        self.d.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setFixedSize(979, 595)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -20, 980, 625))
        self.frame.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.btnTentang = QtGui.QPushButton(self.frame)
        self.btnTentang.setGeometry(QtCore.QRect(670, 160, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Serif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnTentang.setFont(font)
        self.btnTentang.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnTentang.setStyleSheet(_fromUtf8("background-color: rgb(0, 128, 128);"))
        self.btnTentang.setAutoDefault(False)
        self.btnTentang.setFlat(False)
        self.btnTentang.setObjectName(_fromUtf8("btnTentang"))
        self.btnTentang.clicked.connect(self.tentang)
        self.btnGejala = QtGui.QPushButton(self.frame)
        self.btnGejala.setGeometry(QtCore.QRect(550, 160, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Serif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnGejala.setFont(font)
        self.btnGejala.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnGejala.setStyleSheet(_fromUtf8("background-color: rgb(0, 128, 128);"))
        self.btnGejala.setAutoDefault(False)
        self.btnGejala.setFlat(False)
        self.btnGejala.setObjectName(_fromUtf8("btnGejala"))
        self.btnGejala.clicked.connect(self.gejala)
        self.btnPenyakit = QtGui.QPushButton(self.frame)
        self.btnPenyakit.setGeometry(QtCore.QRect(420, 160, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Serif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnPenyakit.setFont(font)
        self.btnPenyakit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPenyakit.setStyleSheet(_fromUtf8("background-color: rgb(0, 128, 128);"))
        self.btnPenyakit.setAutoDefault(False)
        self.btnPenyakit.setFlat(False)
        self.btnPenyakit.setObjectName(_fromUtf8("btnPenyakit"))
        self.btnPenyakit.clicked.connect(self.penyakit)
        self.btnDiagnosa = QtGui.QPushButton(self.frame)
        self.btnDiagnosa.setGeometry(QtCore.QRect(320, 160, 85, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Serif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnDiagnosa.setFont(font)
        self.btnDiagnosa.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnDiagnosa.setAutoFillBackground(False)
        self.btnDiagnosa.setStyleSheet(_fromUtf8("background-color: rgb(0, 128, 128);"))
        self.btnDiagnosa.setAutoDefault(False)
        self.btnDiagnosa.setFlat(False)
        self.btnDiagnosa.setObjectName(_fromUtf8("btnDiagnosa"))
        self.btnDiagnosa.clicked.connect(self.diagnosa)
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 20, 980, 595))
        self.label.setMouseTracking(False)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("icon/home.png")))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.label.raise_()
        self.btnTentang.raise_()
        self.btnGejala.raise_()
        self.btnPenyakit.raise_()
        self.btnDiagnosa.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        # self.actionLogin = QtGui.QAction(MainWindow)
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon/Unlock_20px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.actionLogin.setIcon(icon)
        # self.actionLogin.setSoftKeyRole(QtGui.QAction.PositiveSoftKey)
        # self.actionLogin.setIconVisibleInMenu(True)
        # self.actionLogin.setObjectName(_fromUtf8("actionLogin"))
        # self.actionLogout = QtGui.QAction(MainWindow)
        # self.actionLogout.setObjectName(_fromUtf8("actionLogout"))
        # self.actionExit = QtGui.QAction(MainWindow)
        # self.actionExit.setObjectName(_fromUtf8("actionExit"))
        # self.actionAdmin = QtGui.QAction(MainWindow)
        # self.actionAdmin.setObjectName(_fromUtf8("actionAdmin"))
        # self.actionData_Gejala = QtGui.QAction(MainWindow)
        # self.actionData_Gejala.setObjectName(_fromUtf8("actionData_Gejala"))
        # self.actionData_Penyakit = QtGui.QAction(MainWindow)
        # self.actionData_Penyakit.setObjectName(_fromUtf8("actionData_Penyakit"))
        # self.actionData_Rule = QtGui.QAction(MainWindow)
        # self.actionData_Rule.setObjectName(_fromUtf8("actionData_Rule"))
        # self.actionPetunjuk = QtGui.QAction(MainWindow)
        # self.actionPetunjuk.setObjectName(_fromUtf8("actionPetunjuk"))
        # self.actionTentang_Programmer = QtGui.QAction(MainWindow)
        # self.actionTentang_Programmer.setObjectName(_fromUtf8("actionTentang_Programmer"))
        # self.actionTentang_Program = QtGui.QAction(MainWindow)
        # self.actionTentang_Program.setObjectName(_fromUtf8("actionTentang_Program"))
        # self.actionMinimize = QtGui.QAction(MainWindow)
        # self.actionMinimize.setObjectName(_fromUtf8("actionMinimize"))
        # self.actionMaximize = QtGui.QAction(MainWindow)
        # self.actionMaximize.setObjectName(_fromUtf8("actionMaximize"))
        # self.actionTheme = QtGui.QAction(MainWindow)
        # self.actionTheme.setObjectName(_fromUtf8("actionTheme"))
        # self.actionBackground = QtGui.QAction(MainWindow)
        # self.actionBackground.setObjectName(_fromUtf8("actionBackground"))
        # self.actionGrey = QtGui.QAction(MainWindow)
        # self.actionGrey.setObjectName(_fromUtf8("actionGrey"))
        # self.actionWhite = QtGui.QAction(MainWindow)
        # self.actionWhite.setObjectName(_fromUtf8("actionWhite"))
        # self.actionGreen = QtGui.QAction(MainWindow)
        # self.actionGreen.setObjectName(_fromUtf8("actionGreen"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistem Pakar Diagnosa Penyakit Mata", None))
        self.btnTentang.setText(_translate("MainWindow", "Tentang", None))
        self.btnGejala.setText(_translate("MainWindow", "Data Gejala", None))
        self.btnPenyakit.setText(_translate("MainWindow", "Data Penyakit", None))
        self.btnDiagnosa.setText(_translate("MainWindow", "Diagnosa", None))
        # self.actionLogin.setText(_translate("MainWindow", "Login", None))
        # self.actionLogout.setText(_translate("MainWindow", "Logout", None))
        # self.actionExit.setText(_translate("MainWindow", "Exit", None))
        # self.actionAdmin.setText(_translate("MainWindow", "Admin", None))
        # self.actionData_Gejala.setText(_translate("MainWindow", "Data Gejala", None))
        # self.actionData_Penyakit.setText(_translate("MainWindow", "Data Penyakit", None))
        # self.actionData_Rule.setText(_translate("MainWindow", "Data Rule", None))
        # self.actionPetunjuk.setText(_translate("MainWindow", "Petunjuk", None))
        # self.actionTentang_Programmer.setText(_translate("MainWindow", "Tentang Programmer", None))
        # self.actionTentang_Program.setText(_translate("MainWindow", "Tentang Program", None))
        # self.actionMinimize.setText(_translate("MainWindow", "Minimize", None))
        # self.actionMaximize.setText(_translate("MainWindow", "Maximize", None))
        # self.actionTheme.setText(_translate("MainWindow", "Theme", None))
        # self.actionBackground.setText(_translate("MainWindow", "Background", None))
        # self.actionGrey.setText(_translate("MainWindow", "Grey", None))
        # self.actionWhite.setText(_translate("MainWindow", "White", None))
        # self.actionGreen.setText(_translate("MainWindow", "Green", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

