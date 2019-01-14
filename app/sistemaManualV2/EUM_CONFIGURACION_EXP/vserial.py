# -*- coding: utf-8 -*-
import os
#os.system("sudo touch /home/pi/Desktop/numeroSerial.txt")
os.system("sudo grep Serial /proc/cpuinfo >> /home/pi/Desktop/numeroSerial.txt")
print "EQUIS DE"		
"""
Funciones para leer datos
"""
PATH_ARCHIVO_CONFIGURACION_TERMINAL_SERIAL="/home/pi/Desktop/numeroSerial.txt"

def getSerial():
	configuracion=[]
	archivo=open(PATH_ARCHIVO_CONFIGURACION_TERMINAL_SERIAL, "r")
	for linea in archivo.readlines():
		configuracion.append(linea)
	archivo.close()
	pass
	return configuracion[0]
	pass

def cleanArchivo():
	archivo=open(PATH_ARCHIVO_CONFIGURACION_TERMINAL_SERIAL, "w")
	archivo.write("")
	archivo.close()
	pass

#print getSerial()

from PyQt4 import QtCore, QtGui

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

class dvserial(object):
	def __init__(self, MainWindow):
		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.resize(700, 400)
		MainWindow.setMinimumSize(QtCore.QSize(700, 400))
		MainWindow.setMaximumSize(QtCore.QSize(700, 400))
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
		self.pushButton_2.setGeometry(QtCore.QRect(150, 240, 401, 131))
		font = QtGui.QFont()
		font.setPointSize(48)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.pushButton_2.setFont(font)
		self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
		self.label = QtGui.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(20, 20, 661, 171))
		font = QtGui.QFont()
		font.setPointSize(18)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.label.setFont(font)
		self.label.setText(_fromUtf8(""))
		self.label.setObjectName(_fromUtf8("label"))
		#MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtGui.QStatusBar(MainWindow)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		#MainWindow.setStatusBar(self.statusbar)
		
		ns=getSerial()
		ns=ns.replace(":","")
		self.label.setText(_fromUtf8(str("MODELO\t\t EUM1000\n")+str(ns)))
		#self.pushButton_2.clicked.connect(self.botonCancelar)
		
		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
	
	#def botonCancelar(self):
	#	cleanArchivo()
	#	exit()
		
	
	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
		self.pushButton_2.setText(_translate("MainWindow", "SALIR", None))

'''
if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	MainWindow = QtGui.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
'''
