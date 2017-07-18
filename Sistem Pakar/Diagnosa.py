# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Diagnosa.ui'
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

class Ui_Diagnosa(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(669, 501)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 661, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans"))
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShadow(QtGui.QFrame.Plain)
        self.label.setObjectName(_fromUtf8("label"))

        self.frame_4 = QtGui.QFrame(Dialog)
        self.frame_4.setGeometry(QtCore.QRect(0, -1, 671, 501))
        self.frame_4.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))

        self.frame_0 = QtGui.QFrame(self.frame_4)
        self.frame_0.setGeometry(QtCore.QRect(200, 15, 650,15))
        self.frame_0.setStyleSheet(_fromUtf8("background-color: rgb(0, 128, 128);"))
        self.frame_0.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_0.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_0.setObjectName(_fromUtf8("frame_0"))

        self.btnDiagnosa = QtGui.QPushButton(self.frame_4)
        self.btnDiagnosa.setGeometry(QtCore.QRect(20, 310, 85, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnDiagnosa.setFont(font)
        self.btnDiagnosa.setObjectName(_fromUtf8("btnDiagnosa"))
        self.btnDiagnosa.clicked.connect(self.diagnosa)
        self.btnRefresh = QtGui.QPushButton(self.frame_4)
        self.btnRefresh.setGeometry(QtCore.QRect(130, 310, 85, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnRefresh.setFont(font)
        self.btnRefresh.setObjectName(_fromUtf8("btnRefresh"))
        self.btnRefresh.clicked.connect(self.refresh)
        self.frame_2 = QtGui.QFrame(self.frame_4)
        self.frame_2.setGeometry(QtCore.QRect(10, 240, 651, 61))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.cbGejala = QtGui.QComboBox(self.frame_2)
        self.cbGejala.setGeometry(QtCore.QRect(10, 20, 91, 31))
        self.cbGejala.setObjectName(_fromUtf8("comboBox"))
        self.cbGejala.activated.connect(self.cbGetValue)
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 641, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.tfgej = QtGui.QTextEdit(self.frame_2)
        self.tfgej.setGeometry(QtCore.QRect(110, 20, 511, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(20)
        self.tfgej.setFont(font)
        self.tfgej.setObjectName(_fromUtf8("tfgej"))
        self.tfgej.setEnabled(False)
        self.frame = QtGui.QFrame(self.frame_4)
        self.frame.setGeometry(QtCore.QRect(10, 40, 651, 201))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 6, 281, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.table = QtGui.QTableWidget(self.frame)
        self.table.setGeometry(QtCore.QRect(0, 30, 651, 161))
        self.table.setObjectName(_fromUtf8("table"))
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.frame_3 = QtGui.QFrame(self.frame_4)
        self.frame_3.setGeometry(QtCore.QRect(10, 340, 651, 161))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.label_5 = QtGui.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 56, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 91, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(340, 40, 91, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.tfNama = QtGui.QLineEdit(self.frame_3)
        self.tfNama.setGeometry(QtCore.QRect(100, 10, 231, 27))
        self.tfNama.setObjectName(_fromUtf8("tfNama"))
        self.tfNama.setEnabled(False)
        self.tfPengobatan = QtGui.QTextEdit(self.frame_3)
        self.tfPengobatan.setGeometry(QtCore.QRect(100, 40, 231, 121))
        self.tfPengobatan.setObjectName(_fromUtf8("tfPengobatan"))
        self.tfPengobatan.setEnabled(False)
        self.tfPencegahan = QtGui.QTextEdit(self.frame_3)
        self.tfPencegahan.setGeometry(QtCore.QRect(430, 40, 221, 121))
        self.tfPencegahan.setObjectName(_fromUtf8("tfPencegahan"))
        self.tfPencegahan.setEnabled(False)
        self.frame_0.raise_()
        self.frame_4.raise_()
        self.label.raise_()

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


    def view(self):
        db = self.db.open()
        if db == False :
            self.messageBox('Warning','Connections Failed !!!')
        else :
            self.table.setColumnCount(2)
            self.table.setColumnWidth(1,510)
            self.table.setHorizontalHeaderLabels(['Kode_p','Gejala'])

            row = 0
            sql = "select * from gejala"
            query = QtSql.QSqlQuery(sql)
            
            self.cbGejala.addItem('--- Pilih ---')
            while query.next():
                self.table.insertRow(row)
                self.table.setItem(row,0,QtGui.QTableWidgetItem(query.value(0).toString()))
                self.table.setItem(row,1,QtGui.QTableWidgetItem(query.value(1).toString()))
                self.cbGejala.addItem(query.value(0).toString())
                row += 1

            self.db.close()

    def cbGetValue(self):
        g = str(self.cbGejala.currentText())
        get = self.tfgej.toPlainText()
        if g in get :
            self.messageBox('Warning','Gejala Yang Anda Pilih Sudah Ada !!!')
        else:
            self.tfgej.insertPlainText(g+" ")

    def diagnosa(self):

        gejala = self.tfgej.toPlainText()

        db = self.db.open()
        if db == False :
            self.messageBox('Warning','Connections Failed !!!')
        else :
            if self.tfgej.toPlainText() == "" :
                self.messageBox('Warning','Gejala Belum Dipilih !!!')
            else :
                sql = "SELECT a.nama,a.pengobatan,a.pencegahan FROM rule r, penyakit a WHERE r.penyakit_kode_p = a.kode_p AND r.rules = ?"
                query = QtSql.QSqlQuery()
                query.prepare(sql)
                query.bindValue(0,gejala)
                db = query.exec_()
                
                    
                if query.next():
                    self.messageBox('Informations','Dari Data Gejala Yang Dipilih,\n Penyakit Berhasil Di Diagnosa !!!')
                    self.tfNama.setText(query.value(0).toString())
                    self.tfPengobatan.insertPlainText(query.value(1).toString())
                    self.tfPencegahan.insertPlainText(query.value(2).toString())                
                else :
                    self.messageBox('Warning','Dari Data Gejala Yang Dipilih,\n Penyakit Tidak Ditemukan. Coba Diagnosa Lagi !!!')
                    self.refresh()
           
        self.db.close()
   
    def refresh(self):
        self.cbGejala.setCurrentIndex(0)
        self.tfgej.clear()
        self.tfNama.setText("")
        self.tfPengobatan.clear()
        self.tfPencegahan.clear()


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Form Diagnosa", None))
        self.label.setText(_translate("Dialog", "Diagnosa Penyakit Mata", None))
        self.btnDiagnosa.setText(_translate("Dialog", "Diagnosa", None))
        self.btnRefresh.setText(_translate("Dialog", "Refresh", None))
        self.label_3.setText(_translate("Dialog", "Pilih Gejala Dari Data Gejala Pada Tabel :                                                                                 ", None))
        self.label_2.setText(_translate("Dialog", "Daftar Gejala Penyakit Mata", None))
        self.label_5.setText(_translate("Dialog", "Nama", None))
        self.label_6.setText(_translate("Dialog", "Pengobatan", None))
        self.label_7.setText(_translate("Dialog", "Pencegahan", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

