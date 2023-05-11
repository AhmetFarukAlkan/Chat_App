from tkinter import W
from typing import List
from numpy import append
from Ui_AddFriend import Ui_Form as AddFriend
from PyQt5.QtWidgets import QDialog, QApplication,QListWidgetItem
from FriendRequestWidget import widget as friendRequestWidget

class ClassFriend(QDialog,AddFriend):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        AddFriend.__init__(self)
        self.setupUi(self)
        self.BtnAddFriend.clicked.connect(self.addFri)
    

    global listeKabul, listeRed, Listeİstek

    listeKabul = []
    listeRed = []
    Listeİstek = []

    def acc(self,text):
        listeKabul.append(text)
        Listeİstek.remove(text)
        self.FriendsListWidget.clear() 
        self.setList()           
    def dec(self,text):
        listeRed.append(text)
        self.FriendsListWidget.clear()
        Listeİstek.remove(text)
        self.setList()
    #Eleman ekleme
    def addFri(self):
        reqFrie = friendRequestWidget()
        item = QListWidgetItem()
        reqFrie.callingLabel.setText(self.lineEdit.text())
        item.setSizeHint(reqFrie.maximumSize())
        self.FriendsListWidget.addItem(item)
        self.FriendsListWidget.setMinimumWidth(reqFrie.width())     
        self.FriendsListWidget.setItemWidget(item, reqFrie)
        self.FriendsListWidget.setCurrentRow(self.FriendsListWidget.count() - 1)
        reqFrie.BtnAccept.clicked.connect(lambda: self.acc(reqFrie.callingLabel.text()))
        reqFrie.Btndecline.clicked.connect(lambda: self.dec(reqFrie.callingLabel.text()))
        Listeİstek.append(self.lineEdit.text())        
        self.lineEdit.setText("")
        print(Listeİstek)
        print(listeKabul)
        print(listeRed)   

    def setList(self):
        for i in Listeİstek:
            reqFrie = friendRequestWidget()
            item = QListWidgetItem()
            reqFrie.callingLabel.setText(str(i))
            item.setSizeHint(reqFrie.maximumSize())
            self.FriendsListWidget.addItem(item)
            self.FriendsListWidget.setMinimumWidth(reqFrie.width())     
            self.FriendsListWidget.setItemWidget(item, reqFrie)
            self.FriendsListWidget.setCurrentRow(self.FriendsListWidget.count() - 1)
            reqFrie.BtnAccept.clicked.connect(lambda: self.acc(reqFrie.callingLabel.text()))
            reqFrie.Btndecline.clicked.connect(lambda: self.dec(reqFrie.callingLabel.text()))
            Listeİstek.append(self.lineEdit.text())        
            self.lineEdit.setText("")

def main():
    from sys import argv
    app = QApplication(argv)
    dialog = ClassFriend()
    dialog.show()
    app.exec_()


if __name__ == '__main__':
    main()