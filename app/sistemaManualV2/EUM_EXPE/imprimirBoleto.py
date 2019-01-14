# -*- coding: utf-8 -*-
"""
Estacionamientos unicos de México
Este archivo es para remplaar a acceso4.py
Funcion: 		Funcion de imprimir boleto
Descripcion:	

Funciones que se pueden usar:
	1) imprimirBoletoT tiempo corto formato largo
	2) imprimirBoleto  tiempo largo formato pequeño

"""
from escposprinter import *#original funcional
import tratarImagen as imagen
import configuracionEXP as archivoConfiguracion
import time
import codigoQR as codigoGenerar

PATH_NOMBRE_PLAZA=str(archivoConfiguracion.getName()).replace('\n','')
PATH_NUMERO_TERMINAL=str(archivoConfiguracion.getNumTer()).replace('\n','')
PATH_CODIGOS_QR="/home/pi/Documents/EUM_EXPE/CodigosQR/outputQR.png"

#PATH_NOMBRE_PLAZA="SORIANA AMERICAS"
def instanciarImpresora():
	Generic = printer.Usb(0x0519,0x0001)
	return Generic

def checarPapel():
	Generic = instanciarImpresora()
	return Generic.paper_status()


def imprimirHeader():
	Generic = instanciarImpresora()
	Generic.set(size='2x', align='center')
	Generic.text('Bienvenido \n'+str(PATH_NOMBRE_PLAZA)+'\n')
	Generic.set(size='normal',align='center')
	Generic.text("La empresa no se hace responsable por objetos\npersonales,fallas mecanicas  y/o  electricas,\nsiniestros ocasionados por derrumbes,temblores,\nterremotos o fenomenos naturales,asi como ro-\nbo de accesorios o vandalismo en su vehiculo.\n")
	Generic.text("Por robo total de acuerdo a los terminos  del\nseguro contratado.Boleto Perdido.Se entregara\nel  vehiculo  a quien acredite la  propiedad.\nCosto del boleto perdido es de $100.00\n")
	Generic.text("Al recibir este boleto acepta las condiciones\ndel seguro contra robo total. PARKING TIP S.A\nDE  C.V.  -R.F.C PTI120210571. Escobillera 13\nCol.Paseos de Churubusco Iztapalapa CDMX C.P.\n09030 Horario de Lunes-Domingo de 7 a 22 hrs \n")
	
def imprimirHeaderHermosillo():
	Generic = instanciarImpresora()
	Generic.set(size='2x', align='center')
	Generic.text('Bienvenido \n'+str(PATH_NOMBRE_PLAZA)+'\n')
	Generic.set(size='normal',align='center')
	Generic.text("La empresa no se hace responsable por objetos\npersonales,fallas mecanicas  y/o  electricas,\nsiniestros ocasionados por derrumbes,temblores,\nterremotos o fenomenos naturales,así como ro-\nbo de accesorios o vandalismo en su vehículo.\n")
	Generic.text("Por robo total de acuerdo a los terminos  del\nseguro contratado.Boleto Perdido se entregará\nel  vehículo  a quien acredite la  propiedad.\n")
	Generic.text("Al recibir este boleto acepta las condiciones\ndel seguro contra robo total. PARKING TIP S.A\nDE  C.V.  -R.F.C PTI120210571. Escobillera 13\nCol.Paseos de Churubusco Iztapalapa CDMX C.P.\n09030 Horario de Lunes-Domingo de 7 a 22 hrs \n")
	Generic.text("Tarifa aplicada al estacionamiento: primeras \n2 horas con sello  de WALLMART corresponden a\n$5, hora o fracción $10 MXN, boleto sin sello\n$10 cada hora.Costo del boleto perdido:$100MXN\n")
	#Generic.cut()
	
#imprimirHeaderHermosillo()

	
def imprimirQR(noBol,terminalEnt,fechaIn,horaEnt):
	Generic = instanciarImpresora()
	Generic.text('Expedidora #'+PATH_NUMERO_TERMINAL+'\n')
	Generic.text('Folio: GM'+str(noBol)+' '+fechaIn+' '+horaEnt +'\n')
	Generic.qr(noBol+"\n"+terminalEnt+"\n"+fechaIn+"\n"+horaEnt)
	Generic.cut()
	
def  imprimirQR2(noBol,terminalEnt,fechaIn,horaEnt):
	Generic = instanciarImpresora()
	codigoGenerar.construirCodigoEntrada(noBol,terminalEnt,fechaIn,horaEnt)
	codQR=imagen.cambiarTamQR(PATH_CODIGOS_QR)
	Generic.text('Expedidora #'+PATH_NUMERO_TERMINAL+'\n')
	Generic.text('Folio: GM'+str(noBol)+' '+fechaIn+' '+horaEnt +'\n')
	Generic.image(codQR)
	Generic.cut()


#imprimirHeader()
#imprimirQR("GM:12","3","21/03/2017","8:00:00")


def header():
	Generic = instanciarImpresora()
	Generic.set(size='2x', align='center')
	Generic.text('Bienvenido \n'+str(PATH_NOMBRE_PLAZA))
	Generic.set(size='normal',align='center')

def footer():
	Generic.cut()

def informacionEXT():
	Generic.set(size='normal', align='center')
	Generic.text("La empresa no se hace responsable por objetos\npersonales,fallas mecanicas  y/o  electricas,\nsiestros ocasionados por derrumbes,temblores,\nterremotos o fenomenos naturales,asi como ro-\nbo de accesorios o vandalismo en su vehiculo.\n")
	Generic.text("Por robo total de acuerdo a los terminos  del\nseguro contratado.Boleto Perdido.Se entregara\nel  vehiculo  a quien acredite la  propiedad.\nCosto del boleto perdido es de $100.00\n")
	Generic.text("Al recibir este boleto acepta las condiciones\ndel seguro contra robo total. PARKING TIP S.A\nDE  C.V.  -R.F.C PTI120210571. Escobillera 13\nCol.Paseos de Churubusco Iztapalapa CDMX C.P.\n09030 Horario de Lunes-Domingo de 7 a 22 hrs \n")
	
#imprimirBoletoT(123,4,"6/12/2016")
