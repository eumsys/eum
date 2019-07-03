import requests
import json,os,sys,time
import cliente as Servidor
from datetime import datetime
from Pila.Pila import Pila


from urllib.request import urlopen
class Conexiones:
	"""Clase utilizada para guardar los datos 
	en caso un intento de conexion fallido
	"""

	def __init__(self):
		self.items = []
		cola = Pila()


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

	def servidorActivo(self):
		timestamp=datetime.now()		
		mensaje=str("2")+","+str("0")+","+str(21)
		resultado=Servidor.configSocket("log", mensaje)
		if(resultado==-1):
			return False
		else:
			return True
			
			
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
