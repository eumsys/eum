# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dGestionUsuario.ui'
#
# Created: Sat Dec 31 01:47:54 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

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

class dGestionUsuario(object):
    def __init__(self, dGestionUsuario):
        dGestionUsuario.setObjectName(_fromUtf8("dGestionUsuario"))
        dGestionUsuario.resize(1366, 768)
        dGestionUsuario.setMinimumSize(QtCore.QSize(1366, 768))
        dGestionUsuario.setMaximumSize(QtCore.QSize(1366, 768))
        self.pushButton = QtGui.QPushButton(dGestionUsuario)
        self.pushButton.setGeometry(QtCore.QRect(1039, 642, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton{\n"
"    border:1px solid #5b8a3c;\n"
"   border-top: 1px solid #5b8a3c;\n"
"   background: #5b8a3c;\n"
"   padding: 9px 18px;\n"
"   border-radius: 9px;\n"
"   color: white;\n"
"    font: 75 16pt \"Roboto Condensed\";\n"
"   /*text-decoration: none;*/\n"
"   vertical-align: middle;\n"
"\n"
"}\n"
"  \n"
"QPushButton:hover {\n"
"   border-top-color:rgb(77, 207, 57);\n"
"    background: rgb(77, 207, 57);\n"
"   }"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../Documents/Ticket/Ticket/vista/img/logotipo1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dGestionUsuario.setWindowIcon(icon)
        self.tabWidget = QtGui.QTabWidget(dGestionUsuario)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(190, 110, 961, 491))
        self.tabWidget.setStyleSheet(_fromUtf8(""))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabRegistrar = QtGui.QWidget()
        self.tabRegistrar.setStyleSheet(_fromUtf8(""))
        self.tabRegistrar.setObjectName(_fromUtf8("tabRegistrar"))
        self.txtNombre = QtGui.QLineEdit(self.tabRegistrar)
        self.txtNombre.setGeometry(QtCore.QRect(470, 54, 300, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtNombre.setFont(font)
        self.txtNombre.setObjectName(_fromUtf8("txtNombre"))
        self.txtApp = QtGui.QLineEdit(self.tabRegistrar)
        self.txtApp.setGeometry(QtCore.QRect(470, 98, 300, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtApp.setFont(font)
        self.txtApp.setText(_fromUtf8(""))
        self.txtApp.setObjectName(_fromUtf8("txtApp"))
        self.txtApm = QtGui.QLineEdit(self.tabRegistrar)
        self.txtApm.setGeometry(QtCore.QRect(470, 143, 300, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtApm.setFont(font)
        self.txtApm.setObjectName(_fromUtf8("txtApm"))
        self.txtUsuario = QtGui.QLineEdit(self.tabRegistrar)
        self.txtUsuario.setGeometry(QtCore.QRect(470, 186, 300, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtUsuario.setFont(font)
        self.txtUsuario.setObjectName(_fromUtf8("txtUsuario"))
        self.txtPassword = QtGui.QLineEdit(self.tabRegistrar)
        self.txtPassword.setGeometry(QtCore.QRect(470, 231, 300, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtPassword.setFont(font)
        self.txtPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.txtPassword.setObjectName(_fromUtf8("txtPassword"))
        self.txtPuesto = QtGui.QLineEdit(self.tabRegistrar)
        self.txtPuesto.setGeometry(QtCore.QRect(470, 275, 300, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtPuesto.setFont(font)
        self.txtPuesto.setObjectName(_fromUtf8("txtPuesto"))
        self.cbxRol = QtGui.QComboBox(self.tabRegistrar)
        self.cbxRol.setGeometry(QtCore.QRect(470, 318, 300, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cbxRol.setFont(font)
        self.cbxRol.setObjectName(_fromUtf8("cbxRol"))
        self.cbxRol.addItem(_fromUtf8(""))
        self.cbxRol.addItem(_fromUtf8(""))        
        self.cbxHorario = QtGui.QComboBox(self.tabRegistrar)
        self.cbxHorario.setGeometry(QtCore.QRect(470, 364, 300, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cbxHorario.setFont(font)
        self.cbxHorario.setObjectName(_fromUtf8("cbxHorario"))
        self.cbxHorario.addItem(_fromUtf8(""))
        self.cbxHorario.addItem(_fromUtf8(""))
        self.cbxHorario.addItem(_fromUtf8(""))
        self.label_2 = QtGui.QLabel(self.tabRegistrar)
        self.label_2.setGeometry(QtCore.QRect(200, 53, 161, 341))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tabWidget.addTab(self.tabRegistrar, _fromUtf8(""))
        self.tabConsultar = QtGui.QWidget()
        self.tabConsultar.setObjectName(_fromUtf8("tabConsultar"))
        self.label_5 = QtGui.QLabel(self.tabConsultar)
        self.label_5.setGeometry(QtCore.QRect(200, 52, 161, 291))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.txtCPuesto = QtGui.QLineEdit(self.tabConsultar)
        self.txtCPuesto.setEnabled(False)
        self.txtCPuesto.setGeometry(QtCore.QRect(470, 231, 300, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtCPuesto.setFont(font)
        self.txtCPuesto.setObjectName(_fromUtf8("txtCPuesto"))
        self.txtCApm = QtGui.QLineEdit(self.tabConsultar)
        self.txtCApm.setEnabled(False)
        self.txtCApm.setGeometry(QtCore.QRect(470, 186, 300, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtCApm.setFont(font)
        self.txtCApm.setObjectName(_fromUtf8("txtCApm"))
        self.txtCApp = QtGui.QLineEdit(self.tabConsultar)
        self.txtCApp.setEnabled(False)
        self.txtCApp.setGeometry(QtCore.QRect(470, 143, 300, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtCApp.setFont(font)
        self.txtCApp.setObjectName(_fromUtf8("txtCApp"))
        self.txtCUsuario = QtGui.QLineEdit(self.tabConsultar)
        self.txtCUsuario.setGeometry(QtCore.QRect(470, 54, 300, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtCUsuario.setFont(font)
        self.txtCUsuario.setObjectName(_fromUtf8("txtCUsuario"))
        self.cbxCRol = QtGui.QComboBox(self.tabConsultar)
        self.cbxCRol.setEnabled(False)
        self.cbxCRol.setGeometry(QtCore.QRect(470, 275, 300, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cbxCRol.setFont(font)
        self.cbxCRol.setObjectName(_fromUtf8("cbxCRol"))
        self.cbxCRol.addItem(_fromUtf8(""))
        self.cbxCRol.addItem(_fromUtf8(""))
        self.txtCNombre = QtGui.QLineEdit(self.tabConsultar)
        self.txtCNombre.setEnabled(False)
        self.txtCNombre.setGeometry(QtCore.QRect(470, 98, 300, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtCNombre.setFont(font)
        self.txtCNombre.setText(_fromUtf8(""))
        self.txtCNombre.setObjectName(_fromUtf8("txtCNombre"))
        self.cbxCHorario = QtGui.QComboBox(self.tabConsultar)
        self.cbxCHorario.setEnabled(False)
        self.cbxCHorario.setGeometry(QtCore.QRect(470, 320, 300, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cbxCHorario.setFont(font)
        self.cbxCHorario.setObjectName(_fromUtf8("cbxCHorario"))
        self.cbxCHorario.addItem(_fromUtf8(""))
        self.cbxCHorario.addItem(_fromUtf8(""))
        self.cbxCHorario.addItem(_fromUtf8(""))
        self.tabWidget.addTab(self.tabConsultar, _fromUtf8(""))
        self.tabModificar = QtGui.QWidget()
        self.tabModificar.setObjectName(_fromUtf8("tabModificar"))
        self.txtMApp = QtGui.QLineEdit(self.tabModificar)
        self.txtMApp.setEnabled(False)
        self.txtMApp.setGeometry(QtCore.QRect(470, 142, 300, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtMApp.setFont(font)
        self.txtMApp.setObjectName(_fromUtf8("txtMApp"))
        self.txtMUsuario = QtGui.QLineEdit(self.tabModificar)
        self.txtMUsuario.setGeometry(QtCore.QRect(470, 53, 300, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtMUsuario.setFont(font)
        self.txtMUsuario.setObjectName(_fromUtf8("txtMUsuario"))
        self.cbxMRol = QtGui.QComboBox(self.tabModificar)
        self.cbxMRol.setEnabled(False)
        self.cbxMRol.setGeometry(QtCore.QRect(470, 317, 300, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cbxMRol.setFont(font)
        self.cbxMRol.setObjectName(_fromUtf8("cbxMRol"))
        self.cbxMRol.addItem(_fromUtf8(""))
        self.cbxMRol.addItem(_fromUtf8(""))
        self.cbxMHorario = QtGui.QComboBox(self.tabModificar)
        self.cbxMHorario.setEnabled(False)
        self.cbxMHorario.setGeometry(QtCore.QRect(470, 363, 300, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cbxMHorario.setFont(font)
        self.cbxMHorario.setObjectName(_fromUtf8("cbxMHorario"))
        self.cbxMHorario.addItem(_fromUtf8(""))
        self.cbxMHorario.addItem(_fromUtf8(""))
        self.cbxMHorario.addItem(_fromUtf8(""))
        self.txtMNombre = QtGui.QLineEdit(self.tabModificar)
        self.txtMNombre.setEnabled(False)
        self.txtMNombre.setGeometry(QtCore.QRect(470, 97, 300, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtMNombre.setFont(font)
        self.txtMNombre.setText(_fromUtf8(""))
        self.txtMNombre.setObjectName(_fromUtf8("txtMNombre"))
        self.txtMPassword = QtGui.QLineEdit(self.tabModificar)
        self.txtMPassword.setEnabled(False)
        self.txtMPassword.setGeometry(QtCore.QRect(470, 230, 300, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtMPassword.setFont(font)
        self.txtMPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.txtMPassword.setObjectName(_fromUtf8("txtMPassword"))
        self.txtMApm = QtGui.QLineEdit(self.tabModificar)
        self.txtMApm.setEnabled(False)
        self.txtMApm.setGeometry(QtCore.QRect(470, 185, 300, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtMApm.setFont(font)
        self.txtMApm.setObjectName(_fromUtf8("txtMApm"))
        self.label_7 = QtGui.QLabel(self.tabModificar)
        self.label_7.setGeometry(QtCore.QRect(200, 52, 161, 341))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.txtMPuesto = QtGui.QLineEdit(self.tabModificar)
        self.txtMPuesto.setEnabled(False)
        self.txtMPuesto.setGeometry(QtCore.QRect(470, 274, 300, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtMPuesto.setFont(font)
        self.txtMPuesto.setObjectName(_fromUtf8("txtMPuesto"))
        self.tabWidget.addTab(self.tabModificar, _fromUtf8(""))
        self.tabEliminar = QtGui.QWidget()
        self.tabEliminar.setObjectName(_fromUtf8("tabEliminar"))
        self.txtEPuesto = QtGui.QLineEdit(self.tabEliminar)
        self.txtEPuesto.setEnabled(False)
        self.txtEPuesto.setGeometry(QtCore.QRect(470, 231, 300, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtEPuesto.setFont(font)
        self.txtEPuesto.setObjectName(_fromUtf8("txtEPuesto"))
        self.cbxERol = QtGui.QComboBox(self.tabEliminar)
        self.cbxERol.setEnabled(False)
        self.cbxERol.setGeometry(QtCore.QRect(470, 275, 300, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cbxERol.setFont(font)
        self.cbxERol.setObjectName(_fromUtf8("cbxERol"))
        self.cbxERol.addItem(_fromUtf8(""))
        self.cbxERol.addItem(_fromUtf8(""))
        self.label_8 = QtGui.QLabel(self.tabEliminar)
        self.label_8.setGeometry(QtCore.QRect(200, 52, 161, 291))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.txtEUsuario = QtGui.QLineEdit(self.tabEliminar)
        self.txtEUsuario.setGeometry(QtCore.QRect(470, 54, 300, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtEUsuario.setFont(font)
        self.txtEUsuario.setObjectName(_fromUtf8("txtEUsuario"))
        self.txtENombre = QtGui.QLineEdit(self.tabEliminar)
        self.txtENombre.setEnabled(False)
        self.txtENombre.setGeometry(QtCore.QRect(470, 98, 300, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtENombre.setFont(font)
        self.txtENombre.setText(_fromUtf8(""))
        self.txtENombre.setObjectName(_fromUtf8("txtENombre"))
        self.txtEApm = QtGui.QLineEdit(self.tabEliminar)
        self.txtEApm.setEnabled(False)
        self.txtEApm.setGeometry(QtCore.QRect(470, 186, 300, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtEApm.setFont(font)
        self.txtEApm.setObjectName(_fromUtf8("txtEApm"))
        self.cbxEHorario = QtGui.QComboBox(self.tabEliminar)
        self.cbxEHorario.setEnabled(False)
        self.cbxEHorario.setGeometry(QtCore.QRect(470, 320, 300, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cbxEHorario.setFont(font)
        self.cbxEHorario.setObjectName(_fromUtf8("cbxEHorario"))
        self.cbxEHorario.addItem(_fromUtf8(""))
        self.cbxEHorario.addItem(_fromUtf8(""))
        self.cbxEHorario.addItem(_fromUtf8(""))
        self.txtEApp = QtGui.QLineEdit(self.tabEliminar)
        self.txtEApp.setEnabled(False)
        self.txtEApp.setGeometry(QtCore.QRect(470, 143, 300, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtEApp.setFont(font)
        self.txtEApp.setObjectName(_fromUtf8("txtEApp"))
        self.tabWidget.addTab(self.tabEliminar, _fromUtf8(""))
        self.label = QtGui.QLabel(dGestionUsuario)
        self.label.setGeometry(QtCore.QRect(533, 30, 291, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Return To Sender"))
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_6 = QtGui.QLabel(dGestionUsuario)
        self.label_6.setGeometry(QtCore.QRect(872, 10, 101, 101))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8("/home/pi/Desktop/Ticket/img/logotipo1.png")))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton_2 = QtGui.QPushButton(dGestionUsuario)
        self.pushButton_2.setGeometry(QtCore.QRect(187, 641, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(_fromUtf8("QPushButton{\n"
"   border:1px solid rgb(165, 0, 0);\n"
"   border-top: rgb(165, 0, 0);\n"
"   background: rgb(165, 0, 0);\n"
"   padding: 9px 18px;\n"
"   border-radius: 9px;\n"
"   color: white;\n"
"   font-size: 16px;\n"
"    font: 75 16pt \"Roboto Condensed\";\n"
"   /*text-decoration: none;*/\n"
"   vertical-align: middle;\n"
"\n"
"}\n"
"  \n"
"QPushButton:hover {\n"
"   border-top-color: rgb(235, 0, 3);\n"
"    background:rgb(235, 0, 3);\n"
"   }"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.pushButton_6 = QtGui.QPushButton(dGestionUsuario)
        self.pushButton_6.setGeometry(QtCore.QRect(622, 641, 121, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))

        self.retranslateUi(dGestionUsuario)
        self.tabWidget.setCurrentIndex(0)
        self.cbxRol.setCurrentIndex(0)
        self.cbxCRol.setCurrentIndex(0)
        self.cbxMRol.setCurrentIndex(0)
        self.cbxERol.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(dGestionUsuario)
        #dGestionUsuario.setTabOrder(self.tabWidget, self.txtNombre)
        #dGestionUsuario.setTabOrder(self.txtNombre, self.txtApp)
        #dGestionUsuario.setTabOrder(self.txtApp, self.txtApm)
        #dGestionUsuario.setTabOrder(self.txtApm, self.txtUsuario)
        #dGestionUsuario.setTabOrder(self.txtUsuario, self.txtPassword)
        #dGestionUsuario.setTabOrder(self.txtPassword, self.txtPuesto)
        #dGestionUsuario.setTabOrder(self.txtPuesto, self.cbxRol)
        #dGestionUsuario.setTabOrder(self.cbxRol, self.cbxHorario)
        #dGestionUsuario.setTabOrder(self.cbxHorario, self.pushButton)
        #dGestionUsuario.setTabOrder(self.pushButton, self.pushButton_2)
        #dGestionUsuario.setTabOrder(self.pushButton_2, self.pushButton_6)
        #dGestionUsuario.setTabOrder(self.pushButton_6, dGestionUsuario.txtApp)
        #dGestionUsuario.setTabOrder(dGestionUsuario.txtApp_2, dGestionUsuario.cbxHorario)
        #dGestionUsuario.setTabOrder(dGestionUsuario.cbxHorario_2, dGestionUsuario.cbxRol)
        #dGestionUsuario.setTabOrder(dGestionUsuario.cbxRol_2, dGestionUsuario.txtUsuario)
        #dGestionUsuario.setTabOrder(dGestionUsuario.txtUsuario_2, dGestionUsuario.pushButton_3)
        #dGestionUsuario.setTabOrder(dGestionUsuario.pushButton_3, dGestionUsuario.txtNombre_2)
        #dGestionUsuario.setTabOrder(dGestionUsuario.txtNombre_2, dGestionUsuario.txtApm_2)
        #dGestionUsuario.setTabOrder(dGestionUsuario.txtApm_2, dGestionUsuario.pushButton_4)
        #dGestionUsuario.setTabOrder(dGestionUsuario.pushButton_4, dGestionUsuario.txtPuesto_2)
        #dGestionUsuario.setTabOrder(dGestionUsuario.txtPuesto_2, dGestionUsuario.txtPassword_2)
        #dGestionUsuario.setTabOrder(dGestionUsuario.txtPassword_2, dGestionUsuario.txtApp_3)
        #dGestionUsuario.setTabOrder(dGestionUsuario.txtApp_3, dGestionUsuario.cbxHorario_3)
        #dGestionUsuario.setTabOrder(dGestionUsuario.cbxHorario_3, dGestionUsuario.cbxRol_3)
        #dGestionUsuario.setTabOrder(dGestionUsuario.cbxRol_3, dGestionUsuario.txtUsuario_3)
        #dGestionUsuario.setTabOrder(dGestionUsuario.txtUsuario_3, dGestionUsuario.txtNombre_3)
        #dGestionUsuario.setTabOrder(dGestionUsuario.txtNombre_3, dGestionUsuario.txtApm_3)
        #dGestionUsuario.setTabOrder(dGestionUsuario.txtApm_3, dGestionUsuario.txtPuesto_3)
        #dGestionUsuario.setTabOrder(dGestionUsuario.txtPuesto_3, dGestionUsuario.txtPassword_3)

    def retranslateUi(self, dGestionUsuario):
        dGestionUsuario.setWindowTitle(_translate("dGestionUsuario", "Gestion de Usuarios", None))
        self.tabRegistrar.setToolTip(_translate("dGestionUsuario", "<html><head/><body><p>Permite dar de alta usuarios en el sistema.</p></body></html>", None))
        self.cbxHorario.setItemText(0, _translate("dGestionUsuario", "7:00 am - 15:00 pm", None))
        self.cbxHorario.setItemText(1, _translate("dGestionUsuario", "14:00 pm - 22:00 pm", None))
        self.cbxHorario.setItemText(2, _translate("dGestionUsuario", "22:00 pm - 7:00 am", None))
        self.cbxRol.setProperty("currentText", _translate("dGestionUsuario", "Administrador", None))
        self.cbxRol.setItemText(0, _translate("dGestionUsuario", "Administrador", None))
        self.cbxRol.setItemText(1, _translate("dGestionUsuario", "Cajero", None))
        self.label_2.setText(_translate("dGestionUsuario", "<html><head/><body><p>Nombre</p><p>Apellido Paterno</p><p>Apellido Materno</p><p>Usuario</p><p>Password</p><p>Puesto</p><p>Rol</p><p>Horario</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRegistrar), _translate("dGestionUsuario", "Registrar Usuario", None))
        self.label_5.setText(_translate("dGestionUsuario", "<html><head/><body><p>Usuario</p><p>Nombre</p><p>Apellido Paterno</p><p>Apellido Materno</p><p>Puesto</p><p>Rol</p><p>Horario</p></body></html>", None))
        self.cbxCRol.setProperty("currentText", _translate("dGestionUsuario", "Administrador", None))
        self.cbxCRol.setItemText(0, _translate("dGestionUsuario", "Administrador", None))
        self.cbxCRol.setItemText(1, _translate("dGestionUsuario", "Cajero", None))
        self.cbxCHorario.setItemText(0, _translate("dGestionUsuario", "7:00 am - 15:00 pm", None))
        self.cbxCHorario.setItemText(1, _translate("dGestionUsuario", "14:00 pm - 22:00 pm", None))
        self.cbxCHorario.setItemText(2, _translate("dGestionUsuario", "22:00 pm - 7:00 am", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabConsultar), _translate("dGestionUsuario", "Consultar Usuario", None))
        self.cbxMRol.setProperty("currentText", _translate("dGestionUsuario", "Administrador", None))
        self.cbxMRol.setItemText(0, _translate("dGestionUsuario", "Administrador", None))
        self.cbxMRol.setItemText(1, _translate("dGestionUsuario", "Cajero", None))
        self.cbxMHorario.setItemText(0, _translate("dGestionUsuario", "7:00 am - 15:00 pm", None))
        self.cbxMHorario.setItemText(1, _translate("dGestionUsuario", "14:00 pm - 22:00 pm", None))
        self.cbxMHorario.setItemText(2, _translate("dGestionUsuario", "22:00 pm - 7:00 am", None))
        self.label_7.setText(_translate("dGestionUsuario", "<html><head/><body><p>Usuario</p><p>Nombre</p><p>Apellido Paterno</p><p>Apellido Materno</p><p>Password</p><p>Puesto</p><p>Rol</p><p>Horario</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabModificar), _translate("dGestionUsuario", "Modificar Usuario", None))
        self.cbxERol.setProperty("currentText", _translate("dGestionUsuario", "Administrador", None))
        self.cbxERol.setItemText(0, _translate("dGestionUsuario", "Administrador", None))
        self.cbxERol.setItemText(1, _translate("dGestionUsuario", "Cajero", None))
        self.label_8.setText(_translate("dGestionUsuario", "<html><head/><body><p>Usuario</p><p>Nombre</p><p>Apellido Paterno</p><p>Apellido Materno</p><p>Puesto</p><p>Rol</p><p>Horario</p></body></html>", None))
        self.cbxEHorario.setItemText(0, _translate("dGestionUsuario", "7:00 am - 15:00 pm", None))
        self.cbxEHorario.setItemText(1, _translate("dGestionUsuario", "14:00 pm - 22:00 pm", None))
        self.cbxEHorario.setItemText(2, _translate("dGestionUsuario", "22:00 pm - 7:00 am", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabEliminar), _translate("dGestionUsuario", "Eliminar Usuario", None))
        self.label.setText(_translate("dGestionUsuario", "Gestion de Usuarios", None))
        self.pushButton.setText(_translate("dGestionUsuario", "Aceptar", None))
        self.pushButton.setShortcut(_translate("dGestionUsuario", "Return", None))
        self.pushButton_2.setText(_translate("dGestionUsuario", "Cancelar", None))
        self.pushButton_2.setShortcut(_translate("dGestionUsuario", "Esc", None))

        self.pushButton_6.setText(_translate("dGestionUsuario", "Limpiar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dGestionUsuario = QtGui.QDialog()
    ui = Ui_dGestionUsuario()
    ui.setupUi(dGestionUsuario)
    dGestionUsuario.show()
    sys.exit(app.exec_())

