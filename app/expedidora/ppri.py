from escposprinter import *#original funcional
Generic = printer.Usb(0x0519,0x0001)
import time

Generic.image("/home/pi/Documents/EUM_EXPE/CodigosQR/outputQR.png")
Generic.cut()
time.sleep(4)
Generic.image("/home/pi/Documents/EUM_EXPE/CodigosQR/outputQR.png")
Generic.cut()

