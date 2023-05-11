from concurrent.futures import thread
# from curses import window
from email import message
from http import client
from msilib.schema import Error
from turtle import st
from PyQt5.QtWidgets import QDialog, QApplication, QListWidgetItem
from grpc import Call, server
from matplotlib.pyplot import connect
from Ui_chat import Ui_Dialog as dialog
from receiveWidget import widget as recWidget
from sendWidget import widget as sendWidget
from threading import Thread
import socket
import os
from _thread import *
from PyQt5.QtGui import QPixmap
from PIL import Image
from tkinter import filedialog
from receiveCallWidget import widget as receiveCallWidget
from sendCallWidget import widget as sendCallWidget
from vidstream import AudioSender
from vidstream import AudioReceiver
import threading

myip = '25.80.34.32'
destip = '192.168.88.186'

ServerSideSocket = None


class Dialog(QDialog, dialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        QDialog.__init__(self)
        self.setupUi(self)
        self.sendButton.clicked.connect(self.sendMessage)
        self.reclineEdit.setHidden(True)
        self.reclineEdit.textChanged.connect(self.recMessage)
        self.Addimage.clicked.connect(self.AddImage)
        self.BtnCall.clicked.connect(self.Call)
        self.receiver = AudioReceiver(myip, 8888)
        self.senderr = AudioSender(destip, 8888)
    def sendMessage(self):
        sendW = sendWidget()
        sendW.message.setText(str(self.mlineEdit.text()))
        if ServerSideSocket != None:
            message = self.mlineEdit.text().encode('utf-8')
            ServerSideSocket.send(message)
        item = QListWidgetItem()
        item.setSizeHint(sendW.sizeHint())
        self.ChatlistWidget.addItem(item)
        self.ChatlistWidget.setItemWidget(item, sendW)
        self.ChatlistWidget.setMinimumWidth(sendW.width())
        self.mlineEdit.setText('')
        self.ChatlistWidget.setCurrentRow(self.ChatlistWidget.count() - 1)

    def recMessage(self, text):
        if str(text).startswith("##Text%%") == True:
            recW = recWidget()
            recW.message.setText(str(text).replace("##Text%%", ""))
            item = QListWidgetItem()
            item.setSizeHint(recW.sizeHint())
            self.ChatlistWidget.addItem(item)
            self.ChatlistWidget.setItemWidget(item, recW)
            self.ChatlistWidget.setMinimumWidth(recW.width())
        elif str(text).startswith("##Image%%") == True:
            pixmap = QPixmap('recieved.png')
            sendW = recWidget()
            sendW.message.setPixmap(pixmap)
            item = QListWidgetItem()
            item.setSizeHint(sendW.sizeHint())
            self.ChatlistWidget.addItem(item)
            self.ChatlistWidget.setItemWidget(item, sendW)
            self.mlineEdit.setText('')
            self.ChatlistWidget.setCurrentRow(self.ChatlistWidget.count() - 1)
        elif str(text).startswith("##callRequest%%") == True:
            recCall = receiveCallWidget()
            recCall.callingLabel.setText('Calling ' + 'kisi')
            item = QListWidgetItem()
            item.setSizeHint(recCall.maximumSize())
            self.ChatlistWidget.addItem(item)
            self.ChatlistWidget.setItemWidget(item, recCall)
            self.ChatlistWidget.setMinimumWidth(recCall.width())
            self.mlineEdit.setText('')
            self.ChatlistWidget.setCurrentRow(self.ChatlistWidget.count() - 1)
            recCall.BtnAccept.clicked.connect(self.Answer)
            recCall.Btndecline.clicked.connect(self.Decline)
        elif str(text).startswith("##StopCalling%%") == True:
            self.BtnCall.show()
            self.Decline()
            self.receiver.stop_server()
            self.senderr.stop_stream()

        elif str(text).startswith("##RequestAccept%%") == True:
            self.Speak()

    def AddImage(self):
        global image_path
        image_path = filedialog.askopenfilename()
        self.image_name = os.path.basename(image_path)
        self.image_extension = self.image_name[self.image_name.rfind('.') + 1:]
        pixmap = QPixmap(image_path)
        sendW = sendWidget()
        sendW.message.setPixmap(pixmap)
        global m
        if ServerSideSocket != None:
            f = open(image_path, "rb")
            l = os.path.getsize(image_path)
            m = f.read(l)
            ServerSideSocket.sendall(m)
            f.close()
            print("Done sending...")
        item = QListWidgetItem()
        item.setSizeHint(sendW.sizeHint())
        self.ChatlistWidget.addItem(item)
        self.ChatlistWidget.setItemWidget(item, sendW)
        self.mlineEdit.setText('')
        self.ChatlistWidget.setCurrentRow(self.ChatlistWidget.count() - 1)

    def Decline(self):
        print("Decline")
        self.BtnCall.show() 
        if ServerSideSocket != None:
            message = "##StopCalling%%".encode('utf-8')
            ServerSideSocket.send(message)
        self.receiver.stop_server()
        self.senderr.stop_stream()

    def Answer(self):
        print("Answer")
        self.BtnCall.hide()
        if ServerSideSocket != None:
            message = "##RequestAccept%%".encode('utf-8')
            ServerSideSocket.send(message)
        
        self.Speak()
        #receiveCallWidget.Btndecline.clicked.connect(self.Decline)

    def Speak(self):
        try:
            self.receiver = AudioReceiver(myip, 8888)
            self.senderr = AudioSender(destip, 8888)
            self.receive_thread = threading.Thread(target=self.receiver.start_server)
            self.sender_thread = threading.Thread(target=self.senderr.start_stream)
            self.receive_thread.start()
            self.sender_thread.start()
        except Exception:
            self.receive_thread = threading.Thread(target=self.receiver.start_server)
            self.sender_thread = threading.Thread(target=self.senderr.start_stream)
            self.receive_thread.start()
            self.sender_thread.start()
            print("Offline")
    def Call(self):
        print("Call")
        sendCall = sendCallWidget()

        sendCall.callingLabel.setText('Calling ' + 'kisi')
        item = QListWidgetItem()
        item.setSizeHint(sendCall.maximumSize())
        self.ChatlistWidget.addItem(item)
        self.ChatlistWidget.setItemWidget(item, sendCall)
        self.ChatlistWidget.setMinimumWidth(sendCall.width())
        self.mlineEdit.setText('')
        self.ChatlistWidget.setCurrentRow(self.ChatlistWidget.count() - 1)

        if ServerSideSocket != None:
            message = '##callRequest%%'.encode('utf-8')
            ServerSideSocket.send(message)

        self.BtnCall.hide()

        """def Decline():
                self.BtnCall.show()
                self.receiver.stop_server()
                self.sender.stop_stream()"""

        sendCall.Btndecline.clicked.connect(self.Decline)


class clientThread(Thread):
    def __init__(self, widow):
        Thread.__init__(self)
        self.widow = widow

    def run(self):
        global ServerSideSocket
        ServerSideSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = destip
        port = 4000
        print("Waiting for connection response")
        try:
            ServerSideSocket.connect((host, port))
            while True:
                global message
                message = ServerSideSocket.recv(1024 * 1024)
                try:
                    clearM = message.decode('utf-8')
                    print(str(clearM).startswith('##calling%%'))
                    print(str(clearM).startswith('##StopCalling%%'))
                    if str(clearM).startswith('##callRequest%%') == True:
                        self.widow.reclineEdit.setText(str(clearM))
                    elif str(clearM).startswith('##StopCalling%%') == True:
                        self.widow.reclineEdit.setText(str(clearM))
                    elif str(clearM).startswith('##RequestAccept%%') == True:
                        self.widow.reclineEdit.setText(str(clearM))
                    else:
                        self.widow.reclineEdit.setText("##Text%%" + str(clearM))
                except UnicodeDecodeError as er:
                    f = open("recieved.png", "wb")
                    data = message
                    f.write(data)
                    f.close()
                    print("Done receiving")
                    self.widow.reclineEdit.setText("##Image%%")
        except socket.error as e:
            print(str(e))


def main():
    from sys import argv
    app = QApplication(argv)
    dialog = Dialog()
    client = clientThread(dialog)
    client.start()
    dialog.show()
    app.exec_()


if __name__ == '__main__':
    main()