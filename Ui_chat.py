# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\dursun\Documents\PythonCodes\chat.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(561, 590)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setStyleSheet("QGroupBox{background-color:#f3f6fb;border-radius:10px;}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Photo = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Photo.sizePolicy().hasHeightForWidth())
        self.Photo.setSizePolicy(sizePolicy)
        self.Photo.setText("")
        self.Photo.setPixmap(QtGui.QPixmap(":/sources/21-214439_free-high-quality-person-icon-default-profile-picture-removebg-preview-removebg-preview.png"))
        self.Photo.setObjectName("Photo")
        self.horizontalLayout_3.addWidget(self.Photo)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.BtnCall = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BtnCall.sizePolicy().hasHeightForWidth())
        self.BtnCall.setSizePolicy(sizePolicy)
        self.BtnCall.setMinimumSize(QtCore.QSize(35, 25))
        self.BtnCall.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnCall.setStyleSheet("QPushButton{background-color:#f3f6fb;border-radius:10px;}")
        self.BtnCall.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/sources/phone-call-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnCall.setIcon(icon)
        self.BtnCall.setObjectName("BtnCall")
        self.horizontalLayout_3.addWidget(self.BtnCall)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setStyleSheet("QListWidget{border:0px;background-color:#f3f6fb;}")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setContentsMargins(9, 2, 9, 2)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ChatlistWidget = QtWidgets.QListWidget(self.groupBox_3)
        self.ChatlistWidget.setStyleSheet("")
        self.ChatlistWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ChatlistWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ChatlistWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ChatlistWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.ChatlistWidget.setObjectName("ChatlistWidget")
        self.verticalLayout_2.addWidget(self.ChatlistWidget)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setStyleSheet("QGroupBox{background-color:#fcfdfd;}\n"
"QlinEdit{border:1px solid #d8d9dc;border-radius:5px;}")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Addimage = QtWidgets.QPushButton(self.groupBox_2)
        self.Addimage.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Addimage.setStyleSheet("QPushButton{background-color:#f3f6fb;border-radius:10px;}")
        self.Addimage.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/sources/link.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Addimage.setIcon(icon1)
        self.Addimage.setObjectName("Addimage")
        self.horizontalLayout_2.addWidget(self.Addimage)
        self.mlineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.mlineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.mlineEdit.setObjectName("mlineEdit")
        self.horizontalLayout_2.addWidget(self.mlineEdit)
        self.sendButton = QtWidgets.QPushButton(self.groupBox_2)
        self.sendButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sendButton.setWhatsThis("")
        self.sendButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.sendButton.setAutoFillBackground(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/sources/arrow-34-24.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sendButton.setIcon(icon2)
        self.sendButton.setObjectName("sendButton")
        self.horizontalLayout_2.addWidget(self.sendButton)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.reclineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.reclineEdit.setObjectName("reclineEdit")
        self.verticalLayout.addWidget(self.reclineEdit)
        self.horizontalLayout.addWidget(self.groupBox)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.mlineEdit.setPlaceholderText(_translate("Dialog", "Mesaj"))
        self.sendButton.setText(_translate("Dialog", "Gönder"))
import sources_rc