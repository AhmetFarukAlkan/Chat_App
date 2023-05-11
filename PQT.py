from msilib.schema import ListView
from tkinter import Scrollbar
from PyQt5 import QtWidgets,uic



app = QtWidgets.QApplication([])
call = uic.loadUi("Receive.ui")
#call = uic.loadUi("Send.ui")
#call = uic.loadUi("chat.ui")
call.show()
app.exec()