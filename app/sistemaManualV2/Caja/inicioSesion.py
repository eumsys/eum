import sys
import os
import time
import sched
import psycopg2
from threading import Timer,Thread
from PyQt5.QtWidgets import QMainWindow,QApplication, QDialog, QGridLayout, QMessageBox,QLabel, QPushButton, QLineEdit,QSpinBox, QTableWidget,QTableWidgetItem,QComboBox,QCheckBox
from PyQt5 import QtCore, QtGui, uic
#Usuario Principal usr="3868737" pswd = "3867793"

global ser
leido = 0
banderaServer=0
secs = 0
var = 0

plaza = ""
localidad = ""

def interface(plz,local):
	
	def obtenerPlazaLocalidad():
		global plaza,localidad
		plaza = plz
		localidad = local
	
	def validarSesion():
		try:
			connection = psycopg2.connect(user = usr, password = pswd, database = bd, host = 'localhost')
			with connection.cursor() as cursor:
				cursor.execute("UPDATE sesion SET estado = 2")
				connection.commit()
				connection.close()
			_ventana.close()
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)
	
	class Ventana(QDialog):
		
		def __init__(self):
			QDialog.__init__(self)
			gui = uic.loadUi("/home/pi/Documents/eum/app/sistemaManualV2/Caja/Interfaces/kiosco.ui", self)
			self.stackedWidget.setCurrentIndex(0)
			self.loopFunction()
			self.contadorSegundos()
			self.nomPlaza_6.setText(plaza)
			self.nomLoc_6.setText(localidad)
			self.label_3.setVisible(False)
			self.lineContrasena.setEchoMode(QLineEdit.EchoMode(2))
			self.bnApagar.clicked.connect(self.apagarRasp)
			self.bn1.clicked.connect(lambda:self.tecladoSum(1))
			self.bn2.clicked.connect(lambda:self.tecladoSum(2))
			self.bn3.clicked.connect(lambda:self.tecladoSum(3))
			self.bn4.clicked.connect(lambda:self.tecladoSum(4))
			self.bn5.clicked.connect(lambda:self.tecladoSum(5))
			self.bn6.clicked.connect(lambda:self.tecladoSum(6))
			self.bn7.clicked.connect(lambda:self.tecladoSum(7))
			self.bn8.clicked.connect(lambda:self.tecladoSum(8))
			self.bn9.clicked.connect(lambda:self.tecladoSum(9))
			self.bn0.clicked.connect(lambda:self.tecladoSum(0))
			self.bnBorrarTexto.clicked.connect(lambda:self.tecladoSum(10))
			self.bnLimpiarTexto.clicked.connect(lambda:self.tecladoSum(11))
			self.bnIniciarSesion.clicked.connect(lambda:self.tecladoSum(12))
			self.lineIdEmpleado.editingFinished.connect(self.seleccion_cambiada)
			self.lineContrasena.editingFinished.connect(self.seleccion_cambiada2)
		
		def seleccion_cambiada(self):
			global var
			var = 1
		
		def seleccion_cambiada2(self):
			global var
			var = 2
		
		def apagarRasp(self):
			print("apagando...")
			#os.system("sudo shutdown -P 0")
		
		def tecladoSum(self,val):
			global var
			if(val == 10 and var == 1):														#Borrar el ultimo caracter
				idUser = self.lineIdEmpleado.text()[0:-1]
				self.lineIdEmpleado.setText(idUser)
			elif(val == 10 and var == 2):
				pasw=self.lineContrasena.text()[0:-1] 
				self.lineContrasena.setText(pasw)
			elif(val == 11 and var == 1):													#Limpiar el campo de texto
				self.lineIdEmpleado.setText("")
			elif(val == 11 and var == 2):
				self.lineContrasena.setText("")
			elif(val >= 0 and val <= 9 and var == 1):										#Simbolos numericos para iniciar sesión
				self.lineIdEmpleado.setText(self.lineIdEmpleado.text()+str(val))
			elif(val >= 0 and val <= 9 and var == 2):
				self.lineContrasena.setText(self.lineContrasena.text()+str(val))
			elif(val == 12):																#Inicio de sesion
				#FUNCION PARA INICIAR SESION
				mensajePsw = self.lineContrasena.text()
				mensajeIdUser = self.lineIdEmpleado.text()
				validacion = self.autenticacion(mensajeIdUser,mensajePsw)
				self.lineContrasena.setText("")
				self.lineIdEmpleado.setText("")
				if(validacion == "ack"):
					self.label_3.setVisible(False)
					validarSesion()
				else:
					self.label_3.setVisible(True)
		
		def autenticacion(self,usuario,contrasenia):
			try:
				connection = psycopg2.connect(user = usr, password = pswd, database = bd, host = 'localhost')
				with connection.cursor() as cursor:
					cursor.execute("SELECT idusuario FROM usuario WHERE nomusuario = '{}' and passwd = '{}'".format(str(usuario),str(contrasenia)))
					row = cursor.fetchone()
					if row is not None:
						connection.commit()
						connection.close()
						return "ack"
			except (Exception, psycopg2.DatabaseError) as error:
				print(error)
				return "mal"
		
		def loopFunction(self):
			global leido
			self.label_9.setText(time.strftime("%H:%M:%S"))
			self.label_10.setText(time.strftime("%d-%m-%Y"))
			self.label_30.setText(time.strftime("%H:%M:%S"))
			self.label_29.setText(time.strftime("%d-%m-%Y"))
			if(leido == 1):
				leido = 0
				self.activarBotones()
			QtCore.QTimer.singleShot(5,self.loopFunction)
		
		def contadorSegundos(self):
			global banderaServer, secs
			if(banderaServer == 1):
				secs=secs+1
				if(secs==4):
					self.mensajeServer.setText("")
					secs = 0
					banderaServer = 0
			QtCore.QTimer.singleShot(1000,self.contadorSegundos)
	
	obtenerPlazaLocalidad()
	app = QApplication(sys.argv)
	_ventana = Ventana()
	_ventana.move(160,0)
	_ventana.show()
	res = app.exec_()
	#print(res)
	#return res
