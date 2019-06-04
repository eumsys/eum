import time
import leerBotones as botones
import generarFolio as folio
#import codigoQR as qr
import imprimirBoleto as imprimir
import tratarImagen as imagen
import fechaUTC
import RPi.GPIO as GPIO
import configuracionEXP as archivoConfiguracion
import cortesExpFun as conectionBD
import resetFolios as re
import leerConfiguracionFechaHora as confFH
import cliente as clientes
from threading import Thread
#from pygame import mixer
#import psycopg2
import sys, tty, termios
import os
from escposprinter import *
import serial
from PIL import Image, ImageDraw, ImageFont
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QMainWindow,QApplication, QDialog, QGridLayout, QMessageBox,QLabel, QPushButton, QLineEdit,QSpinBox, QTableWidget,QTableWidgetItem,QComboBox,QCheckBox

from Conexiones.Conexiones import Conexiones
from Pila.Pila import Pila


limite_impresiones = 1000
boleto_previo = True
espera = 0
error_ayuda = 0	
estado = 0
plaza = ""
localidad = ""
NoEquipo=0
pol=""
pol1=""
pol2=""
pol3=""
pol4=""
pol5=""
impresora=0
anchoPapel=0
avanza=0
z=0
terminalEnt = 0
usuario = 'postgres'
contrasenia = 'Postgres3UMd6'
bd = "dbeum_tecamac"
teclaF3= 0
panelConf=0
errImpresora=0

GPIO.setmode(GPIO.BCM)

ser = serial.Serial("/dev/ttyS0")
ser.baudrate = 9600
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE
ser.bytesize = serial.EIGHTBITS
ser.timeout = .005


conexion_activa=False
camInicial=''
USUARIO=''
host=''
ip=''
noEquipo = 0
plaza = ""
localidad = ""
user="eueme"
pswd="emeue"
segundos=0
sensor=2
comienzaConteo=0
zz=0
regreso=False

fechaIn	= fechaUTC.fechaConFormato()
horaEnt = fechaUTC.tiempoConFormato()


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
		return QApplication.translate(context, text, disambig)

class Ui_ventanaAcceso(QDialog):

	def __init__(self):
		global panelConf
		QDialog.__init__(self)
		gui = uic.loadUi("/home/pi/Documents/eum/app/expedidora/Interfaces_EXP/expedidoraf.ui", self)
		#gui = uic.loadUi("/home/pi/Documents/eum/app/expedidora/Interfaces_EXP/expedidoraA.ui", self)
		self.panelConfig()
		self.contadorSegundos()
		self.configurarPinesGPIO()
		self.stackedWidget.setCurrentIndex(0)
		self.breiniciar.clicked.connect(lambda:self.reiniciarRasp())
		self.bapagar.clicked.connect(lambda:self.apagarRasp())
		#self.pushButton_3.clicked.connect(lambda:self.reiniciarRasp())
		#self.pushButton_4.clicked.connect(lambda:self.apagarRasp())
		#self.pushButton_5.clicked.connect(lambda:self.reinicioConteo())
		#self.pushButton_6.clicked.connect(lambda:self.reinicioConteo())
		#self.bF3.clicked.connect(self.solicitudBoleto)
		self.F3.clicked.connect(self.solicitudBoleto)
		self.bcambiarFecha.clicked.connect(self.cambiaFecha)
		self.bpanelconf.clicked.connect(self.panelConfig)
		self.bpanelconfb.clicked.connect(self.panelConfig)
		self.bpanelconf2.clicked.connect(lambda:self.cambia(1))
		self.bcan.clicked.connect(lambda:self.cambia(7))
		self.bcan2.clicked.connect(self.nada)
		self.bcan3.clicked.connect(lambda:self.cambia(9))
		self.bguardar.clicked.connect(self.setConfig)
		self.bsalirConfig.clicked.connect(self.salirConf)
		#self.bF3.setShortcut("F3")
		#self.F3.setShortcut("F3")
		self.breporte.setShortcut("R")
		self.bfindeturno.setShortcut("T")
		self.bsi.setShortcut("S")
		self.bpanelconf.setShortcut("ESCAPE")
		self.bpanelconfb.setShortcut("C")
		self.bpanelconf2.setShortcut("ESCAPE")
		self.bcan.setShortcut("ESCAPE")
		self.bcan2.setShortcut("ESCAPE")
		self.bcan3.setShortcut("ESCAPE")
		self.bsalirConfig.setShortcut("ESCAPE")
		self.bescritorio.clicked.connect(self.modoEscritorio)
		self.leerBotones()
		panelConf=0
		#self.hilos2()
		
		
	################MODS########
		self.bconfirmarIP.clicked.connect(self.cambiaIp)
		#self.bpanelconf.clicked.connect(self.)
		self.bsalirConfig.clicked.connect(lambda:self.cambia(1))
		
		self.bsalirLogin.clicked.connect(lambda:self.cambia(1))
		self.bsalirsucursal.clicked.connect(lambda:self.cambia(4))
		self.bsalirred.clicked.connect(lambda:self.cambia(4))
		self.bsalirCambiarFecha.clicked.connect(lambda:self.cambia(4))
		self.bsucursal.clicked.connect(lambda:self.cambia(3))
		self.bred.clicked.connect(lambda:self.cambia(2))
		self.bhora.clicked.connect(lambda:self.cambia(6))
		
		self.lerror1.setVisible(False)
		self.bentrar.clicked.connect(self.validaLogin)
		self.bcambiarFecha.clicked.connect(self.cambiaFecha)
		#self.bguardar.clicked.connect(self.setConfig)
		#self.bsalirConfig.clicked.connect(self.salirConf)
		#self.bconfirmarplaza.clicked.connect(self.setConfig)
		self.panelConfig()
		self.datosEstacionamiento()
		self.cambia(1)
		self.F3.setEnabled(True)
		self.bsalirreportes.clicked.connect(lambda:self.cambia(1))
		self.bfindeturno.clicked.connect(lambda:self.cambia(11))
		self.bno.clicked.connect(lambda:self.cambia(10))
		self.breporte.clicked.connect(lambda:self.cambia(10))
		self.bsi.clicked.connect(self.corte)
		self.bfindeturno.clicked.connect(self.imprimeCorte)
		self.logsDeApagado(2)
		
	def nada(self):
		pass
	def modoEscritorio(self):
		os.system("sudo shutdown -r 0")
		
	def imprimeCorte(self):
		self.cambia(11)
		os.system('sudo python3 /home/pi/Documents/eum/app/expedidora/corte.py')
		
	def corte(self):
		infile = open("/home/pi/Documents/eum/app/expedidora/archivos_config/UltimoFolio.txt","r")
		folioInicio=infile.readline()
		print('fiii',folioInicio)
		infile.close()
		infile = open("/home/pi/Documents/eum/app/expedidora/datos/corte.txt","r")
		datoss=infile.readline().split(',')
		turno=datoss[2]
		print('fiii',folioInicio)
		infile.close()
		x=''
		if(turno=='M'):
			x='V'
		else:
			x='M'
		infile = open("/home/pi/Documents/eum/app/expedidora/datos/corte.txt", 'w')
		wr='0,'+str(int(folioInicio))+','+x
		c=infile.write(wr)
		infile.close()
		self.cambia(1)	
	
		
		
	def validaLogin(self):
		global cur,accesoAcaja,USUARIO,correoUSUARIO,user,pswd
		nom=self.lusu.text()
		rol_us=""
		indice=0
		contr=self.lcont.text()
		if(nom==user):
			if(contr==pswd):
				self.cambia(5)
			else:
				self.lerror1.setText("usuario o contraseña incorrectos")
				self.lerror1.setVisible(True)
		else:
			self.lerror1.setText("usuario o contraseña incorrectos")
			self.lerror1.setVisible(True)
		"""cur.execute("SELECT * FROM \"USUARIO\" WHERE usuario=%s and contra=%s order by \"idUsuario\" ASC",(nom,contr))

		print("nom,contr=",nom,contr)
		for reg in cur:
			print(reg[1],reg[2],reg[3],reg[4],reg[5],reg[6])
			rol_us=reg[1]
			indice=1
		if(indice==0):
			self.lerror1.setText("usuario o contraseña incorrectos")
			self.lerror1.setVisible(True)
		else:
			USUARIO=str(reg[0])
			self.cambia(5)"""
	
	def cambiaFecha(self):
		a=self.dtime.dateTime()
		b=self.dtime.textFromDateTime(a)
		print(b,type(b))
		os.system("sudo date -s '"+b+"' ")
		
	def setConfig(self):
		global plaza,localidad,noEquipo,host,ip,pol,pol1,pol2,pol3,pol4,pol5,impresora,anchoPapel
		lenn=0
		plaza=str(self.lnom.text())
		localidad=str(self.lloc.text())
		noEquipo=str(self.leq.text())
		
		
		print(plaza,localidad)
		dat=plaza+","+localidad+","+str(noEquipo)
		infile = open("/home/pi/Documents/eum/app/expedidora/archivos_config/datos.txt", 'w')
		c=infile.write(dat)
		
		self.datosEstacionamiento()
		self.cambia(0)
		
	
		
	"""	
	def datosEstacionamiento(self):
		global plaza,localidad,noEquipo,host,ip,pol,pol1,pol2,pol3,pol4,pol5,impresora,anchoPapel
		lenn=0
		self.lnom.setText(plaza)
		self.lloc.setText(localidad)
		self.leq.setText(str(noEquipo))
		self.nomPlaza.setText(plaza)
		self.nomLoc.setText(localidad)
		self.lhost.setText(host)
		self.lip.setText(ip)
		
	
	def panelConfig(self):
		global plaza,localidad,noEquipo,host,ip
		infile = open('/home/pi/Documents/eum/app/caseta/archivos_config/datos.txt','r')
		datos= infile.readline()
		arr=datos.split(',')
		plaza=arr[0]
		localidad=arr[1]
		noEquipo=arr[2]
		infile.close()
		
		infile = open('/home/pi/Documents/eum/app/caseta/archivos_config/red.txt','r')
		datos= infile.readline()
		arr=datos.split(',')
		host=arr[0]
		ip=arr[1]
		infile.close()
	"""	
	
	
	
		

		
	def salirConf(self):
		global panelConf
		panelConf=0
		self.cambia(1)
		

	
	
	
	def sustituye(self,archivo,buscar,reemplazar):
		"""

		Esta simple función cambia una linea entera de un archivo

		Tiene que recibir el nombre del archivo, la cadena de la linea entera a

		buscar, y la cadena a reemplazar si la linea coincide con buscar

		"""
		with open(archivo, "r") as f:

			# obtenemos las lineas del archivo en una lista

			lines = (line.rstrip() for line in f)
			print(lines)

	 

			# busca en cada linea si existe la cadena a buscar, y si la encuentra

			# la reemplaza

			

			altered_lines = [reemplazar if line==buscar else line for line in lines]
			f= open(archivo, "w+")
			print(altered_lines[0],len(altered_lines))
			for i in range(len(altered_lines)):
				if(buscar in altered_lines[i]):
					print (altered_lines[i])
					cambia=altered_lines[i]
					f.write(reemplazar+"\n")
				else:
					f.write(altered_lines[i]+"\n")
			f.close()
			
			
	def cambiaIp(self):
		global sensor,segundos
		host=self.lhost.text()
		#ip=self.lip.text()

		

		
		segundos=str(self.lhost.text())
		sensor=int(self.ch1.checkState())
		
		
		print(plaza,localidad)
		dat=str(sensor)+","+str(segundos)
		infile = open("/home/pi/Documents/eum/app/expedidora/archivos_config/sensor.txt", 'w')
		c=infile.write(dat)
		
		self.datosEstacionamiento()
		self.cambia(1)
		
		
	def muestraPanel(self):
		self.cambia(4)
		#datos=obtenerPlazaYLocalidad()
		#self.lno.setText(str(datos[0]))
		#self.llo.setText(str(datos[1]))
		#datos=obtenerTerminal()
		self.lusu.setText('')
		self.lcont.setText('')
		self.lerror1.setText('')
		
	def cambia(self,val):
		self.stackedWidget.setCurrentIndex(val)
		############################MODS FIN#################
		
		
	def sustituye(self,archivo,buscar,reemplazar):
		"""

		Esta simple función cambia una linea entera de un archivo

		Tiene que recibir el nombre del archivo, la cadena de la linea entera a

		buscar, y la cadena a reemplazar si la linea coincide con buscar

		"""
		with open(archivo, "r") as f:

			# obtenemos las lineas del archivo en una lista

			lines = (line.rstrip() for line in f)
			print(lines)

	 

			# busca en cada linea si existe la cadena a buscar, y si la encuentra

			# la reemplaza

			

			altered_lines = [reemplazar if line==buscar else line for line in lines]
			f= open(archivo, "w+")
			print(altered_lines[0],len(altered_lines))
			for i in range(len(altered_lines)):
				if(buscar in altered_lines[i]):
					print (altered_lines[i])
					cambia=altered_lines[i]
					f.write(reemplazar+"\n")
				else:
					f.write(altered_lines[i]+"\n")
			f.close()
			
			
	def cambiaFecha(self):
		a=self.dtime.dateTime()
		b=self.dtime.textFromDateTime(a)
		print(b,type(b))
		os.system("sudo date -s '"+b+"' ")
	def setConfig(self):
		global plaza,localidad,terminalEnt,pol,pol1,pol2,pol3,pol4,pol5,impresora,anchoPapel
		lenn=0
		plaza=str(self.lno.text())
		localidad=str(self.llo.text())
		terminalEnt=str(self.le.text())
		impresora=int(self.cimpresora2.currentIndex())
		anchoPapel=int(self.cpapel2.currentIndex())
		
		pol1=str(self.Lp1.toPlainText())
		pol2=str(self.Lp2.toPlainText())
		pol3=str(self.Lp3.toPlainText())
		pol4=str(self.Lp4.toPlainText())
		pol5=str(self.Lp5.toPlainText())
		pol=pol1+pol2+pol3+pol4+pol5
		
		image = Image.open('/home/pi/Documents/eum/app/expedidora/logo.png')
		draw = ImageDraw.Draw(image)
		font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf', size=16)
 		 
		(x, y) = (0, 40)
		message1 = plaza
		color = 'rgb(0, 0, 0)' # black color		 
		draw.text((x, y), message1, fill=color, font=font)
		(x, y) = (0, 60)
		message2 = localidad
		draw.text((x, y), message2, fill=color, font=font)
		(x, y) = (0, 10)
		message3 = "¡BIENVENIDO!"
		font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf', size=22)
		draw.text((x, y), message3, fill=color, font=font)
		image.save('/home/pi/Documents/eum/app/expedidora/logoPT.png')
		
		
		
		if(impresora==0):
			#self.sustituye("/home/pi/.config/lxsession/LXDE-pi/autostart","@usr/bin/python3","@usr/bin/python3 /home/pi/Documents/eum/app/expedidora/firstMMM.py")
			self.sustituye("/home/pi/.bashrc","python3","sudo python3 /home/pi/Documents/eum/app/expedidora/firstMMM.py")
			if(anchoPapel==1):
				lista=pol.split("\n")
				pol=""
				for linea in lista:
					lenn += 1
					linea="   "+linea+"\n"
					pol=pol+linea
					print(lenn,linea)
				print("POOOOL",pol)
				
			if(anchoPapel==0):
				lista=pol.split("\n")
				pol=""
				for linea in lista:
					lenn += 1
					linea=""+linea+"\n"
					pol=pol+linea
					print(lenn,linea)
				print("POOOOL",pol)
				
			if(anchoPapel==2):
				lista=pol.split("\n")
				pol=""
				for linea in lista:
					lenn += 1
					linea="              "+linea+"\n"
					print(lenn,linea)
					pol=pol+linea
				print("POOOOL",pol)
		else:
			self.sustituye("/home/pi/.bashrc","python3","sudo python3 /home/pi/Documents/eum/app/expedidoraEpson/firstMMM.py")
					
		print(plaza,localidad)
		dat=plaza+","+localidad+","+str(terminalEnt)+","+str(impresora)+","+str(anchoPapel)
		infile = open("/home/pi/Documents/eum/app/expedidora/datos.txt", 'w')
		c=infile.write(dat)
		
		infile.close()
		infile = open("/home/pi/Documents/eum/app/expedidora/datos/pols.txt", 'w')
		c=infile.write(str(""))
		c=infile.write(str(pol))
		infile.close()
		infile = open("/home/pi/Documents/eum/app/expedidora/datos/pols1.txt", 'w')
		c=infile.write(str(pol1))
		infile.close()
		infile = open("/home/pi/Documents/eum/app/expedidora/datos/pols2.txt", 'w')
		c=infile.write(str(pol2))
		infile.close()
		infile = open("/home/pi/Documents/eum/app/expedidora/datos/pols3.txt", 'w')
		c=infile.write(str(pol3))
		infile.close()
		infile = open("/home/pi/Documents/eum/app/expedidora/datos/pols4.txt", 'w')
		c=infile.write(str(pol4))
		infile.close()
		infile = open("/home/pi/Documents/eum/app/expedidora/datos/pols5.txt", 'w')
		c=infile.write(str(pol5))
		infile.close()
		
		
		self.datosEstacionamiento()
		self.cambia(1)
		
		
	def salirConf(self):
		global panelConf
		panelConf=0
		self.cambia(1)
		
	def panelConfig(self):
		global sensor,segundos,plaza,localidad,terminalEnt,pol,pol1,pol2,pol3,pol4,pol5,impresora,anchoPapel,panelConf
		
		panelConf=1
		infile = open("/home/pi/Documents/eum/app/expedidora/datos.txt", 'r')
		c=infile.readline()
		arr=c.split(',')
		plaza=str(arr[0])
		localidad=str(arr[1])
		terminalEnt=str(arr[2])
		impresora=int(arr[3])
		anchoPapel=int(arr[4])
		infile.close()
		
		
		infile = open("/home/pi/Documents/eum/app/expedidora/archivos_config/sensor.txt", 'r')
		c=infile.readline()
		arr=c.split(',')
		sensor=int(arr[0])
		segundos=str(arr[1])
		infile.close()
		
		
		infile = open("/home/pi/Documents/eum/app/expedidora/datos/pols.txt", 'r')
		c=infile.read()
		pol=str(c)
		infile.close()
		infile = open("/home/pi/Documents/eum/app/expedidora/datos/pols1.txt", 'r')
		c=infile.read()
		pol1=str(c)
		infile.close()
		infile = open("/home/pi/Documents/eum/app/expedidora/datos/pols2.txt", 'r')
		c=infile.read()
		pol2=str(c)
		infile.close()
		infile = open("/home/pi/Documents/eum/app/expedidora/datos/pols3.txt", 'r')
		c=infile.read()
		pol3=str(c)
		infile.close()
		infile = open("/home/pi/Documents/eum/app/expedidora/datos/pols4.txt", 'r')
		c=infile.read()
		pol4=str(c)
		infile.close()
		infile = open("/home/pi/Documents/eum/app/expedidora/datos/pols5.txt", 'r')
		c=infile.read()
		pol5=str(c)
		infile.close()
		self.lusu.setText('')
		self.lcont.setText('')
		self.lerror1.setText('')
		self.datosEstacionamiento()
		self.cambia(4)
		
		
	def datosEstacionamiento(self):
		global sensor,segundos,plaza,localidad,terminalEnt,pol,pol1,pol2,pol3,pol4,pol5,impresora,anchoPapel
		self.lhost.setText(str(segundos))
		self.ch1.setCheckState(int(sensor))
		self.nomPlaza.setText(plaza)
		self.nomLoc.setText(localidad)
		self.nomPlaza2.setText(plaza)
		self.nomLoc2.setText(localidad)
		#self.nomPlaza3.setText(plaza)
		#self.nomLoc3.setText(localidad)
		#self.nomPlaza4.setText(plaza)
		#self.nomLoc4.setText(localidad)
		#self.nomPlaza5.setText(plaza)
		#self.nomLoc5.setText(localidad)
		
		#self.nomPlaza_2.setText(plaza)
		#self.nomPlaza_5.setText(plaza)
		self.lno.setText(plaza)
		self.llo.setText(localidad)
		self.le.setText(terminalEnt)
		#self.nomLoc.setText(localidad)
		#self.nomLoc_2.setText(localidad)
		#self.nomLoc_5.setText(localidad)
		self.Lp1.setText(pol1)
		self.Lp2.setText(pol2)
		self.Lp3.setText(pol3)
		self.Lp4.setText(pol4)
		self.Lp5.setText(pol5)
		self.cimpresora2.setCurrentIndex(impresora)
		self.cpapel2.setCurrentIndex(anchoPapel)

		
	def cambia(self,val):
		self.stackedWidget.setCurrentIndex(val)
		
	def solicitudBoleto(self):
		global teclaF3
		self.cambia(7)
		self.F3.setEnabled(False)
		print("F333333")
		teclaF3=1
		
	def configurarPinesGPIO(self):
		botones.configurarPinesGPIO()
		botones.configurarPinesGPIOBobina()

	pantalla = 0
	inicio = 0
	error = 0
	antes = 0
	f1 = f2 = f3 = f4 = f5 = f6 = False
				
		
	def registrarBoleto(self,mensaje):
		global conexion_activa
		if(not conexion_activa):
			""" Si no hay comunicacion con el servidor se procede
			a encolar los datos del pago para registrarlos cuando 
			vuelva la conexion"""
			try:
				print("Sin conexion")
				print("Encolando nuevo boleto: ",cola.incluir(mensaje))
				print("boletos pendientes: ",cola.inspeccionar())
				print("Cantidad de boletos: ",cola.tamano())
				resultado=-1
			except:
				print("Error al encolar el boleto")
		else:
			""" Si hay comunicacion con el servidor se busca que no
			existan pagos pendientes por alguna perdida de comunicaion
			y posteriormente se registra el pago
			vuelva la conexion"""
			try:
				validacion = clientes.configSocket("registro boleto",mensaje)
				resultado = clientes.enviarMensaje(validacion,mensaje)
				if(resultado==-1):
					print("No se pudo registrar el boleto")
				print("vacia", cola.estaVacia())
				while(not cola.estaVacia()):
					print("boleto pendientes: ",cola.inspeccionar())
					print("boleto restantes: ",cola.tamano())
					validacion = clientes.configSocket("registro boleto",mensaje)
					resultado = clientes.enviarMensaje(validacion,cola.extraer())
					if(resultado==-1):
						#break
						print("No se pudo registrar el boleto")
			except:
				print("Error al registrar boleto pendientes")
			
		
	def mostrarIconoWifi(self):
		global conexion_activa
		try:
			if(conexion_activa):
				self.bwifi.setEnabled(True)
			else:
				self.bwifi.setEnabled(False)
		except:
			print("ocurrio un error")
		
		
		
			
	def contadorSegundos(self):
		global avanza,z,zz,segundos, comienzaConteo,regreso
		
		self.mostrarIconoWifi()
		##HABILITAR DESHAB ANCHO PAPEL
		
		if(avanza==1):
			z=z+1
			print("ZZZZZZZZZZZZZZZZZZZ",z)
			if(z==5):
				self.cambia(9)
				z=0
				avanza=0
		if(comienzaConteo==1):
			zz=zz+1
			print("contando....,segundos",zz,segundos)
			if(int(zz)==int(segundos)):
				print("contando....,segundos",zz,segundos)
				print("contando....,segundos",zz,segundos)
				print("contando....,segundos",zz,segundos)
				print("contando....,segundos",zz,segundos)
				print("OKKKKK....,segundos",zz,segundos)
				print("contando....,segundos",zz,segundos)
				print("contando....,segundos",zz,segundos)
				print("contando....,segundos",zz,segundos)
				print("contando....,segundos",zz,segundos)
				print("contando....,segundos",zz,segundos)
				print("contando....,segundos",zz,segundos)
				print("contando....,segundos",zz,segundos)
				print("contando....,segundos",zz,segundos)
				print("contando....,segundos",zz,segundos)
				print("contando....,segundos",zz,segundos)
				print("contando....,segundos",zz,segundos)
				self.f1 = self.f2 = regreso = self.f4 = self.f5 = self.f6 = False
				zz=0
				self.cambia(1)
				self.F3.setEnabled(True)
				comienzaConteo=0
		QtCore.QTimer.singleShot(500, self.contadorSegundos)
			
	def leerBotones(self):
		global regreso,boleto_previo, espera, limite_impresiones,teclaF3,ser,panelConf,avanza,errImpresora,segundos,comienzaConteo,sensor
		##HABILITAR DESHAB ANCHO PAPEL
		
		if(self.cimpresora2.currentIndex()==1):
			self.cpapel2.setEnabled(False)
		else:
			self.cpapel2.setEnabled(True)
		print("PAPEL:",self.cpapel2.currentIndex())
		re.setReset()
		self.mostrarFechayHora()
		if self.pantalla == 0:
			pass
		elif self.pantalla == 1:
			if espera == 0:
				#mixer.init()
				#mixer.music.load('/home/pi/Documents/eum/app/expedidora/sonidos/mensaje2.mp3')
				#mixer.music.play()
				pass
			pass
			espera = espera + 1
			if espera == 25:
				espera = 0
				self.pantalla = 0
		else:
			pass
			espera = espera + 1
			if espera == 25:
				espera = 0
				self.pantalla = 0
		if self.inicio == 0:
			self.error = 0
			self.inicio = 1
			#self.checarFecha()
			#self.limpiarBD()
			#self.inicioImpresion()
			respuesta = imprimir.footer()
			#self.finImpresion()
			if respuesta == "No esta conectada la impresora":
				mensaje = str(terminalEnt) + "," + str(4) + "," + str("iniciada")
				#####validacion = clientes.configSocket("log expedidora")
				#####clientes.logExpedidora(validacion,"log expedidora",mensaje)
				self.error = 3
				self.pantalla = 1
		if botones.leerAyuda() == 1:
			self.pantalla = 2
		if self.error == 0:
			if boleto_previo == True and self.f1 == False:
				#self.inicioImpresion()
				respuesta = imprimir.imprimirHeader()
				#self.finImpresion()
				if respuesta == "No esta conectada la impresora":
					mensaje = str(terminalEnt) + "," + str(4) + "," + str("iniciada")
					#####validacion = clientes.configSocket("log expedidora")
					#####clientes.logExpedidora(validacion,"log expedidora",mensaje)
					self.error = 3
					self.pantalla = 1
				else:
					boleto_previo = False
			else:
				if botones.leerMasa() == 1:
					if self.f1 == False:
						print("------Preguntar Botones --------")	
						
						self.f1 = botones.leerBotonesEntrada()
						
						#self.f1 = teclaF3
						if(not panelConf):
							self.cambia(1)
							self.F3.setEnabled(True)
							if(errImpresora==1):
								self.lpress.setText("Disculpe la molestia\nPresione Nuevamente")
							else:
								self.lpress.setText("Presione")
						print("aaaaa",teclaF3)
					if self.f1 == True and self.f2 == False and regreso == False and self.f4 == False and self.f5 == False:
						if boleto_previo == False:
							self.cambia(7)
							self.F3.setEnabled(False)
							teclaF3 = 0
							noBolF = folio.saberFolio()
							folioBD = noBolF
							fechaIn	= fechaUTC.fechaConFormato()
							horaEnt = fechaUTC.tiempoConFormato()
							fechatimestamp = str(fechaIn)+" "+str(horaEnt)
							#self.insertarBoleto(plaza,terminalEnt,noBolF,fechatimestamp,'DEFAULT-ESCOM')
							''' Operacion 1.- Registro de boleto'''
							#mensaje = (idBoleto,idExpedidora,FechaExpedicion, idestado, idtipodescuento, idSalida)
							mensaje = noBolF + "," + str(terminalEnt) + "," + fechatimestamp + "," + str(1) + "," + str(1) + "," + str(0)
							#####validacion = clientes.configSocket("registro boleto")
							validacion = 1
							if validacion == "error":
								self.f1 = self.f2 = regreso = self.f4 = self.f5 = False
								self.pantalla = 1
							else:
								#####valor = clientes.enviarMensaje(validacion,mensaje)
								valor = 1
								if valor == "error":
									self.f1 = self.f2 = regreso = self.f4 = self.f5 = False
									self.pantalla = 1
								else:
									#self.insertarBoleto(plaza,terminalEnt,noBolF,fechatimestamp,'DEFAULT-ESCOM')
									
									#self.inicioImpresion()
									#respuesta = imprimir.imprimirQR22(noBolF,str(terminalEnt),str(fechaIn),str(horaEnt),plaza,localidad,costo)
									self.cambia(7)
									respuesta = imprimir.imprimirQR22(noBolF,str(terminalEnt),str(fechaIn),str(horaEnt),plaza,localidad,pol)
									print("respuesta= ",respuesta)
									#self.finImpresion()
									if respuesta != "ack":
										errImpresora=1
										print("ERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
										print("ERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
										print("ERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
										print("ERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
										print("ERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
										boleto_previo = True
										self.cambia(1)
										self.F3.setEnabled(True)
										self.lpress.setText("Disculpe la molestia\nPresione Nuevamente")
										errImpresora=1
										self.f1 = self.f2 = regreso = self.f4 = self.f5 = self.f6 = False
									else:
										#papel_cont = self.conteoBoletos()
										try:
											self.registrarBoleto(mensaje)
										except:
											print("Error al registrar en servidor")
											self.lpress.setText("Sin Comunicacion",validacion,valor)
										folio.escribirArchivoFolios(noBolF)
										papel_cont = 1
										errImpresora=0
										if papel_cont == limite_impresiones:
											#MANDAR MENSAJE AL SERVIDOR DE PAPEL CASI AGOTADO
											mensaje = str(terminalEnt) + "," + str(3) + "," + str("iniciada")
											#####validacion = clientes.configSocket("log expedidora")
											#####clientes.logExpedidora(validacion,"log expedidora",mensaje)
										papel_cont = papel_cont + 1
										##self.aumentoConteo(papel_cont)
										#mixer.init()
										#mixer.music.load('/home/pi/Documents/eum/app/expedidora/sonidos/mensaje1.mp3')
										#mixer.music.play()
										boleto_previo = True
										self.f2 = True
										self.lpress.setText("Presione")
										print("f2,regreso,f4,f5.f6= ",self.f2 ,regreso ,self.f4, self.f5,self.f6)
				if self.f2 == True and regreso == False and self.f4 == False  and self.f5 == False:
					if self.f6 == False:
						avanza=1
						print("Avance")
						
						time.sleep(1.5)
						botones.abrir()
						print("Abriendo")
						self.cambia(8)
						#self.lcabezal.setText("ESPERE")
						self.f6 = True
						
					if(comienzaConteo==0):
						#segundos=0
						
						comienzaConteo=1
						
						if(int(sensor)==2):
							print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",sensor)
							print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",sensor)
							print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",sensor)
							comienzaConteo=1
							print("NOTTTTTTTTTTTTTTTTTTTTT",regreso)
								
						else:
							comienzaConteo=0
							regreso = botones.leerBobina2Subida()
							print("ERRERERERERERERERE",regreso)
					#else:
					print("regresooooooo",regreso)	
					if regreso == True:
						print("F3=TRUEEEEEEEEEEEEE")
						print("F3=TRUEEEEEEEEEEEEE")
						print("F3=TRUEEEEEEEEEEEEE")
						print("F3=TRUEEEEEEEEEEEEE")
						print("F3=TRUEEEEEEEEEEEEE")
						print("F3=TRUEEEEEEEEEEEEE")
						print("F3=TRUEEEEEEEEEEEEE")
						print("F3=TRUEEEEEEEEEEEEE")
						print("F3=TRUEEEEEEEEEEEEE")
						print("F3=TRUEEEEEEEEEEEEE")
						print("F3=TRUEEEEEEEEEEEEE")
						self.F3.setEnabled(True)
						self.cambia(1)
						#self.lcabezal.setText("BIENVENIDO")
						self.f2 = False
				if self.f2 == False and regreso == True and self.f5 == False:
					self.f4 = botones.abrirBarrera()
					if self.f4 == True:
						regreso = False
				if self.f2 == False and regreso == False and self.f4 == True:
					self.f5 = botones.CerrarBarrera()
					if self.f5 == True:
						teclaF3 = 0
						self.f4 = False
				if self.f2 == False and regreso == False and self.f4 == False  and self.f5 == True:
					teclaF3 = 0
					self.f1 = self.f2 = regreso = self.f4 = self.f5 = self.f6 = False
		elif self.error == 2:
			respuesta = imprimir.imprimirHeader()
			if respuesta == "ack":
				boleto_previo = False
				self.error = 0
		elif self.error == 3:
			respuesta = imprimir.instanciarImpresora()
			if respuesta != "No esta conectada la impresora":
				self.error = 0
		QtCore.QTimer.singleShot(100, self.leerBotones)

	def inicioImpresion(self):
		try:
			connection = psycopg2.connect(user=usuario, password=contrasenia, database=bd, host='localhost')
			with connection.cursor() as cursor:
				cursor.execute(" UPDATE estado_impresora SET estado = 1,fecha = '"+ str(fechaUTC.fechaConFormato() + " " + fechaUTC.tiempoConFormato()) +"' WHERE idestadoimpresora = 1")
				connection.commit()
				connection.close()
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)

	def checarFecha(self):
		try:
			connection = psycopg2.connect(user=usuario, password=contrasenia, database=bd, host='localhost')
			with connection.cursor() as cursor:
				cursor.execute("SELECT max(fecha) FROM boletos;")
				row2 = cursor.fetchone()
				if row2[0] is not None:
					fec = row2[0].strftime("%d-%m-%Y")
					if fec != fechaUTC.fechaConFormato():
						escribeArch = open("/home/pi/Documents/eum/app/expedidora/archivos_config/UltimoFolio.txt","w")
						res = 0
						escribeArch.write(str(res)+"\n")
						escribeArch.close()
				else:
					escribeArch = open("/home/pi/Documents/eum/app/expedidora/archivos_config/UltimoFolio.txt","w")
					res = 0
					escribeArch.write(str(res)+"\n")
					escribeArch.close()	
				connection.commit()
				connection.close()
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)

	def limpiarBD(self):
		try:
			connection = psycopg2.connect(user=usuario, password=contrasenia, database=bd, host='localhost')
			with connection.cursor() as cursor:
				fecAct = fechaUTC.fechaConFormato()
				salto = 0
				dAct = ""
				mAct = ""
				aAct = ""
				for linea in fecAct:
					if salto == 0 and linea != "-":
						dAct = dAct + linea
					if salto == 1 and linea != "-":
						mAct = mAct + linea
					if salto == 2 and linea != "-":
						aAct = aAct + linea
					if linea == "-":
						salto = salto + 1
				mAct = int(mAct)
				aAct = int(aAct)
				if mAct > 4:
					mReg = mAct-4
					aReg = aAct
				else:
					mReg = 8 + mAct
					aReg = aReg - 1
				if mReg > 9:
					fechaReg = str(aReg) +"-"+str(mReg)+"-" + dAct +" 01:00:00"
				else:
					fechaReg = str(aReg) +"-0"+str(mReg)+"-" + dAct +" 01:00:00"
				cursor.execute("DELETE FROM boletos WHERE fecha < '{}';".format(fechaReg))
				connection.commit()
				connection.close()
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)

	def insertarBoleto(self,plz,terEnt,fol,fec,placa):
		try:
			connection = psycopg2.connect(user=usuario, password=contrasenia, database=bd, host='localhost')
			with connection.cursor() as cursor:
				cursor.execute("SELECT idplaza FROM plaza WHERE nombre_plaza = '" + plz + "';")
				row = cursor.fetchone()
				if row is not None:
					valor = int(row[0])
					connection.commit()
				cursor.execute("SELECT max(idboleto) FROM boletos;")
				row2 = cursor.fetchone()
				if row2[0] is not None:
					idbol = row2[0]
					idbol = idbol + 1
					connection.commit()
				else:
					idbol = 1
				cursor.execute("SELECT id_expedidora FROM datos_expedidora WHERE num_expedidora = {};".format(terEnt))
				row3 = cursor.fetchone()
				if row3[0] is not None:
					exp = row3[0]
					connection.commit()
				cursor.execute("INSERT INTO boletos (idboleto,plaza,expedidora,folio,fecha,placa) VALUES ({},{},{},{},'{}','{}');".format(idbol,valor,exp,fol,fec,placa))
				connection.commit()
				connection.close()
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)

	def finImpresion(self):
		try:
			connection = psycopg2.connect(user=usuario, password=contrasenia, database=bd, host='localhost')
			with connection.cursor() as cursor:
				cursor.execute(' UPDATE estado_impresora SET estado = 0 WHERE idestadoimpresora = 1')
				connection.commit()
				connection.close()
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)

	def mostrarFechayHora(self):
		fecha = fechaUTC.fechaConFormato()
		self.label_7.setText(fecha)
		#self.label_9.setText(fecha)
		self.label_21.setText(fecha)
		hora = fechaUTC.tiempoConFormato()
		self.label.setText(hora)
		#self.label_2.setText(hora)
		self.label_3.setText(hora)



		
	def logsDeApagado(self,tipo):
		infile = open("/home/pi/Documents/eum/app/expedidora/datos/logs.txt","r")
		datoss=infile.readline().split(',')
		if(tipo==1):
			encendidos=datoss[0]
			apagados=int(datoss[1])+1
		else:
			encendidos=int(datoss[0])+1
			apagados=datoss[1]
		print('apagados...',apagados)
		infile.close()
		
		infile = open("/home/pi/Documents/eum/app/expedidora/datos/logs.txt", 'w')
		wr=str(encendidos)+','+str(apagados)
		c=infile.write(wr)
		infile.close()
		
	def apagarRasp(self):
		self.logsDeApagado(1)
		os.system("sudo shutdown 0")

	def reiniciarRasp(self):
		os.system("sudo shutdown -r 0")

	

	def conteoBoletos(self):
		try:
			connection = psycopg2.connect(user=usuario, password=contrasenia, database=bd, host='localhost')
			with connection.cursor() as cursor:
				cursor.execute(
					' SELECT conteo FROM contador_tickets WHERE idconteo = 1')
				row = cursor.fetchone()
				if row is not None:
					conteo = int(row[0])
					connection.commit()
					connection.close()
					return conteo
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)

	def aumentoConteo(self,aumento):
		try:
			connection = psycopg2.connect(user=usuario, password=contrasenia, database=bd, host='localhost')
			with connection.cursor() as cursor:
				cursor.execute("UPDATE contador_tickets SET conteo = {} WHERE idconteo = 1".format(aumento))
				connection.commit()
				connection.close()
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)

	def reinicioConteo(self):
		try:
			connection = psycopg2.connect(user=usuario, password=contrasenia, database=bd, host='localhost')
			with connection.cursor() as cursor:
				cursor.execute("UPDATE contador_tickets SET conteo = 0 WHERE idconteo = 1")
				connection.commit()
				connection.close()
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)

class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        a=[0,0,0,0,0,0]
        #print(a)
        try:
            tty.setraw(sys.stdin.fileno())
            a[0]=ord(sys.stdin.read(1))
            if a[0]==27:
                a[1]=ord(sys.stdin.read(1))
            
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        # Decode keypress
        # https://mail.python.org/pipermail/python-list/2006-June/367344.html

        if a==[ 27, 91, 91,  67,   0, 0]: k=1061   # F3

        else:                               k=a[0]   # Ascii code

        return k

class BotonAyuda():
	
	def __init__(self):
		#self.configBotones()
		self.botonAyuda()
	
	def configBotones(self):
		botones.configurarPinesGPIO()
	
	
	def botonAyuda(self):
		global error_ayuda
		while (True):
			if botones.leerAyuda() == 1 and error_ayuda == 0:
				#mixer.init()
				#mixer.music.load('/home/pi/Documents/eum/app/expedidora/sonidos/mensajeayuda.mp3')
				#mixer.music.play()
				mensaje = str(terminalEnt) + "," + str(1) + "," + str("iniciada")
				#####validacion = clientes.configSocket("log expedidora")
				#####clientes.logExpedidora(validacion,"log expedidora",mensaje)
				error_ayuda = 1
			if error_ayuda == 1 and botones.leerAyuda() == 0:
				error_ayuda = 0
			time.sleep(1)

class EstadoImpresion():

	def __init__(self):
		self.estadoImpresora()

	#estado 0 sin problemas, estado 1 iniciado, estado 2 error enviado
	def estadoImpresora(self):
		global estado
		while(True):
			estado = self.consultaEstadoImpresora()
			if estado == 1:
				tiempo = self.consultarTiempoImpresion()
				if tiempo > 6:
					mensaje = str(terminalEnt) + "," + str(2) + "," + str("iniciada")
					#####validacion = clientes.configSocket("log expedidora")
					#####clientes.logExpedidora(validacion,"log expedidora",mensaje)
					self.errorEnviado()
			time.sleep(.200)

	def errorEnviado(self):
		try:
			connection = psycopg2.connect(user=usuario, password=contrasenia, database=bd, host='localhost')
			with connection.cursor() as cursor:
				cursor.execute(' UPDATE estado_impresora SET estado = 2 WHERE idestadoimpresora = 1')
				connection.commit()
				connection.close()
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)

	def consultarTiempoImpresion(self):
		try:
			connection = psycopg2.connect(user=usuario, password=contrasenia, database=bd, host='localhost')
			with connection.cursor() as cursor:
				cursor.execute(
					' SELECT fecha FROM estado_impresora WHERE idestadoimpresora = 1')
				row = cursor.fetchone()
				if row is not None:
					tiempo = self.tiempoEspera(row[0].strftime("%Y-%m-%d %H:%M:%S"))
					connection.commit()
					connection.close()
					return tiempo
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)

	def tiempoEspera(self,fecha_intento):
		tiempo_st = time.strptime(fecha_intento, "%Y-%m-%d %H:%M:%S")
		resultado = time.mktime(time.localtime()) - time.mktime(tiempo_st)
		return resultado

	def consultaEstadoImpresora(self):
		try:
			connection = psycopg2.connect(user=usuario, password=contrasenia, database=bd, host='localhost')
			with connection.cursor() as cursor:
				cursor.execute(
					' SELECT estado FROM estado_impresora WHERE idestadoimpresora = 1')
				row = cursor.fetchone()
				if row is not None:
					estado = int(row[0])
					connection.commit()
					connection.close()
					return estado
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)

def hilos():
	thread = Thread(target = activarFuncion, args=())
	thread1 = Thread(target = activarAyuda, args=())
	thread2 = Thread(target = pollConexion, args=())
	try:
		thread2.start()
		thread.start()
		thread1.start()
		
	except Exception:
		pass

def obtenerPlazaYLocalidad():
	global plaza
	global localidad
	try:
		connection = psycopg2.connect(user=usuario, password=contrasenia, database=bd, host='localhost')
		with connection.cursor() as cursor:
			cursor.execute(
				' SELECT nombre_plaza,estado FROM plaza WHERE idplaza = 1')
			row = cursor.fetchone()
			if row is not None:
				plaza = str(row[0])
				localidad = str(row[1])
				connection.commit()
				connection.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)

def obtenerTerminal():
	global terminalEnt
	try:
		connection = psycopg2.connect(user=usuario, password=contrasenia, database=bd, host='localhost')
		with connection.cursor() as cursor:
			cursor.execute(
				' SELECT num_expedidora FROM datos_expedidora WHERE id_expedidora = 1')
			row = cursor.fetchone()
			if row is not None:
				terminalEnt = int(row[0])
				connection.commit()
				connection.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)

def activarEstadoImpresion():
	EstadoImpresion()

def activarAyuda():
	BotonAyuda()
	
	
def pollearConexion():
	global conexion_activa
	try:
		conexion_activa = conexion.activo()
		print("conexion:",conexion_activa)
	except:
		print("ocurrio un error")

def pollConexion():
	while(1):
		pollearConexion()
		time.sleep(1)
	

def activarFuncion():
	import sys
	#logfile=open('logfile.log','w')
	#sys.stdout = logfile
	#sys.stdin = logfile
	#sys.stderr = logfile
	app = QApplication(sys.argv)
	ui = Ui_ventanaAcceso()
	ui.show()
	app.exec_()
	


			

if __name__ == "__main__":
	#obtenerTerminal()
	#obtenerPlazaYLocalidad()
	
	hilos()
	conexion = Conexiones()
	cola = Pila()
