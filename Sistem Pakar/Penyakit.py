# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Penyakit.ui'
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

class Ui_Penyakit(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(682, 383)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 681, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans"))
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 60, 291, 271))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 91, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 91, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 91, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 210, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.tfPencegahan = QtGui.QTextEdit(self.frame)
        self.tfPencegahan.setGeometry(QtCore.QRect(110, 210, 181, 61))
        self.tfPencegahan.setObjectName(_fromUtf8("tfPencegahan"))
        self.tfKode = QtGui.QLineEdit(self.frame)
        self.tfKode.setGeometry(QtCore.QRect(110, 0, 181, 27))
        self.tfKode.setObjectName(_fromUtf8("tfKode"))
        self.tfNama = QtGui.QLineEdit(self.frame)
        self.tfNama.setGeometry(QtCore.QRect(110, 30, 181, 27))
        self.tfNama.setObjectName(_fromUtf8("tfNama"))
        self.tfPenyebab = QtGui.QTextEdit(self.frame)
        self.tfPenyebab.setGeometry(QtCore.QRect(110, 70, 181, 61))
        self.tfPenyebab.setObjectName(_fromUtf8("tfPenyebab"))
        self.tfPengobatan = QtGui.QTextEdit(self.frame)
        self.tfPengobatan.setGeometry(QtCore.QRect(110, 140, 181, 61))
        self.tfPengobatan.setObjectName(_fromUtf8("tfPengobatan"))
        self.frame_2 = QtGui.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(310, 60, 361, 281))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.tableWidget = QtGui.QTableWidget(self.frame_2)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 361, 271))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.frame_3 = QtGui.QFrame(Dialog)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 681, 391))
        self.frame_3.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.btnDelete = QtGui.QPushButton(self.frame_3)
        self.btnDelete.setGeometry(QtCore.QRect(140, 340, 71, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnDelete.setFont(font)
        self.btnDelete.setObjectName(_fromUtf8("btnDelete"))
        self.btnRefreh = QtGui.QPushButton(self.frame_3)
        self.btnRefreh.setGeometry(QtCore.QRect(220, 340, 71, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnRefreh.setFont(font)
        self.btnRefreh.setObjectName(_fromUtf8("btnRefreh"))
        self.btnRefreh.clicked.connect(self.refresh)
        self.btnInsert = QtGui.QPushButton(self.frame_3)
        self.btnInsert.setGeometry(QtCore.QRect(60, 340, 71, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnInsert.setFont(font)
        self.btnInsert.setObjectName(_fromUtf8("btnInsert"))
        self.btnInsert.clicked.connect(self.insert)
        self.frame_4 = QtGui.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(170, 10, 511, 16))
        self.frame_4.setStyleSheet(_fromUtf8("background-color: rgba(0, 128, 128);"))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.frame_3.raise_()
        self.frame_4.raise_()
        self.label.raise_()
        self.frame.raise_()
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

    def insert(self):
        db = self.db.open()
        if db == False :
            self.messageBox('Warning','Connections Failed !!!')
        else :
            kode_p = self.tfKode.text()
            nama = self.tfNama.text()
            penyebab = self.tfPenyebab.toPlainText()
            pengobatan = self.tfPengobatan.toPlainText()
            pencegahan = self.tfPencegahan.toPlainText()

            sql = "insert into penyakit(kode_p,nama,penyebab,pengobatan,pencegahan) values(:kode_p,:nama,:penyebab,:pengobatan,:pencegahan)"
            query = QtSql.QSqlQuery()
            query.prepare(sql)
            query.bindValue(":kode_p",kode_p)
            query.bindValue(":nama",nama)
            query.bindValue(":penyebab",penyebab)
            query.bindValue(":pengobatan",pengobatan)
            query.bindValue(":pencegahan",pencegahan)
            

            db = query.exec_()
            if db == True:
                self.messageBox('Informations','Insert Succesfull !!!')
                self.refresh()
                self.view()
            else :
                self.messageBox('Informations','Insert Failed !!!')

            self.db.close()

    def view(self):
        db = self.db.open()
        if db == False :
            self.messageBox('Warning','Connections Failed !!!')
        else :
            self.tableWidget.setColumnCount(2)
            self.tableWidget.setColumnWidth(0,63)
            self.tableWidget.setColumnWidth(1,280)
            self.tableWidget.setHorizontalHeaderLabels(['Kode_p','Nama'])

            row = 0
            sql = "select kode_p,nama from penyakit"
            query = QtSql.QSqlQuery(sql)
            
            while query.next():
                self.tableWidget.insertRow(row)
                self.tableWidget.setItem(row,0,QtGui.QTableWidgetItem(query.value(0).toString()))
                self.tableWidget.setItem(row,1,QtGui.QTableWidgetItem(query.value(1).toString()))
                row += 1

            self.db.close()

    def refresh(self):
        self.tfKode.setText("")
        self.tfPengobatan.setPlainText("")
        self.tfPenyebab.setPlainText("")
        self.tfPencegahan.setPlainText("")
        self.tfNama.setText("")
        self.tableWidget.clear()
        self.view()


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Form Penyakit", None))
        self.label.setText(_translate("Dialog", "Data Penyakit Mata", None))
        self.label_2.setText(_translate("Dialog", "Kode ", None))
        self.label_3.setText(_translate("Dialog", "Nama", None))
        self.label_4.setText(_translate("Dialog", "Penyebab", None))
        self.label_5.setText(_translate("Dialog", "Pengobatan", None))
        self.label_6.setText(_translate("Dialog", "Pencegahan", None))
        self.btnDelete.setText(_translate("Dialog", "Delete", None))
        self.btnRefreh.setText(_translate("Dialog", "Refresh", None))
        self.btnInsert.setText(_translate("Dialog", "Insert", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

