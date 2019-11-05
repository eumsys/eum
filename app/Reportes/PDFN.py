import time
import threading
import psycopg2, psycopg2.extras
import time
import fpdf 
from fpdf import FPDF
import os,sys,getopt


connection = psycopg2.connect(user='eumdb', password='Ingenieria3UMd6', database='dbeum_tecamac', host='localhost')
cursor = connection.cursor()


from datetime import datetime, date, timedelta
import time


fecha_hoy = '2017-11-26'
#fecha_hoy = str(date.today())

#fechaQuery1="2017-11-26 07:00:00"
#fechaQuery2="2017-11-26 22:00:00"

class PDF():
    def __init__(self, nombre, fecha1, fecha2,descripcion = "" ):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha1 = fecha1
        self.fecha2 = fecha2

        self.pdf=FPDF()
        self.pdf.add_page()
        #self.pdf=FPDF()
        #self.pdf.add_page()
        self.pdf.set_font('Arial','',32)
        self.pdf.cell(30,10,self.nombre)
        self.pdf.ln()
        self.pdf.ln()
        self.pdf.set_font('Arial','',18)
        #self.pdf.cell(30,10,self.fecha1.rstrip(' 00:00:00')+' - '+self.fecha2.rstrip(' 23:59:59'))
        self.pdf.cell(30,10,self.fecha1+' - '+self.fecha2)
        #fechaA=str(fecha1.rstrip(' 00:00:00')).replace("/","-")
        #fechaB=str(fecha2.rstrip(' 23:59:59')).replace("/","-")
        #self.pdf.ln()
        #self.pdf.cell(30,10,"Cajero: "+str(idCajero))
        self.agregarSubtitulo('Generado: '+str(time.strftime("%Y/%m/%d  %H:%M:%S")))
        self.agregarSubtitulo('Tipo: General')

        #self.pdf.ln()
        
        '''self.pdf.cell(45,10,'Fecha',1)
        self.pdf.cell(45,10,'Usuario',1)
        self.pdf.cell(45,10,'Evento',1)
        self.pdf.cell(55,10,'Detalle',1)
        self.pdf.set_font('Arial','',12)
        self.pdf.ln()'''
    def agregarSubtitulo(self,nombre):
        self.pdf.ln()
        #self.pdf.ln()
        self.pdf.set_font('Arial','',18)
        self.pdf.cell(30,10,nombre)
        self.pdf.ln()

    def generarPdf(self):
        self.pdf.output('reportes/'+self.nombre+'_'+self.fecha2[:10]+'.pdf','F')
        #self.pdf.output('reportes/'+self.nombre+''+self.fecha1+'_'+self.fecha2[:10]+'.pdf','F')

    def establecerRangoFechas(self,fecha1,fecha2):
        self.fecha1 = fecha1
        self.fecha2 = fecha2
    def obtenerRangoFechas(self,fecha1,fecha2):
        return self.fecha1,self.fecha2
    def establecerFuente(self,fuente,tipo,tamano):
        self.pdf.set_font(fuente,tipo,tamano)
    def dibujarCelda(self,ancho,alto,nombre,dato):
        self.pdf.cell(ancho,alto,nombre,dato)
    def dibujarSalto(self):
        self.pdf.ln()


class Tabla():

    def __init__(self, pdf,nombre, descripcion = ""):


            self.pdf=pdf
            #self.agregarPagina()
            #self.pdf.set_font('Arial','B',48)
            #pdf.cell(30,10,'Reporte de Eventos\n')
            #self.pdf.cell(30,10,nombre+'\n')
            self.query = ''

            self.nombre = nombre
            self.descripcion = descripcion

            self.fecha1 = ''
            self.fecha2 = ''

            self.encabezados = []
            self.celdas = []


    def agregarPagina (self):
        self.pdf.add_page()


    def establecerFuente(self,fuente,tipo,tamano):
        self.pdf.set_font(fuente,tipo,tamano)

    def agregarCeldas(self,nombre,dato):
        celda = [nombre,dato]
        self.celdas.append(celda)

        #self.pdf.cell(ancho,alto,nombre,dato)


    def agregarEncabezado(self,ancho,alto,nombre,dato):
        encabezado = [ancho,alto,nombre,dato]
        self.encabezados.append(encabezado)
        #self.pdf.cell(ancho,alto,nombre,dato)

    def agregarSubtitulo(self,nombre):
        self.pdf.ln()
        #self.pdf.ln()
        self.pdf.set_font('Arial','',18)
        self.pdf.cell(30,10,nombre)
        self.pdf.ln()


    def dibujarTabla(self):
        distribucion = len(self.celdas)/len(self.encabezados)
        i=0
        #self.pdf.cell(45,10,'Fecha',1)
        
        if distribucion:
            self.pdf.establecerFuente('Arial','B',8)
            for encabezado in self.encabezados:
                print(encabezado)
                self.pdf.dibujarCelda(encabezado[0],encabezado[1],encabezado[2],encabezado[3])

            self.pdf.dibujarSalto()
            self.pdf.establecerFuente('Arial','',8)
            for celda in self.celdas:
                if i >= len(self.encabezados) :
                    i = 0
                    self.pdf.dibujarSalto()

                ancho = self.encabezados[i][0]
                alto = self.encabezados[i][1]
                self.pdf.dibujarCelda(ancho,alto,celda[0],celda[1])
                i=i+1
        else:
            print('tabla malformada')

    def establecerQuery(self,query):
        self.query = query

    def establecerRangoFechas(self):
        fechas = self.pdf.obtenerRangoFechas()
        fechas.split(',')
        self.fecha1 = fechas[0]
        self.fecha2 = fechas[1]

    def establecerRangoFechas(self,fecha1,fecha2):
        self.fecha1 = fecha1
        self.fecha2 = fecha2

    
        

    def cabecera(self):
        #self.pdf=FPDF()
        #self.pdf.add_page()
        self.pdf.set_font('Arial','',32)
        self.pdf.cell(30,10,self.nombre)
        self.pdf.ln()
        self.pdf.ln()
        self.pdf.set_font('Arial','',18)
        #self.pdf.cell(30,10,self.fecha1.rstrip(' 00:00:00')+' - '+self.fecha2.rstrip(' 23:59:59'))
        self.pdf.cell(30,10,self.fecha1+' - '+self.fecha2)
        #fechaA=str(fecha1.rstrip(' 00:00:00')).replace("/","-")
        #fechaB=str(fecha2.rstrip(' 23:59:59')).replace("/","-")
        #self.pdf.ln()
        #self.pdf.cell(30,10,"Cajero: "+str(idCajero))
        self.agregarSubtitulo('Generado: '+str(time.strftime("%Y/%m/%d  %H:%M:%S")))
        self.agregarSubtitulo('Tipo: General')

        #self.pdf.ln()
        
        '''self.pdf.cell(45,10,'Fecha',1)
        self.pdf.cell(45,10,'Usuario',1)
        self.pdf.cell(45,10,'Evento',1)
        self.pdf.cell(55,10,'Detalle',1)
        self.pdf.set_font('Arial','',12)
        self.pdf.ln()'''




def aclaraciones(pdf):
    """pdf1=FPDF()
    pdf1.add_page()
    tablaAclaraciones = Tabla(pdf1,'Aclaraciones\n','')
    tablaAclaraciones.establecerRangoFechas(fechaQuery1,fechaQuery2)
    tablaAclaraciones.cabecera()
    """
    fechaQuery1 = pdf.fecha1
    fechaQuery2 = pdf.fecha2

    tablaAclaraciones = Tabla(pdf,'Aclaraciones\n','')

    tablaAclaraciones.agregarEncabezado(25,5,'Folio',1)
    tablaAclaraciones.agregarEncabezado(25,5,'Entrada',1)
    tablaAclaraciones.agregarEncabezado(45,5,'Fecha expedicion',1)
    tablaAclaraciones.agregarEncabezado(25,5,'Estado',1)
    tablaAclaraciones.agregarEncabezado(25,5,'Tipo descuento',1)
    tablaAclaraciones.agregarEncabezado(25,5,'Validado',1)
    '''
    tablaAclaraciones.agregarCeldas('Validado0',1)
    tablaAclaraciones.agregarCeldas('Validado1',1)
    tablaAclaraciones.agregarCeldas('Validado2',1)
    tablaAclaraciones.agregarCeldas('Validado3',1)
    tablaAclaraciones.agregarCeldas('Validado4',1)
    tablaAclaraciones.agregarCeldas('Validado5',1)
    tablaAclaraciones.agregarCeldas('Validado6',1)
    tablaAclaraciones.agregarCeldas('Validado7',1)
    tablaAclaraciones.agregarCeldas('Validado8',1)
    tablaAclaraciones.agregarCeldas('Validado9',1)
    '''
    queryAclaraciones = "select boleto.* from boleto left JOIN pagos on boleto.idboleto = pagos.idboleto and boleto.idexpedidora = pagos.idexpedidora and boleto.fechaexpedicion=pagos.fechaexpedicion where boleto.fechaexpedicion between '{0}' and '{1}' and pagos.idboleto ISNULL".format(fechaQuery1,fechaQuery2)
    
    aclaraciones = consultaBD(2,queryAclaraciones)
    for regs in aclaraciones:
        for aclaracion in regs:
            tablaAclaraciones.agregarCeldas(str(aclaracion),1)
    #tablaAclaraciones.agregarPagina()
    
    tablaAclaraciones.dibujarTabla()






    pdf.generarPdf()


def consultaBD(tipoQuery,query):
    if tipoQuery == 1:
        cursor.execute(query)
        result = cursor.fetchone()[0]
        return result
    elif tipoQuery == 2:
        cursor.execute(query)

        return cursor
    elif tipoQuery == 3:
        cursor.execute(query)
        detallesCorte = ""
        for reg in cursor:
            detallesCorte += str(reg[1])+"x"+str(reg[0])+" "
        return detallesCorte

def resumenBoletaje(pdf):
    """pdf1=FPDF()
    pdf1.add_page()
    tablaBoletaje = Tabla(pdf1,'CC\n','')
    tablaBoletaje.establecerRangoFechas('2019-09-01 07:00:00','2019-09-10 22:00:00')
    tablaBoletaje.cabecera()
    """

    fechaQuery1 = pdf.fecha1
    fechaQuery2 = pdf.fecha2
    tablaBoletaje = Tabla(pdf,'CC\n','')
    
    tablaBoletaje.agregarEncabezado(17,5,'Expedidos',1)
    tablaBoletaje.agregarEncabezado(17,5,'Cobrados',1)
    tablaBoletaje.agregarEncabezado(17,5,'Por aclarar',1)
    tablaBoletaje.agregarEncabezado(17,5,'Validados',1)
    tablaBoletaje.agregarEncabezado(17,5,'Locatarios',1)
    #tablaBoletaje.agregarEncabezado(25,5,'Tolerancias',1)
    tablaBoletaje.agregarEncabezado(25,5,'Importe',1)


    tablaBoletaje.agregarEncabezado(5,5,'$1',1)
    tablaBoletaje.agregarEncabezado(5,5,'$2',1)
    tablaBoletaje.agregarEncabezado(5,5,'$5',1)
    tablaBoletaje.agregarEncabezado(7,5,'$10',1)
    tablaBoletaje.agregarEncabezado(7,5,'$20',1)
    tablaBoletaje.agregarEncabezado(7,5,'$50',1)
    tablaBoletaje.agregarEncabezado(8,5,'$100',1)

    '''
    tablaBoletaje.agregarCeldas('Validado0',1)
    tablaBoletaje.agregarCeldas('Validado1',1)
    tablaBoletaje.agregarCeldas('Validado2',1)
    tablaBoletaje.agregarCeldas('Validado3',1)
    tablaBoletaje.agregarCeldas('Validado4',1)
    tablaBoletaje.agregarCeldas('d1',1)
    tablaBoletaje.agregarCeldas('d',1)
    tablaBoletaje.agregarCeldas('d',1)
    tablaBoletaje.agregarCeldas('d',1)
    tablaBoletaje.agregarCeldas('d',1)
    tablaBoletaje.agregarCeldas('d',1)
    tablaBoletaje.agregarCeldas('d',1)
    tablaBoletaje.agregarCeldas('d',1)
    #tablaBoletaje.agregarPagina()
    #tablaBoletaje.cabecera()
    '''


    fechaHoy=time.strftime("%Y-%m-%d")
    horaHoy=time.strftime("%H:%M:%S")
    #fechaQuery='2019-01-09'



    queryExpedidos = "select count(idboleto) from boleto where fechaexpedicion between '{0}' and '{1}'".format(fechaQuery1,fechaQuery2)
    queryCobrados = "select count(idboleto) from pagos where fechaexpedicion between '{0}' and '{1}'".format(fechaQuery1,fechaQuery2)
    queryRecuperados = "select count(idboleto) from boleto where fechaexpedicion between '{0}' and '{1}' and idestado=4".format(fechaQuery1,fechaQuery2)
    queryLocatarios = "select count(idboleto) from boleto where fechaexpedicion between '{0}' and '{1}' and idestado=6".format(fechaQuery1,fechaQuery2)
    #queryTolerancias = "select count(idboleto) from boleto where fechaexpedicion between '{0}' and '{1}' and idestado=6".format(fechaQuery1,fechaQuery2)
    queryCorteCaja = "select sum(monto) from pagos where fechaexpedicion between '{0}' and '{1}'".format(fechaQuery1,fechaQuery2)
    queryDetallesCorte = "select monto,count(monto) from pagos where fechaexpedicion between '{0}' and '{1}' group by monto".format(fechaQuery1,fechaQuery2)
    queryAclaraciones = "select count(boleto.idboleto) from boleto left JOIN pagos on boleto.idboleto = pagos.idboleto and boleto.idexpedidora = pagos.idexpedidora and boleto.fechaexpedicion=pagos.fechaexpedicion where boleto.fechaexpedicion between '{0}' and '{1}' and pagos.idboleto ISNULL".format(fechaQuery1,fechaQuery2)
    queryAclaraciones2 = "select count(boleto.idboleto) from boleto left JOIN pagos on boleto.idboleto = pagos.idboleto and boleto.idexpedidora = pagos.idexpedidora and boleto.fechaexpedicion=pagos.fechaexpedicion where boleto.fechaexpedicion between '{0}' and '{1}' ".format(fechaQuery1,fechaQuery2)
    
    expedidos = consultaBD(1,queryExpedidos)
    cobrados = consultaBD(1,queryCobrados)
    recuperados = consultaBD(1,queryRecuperados)
    locatarios = consultaBD(1,queryLocatarios)
    corteCaja = consultaBD(1,queryCorteCaja)
    detallesCorte = consultaBD(3,queryDetallesCorte)
    aclaraciones = consultaBD(1,queryAclaraciones)
    aclaraciones2 = consultaBD(1,queryAclaraciones2)
    '''cursor = connection.cursor()
    cursor.execute(queryExpedidos)
    expedidos = cursor.fetchone()[0]
    cursor.execute(queryRecuperados)
    recuperados = cursor.fetchone()[0]
    cursor.execute(queryCobrados)
    cobrados = cursor.fetchone()[0]
    cursor.execute(queryLocatarios)
    locatarios = cursor.fetchone()[0]
    cursor.execute(queryCorteCaja)
    corteCaja = cursor.fetchone()[0]
    cursor.execute(queryDetallesCorte)
    detallesCorte=""
    for reg in cursor:
        detallesCorte += str(reg[1])+"x"+str(reg[0])+" "
    '''
    if(not expedidos):
        expedidos=0
    if(not recuperados):
        recuperados=0
    #if(not tolerancias):
    #    tolerancias=0
    if(not locatarios):
        locatarios=0
    if(not corteCaja):
        corteCaja=0
    if(not detallesCorte):
        detallesCorte=0
    print(fechaQuery1,fechaQuery2)
    print(expedidos)
    print(recuperados)
    #print(tolerancias)
    print(locatarios)
    print(corteCaja)
    print(detallesCorte)
    print(aclaraciones)
    print(aclaraciones2)
    
    tablaBoletaje.agregarCeldas(str(expedidos),1)
    tablaBoletaje.agregarCeldas(str(cobrados),1)
    tablaBoletaje.agregarCeldas(str(aclaraciones),1)
    
    tablaBoletaje.agregarCeldas(str(recuperados),1)
    tablaBoletaje.agregarCeldas(str(locatarios),1)
    tablaBoletaje.agregarCeldas(str(corteCaja),1)
    


    tablaBoletaje.dibujarTabla()


    tablaCorteCajero = Tabla(pdf,'CC\n','')
    pdf.agregarSubtitulo("Resumen Cajeros")
    tablaCorteCajero.agregarEncabezado(10,15,'Cajero',1)
    tablaCorteCajero.agregarEncabezado(15,15,'Boletos',1)
    tablaCorteCajero.agregarEncabezado(20,15,'Ingreso',1)
    tablaCorteCajero.agregarEncabezado(5,15,'$1',1)
    tablaCorteCajero.agregarEncabezado(5,15,'$2',1)
    tablaCorteCajero.agregarEncabezado(5,15,'$5',1)
    tablaCorteCajero.agregarEncabezado(7,15,'$10',1)
    tablaCorteCajero.agregarEncabezado(7,15,'$20',1)
    tablaCorteCajero.agregarEncabezado(7,15,'$50',1)
    tablaCorteCajero.agregarEncabezado(8,15,'$100',1)
    tablaCorteCajero.agregarEncabezado(100,15,'Desglose',1)
    cortePorCajero(pdf,tablaCorteCajero,1)
    cortePorCajero(pdf,tablaCorteCajero,2)
    cortePorCajero(pdf,tablaCorteCajero,3)
    cortePorCajero(pdf,tablaCorteCajero,4)
    cortePorCajero(pdf,tablaCorteCajero,5)
    cortePorCajero(pdf,tablaCorteCajero,6)
    cortePorCajero(pdf,tablaCorteCajero,7)
    cortePorCajero(pdf,tablaCorteCajero,8)
    cortePorCajero(pdf,tablaCorteCajero,9)
    '''cortePorCajero(pdf1,2)
    cortePorCajero(pdf1,3)
    cortePorCajero(pdf1,5)
    cortePorCajero(pdf1,6)
    cortePorCajero(pdf1,7)
    cortePorCajero(pdf1,8)
    cortePorCajero(pdf1,9)'''


    tablaCorteCajero.dibujarTabla()
    pdf.generarPdf()


def cortePorCajero(pdf,tablaCorteCajero,numero):
    

    fechaQuery1 = pdf.fecha1
    fechaQuery2 = pdf.fecha2
    #queryExpedidos = "select count(idboleto) from boleto where fechaexpedicion between '{0}' and '{1}'".format(fechaQuery1,fechaQuery2)
    queryCobrados = "select count(idpago) from pagos where fechaexpedicion between '{0}' and '{1}' and idcaj={2}".format(fechaQuery1,fechaQuery2,numero)
    queryCorteCaja = "select sum(monto) from pagos where fechaexpedicion between '{0}' and '{1}' and idcaj={2}".format(fechaQuery1,fechaQuery2,numero)

    queryDetallesCorte = "select monto,count(monto) from pagos where fechaexpedicion between '{0}' and '{1}' and idcaj={2} group by monto".format(fechaQuery1,fechaQuery2,numero)

    cobrados = consultaBD(1,queryCobrados)
    corteCaja = consultaBD(1,queryCorteCaja)
    detallesCorte = consultaBD(3,queryDetallesCorte)

    tablaCorteCajero.agregarCeldas(str(numero),1)
    tablaCorteCajero.agregarCeldas(str(cobrados),1)
    tablaCorteCajero.agregarCeldas(str(corteCaja),1)
    tablaCorteCajero.agregarCeldas(str('-'),1)
    tablaCorteCajero.agregarCeldas(str('-'),1)
    tablaCorteCajero.agregarCeldas(str('-'),1)
    tablaCorteCajero.agregarCeldas(str('-'),1)
    tablaCorteCajero.agregarCeldas(str('-'),1)
    tablaCorteCajero.agregarCeldas(str('-'),1)
    tablaCorteCajero.agregarCeldas(str('-'),1)
    tablaCorteCajero.agregarCeldas(str(detallesCorte),1)

    

    

    
def main (argv):
    f_inicio = ''
    f_fin = ''
    tipo = ''

    horario_inicio = ""
    horario_fin = ""

    horario_matutino = "07:00:00"
    horario_vespertino = "15:00:00"
    horario_nocturno = "23:00:00"

    #fecha_hoy = str(date.today())
    fecha_ayer = str(datetime.strptime(fecha_hoy,"%Y-%m-%d").date() - timedelta(days=1))


    ###### CORTE MATUTINO #######
    datetime_matutino_hoy_inicio = fecha_hoy+' '+horario_matutino
    datetime_matutino_hoy_fin = fecha_hoy+' '+horario_vespertino

    datetime_matutino_ayer_inicio = fecha_ayer+' '+horario_matutino
    datetime_matutino_ayer_fin = fecha_ayer+' '+horario_vespertino

    ###### CORTE VESPERTINO #######
    datetime_vespertino_hoy_inicio = fecha_hoy+' '+horario_vespertino
    datetime_vespertino_hoy_fin = fecha_hoy+' '+horario_nocturno

    datetime_vespertino_ayer_inicio = fecha_ayer+' '+horario_vespertino
    datetime_vespertino_ayer_fin = fecha_ayer+' '+horario_nocturno

    ###### CORTE NOCTURNO #######
    datetime_nocturno_hoy_inicio = fecha_hoy+' '+horario_nocturno
    datetime_nocturno_hoy_fin = fecha_hoy+' '+horario_matutino

    datetime_nocturno_ayer_inicio = fecha_ayer+' '+horario_nocturno
    datetime_nocturno_ayer_fin = fecha_ayer+' '+horario_matutino

    """
    #datetime_matutino_ayer = 
    print(datetime_matutino_hoy_inicio,datetime_matutino_hoy_fin,datetime_matutino_ayer_inicio,datetime_matutino_ayer_fin)
    exit(0)
    hora_actual = time.strftime("%H:%M:%S")
    hoy = date.today()
    ayer = hoy - timedelta(days=1)
    print(hoy,ayer)
    """



    try:
        opts, args = getopt.getopt(argv,"hi:f:t",["fechaInicio=","fechaFin=","tipo="])
    except getopt.GetoptError:
        print ('test.py -i <fechaInicio> -f <fechaFin> -t <tipo>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -i <fechaInicio> -f <fechaFin>')
            sys.exit()
        elif opt in ("-i", "--fechaInicio"):
            f_inicio = arg
        elif opt in ("-f", "--fechaFin"):
            f_fin = arg
        elif opt in ("-t", "--tipo"):
            tipo = arg
    print ('fechaInicio: "', datetime_matutino_hoy_fin , type(datetime_matutino_hoy_fin))
    print ('fechaFin "', f_fin)
    print ('tipo "', tipo)
    


    #if(tipo == 'm'):
        #pdfAclaracionesM = PDF('Aclaraciones Matutinon\n',"2017-11-26 07:00:00","2017-11-26 07:01:00",'')
    pdfResumenBoletaje = PDF('Resumen Boletaje Matutino',datetime_matutino_hoy_inicio,datetime_matutino_hoy_fin,'')
    pdfAclaraciones = PDF('Aclaraciones',datetime_matutino_ayer_inicio,datetime_matutino_ayer_fin,'')
    aclaraciones(pdfAclaraciones)
    resumenBoletaje(pdfResumenBoletaje)
    '''    
    elif(tipo == 'v'):
        pdfResumenBoletaje = PDF('Resumen Boletaje Vespertino\n',datetime_vespertino_hoy_inicio,datetime_vespertino_hoy_fin,'')
        pdfAclaraciones = PDF('Aclaraciones\n',datetime_vespertino_ayer_inicio,datetime_vespertino_ayer_fin,'')
    elif(tipo == 'n'):
        pdfResumenBoletaje = PDF('Resumen Boletaje Nocturno\n',datetime_nocturno_hoy_inicio,datetime_nocturno_hoy_fin,'')
        pdfAclaraciones = PDF('Aclaraciones\n',datetime_nocturno_ayer_inicio,datetime_nocturno_ayer_fin,'')

    aclaraciones(pdfAclaraciones)
    resumenBoletaje(pdfResumenBoletaje)
    '''
    exit(0)
    #pdfAclaracionesM = PDF('Aclaraciones Matutino\n',"2017-11-26 07:00:00","2017-11-26 07:01:00",'')
    #pdfAclaracionesV = PDF('Aclaraciones Vespertino\n',"2017-11-26 15:00:00","2017-11-26 23:00:00",'')
    #pdfAclaracionesN = PDF('Aclaraciones\n',"2017-11-26 23:00:00","2017-11-26 07:00:00",'')
    #pdfResumenBoletajeM = PDF('Resumen Boletaje Matutino\n',"2017-11-26 07:00:00","2017-11-26 22:00:00",'')
    #pdfResumenBoletajeV = PDF('Resumen Boletaje Vespertino\n',"2017-11-26 07:00:00","2017-11-26 22:00:00",'')
    #pdfResumenBoletajeN = PDF('Resumen Boletaje\n',"2017-11-26 07:00:00","2017-11-26 22:00:00",'')
    
    #pdfAclaraciones.establecerRangoFechas("2017-11-26 07:00:00","2017-11-26 22:00:00")
    #pdfResumenBoletaje.establecerRangoFechas("2017-11-26 07:00:00","2017-11-26 22:00:00")
    #aclaraciones(pdfAclaracionesM)
    #aclaraciones(pdfAclaracionesV)
    #resumenBoletaje(pdfResumenBoletajeM)
    #resumenBoletaje(pdfResumenBoletajeV)
    
    
if __name__ == "__main__":
    main (sys.argv[1:])
    
