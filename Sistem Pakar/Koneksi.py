from PyQt4 import QtSql

class Koneksi :

	def __init__(self,host,user,passw,database):
		self.db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
        self.db.setHostName(host)
        self.db.setUserName(user)
        self.db.setPassword(passw)
        self.db.setDatabaseName(database)
		

	def connections(self):
		self.__init__('127.0.0.1','localhost','','sipa')
		
a = Koneksi()