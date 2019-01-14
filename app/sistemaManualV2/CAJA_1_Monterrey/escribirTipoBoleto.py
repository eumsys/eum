# -*- coding: utf-8 -*-

"""
Funciones para leer datos
"""
PATH_ARCHIVO_CONFIGURACION_TERMINAL="/home/pi/Documents/CAJA_1_Monterrey/tipoBoleto.txt"

configuracion=''

def getDato():
	archivo=open(PATH_ARCHIVO_CONFIGURACION_TERMINAL, "r")
	for linea in archivo.readlines():
		configuracion =linea
	archivo.close()
	return configuracion
	pass
	
def putDato(boleto):
	archivo=open(PATH_ARCHIVO_CONFIGURACION_TERMINAL, "w")
	archivo.write(boleto)
	archivo.close()


#putDato("Suburbia")
#print getDato()
