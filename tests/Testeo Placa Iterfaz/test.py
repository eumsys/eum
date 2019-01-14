# -*- coding: utf-8 -*-
import leerBotones as botones

PATH_IMAGEN_PLACA="/home/pi/Documents/Testeo Placa Iterfaz/placa.png"
PATH_IMAGEN_LOGO="/home/pi/Documents/img/logotipo1.png"

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
	def setupUi(self, Form):
		Form.setObjectName(_fromUtf8("Form"))
		Form.resize(1366, 768)
		Form.setMinimumSize(QtCore.QSize(1366, 768))
		Form.setMaximumSize(QtCore.QSize(1366, 768))
		Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8(PATH_IMAGEN_LOGO)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		Form.setWindowIcon(icon)
		Form.setStyleSheet(_fromUtf8(""))
		self.label_1 = QtGui.QLabel(Form)
		self.label_1.setGeometry(QtCore.QRect(270, 10, 791, 61))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Return To Sender"))
		font.setPointSize(36)
		font.setBold(False)
		font.setWeight(50)
		self.label_1.setFont(font)
		self.label_1.setObjectName(_fromUtf8("label_1"))
		self.label_2 = QtGui.QLabel(Form)
		self.label_2.setGeometry(QtCore.QRect(60, 80, 440, 610))
		self.label_2.setText(_fromUtf8(""))
		self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(PATH_IMAGEN_PLACA)))
		self.label_2.setScaledContents(True)
		self.label_2.setObjectName(_fromUtf8("label_2"))
		self.label = QtGui.QLabel(Form)
		self.label.setGeometry(QtCore.QRect(530, 80, 260, 31))
		font = QtGui.QFont()
		font.setPointSize(20)
		self.label.setFont(font)
		self.label.setObjectName(_fromUtf8("label"))
		self.label_3 = QtGui.QLabel(Form)
		self.label_3.setGeometry(QtCore.QRect(660, 120, 90, 30))
		font = QtGui.QFont()
		font.setPointSize(15)
		self.label_3.setFont(font)
		self.label_3.setObjectName(_fromUtf8("label_3"))
		self.label_4 = QtGui.QLabel(Form)
		self.label_4.setGeometry(QtCore.QRect(660, 150, 90, 30))
		font = QtGui.QFont()
		font.setPointSize(15)
		self.label_4.setFont(font)
		self.label_4.setObjectName(_fromUtf8("label_4"))
		self.label_5 = QtGui.QLabel(Form)
		self.label_5.setGeometry(QtCore.QRect(870, 80, 81, 31))
		font = QtGui.QFont()
		font.setPointSize(20)
		self.label_5.setFont(font)
		self.label_5.setObjectName(_fromUtf8("label_5"))
		self.label_6 = QtGui.QLabel(Form)
		self.label_6.setGeometry(QtCore.QRect(530, 200, 280, 31))
		font = QtGui.QFont()
		font.setPointSize(20)
		self.label_6.setFont(font)
		self.label_6.setObjectName(_fromUtf8("label_6"))
		self.label_7 = QtGui.QLabel(Form)
		self.label_7.setGeometry(QtCore.QRect(570, 240, 170, 30))
		font = QtGui.QFont()
		font.setPointSize(15)
		self.label_7.setFont(font)
		self.label_7.setObjectName(_fromUtf8("label_7"))
		self.label_8 = QtGui.QLabel(Form)
		self.label_8.setGeometry(QtCore.QRect(570, 280, 170, 30))
		font = QtGui.QFont()
		font.setPointSize(15)
		self.label_8.setFont(font)
		self.label_8.setObjectName(_fromUtf8("label_8"))
		self.label_9 = QtGui.QLabel(Form)
		self.label_9.setGeometry(QtCore.QRect(570, 320, 170, 30))
		font = QtGui.QFont()
		font.setPointSize(15)
		self.label_9.setFont(font)
		self.label_9.setObjectName(_fromUtf8("label_9"))
		self.label_10 = QtGui.QLabel(Form)
		self.label_10.setGeometry(QtCore.QRect(570, 360, 170, 30))
		font = QtGui.QFont()
		font.setPointSize(15)
		self.label_10.setFont(font)
		self.label_10.setObjectName(_fromUtf8("label_10"))
		self.label_12 = QtGui.QLabel(Form)
		self.label_12.setGeometry(QtCore.QRect(530, 410, 280, 31))
		font = QtGui.QFont()
		font.setPointSize(20)
		self.label_12.setFont(font)
		self.label_12.setObjectName(_fromUtf8("label_12"))
		self.label_13 = QtGui.QLabel(Form)
		self.label_13.setGeometry(QtCore.QRect(530, 460, 170, 30))
		font = QtGui.QFont()
		font.setPointSize(15)
		self.label_13.setFont(font)
		self.label_13.setObjectName(_fromUtf8("label_13"))
		self.label_14 = QtGui.QLabel(Form)
		self.label_14.setGeometry(QtCore.QRect(780, 460, 120, 30))
		font = QtGui.QFont()
		font.setPointSize(15)
		self.label_14.setFont(font)
		self.label_14.setObjectName(_fromUtf8("label_14"))
		self.label_15 = QtGui.QLabel(Form)
		self.label_15.setGeometry(QtCore.QRect(910, 460, 170, 30))
		font = QtGui.QFont()
		font.setPointSize(15)
		self.label_15.setFont(font)
		self.label_15.setObjectName(_fromUtf8("label_15"))
		self.label_16 = QtGui.QLabel(Form)
		self.label_16.setGeometry(QtCore.QRect(680, 460, 90, 30))
		font = QtGui.QFont()
		font.setPointSize(15)
		self.label_16.setFont(font)
		self.label_16.setObjectName(_fromUtf8("label_16"))
		self.label_17 = QtGui.QLabel(Form)
		self.label_17.setGeometry(QtCore.QRect(1100, 460, 170, 30))
		font = QtGui.QFont()
		font.setPointSize(15)
		self.label_17.setFont(font)
		self.label_17.setObjectName(_fromUtf8("label_17"))
		self.pushButton = QtGui.QPushButton(Form)
		self.pushButton.setGeometry(QtCore.QRect(970, 120, 98, 27))
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.pushButton_2 = QtGui.QPushButton(Form)
		self.pushButton_2.setGeometry(QtCore.QRect(970, 150, 98, 27))
		self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
		self.txtFolio = QtGui.QLineEdit(Form)
		self.txtFolio.setEnabled(False)
		self.txtFolio.setGeometry(QtCore.QRect(820, 120, 141, 32))
		self.txtFolio.setObjectName(_fromUtf8("txtFolio"))
		self.txtFolio_2 = QtGui.QLineEdit(Form)
		self.txtFolio_2.setEnabled(False)
		self.txtFolio_2.setGeometry(QtCore.QRect(820, 150, 141, 32))
		self.txtFolio_2.setObjectName(_fromUtf8("txtFolio_2"))
		
		font = QtGui.QFont()
		font.setPointSize(28)
		
		self.txtFolio_3 = QtGui.QLineEdit(Form)
		self.txtFolio_3.setFont(font)
		self.txtFolio_3.setEnabled(False)
		self.txtFolio_3.setGeometry(QtCore.QRect(820, 240, 141, 32))
		self.txtFolio_3.setObjectName(_fromUtf8("txtFolio_3"))
		self.txtFolio_4 = QtGui.QLineEdit(Form)
		self.txtFolio_4.setFont(font)
		self.txtFolio_4.setEnabled(False)
		self.txtFolio_4.setGeometry(QtCore.QRect(820, 280, 141, 32))
		self.txtFolio_4.setObjectName(_fromUtf8("txtFolio_4"))
		self.txtFolio_5 = QtGui.QLineEdit(Form)
		self.txtFolio_5.setFont(font)
		self.txtFolio_5.setEnabled(False)
		self.txtFolio_5.setGeometry(QtCore.QRect(820, 320, 141, 32))
		self.txtFolio_5.setObjectName(_fromUtf8("txtFolio_5"))
		self.txtFolio_6 = QtGui.QLineEdit(Form)
		self.txtFolio_6.setFont(font)
		self.txtFolio_6.setEnabled(False)
		self.txtFolio_6.setGeometry(QtCore.QRect(820, 360, 141, 32))
		self.txtFolio_6.setObjectName(_fromUtf8("txtFolio_6"))
		self.txtFolio_7 = QtGui.QLineEdit(Form)
		self.txtFolio_7.setFont(font)
		self.txtFolio_7.setEnabled(False)
		self.txtFolio_7.setGeometry(QtCore.QRect(550, 500, 70, 32))
		self.txtFolio_7.setObjectName(_fromUtf8("txtFolio_7"))
		self.txtFolio_8 = QtGui.QLineEdit(Form)
		self.txtFolio_8.setFont(font)
		self.txtFolio_8.setEnabled(False)
		self.txtFolio_8.setGeometry(QtCore.QRect(700, 500, 70, 32))
		self.txtFolio_8.setObjectName(_fromUtf8("txtFolio_8"))
		self.txtFolio_9 = QtGui.QLineEdit(Form)
		self.txtFolio_9.setFont(font)
		self.txtFolio_9.setEnabled(False)
		self.txtFolio_9.setGeometry(QtCore.QRect(810, 500, 70, 32))
		self.txtFolio_9.setObjectName(_fromUtf8("txtFolio_9"))
		self.txtFolio_10 = QtGui.QLineEdit(Form)
		self.txtFolio_10.setFont(font)
		self.txtFolio_10.setEnabled(False)
		self.txtFolio_10.setGeometry(QtCore.QRect(960, 500, 70, 32))
		self.txtFolio_10.setObjectName(_fromUtf8("txtFolio_10"))
		self.txtFolio_11 = QtGui.QLineEdit(Form)
		self.txtFolio_11.setFont(font)
		self.txtFolio_11.setEnabled(False)
		self.txtFolio_11.setGeometry(QtCore.QRect(1100, 500, 70, 32))
		self.txtFolio_11.setObjectName(_fromUtf8("txtFolio_11"))
		self.txtFolio_12 = QtGui.QLineEdit(Form)
		self.txtFolio_12.setFont(font)
		self.txtFolio_12.setEnabled(False)
		self.txtFolio_12.setGeometry(QtCore.QRect(1190, 500, 70, 32))
		self.txtFolio_12.setObjectName(_fromUtf8("txtFolio_12"))
		self.pushButton_3 = QtGui.QPushButton(Form)
		self.pushButton_3.setGeometry(QtCore.QRect(1090, 120, 98, 27))
		self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
		self.pushButton_4 = QtGui.QPushButton(Form)
		self.pushButton_4.setGeometry(QtCore.QRect(1090, 150, 98, 27))
		self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
		self.pushButton_5 = QtGui.QPushButton(Form)
		self.pushButton_5.setGeometry(QtCore.QRect(980, 240, 98, 27))
		self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
		self.pushButton_6 = QtGui.QPushButton(Form)
		self.pushButton_6.setGeometry(QtCore.QRect(980, 280, 98, 27))
		self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
		self.pushButton_7 = QtGui.QPushButton(Form)
		self.pushButton_7.setGeometry(QtCore.QRect(980, 320, 98, 27))
		self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
		self.pushButton_8 = QtGui.QPushButton(Form)
		self.pushButton_8.setGeometry(QtCore.QRect(980, 360, 98, 27))
		self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
		self.pushButton_9 = QtGui.QPushButton(Form)
		self.pushButton_9.setGeometry(QtCore.QRect(530, 540, 98, 27))
		self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
		self.pushButton_10 = QtGui.QPushButton(Form)
		self.pushButton_10.setGeometry(QtCore.QRect(670, 540, 98, 27))
		self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
		self.pushButton_11 = QtGui.QPushButton(Form)
		self.pushButton_11.setGeometry(QtCore.QRect(790, 540, 98, 27))
		self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
		self.pushButton_12 = QtGui.QPushButton(Form)
		self.pushButton_12.setGeometry(QtCore.QRect(940, 540, 98, 27))
		self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
		self.pushButton_13 = QtGui.QPushButton(Form)
		self.pushButton_13.setGeometry(QtCore.QRect(1130, 540, 98, 27))
		self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
		self.pushButton_14 = QtGui.QPushButton(Form)
		self.pushButton_14.setGeometry(QtCore.QRect(780, 600, 260, 60))
		self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
		#BOTONES
		self.pushButton.clicked.connect(self.botonLevanta)
		self.pushButton_2.clicked.connect(self.botonBaja)
		self.pushButton_3.clicked.connect(self.botonLeerLevanta)
		self.pushButton_4.clicked.connect(self.botonLeerBaja)
		self.pushButton_5.clicked.connect(self.botonLeerMasa)
		self.pushButton_6.clicked.connect(self.botonLeerTicket)
		self.pushButton_7.clicked.connect(self.botonLeerBobina2)
		self.pushButton_8.clicked.connect(self.botonLeerAyuda)
		# pines de configuracion
		self.pushButton_9.clicked.connect(self.botonLeerAyuda)
		self.pushButton_10.clicked.connect(self.botonLeerBobina2)
		self.pushButton_11.clicked.connect(self.botonLeerTicket)
		self.pushButton_12.clicked.connect(self.botonLeerMasa)
		self.pushButton_13.clicked.connect(self.botonConfiguracion)
		# pines de configuracion fin
		self.pushButton_14.clicked.connect(self.botonTodo)
		#FIN BOTONES
		self.configurar()
		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def configurar(self):
		botones.configurarPinesGPIO()
		botones.configurarPinesGPIOBobina()
		#botones.gpiocleanup()
		print "Termino de configurar pines"

	def botonLevanta(self):
		botones.abrir()
		print " Levanta "

	def botonBaja(self):
		print " Baja"
		botones.cerrar()
	
	def botonLeerLevanta(self):
		botones.leerLevanta()
		print " Leer Levanta"

	def botonLeerBaja(self):
		botones.leerBaja()
		print " Leer baja "

	def botonLeerMasa(self):
		r=botones.leerMasa()
		self.txtFolio_3.setText(str(r))
		self.txtFolio_10.setText(str(r))
		print " leer masa "

	def botonLeerTicket(self):
		r=botones.leerTicket()
		self.txtFolio_4.setText(str(r))
		self.txtFolio_9.setText(str(r))
		print " leer ticket"

	def botonLeerBobina2(self):
		r=botones.leer2bobina()
		self.txtFolio_5.setText(str(r))
		self.txtFolio_8.setText(str(r))
		print " Leer bobina 2 "

	def botonLeerAyuda(self):
		print " LeerAyuda no implementado"
		self.txtFolio_6.setText("x")
		self.txtFolio_7.setText("x")
	
	def botonConfiguracion(self):
		print " Leer Configuracion"
		r1,r2=botones.leerConfiguracion()
		self.txtFolio_11.setText(str(r1))
		self.txtFolio_12.setText(str(r2))
	
	def botonTodo(self):
		self.botonConfiguracion()
		self.botonLeerBobina2()
		self.botonLeerTicket()
		self.botonLeerMasa()
		print " Leer Todo"
		QtCore.QTimer.singleShot(200, self.botonTodo)



	def retranslateUi(self, Form):
		Form.setWindowTitle(_translate("Form", "Estacionamientos Unicos de Mexico - TEST PLACA DE INTERFAZ", None))
		self.label_1.setText(_translate("Form", "TEST DE PLACA DE INTERFAZ", None))
		self.label.setText(_translate("Form", "Terminales de Salida", None))
		self.label_3.setText(_translate("Form", "Levanta", None))
		self.label_4.setText(_translate("Form", "Baja", None))
		self.label_5.setText(_translate("Form", "Valor", None))
		self.label_6.setText(_translate("Form", "Terminales de Entrada", None))
		self.label_7.setText(_translate("Form", "Detector de Masa", None))
		self.label_8.setText(_translate("Form", "Botón ticket", None))
		self.label_9.setText(_translate("Form", "Bobina 2", None))
		self.label_10.setText(_translate("Form", "Botón Ayuda", None))
		self.label_12.setText(_translate("Form", "Conexion Raspberry", None))
		self.label_13.setText(_translate("Form", "Botón Ayuda", None))
		self.label_14.setText(_translate("Form", "Botón ticket", None))
		self.label_15.setText(_translate("Form", "Detector de Masa", None))
		self.label_16.setText(_translate("Form", "Bobina 2", None))
		self.label_17.setText(_translate("Form", "CONFIGURACION", None))
		self.pushButton.setText(_translate("Form", "Levantar", None))
		self.pushButton_2.setText(_translate("Form", "Bajar", None))
		self.pushButton_3.setText(_translate("Form", "Leer", None))
		self.pushButton_4.setText(_translate("Form", "Leer", None))
		self.pushButton_5.setText(_translate("Form", "Leer", None))
		self.pushButton_6.setText(_translate("Form", "Leer", None))
		self.pushButton_7.setText(_translate("Form", "Leer", None))
		self.pushButton_8.setText(_translate("Form", "Leer", None))
		self.pushButton_9.setText(_translate("Form", "Leer", None))
		self.pushButton_10.setText(_translate("Form", "Leer", None))
		self.pushButton_11.setText(_translate("Form", "Leer", None))
		self.pushButton_12.setText(_translate("Form", "Leer", None))
		self.pushButton_13.setText(_translate("Form", "Leer", None))
		self.pushButton_14.setText(_translate("Form", "Leer Todo", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

