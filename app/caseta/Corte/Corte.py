# -*- coding: utf-8 -*-
"""

Estacionamientos unicos de México
Consulta la base de datos en un intervalo de fechas.
Envia datos a la api para registrar corte 


"""
import fechaUTC as hora
import time
import psycopg2, psycopg2.extras
import datetime
import qrcode
import requests
import json
import os,sys

fechaHoy=time.strftime("%Y-%m-%d")
horaHoy=time.strftime("%H:%M:%S")






	
def checale(fecha1,fecha2,turno,folio):
	global cur,generic,dats,tipos,sucursal,fechaHoy,horaHoy
	boletaje='-'
	fecha=hora.mostrarFechayHora()
	
	infile = open('/home/pi/Documents/eum/app/caseta/archivos_config/datos.txt','r')
	datos= infile.readline()
	arr=datos.split(',')
	plaza=arr[0]
	localidad=arr[1]
	idCajero=arr[2]
	infile.close()
			
	
	importe=''
	cur.execute("select costo,COUNT(\"idBoleto\") from \"BOLETO\" where \"fechaExpedicion\" BETWEEN '"+fecha1+"' and '"+fecha2+"' group by costo ")
	for reg in cur: 
		#print(reg[0],reg[1])
		#Generic.text('Boletos de '+str(reg[0])+' --> '+str(reg[1])+'\n')
		boletaje=boletaje+str(reg[1])+':'+str(int(reg[0]))+'\n'
	print(boletaje)
		
	cur.execute("select SUM(\"costo\") from \"BOLETO\" where \"fechaExpedicion\" BETWEEN '"+fecha1+"' and '"+fecha2+"'")
	for reg in cur: 
		#print("AAAS"reg[0])
		#Generic.text('\nDinero total:'+str(reg[0])+'\n\n')
		tot=str(reg[0])
		if(tot=='None'):
			tot=0
		else:
			tot=int(reg[0])
	#print(dats)
	conn = psycopg2.connect(database='caseta',user='postgres',password='Postgres3UMd6', host='localhost')
	cur = conn.cursor()
	cur2 = conn.cursor()
	print(fecha1,fecha2)
	cur.execute("select tipo,COUNT(\"idBoleto\") from \"BOLETO\" where \"fechaExpedicion\" BETWEEN '"+fecha1+"' and '"+fecha2+"' group by tipo ")
	for rega in cur: 
		print("tipazos",rega[0],rega[1])
		cur2.execute("select nombre from \"TIPO\" where \"idTipo\"="+str(rega[0])+"")
		for reg in cur2: 
			print(reg[0])
			
		#Generic.text('Pagos '+str(reg[0])+' --> '+str(rega[1])+'\n')
		print("TIPOSSSSSSSSSSSSSSSSS1",tipos)
		print("TIPOSSSSSSSSSSSSSSSSS2",rega[0],rega[1], int(rega[0])-1,(rega[1]))
		
		tipos[int(rega[0])-1]=(rega[1])
		print("TIPOSSSSSSSSSSSSSSSSS3",tipos)
		dats=dats+'Pagos '+str(reg[0])+' --> '+str(rega[1])+'\n'
		
	#print(dats)
	cur.execute("select SUM(\"costo\") from \"BOLETO\" where \"fechaExpedicion\" BETWEEN '"+fecha1+"' and '"+fecha2+"'")
	for reg in cur: 
		print(reg[0])
		#Generic.text('Dinero total:'+str(reg[0])+'\n\n')

	#Generic.cut()
	##tipos[5]:Cobrados,tipos6:Incompletos,tipos4:propina, tipos7:s/propina, tipos2: Perdidos
	sinSello='0'
	locales='0'
	cancelados='0'
	proovedores='0'
	tolerancias='0'
	
	cortesias='0'
	gastos='0'
	nomina='0'
	bonos='0'
	dobletes='0'
	anticipoDeDepositos='0'
	
	dats=folio+";"+plaza+"; ;"+fecha+";"+str(idCajero)+";"+turno+";"+str(sinSello)+";"+str(tipos[5])+";"+str(tipos[6])+";"+str(tipos[4])+";"+str(tipos[7])+";"+locales+";"+cancelados+";"+proovedores+";"+tolerancias+";"+str(tipos[2])+";"+str(tot)+";"+boletaje+";"+cortesias+";"+gastos+";"+nomina+";"+bonos+";"+dobletes+";"+anticipoDeDepositos
	##tipos[5]:Cobrados,tipos6:Incompletos,tipos4:propina, tipos7:s/propina, tipos2: Perdidos
	qr= qrcode.QRCode(
		version=4,
		box_size=7,
		border=4,
	)
	conexionServ=os.system("ping -c 1 parkingtip.pythonanywhere.com")
	print("conexionServ",conexionServ)
	if conexionServ != 0:
		try:
			qr.add_data(dats)
			qr.make(fit=True)
			img= qr.make_image(back_color='black')
			f = open("/home/pi/Documents/eum/app/iconos/outputQR2.png", "wb")
			img.save(f)
			f.close()
		except:
			print("Error de registro del corte privado")
			return "Error registro corte privado"
	else:
		try:
			print("turno:",turno)
			if("V" in turno):
				turno="Vespertino"
			else:
				turno="Matutino"
			payload = {
			"turno": turno,
			"boletaje": "0",
			"recuperados": str(int(tipos[5])+int(tipos[8])+int(tipos[1])),
			"sellados": str(tipos[5]),
			"noSellados": str(tipos[8]),
			"incompletos": str(tipos[6]),
			"propina": str(tipos[4]),
			"sinpropina": str(tipos[7]),
			"cortesias": "0",
			"tolerancias": tolerancias,
			"locatarios": str(tipos[1]),
			"caja": str(idCajero),
			"created": fechaHoy+"T"+horaHoy,
			"ingreso": str(tot),
			"detalles": boletaje,
			"encargado": "1",
			"sucursal_id": sucursal
			}
			r = requests.post("https://parkingtip.pythonanywhere.com/api/cortes/create/", json=payload)
			#r = requests.post("http://127.0.0.1:8000/api/cortes/create/", json=payload)
			print("Result...:",r.text,", turno:",turno)
		except:
			print("Error de registro del corte publico")
			return "Error registro corte publico"
		
		


			
			
			
			gui = uic.loadUi("/home/pi/Documents/eum/app/caseta/rbCaseta.ui", self)
			self.montos()

class Corte():
	def __init__(self):
		self.sucursal = "11"
		
	def obtenerCorte(self,fecha1,fecha2,folio):
		importe=''
		boletaje='-'
		tipos=[0,0,0,0,0,0,0,0,0]
		dats = ""
		infile = open('/home/pi/Documents/eum/app/caseta/archivos_config/datos.txt','r')
		datos= infile.readline()
		arr=datos.split(',')
		plaza=arr[0]
		localidad=arr[1]
		idCajero=arr[2]
		infile.close()
		fecha=hora.mostrarFechayHora()

				
		#Conectando a la base
		conn = psycopg2.connect(database='caseta',user='postgres',password='Postgres3UMd6', host='localhost')
		cur = conn.cursor()
		
		cur.execute("select costo,COUNT(\"idBoleto\") from \"BOLETO\" where \"fechaExpedicion\" BETWEEN '"+fecha1+"' and '"+fecha2+"' group by costo ")
		for reg in cur: 
			#print(reg[0],reg[1])
			#Generic.text('Boletos de '+str(reg[0])+' --> '+str(reg[1])+'\n')
			boletaje=boletaje+str(reg[1])+':'+str(int(reg[0]))+'\n'
		print("Boletaje:",boletaje)
			
		cur.execute("select SUM(\"costo\") from \"BOLETO\" where \"fechaExpedicion\" BETWEEN '"+fecha1+"' and '"+fecha2+"'")
		for reg in cur: 
			#print("AAAS"reg[0])
			#Generic.text('\nDinero total:'+str(reg[0])+'\n\n')
			importe=str(reg[0])
			if(importe=='None'):
				importe=0
			else:
				importe=int(reg[0])
		print(importe)
		conn = psycopg2.connect(database='caseta',user='postgres',password='Postgres3UMd6', host='localhost')
		cur = conn.cursor()
		cur2 = conn.cursor()
		print(fecha1,fecha2)
		cur.execute("select tipo,COUNT(\"idBoleto\") from \"BOLETO\" where \"fechaExpedicion\" BETWEEN '"+fecha1+"' and '"+fecha2+"' group by tipo ")
		for rega in cur: 
			#print("tipazos",rega[0],rega[1])
			cur2.execute("select nombre from \"TIPO\" where \"idTipo\"="+str(rega[0])+"")
			for reg in cur2: 
				print(reg[0])
				
			#Generic.text('Pagos '+str(reg[0])+' --> '+str(rega[1])+'\n')
			#print("TIPOSSSSSSSSSSSSSSSSS1",tipos)
			#print("TIPOSSSSSSSSSSSSSSSSS2",rega[0],rega[1], int(rega[0])-1,(rega[1]))
			
			tipos[int(rega[0])-1]=(rega[1])
			print("Desglose:",tipos)
			dats=dats+'Pagos '+str(reg[0])+' --> '+str(rega[1])+'\n'
			
		#print(dats)
		cur.execute("select SUM(\"costo\") from \"BOLETO\" where \"fechaExpedicion\" BETWEEN '"+fecha1+"' and '"+fecha2+"'")
		for reg in cur: 
			print(reg[0])
			#Generic.text('Dinero total:'+str(reg[0])+'\n\n')


		return boletaje,importe,tipos
		
	def enviarDatosApi(self,boletaje,importe,tipos,turno):
		#Generic.cut()
		##tipos[5]:Cobrados,tipos6:Incompletos,tipos4:propina, tipos7:s/propina, tipos2: Perdidos
		fecha=hora.mostrarFechayHora()
		infile = open('/home/pi/Documents/eum/app/caseta/archivos_config/datos.txt','r')
		datos= infile.readline()
		arr=datos.split(',')
		plaza=arr[0]
		localidad=arr[1]
		idCajero=arr[2]
		infile.close()
		
		sinSello='0'
		locales='0'
		cancelados='0'
		proovedores='0'
		tolerancias='0'
		
		cortesias='0'
		gastos='0'
		nomina='0'
		bonos='0'
		dobletes='0'
		anticipoDeDepositos='0'
		
		dats=folio+";"+plaza+"; ;"+fecha+";"+str(idCajero)+";"+turno+";"+str(sinSello)+";"+str(tipos[5])+";"+str(tipos[6])+";"+str(tipos[4])+";"+str(tipos[7])+";"+locales+";"+cancelados+";"+proovedores+";"+tolerancias+";"+str(tipos[2])+";"+str(importe)+";"+boletaje+";"+cortesias+";"+gastos+";"+nomina+";"+bonos+";"+dobletes+";"+anticipoDeDepositos
		##tipos[5]:Cobrados,tipos6:Incompletos,tipos4:propina, tipos7:s/propina, tipos2: Perdidos
		qr= qrcode.QRCode(
			version=4,
			box_size=7,
			border=4,
		)
		conexionServ=os.system("ping -c 1 parkingtip.pythonanywhere.com")
		print("conexionServ",conexionServ)
		if conexionServ != 0:
			try:
				qr.add_data(dats)
				qr.make(fit=True)
				img= qr.make_image(back_color='black')
				f = open("/home/pi/Documents/eum/app/iconos/outputQR2.png", "wb")
				img.save(f)
				f.close()
			except:
				print("Error de registro del corte privado")
				return "Error registro corte privado"
		else:
			#try:
			print("turno:",turno)
			if("V" in turno):
				turno="Vespertino"
			else:
				turno="Matutino"
			payload = {
			"turno": turno,
			"boletaje": "0",
			"recuperados": str(int(tipos[5])+int(tipos[8])+int(tipos[1])),
			"sellados": str(tipos[5]),
			"noSellados": str(tipos[8]),
			"incompletos": str(tipos[6]),
			"propina": str(tipos[4]),
			"sinpropina": str(tipos[7]),
			"cortesias": "0",
			"tolerancias": tolerancias,
			"locatarios": str(tipos[1]),
			"caja": str(idCajero),
			"created": fechaHoy+"T"+horaHoy,
			"ingreso": str(importe),
			"detalles": boletaje,
			"encargado": "1",
			"sucursal_id": self.sucursal
			}
			r = requests.post("https://parkingtip.pythonanywhere.com/api/cortes/create/", json=payload)
			#r = requests.post("http://127.0.0.1:8000/api/cortes/create/", json=payload)
			
			#r = requests.get(endpoint)
			print("Result:",r.text,", turno:",turno,"status:",r.status_code)
			print("STATUS_CODE: ",r.status_code,r)
			if r.status_code == 201:
				return 1
			else:
				return 0
			
		#except:
			print("Error de registro del corte publico")
			#return 0
				
	def registroExitoso(self):
		pass
	
	def registroFallido(self):
		return 0
		
	def obtenerIdSucursal():
		return 

hoy=datetime.datetime.today()
ayer=hoy+datetime.timedelta(days=-1)
m=str(ayer).split(" ")
n=m[0].split("-")
fechaayer=n[2]+"/"+n[1]+"/"+n[0]


hoy=datetime.datetime.today()
a=str(hoy).split(" ")
b=a[0].split("-")
fec=b[2]+"/"+b[1]+"/"+b[0]


#horaEnt=time.strftime("%H:%M:%S")
#fec=fec+','+horaEnt+','+str(aux_tarifa)
#fecha1=fec+" 15:00:00"
#fecha2=fec+" 22:00:00"
horaEnt=time.strftime("%H:%M:%S")
infile = open("/home/pi/Documents/eum/app/caseta/archivos_config/fechaDeCorte.txt", 'r')
c=infile.readline()
infile.close()
c=c.split(',')

fecha2=fec+" "+str(horaEnt)
fecha1=c[0]
turno=c[1]
folio=c[2]
print(fecha1,fecha2)
#checale(fecha1,fecha2)
#checale(fecha1,fecha2,str(turno),str(folio))
#checale(fecha1,fecha2,turno)
#imprimirBoletoC2(fe,he,str(costo),str(folio),str(expedidora))
