# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gejala.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui, QtSql

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

class Ui_Gejala(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(763, 350)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 641, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans"))
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtGui.QFrame.Panel)
        self.label.setFrameShadow(QtGui.QFrame.Raised)
        self.label.setLineWidth(0)
        self.label.setObjectName(_fromUtf8("label"))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(10, 60, 241, 141))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))

        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, -4, 56, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 56, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.tfKode = QtGui.QLineEdit(self.frame)
        self.tfKode.setGeometry(QtCore.QRect(60, 0, 181, 27))
        self.tfKode.setObjectName(_fromUtf8("tfKode"))
        self.tfGejala = QtGui.QTextEdit(self.frame)
        self.tfGejala.setGeometry(QtCore.QRect(60, 30, 181, 111))
        self.tfGejala.setObjectName(_fromUtf8("tfGejala"))
        self.btnInsert = QtGui.QPushButton(Dialog)
        self.btnInsert.setGeometry(QtCore.QRect(50, 210, 61, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnInsert.setFont(font)
        self.btnInsert.setObjectName(_fromUtf8("btnInsert"))
        self.btnInsert.clicked.connect(self.insert)
        self.btnDelete = QtGui.QPushButton(Dialog)
        self.btnDelete.setGeometry(QtCore.QRect(120, 210, 61, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnDelete.setFont(font)
        self.btnDelete.setObjectName(_fromUtf8("btnDelete"))
        self.btnRefresh = QtGui.QPushButton(Dialog)
        self.btnRefresh.setGeometry(QtCore.QRect(190, 210, 61, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnRefresh.setFont(font)
        self.btnRefresh.setObjectName(_fromUtf8("btnRefresh"))
        self.btnRefresh.clicked.connect(self.refresh)
        self.frame_2 = QtGui.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(260, 60, 500, 280))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.tableWidget = QtGui.QTableWidget(self.frame_2)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 498, 280))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.frame_3 = QtGui.QFrame(Dialog)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 763, 391))
        self.frame_3.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.frame_4 = QtGui.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(220, 10, 621, 16))
        self.frame_4.setStyleSheet(_fromUtf8("background-color: rgb(0, 128, 128);"))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.frame_3.raise_()
        self.frame_4.raise_()
        self.label.raise_()
        self.frame.raise_()
        self.btnInsert.raise_()
        self.btnDelete.raise_()
        self.btnRefresh.raise_()
        self.frame_2.raise_()


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
        self.db.setHostName('127.0.0.1')
        self.db.setUserName('root')
        self.db.setPassword('')
        self.db.setDatabaseName('sipa')
        self.view()

    def messageBox(self,title,pesan):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(pesan)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()

    def insert(self) :
        db = self.db.open()
        if db == False :
            self.messageBox('Warning','Connections Failed !!!')
        else :
            kode_g = self.tfKode.text()
            gejala = self.tfGejala.toPlainText()

            sql = "insert into gejala(kode_g,gejala) values(:kode_g,:gejala)"
            query = QtSql.QSqlQuery()
            query.prepare(sql)
            query.bindValue(":kode_g",kode_g)
            query.bindValue(":gejala",gejala)

            db = query.exec_()
            if db == True:
                self.messageBox('Informations','Insert Succesfull !!!')
                self.refresh()
                self.view()
            else :
                self.messageBox('Informations','Insert Faled !!!')

            self.db.close()

    def view(self):
        db = self.db.open()
        if db == False :
            self.messageBox('Warning','Connections Failed !!!')
        else :
            self.tableWidget.setColumnCount(2)
            self.tableWidget.setColumnWidth(0,50)
            self.tableWidget.setColumnWidth(1,407)
            self.tableWidget.setHorizontalHeaderLabels(['Kode_p','Gejala'])

            row = 0
            sql = "select * from gejala"
            query = QtSql.QSqlQuery(sql)
            
            while query.next():
                self.tableWidget.insertRow(row)
                self.tableWidget.setItem(row,0,QtGui.QTableWidgetItem(query.value(0).toString()))
                self.tableWidget.setItem(row,1,QtGui.QTableWidgetItem(query.value(1).toString()))
                row += 1

            self.db.close()

    def refresh(self):
        self.tfGejala.setPlainText("")
        self.tfKode.setText("")
        self.tableWidget.clear()
        self.view()


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Form Gejala", None))
        self.label.setText(_translate("Dialog", "Data Gejala Penyakit Mata", None))
        self.label_2.setText(_translate("Dialog", "Kode", None))
        self.label_3.setText(_translate("Dialog", "Gejala", None))
        self.btnInsert.setText(_translate("Dialog", "Insert", None))
        self.btnDelete.setText(_translate("Dialog", "Delete", None))
        self.btnRefresh.setText(_translate("Dialog", "Refresh", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

