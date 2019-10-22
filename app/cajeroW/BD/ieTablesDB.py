#!/usr/bin/python
import os
from time import sleep


ruta =  os.path.join(os.path.dirname(os.path.abspath(__file__)))
ruta = ruta + "/"
def obtenerUsuario(ruta):
	lista = ruta.split("/")
	return "/"+lista[1]+"/"+lista[2]+"/"	
rutaUsuario = obtenerUsuario(ruta)
print(rutaUsuario)



def pedirNumeroEntero(label):
 
	correcto=False
	num=0
	while(not correcto):
		try:
			num = int(input(label))
			correcto=True
		except ValueError:
			print('Opcion invalida')
	 
	return num
 
salir = False
opcion = 0
 
def menu():

	os.system('clear') # NOTA para windows tienes que cambiar clear por cls

	print ("\t\t----- Menu de configuracion Sistemas EUM------\n")

	print ("\t1 - exportar tabla")

	print ("\t2 - importar tabla")

	print ("\t3 - importar logs")
	
	print ("\t4 - importar descuentos")

	print ("\t5 - Salir")
	
def tecla():	
	input("Enter para continuar...")
 
while not salir:

	menu()
	opcion = pedirNumeroEntero("\nIngresa una opcion: ")
 
	if opcion == 1:
		db = input("Ingresa el la base de datos origen:")
		print ("base de datos: ",db)
		tabla = input("Ingresa la tabla a exportar:")
		print ("tabla: ",tabla)
		file = input("nombre archivo destino: ")
		print ("resultado: ",file)
		os.system("pg_dump --table {0} -FC {1} > {2}".format(tabla, db, file+".sql"))
		tecla()
	elif opcion == 2:
		db = input("Ingresa el la base de datos destino:")
		print ("base de datos: ",db)
		tabla = input("Ingresa la tabla a importar:")
		print ("tabla: ",tabla)
		file = input("nombre archivo origen: ")
		print ("resultado: ",file)
		os.system("pg_restore --dbname {0} --table={1} {2} ".format(db, tabla, file+".sql"))
		tecla()
	elif opcion == 3:
		db = "dbtest"
		print ("base de datos: ",db)
		tabla = "logs"
		print ("tabla: ",tabla)
		file = "logs"
		print ("resultado: ",file)
		os.system("pg_restore --dbname {0} --table={1} {2} ".format(db, tabla, file+".sql"))
		os.system("cat addPk.txt | psql dbtest")
		tecla()
	elif opcion == 4:
		db = "CajerOk"
		print ("base de datos: ",db)
		tabla = "logs"
		print ("tabla: ",tabla)
		file = ruta+"CajerOk_30Jul"
		print ("resultado: ",file)

		#pg_restore -h localhost -p 5432 -U postgres -d CajerOk -v Documents/eum/app/cajeroW/BD/CajerOk_30Jul.backup 
		print ("\nPostgres3UMd6")
		print ("reiniciando servicio postrgesql...")
		os.system("sudo service postgresql restart")
		os.system("echo zxcdsf")

		print ("borrando bd...")
		os.system("dropdb -h localhost -p 5432 -U postgres -W {0}".format(db))
		os.system("echo zxcdsf")
		print ("creando bd...")
		os.system("createdb -h localhost -p 5432 -U postgres -W {0}".format(db))
		print ("restaurando bd...")
		os.system("pg_restore -h localhost -p 5432 -U postgres -d {0} -v {1} ".format(db, file+".backup"))
		#os.system("cat addPk.txt | psql dbtest")
		tecla()

	elif opcion == 5:
		salir = True
	else:
		print ("Introduce un numero entre 1 y 3")
 
print ("Fin")
