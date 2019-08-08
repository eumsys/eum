import requests
import json,os,sys,time
from datetime import datetime
from Pila.Pila import Pila


from urllib.request import urlopen



ruta =  os.path.join(os.path.dirname(os.path.abspath(__file__)))
ruta = ruta + "/"
def obtenerUsuario(ruta):
	lista = ruta.split("/")
	return "/"+lista[1]+"/"+lista[2]+"/"	
rutaUsuario = obtenerUsuario(ruta)
print(rutaUsuario)



raiz =  os.path.join(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(raiz)

import cliente as Servidor
class Conexiones:
	"""Clase utilizada para guardar los datos 
	en caso un intento de conexion fallido
	"""

	def __init__(self):
		self.items = []
		cola = Pila()
		self.obtenerConfiguracion()

	def activo(self):
		conexionServ=1
		try:
			conexionServ=os.system("sudo ping -c 1 192.168.1.129")
			if conexionServ:
				return False
			else:
				return True
		except: 
			return conexionServ
	
	def obtenerConfiguracion(self):
		#global equipo, sucursal, tipo
		try:
			infile = open(rutaUsuario+"eum.conf", 'r')
			c=infile.readline()
			arr=c.split(',')
			self.__equipo=int(arr[0])
			self.__sucursal=int(arr[1])
			self.__tipo=int(arr[2])
			infile.close()
		except:
			self.__equipo=1
			self.__sucursal=1
			self.__tipo=0
			infile = open(rutaUsuario+"eum.conf", "w")
			infile. write(str(self.__equipo)+","+str(self.__sucursal)+","+str(self.__tipo))
			infile. close()
		print("equipo,sucursal,tipo ",self.__equipo,self.__sucursal,self.__tipo)

		
		
	
	def servidorActivo(self):
		timestamp=datetime.now()		
		mensaje=str("2")+","+str("0")+","+str(21)
		resultado=Servidor.configSocket("log", mensaje)
		if(resultado==-1):
			return False
		else:
			return True


	def pollConexion(self,tipo):
		timestamp=datetime.now()	
		print("equipo.......",self.__equipo,self.__tipo)	
		mensaje=str("2")+","+str(tipo)+","+str(self.__tipo)+str(self.__equipo)
		resultado=Servidor.configSocket("log", mensaje)
		if(resultado==-1):
			return False
		else:
			return True

	def logPrendido(self):
		mensaje=str("2")+","+str("1")+","+str(self.__tipo)+str(self.__equipo)
		resultado=Servidor.configSocket("log", mensaje)
		if(resultado==-1):
			return False
		else:
			return True

	def obtenerLogs(self):
		mensaje=str("2")+","+str("4")+","+str(21)
		logs=Servidor.configSocket("log", mensaje)
		if(logs==-1):
			return False
		else:
			logsResult =  []
			logs =  str(logs.decode('utf-8'))
			tmp = len(logs)
			logs = logs[:tmp -1]
			logs = logs.replace("["," ")        
			logs = logs.split(",")
	       	#logs = logs[3]
	       	#logs = logs.split(',')
	        #for log in logs:
	        #    print("Nodo: "+str(log[3])+"  "+"Fecha:"+str(log[1]))
			for log in logs:
				tmp = len(log)
				log = log[2:tmp -1]
				logsResult.append(log)
			return logsResult
			
			
	def buscarTicket(self,mensaje):
		try:
			resultado=Servidor.configSocket("informacion boleto", mensaje)
			if(resultado == "boleto no localizado"):
				print("Registrando boleto no localizado...")
			else:
				print("boleto no localizado, esperando su registro...")
			return resultado
		except:
			print("Error en la busqueda del ticket")
			return -1
			
			
	def registrarPago(self,mensaje):
		try:
			Servidor.configSocket("pago boleto", mensaje)
			if(resultado == "boleto no localizado"):
				print("Registrando boleto no localizado...")
			else:
				print("boleto no localizado, esperando su registro...")
			return resultado
		except:
			print("Error en el registro del pago")
			return -1
			
	def encolarPago(self,mensaje):
		try:
			print(cola.estaVacia())
		except:
			print("Error al encolar el pago")
			return -1


	def estaVacia(self):
		return self.items == []

	def incluir(self, item):
		self.items.append(item)

	def extraer(self):
		return self.items.pop()

	def inspeccionar(self):
		return self.items[len(self.items)-1]

	def tamano(self):
		return len(self.items)
