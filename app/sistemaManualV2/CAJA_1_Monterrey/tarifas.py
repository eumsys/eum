# -*- coding: utf-8 -*-

import math

import escribirTipoBoleto as boleto
import os

COSTO_POR_HORA_EXTRA=10
COSTO_POR_HORA_EXTRA_CON_SELLO=3.4
COSTO_POR_HORA_EXTRA_SIN_SELLO=10
HORAS_DE_COOPERACION_VOLUNTARIA=120 #MINUTOS
COSTO_BOLETO_PERDIDO=100
TIEMPO_TOLERANCIA_TAXI=5
PATH_INTERFAZ_TIPO_BOLETO="/home/pi/Documents/CAJA_1_Monterrey/tipoBoleto.py"
#PATH_TARIFAS = "/home/pi/Documents/CAJA_1_Monterrey/datos_tikets/tarifa.txt"


def preguntarPorVoluntario():
	#LLAMO A A¿LA INTERFAZ
	os.system("python "+PATH_INTERFAZ_TIPO_BOLETO)
	return boleto.getDato()

def calcularMonto(purosMinutos,tar,volunt):
	total=0
	tarifa=int(tar)
	tiempo=int(purosMinutos)
	voluntaria=int(volunt)
	#archi = open(PATH_TARIFAS,"r")
	#COSTO_POR_HORA_EXTRA_CON_SELLO=int(archi.readline())
	#archi.close()
	print("TARIFA:"+COSTO_POR_HORA_EXTRA_CON_SELLO)
	print tiempo 
	#tarifa1  reglas: 2 primeras horas cooperacion voluntaria, restante 10 cada hora o fraccion adicional
	if tarifa==1:
		if tiempo>HORAS_DE_COOPERACION_VOLUNTARIA:
			tarifaSELLO=preguntarPorVoluntario()#Preguntamos por el sello
			if tarifaSELLO=='conBanco'  or tarifaSELLO=='conSuburbia':
				tiempoResiduo=(tiempo-HORAS_DE_COOPERACION_VOLUNTARIA)
				horasPasadas=float(float(tiempoResiduo)/60.0)
				horasPasadas=math.ceil(horasPasadas) #subimos al entero proximo
				total=(horasPasadas)*COSTO_POR_HORA_EXTRA_SIN_SELLO
				total=total+COSTO_POR_HORA_EXTRA_CON_SELLO
				if tarifaSELLO=='conBanco':
					return float(total),4
				else:
					return float(total),5
			elif tarifaSELLO=='sin':
				horasPasadas=float(float(tiempo)/60.0)
				horasPasadas=math.ceil(horasPasadas) #subimos al entero proximo
				total=(horasPasadas)*COSTO_POR_HORA_EXTRA_SIN_SELLO
				return float(total),1
			elif tarifaSELLO=='taxi':
				if tiempo<=5:
					total=0
					return float(total),6
				else:
					horasPasadas=float(float(tiempo)/60.0)
					horasPasadas=math.ceil(horasPasadas) #subimos al entero proximo
					total=(horasPasadas)*COSTO_POR_HORA_EXTRA_SIN_SELLO
					return float(total),6
		if tiempo<=HORAS_DE_COOPERACION_VOLUNTARIA:
			tarifaSELLO=preguntarPorVoluntario()#Preguntamos por el sello
			if tarifaSELLO=='conBanco'  or tarifaSELLO=='conSuburbia':
				total=COSTO_POR_HORA_EXTRA_CON_SELLO
				if tarifaSELLO=='conBanco':
					return float(total),4
				else:
					return float(total),5
			elif tarifaSELLO=='sin':
				horasPasadas=float(float(tiempo)/60.0)
				horasPasadas=math.ceil(horasPasadas) #subimos al entero proximo
				total=(horasPasadas)*COSTO_POR_HORA_EXTRA_SIN_SELLO
				return float(total),1
			elif tarifaSELLO=='taxi':
				if tiempo<=5:
					total=0
					return float(total),6
				else:
					horasPasadas=float(float(tiempo)/60.0)
					horasPasadas=math.ceil(horasPasadas) #subimos al entero proximo
					total=(horasPasadas)*COSTO_POR_HORA_EXTRA_SIN_SELLO
					return float(total),6
	#tarifa2 reglas: Locatario 0 Pesos
	if tarifa==2:
		total=0
		print(total)
		return float(total),2
	#tarifa3 reglas:Boleto perdido 
	if tarifa==3:
		total=COSTO_BOLETO_PERDIDO
		print(total)
		return float(total),3

#print calcularMonto(12,1,25342534)


