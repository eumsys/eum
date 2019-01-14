import sys
import os
import time
import sched
import psycopg2
import inicioSesion as sesion
import caja

from threading import Timer,Thread
from PyQt5.QtWidgets import QMainWindow,QApplication, QDialog, QGridLayout, QMessageBox,QLabel, QPushButton, QLineEdit,QSpinBox, QTableWidget,QTableWidgetItem,QComboBox,QCheckBox
from PyQt5 import QtCore, QtGui, uic

kill = 0
killer = 0
plaza = ""
localidad = ""
bd = "dbeum_manual"
usr = "postgres"
pswd = "Postgres3UMd6"
i = 1

def obtenerPlazaYLocalidad():
	global plaza,localidad
	try:
		connection = psycopg2.connect(user = usr, password = pswd, database = bd, host = 'localhost')
		with connection.cursor() as cursor:
			cursor.execute('SELECT nombre_plaza, estado FROM plaza WHERE idplaza = 1')
			row = cursor.fetchone()
			if row is not None:
				plaza = str(row[0])
				localidad = str(row[1])
				connection.commit()
				connection.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)

def funcionCaja():
	caja.interface(plaza,localidad)

def funcionSesion():
	sesion.interface(plaza,localidad)

def leerCodQR():
	lee = os.system("zbarcam --raw --prescale=10x10  /dev/video0 > /home/pi/Documents/eum/app/sistemaManualV2/Caja/archivosTXT/ticket.txt")

def leerArchivo():
	global leido,kill,killer,folio,inTerminal,inFecha,inHora
	while(kill == 0):
		while(killer == 0 and kill == 0):
			leerArch = open("/home/pi/Documents/eum/app/sistemaManualV2/Caja/archivosTXT/ticket.txt", "r")
			folio=''
			folio=leerArch.readline().rstrip("\n")
			time.sleep(.2)
			leido=0
			if(folio != ''):													#Si existe algun folio
				if(str("Estacionamientos unicos de Mexico") in str(folio)):	#Si el folio pertenece al estacionamiento
					leido=1
					killer = 1
					leerArch.close()
					leerArch = open("/home/pi/Documents/eum/app/sistemaManualV2/Caja/archivosTXT/ticket.txt", "r")
					leyenda=(leerArch.readline().rstrip("\n")).lstrip("\x00")	#Estacionamientos unicos de mexico
					folio=(leerArch.readline().rstrip("\n")).lstrip("\x00")		#id del boleto
					inTerminal=leerArch.readline().rstrip("\n")					#id expedidora
					inFecha=leerArch.readline().rstrip("\n")					#fecha entrada dd/mm/aaaa
					inHora=leerArch.readline().rstrip("\n")						#hora entrada hh:mm:ss
					leerArch.close()
					leerArch = open("/home/pi/Documents/eum/app/sistemaManualV2/Caja/archivosTXT/ticket.txt", "w")
					leerArch.write('')
					leerArch.close()
				else:															#Si el folio no pertenece al estacionamiendo borro el archivo
					leerArch.close()
					leerArch = open("/home/pi/Documents/eum/app/sistemaManualV2/Caja/archivosTXT/ticket.txt", "w")
					leerArch.write('')
					leerArch.close()
			else:				#Si no existe ningun folio 
				leerArch.close()

def hilos():
	#INICIALIZAMOS EL HILO DE LA INTERFAZ
	thread1 = Thread(target=leerCodQR,args=())
	thread4 = Thread(target=leerArchivo, args=())
	try:
		thread1.start()
		thread4.start()
	except Exception as e:
		pass

def principal():
	est1 = 0
	est2 = 1
	while (True):
		if est1 == 0:
			funcionSesion()
			est1 = 1
			est2 = 0
		if est2 == 0:
			funcionCaja()
			est1 = 0
			est2 = 1
		time.sleep(1)

if __name__ == "__main__":
	obtenerPlazaYLocalidad()
	hilos()
	principal()
