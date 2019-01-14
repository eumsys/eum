# -*- coding: utf-8 -*-

from escposprinter import *#original funcional
import tratarImagen as imagen
import configuracionEXP as archivoConfiguracion
import time
import codigoQR as codigoGenerar
import psycopg2
import signal

usuario = 'postgres'
contrasenia = 'Postgres3UMd6'
db = 'dbeum_tecamac'

def instanciarImpresora():
	try:
		Generic = printer.Usb(0x0519,0x0001)
		return Generic
	except Exception as error:
		return "No esta conectada la impresora"

def imprimirHeader():
	nom_plaza = ""
	politicas = ""
	try:
		connection = psycopg2.connect(user=usuario, password=contrasenia, database=db, host='localhost')
		with connection.cursor() as cursor:
			cursor.execute(' SELECT nombre_plaza FROM plaza WHERE idplaza = 1')
			row = cursor.fetchone()
			if row is not None:
				nom_plaza = str(row[0])
				connection.commit()
			else:
				print("No se encontro la plaza")
			cursor.execute(' SELECT descripcion FROM politicas WHERE idpoliticas = 1')
			row2 = cursor.fetchone()
			if row2 is not None:
				politicas = str(row2[0])
				connection.commit()
			else:
				print("No se encontraron las politicas")
			connection.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
		return "No se pudo establecer conexion con la base de datos"
	try:
		Generic = instanciarImpresora()
		if Generic == "No esta conectada la impresora":
			return Generic
		Generic.set(size='2x', align='center')
		Generic.text('Bienvenido \n'+str(nom_plaza)+'\n')
		Generic.set(size='normal',align='center')
		palabra = ""
		for letra in politicas:
			if letra != "|":
				palabra = palabra + letra
			else:
				Generic.text(palabra)
				Generic.text(" \n")
				palabra = ""
		return "ack"
	except Exception as error:
		print(error)
		return "No se pudo imprimir"
	except TimeoutException:
		return "No se pudo imprimir"

def imprimirQR2(noBol,terminalEnt,fechaIn,horaEnt):
	try:
		Generic = instanciarImpresora()
		if Generic == "No esta conectada la impresora":
			return Generic
		Generic.text('Expedidora #'+terminalEnt+'\n')
		Generic.text('Folio:'+str(noBol)+'   '+fechaIn+' '+horaEnt +'\n')
		Generic.qr("Estacionamientos unicos de Mexico\n"+noBol+"\n"+terminalEnt+"\n"+fechaIn+"\n"+horaEnt)
		Generic.cut()
		print("QR bien impresa")
		return "ack"
	except Exception as error:
		print("ERROR AL IMPRIMIR QR")
		return "No se pudo imprimir"

def footer():
	try:
		Generic = instanciarImpresora()
		if Generic == "No esta conectada la impresora":
			return Generic
		Generic.cut()
		print(e)
		return "ack"
	except Exception as error:
		return "No se pudo imprimir"

#imprime= commands.getoutput("lp -d SANEI_SK_Series /home/pi/Documents/eum/impresora/pruebas/test.pdf")
#imprimirHeader()
#imprimirQR2("28","1","07/09/2017","09:42:00")
