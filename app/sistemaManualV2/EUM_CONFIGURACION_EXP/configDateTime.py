# -*- coding: utf-8 -*-


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

class dConfDT(object):
    def __init__(self, dConfDT):
    #def setupUi(self, dConfDT):
        dConfDT.setObjectName(_fromUtf8("dConfDT"))
        dConfDT.setEnabled(True)
        dConfDT.resize(500, 500)
        dConfDT.setMinimumSize(QtCore.QSize(500, 500))
        dConfDT.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(16)
        dConfDT.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../Ticket/Version 1/img/logotipo1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dConfDT.setWindowIcon(icon)
        self.label_Atributo = QtGui.QLabel(dConfDT)
        self.label_Atributo.setGeometry(QtCore.QRect(60, 90, 161, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_Atributo.setFont(font)
        self.label_Atributo.setObjectName(_fromUtf8("label_Atributo"))
        self.pushButton_Aceptar = QtGui.QPushButton(dConfDT)
        self.pushButton_Aceptar.setGeometry(QtCore.QRect(360, 450, 121, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_Aceptar.setFont(font)
        self.pushButton_Aceptar.setStyleSheet(_fromUtf8("QPushButton{\n"
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
        self.pushButton_Aceptar.setObjectName(_fromUtf8("pushButton_Aceptar"))
        self.label_Titulo = QtGui.QLabel(dConfDT)
        self.label_Titulo.setGeometry(QtCore.QRect(40, 20, 451, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Return To Sender"))
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.label_Titulo.setFont(font)
        self.label_Titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Titulo.setObjectName(_fromUtf8("label_Titulo"))
        self.pushButton_Cancelar = QtGui.QPushButton(dConfDT)
        self.pushButton_Cancelar.setGeometry(QtCore.QRect(20, 450, 131, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_Cancelar.setFont(font)
        self.pushButton_Cancelar.setStyleSheet(_fromUtf8("QPushButton{\n"
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
        self.pushButton_Cancelar.setShortcut(_fromUtf8(""))
        self.pushButton_Cancelar.setObjectName(_fromUtf8("pushButton_Cancelar"))
        self.label_Imagen = QtGui.QLabel(dConfDT)
        self.label_Imagen.setGeometry(QtCore.QRect(210, 340, 111, 111))
        self.label_Imagen.setText(_fromUtf8(""))
        self.label_Imagen.setPixmap(QtGui.QPixmap(_fromUtf8("../Ticket/Version 1/img/logotipo1.png")))
        self.label_Imagen.setScaledContents(True)
        self.label_Imagen.setObjectName(_fromUtf8("label_Imagen"))
        self.dateTimeEdit = QtGui.QDateTimeEdit(dConfDT)
        self.dateTimeEdit.setGeometry(QtCore.QRect(40, 220, 450, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Arabic Kufi"))
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setMinimumDate(QtCore.QDate(1790, 9, 20))
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        from datetime import datetime
        mydate=datetime.now()
        #print mydate
        self.dateTimeEdit.setDateTime(mydate)
        self.label_Atributo_2 = QtGui.QLabel(dConfDT)
        self.label_Atributo_2.setGeometry(QtCore.QRect(290, 90, 161, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_Atributo_2.setFont(font)
        self.label_Atributo_2.setObjectName(_fromUtf8("label_Atributo_2"))
        self.label_Atributo_3 = QtGui.QLabel(dConfDT)
        self.label_Atributo_3.setGeometry(QtCore.QRect(30, 330, 431, 111))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_Atributo_3.setFont(font)
        self.label_Atributo_3.setObjectName(_fromUtf8("label_Atributo_3"))

        self.retranslateUi(dConfDT)
        QtCore.QMetaObject.connectSlotsByName(dConfDT)

    def retranslateUi(self, dConfDT):
        dConfDT.setWindowTitle(_translate("dConfDT", "Registro de Usuarios", None))
        self.label_Atributo.setText(_translate("dConfDT", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Fecha </span></p><p align=\"center\"><span style=\" font-size:18pt;\">(dd-mm-aaaa)</span><br/></p></body></html>", None))
        self.pushButton_Aceptar.setText(_translate("dConfDT", "Aceptar", None))
        self.pushButton_Aceptar.setShortcut(_translate("dConfDT", "Return", None))
        self.label_Titulo.setText(_translate("dConfDT", "Fecha y Hora", None))
        self.pushButton_Cancelar.setText(_translate("dConfDT", "Cancelar", None))
        self.label_Atributo_2.setText(_translate("dConfDT", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Hora</span></p><p align=\"center\"><span style=\" font-size:18pt;\">(HH:MM)</span><br/></p></body></html>", None))
        self.label_Atributo_3.setText(_translate("dConfDT", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Puedes modificar la fecha y la hora</span></p><p align=\"center\"><span style=\" font-size:18pt;\">Posteriormente Aceptar.</span></p></body></html>", None))

"""
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dConfigurarFechaHora = QtGui.QDialog()
    ui = Ui_dConfDT()
    ui.setupUi(dConfigurarFechaHora)
    dConfigurarFechaHora.show()
    sys.exit(app.exec_())
"""
