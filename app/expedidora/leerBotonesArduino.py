# -*- coding: utf-8 -*-
##########################################
#
#	Libreria leerBotones para usar Arduino como interfaz (Instalación en PC)
#
##########################################

import serial
import time
import os

def iniciaSerial():
	ser = None
	for numero_arduino in range(0,5):
		mi_arduino = '/dev/ttyUSB'+ str(numero_arduino)
		if os.path.exists(mi_arduino):
			print(mi_arduino)
			ser = serial.Serial(mi_arduino, 9600)
			break
		else:
			print("No existe "+mi_arduino)
	return ser

def leerSerial(ser, imprimir=0):
	ser.flushInput()
	time.sleep(.2)
	r=ser.read(ser.inWaiting())
	r=ser.read(1)
	if(imprimir == 1):
		print(">> LECTURA SERIAL: ",r)
	time.sleep(0.01)
	return r


def leerMasa(arduino):
	r = leerSerial(arduino)
	valor = r[0]&0b00000001
	print("		Sensor masa: ", valor)
	if valor != 0:
		return True
	else:
		return False


def leerBotonesEntrada(arduino):
	r = leerSerial(arduino)
	valor = r[0]&0b00000010
	print("		Sensor boton: ", valor)
	if valor != 0:
		return True
	else:
		return False

def leerBobina2Subida(arduino):
	r = leerSerial(arduino)
	valor = r[0]&0b00000100
	print("		Sensor boton: ", valor)
	if valor != 0:
		return True
	else:
		return False
		
def leerAyuda():
	return 0

def abrir(ser):
	ser.write(b'O')
	return
	
def abrirBarrera():
	print(' -----TRATANDO DE ACCEDER FUNCION abrirBarrera')
	return True
	
def CerrarBarrera():
	print(' -----TRATANDO DE ACCEDER FUNCION CerrarBarrera')
	return True

if __name__ == "__main__":
	arduino = iniciaSerial()
	while True:
		leerMasa(arduino)
		leerBotonesEntrada(arduino)
		leerBobina2Subida(arduino)
		print('--------------')
