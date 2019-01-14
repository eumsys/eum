import sys
import os
import time
import sched
import psycopg2

bd = "dbeum_manual"
usr = "postgres"
pswd = "Postgres3UMd6"

def consultaPlazaLocalidad():
	try:
		plaza = ""
		localida = ""
		connection = psycopg2.connect(user = usr, password = pswd, database = bd, host = 'localhost')
		with connection.cursor() as cursor:
			cursor.execute('SELECT nombre_plaza, estado FROM plaza WHERE idplaza = 1')
			row = cursor.fetchone()
			if row is not None:
				plaza = str(row[0])
				localidad = str(row[1])
				connection.commit()
				connection.close()
		return plaza,localidad
	except (Exception, psycopg2.DatabaseError) as error:
		return "error"

def iniciarSesion(self,usuario,contrasenia):
			try:
				connection = psycopg2.connect(user = usr, password = pswd, database = bd, host = 'localhost')
				with connection.cursor() as cursor:
					cursor.execute("SELECT idusuario FROM usuario WHERE nomusuario = '{}' and passwd = '{}'".format(str(usuario),str(contrasenia)))
					row = cursor.fetchone()
					if row is not None:
						connection.commit()
						connection.close()
						return "encontrado"
					else:
						return "no encontrado"
			except (Exception, psycopg2.DatabaseError) as error:
				return "error"
