from concurrent.futures import thread
# from curses import window
from email import message
from http import client
from logging.config import stopListening
from msilib.schema import Error
from turtle import st
from PyQt5.QtWidgets import QDialog, QApplication, QListWidgetItem
from cv2 import add
from grpc import server
from matplotlib import image
from matplotlib.pyplot import connect
from numpy import imag
from Ui_chat import Ui_Dialog as dialog
from receiveWidget import widget as recWidget
from sendWidget import widget as sendWidget
from receiveCallWidget import widget as receiveCallWidget
from sendCallWidget import widget as sendCallWidget
from AddFriendWindow import Dialog as AddFriend
from threading import Thread
import socket
from tkinter import filedialog
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from _thread import *
from vidstream import AudioSender
from vidstream import AudioReceiver
import threading
from MemberWidget import widget as Member


myip = '10.123.12.206'
destip = '25.73.110.228'

conn = None

Mes = ["##TextRec%%Merhaba", "##TextSend%%Hasan Nasılsın", "##TextRec%%iyidir"]


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
        self.BtnAddFriend.clicked.connect(self.AddFriend)
        self.receiver = AudioReceiver(myip, 8888)
        self.senderr = AudioSender(destip, 8888)
        self.setMessageList()
    def setMessageList(self):
        for i in Mes:
            if i.startswith("##TextRec%%"):
                recW = recWidget()
                recW.message.setText(str(i).replace("##TextRec%%"))
                item = QListWidgetItem()
                item.setSizeHint(recW.sizeHint())
                self.ChatlistWidget.addItem(item)
                self.ChatlistWidget.setItemWidget(item, recW)
                self.ChatlistWidget.setMinimumWidth(recW.width())
                self.ChatlistWidget.setCurrentRow(self.ChatlistWidget.count() - 1)   
            else:    
                sendW = sendWidget()
                sendW.message.setText(str(i).replace("##TextSend%%"))
                if conn != None:
                    message = self.mlineEdit.text().encode('utf-8')
                    conn.send(message)
                item = QListWidgetItem()
                item.setSizeHint(sendW.sizeHint())
                self.ChatlistWidget.addItem(item)
                self.ChatlistWidget.setItemWidget(item, sendW)
                self.ChatlistWidget.setMinimumWidth(sendW.width())
                self.mlineEdit.setText('')
                self.ChatlistWidget.setCurrentRow(self.ChatlistWidget.count() - 1)
        pass


    def sendMessage(self):
        sendW = sendWidget()
        sendW.message.setText(str(self.mlineEdit.text()))
        if conn != None:
            message = self.mlineEdit.text().encode('utf-8')
            conn.send(message)
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
            self.ChatlistWidget.setCurrentRow(self.ChatlistWidget.count() - 1)
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
            self.receiver.stop_server()
            self.senderr.stop_stream()

        elif str(text).startswith("##RequestAccept%%") == True:
            self.Speak()

    def AddFriend(self):
        member = Member()
        member.callingLabel.setText("MAas")
        item = QListWidgetItem()
        item.setSizeHint(member.maximumSize())
        self.FriendsListWidget.addItem(item)
        self.FriendsListWidget.setMinimumWidth(member.width())     
        self.FriendsListWidget.setItemWidget(item, member)
        self.FriendsListWidget.setCurrentRow(self.FriendsListWidget.count() - 1)
        self.addFriend = AddFriend() 
        self.addFriend.show()
        

    def AddImage(self):
        global image_path
        image_path = filedialog.askopenfilename()
        self.image_name = os.path.basename(image_path)
        self.image_extension = self.image_name[self.image_name.rfind('.') + 1:]
        pixmap = QPixmap(image_path)
        sendW = sendWidget()
        sendW.message.setPixmap(pixmap)
        global m
        if conn != None:
            f = open(image_path, "rb")
            l = os.path.getsize(image_path)
            m = f.read(l)
            conn.sendall(m)
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
        if conn != None:
            message = "##StopCalling%%".encode('utf-8')
            conn.send(message)
        self.receiver.stop_server()
        self.senderr.stop_stream()


    def Answer(self):
        print("Answer")
        self.BtnCall.hide()
        if conn != None:
            message = "##RequestAccept%%".encode('utf-8')
            conn.send(message)
           
        self.Speak()
        #receiveCallWidget.Bt.clicked.connect(self.Decline)

    def Speak(self):
        print("Speak")
        try:
            self.receiver = AudioReceiver(myip, 8888)
            self.senderr = AudioSender(destip, 8888)

            #self.receiver = AudioReceiver('10.104.2.193', 8888)  # me sesi gönderen
            self.receive_thread = threading.Thread(target=self.receiver.start_server)
            print("receive")
            #self.sender = AudioSender('10.104.2.193', 8888)  # he/she sesi alan
            self.sender_thread = threading.Thread(target=self.senderr.start_stream)
            print("sender")
        
            self.receive_thread.start()
            self.sender_thread.start()
        except Exception:
            #self.receiver = AudioReceiver('10.104.2.193', 8888)  # me sesi gönderen
            self.receive_thread = threading.Thread(target=self.receiver.start_server)
            print("receive")
            #self.sender = AudioSender('10.104.2.193', 8888)  # he/she sesi alan
            self.sender_thread = threading.Thread(target=self.senderr.start_stream)
            print("sender")
        
            self.receive_thread.start()
            self.sender_thread.start()
            print("Offline")    
        print("Thread")
    def Call(self):
        print("Call")
        sendCall = sendCallWidget()
        sendCall.callingLabel.setText('Calling ' + 'kisi')
        item = QListWidgetItem()
        item.setSizeHint(sendCall.maximumSize())
        self.ChatlistWidget.addItem(item)
        self.ChatlistWidget.setItemWidget(item, sendCall)
        self.ChatlistWidget.setMinimumWidth(sendCall.width())
        # self.reclineEdit.setText('requestCall')
        self.reclineEdit.setText('')
        self.ChatlistWidget.setCurrentRow(self.ChatlistWidget.count() - 1)

        if conn != None:
            message = '##callRequest%%'.encode('utf-8')
            conn.send(message)

        """self.receive_thread.start()
        self.sender_thread.start()"""
        self.BtnCall.hide()
        sendCall.Btndecline.clicked.connect(self.Decline)


class serverThread(Thread):
    def __init__(self, widow):
        Thread.__init__(self)
        self.widow = widow

    def run(self):
        ServerSideSocket = socket.socket()
        host = myip
        port = 4000
        ServerSideSocket.bind((host, port))
        ServerSideSocket.listen(5)
        global conn
        print("Socket is listening...")
        try:
            (conn, (ip, pot)) = ServerSideSocket.accept()
            print("Connect to: " + str(ip) + ":" + str(pot))
            while True:
                global message
                message = conn.recv(1024 * 1024)
                try:
                    clearM = message.decode('utf-8')

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
    server = serverThread(dialog)
    server.start()
    dialog.show()
    app.exec_()


if __name__ == '__main__':
    main()