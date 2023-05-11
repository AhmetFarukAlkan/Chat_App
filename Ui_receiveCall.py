# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\dursun\Documents\PythonCodes\receiveCall.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(480, 86)
        Form.setMaximumSize(QtCore.QSize(480, 90))
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 10, 480, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMaximumSize(QtCore.QSize(480, 90))
        self.groupBox_2.setStyleSheet("QGroupBox{background-color:transparent;border:0px;}")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setStyleSheet("QGroupBox{background-color:#ffffff;border-radius:10px;}\n"
"QLabel{color:#4f596f;}")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_4.setFlat(False)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.callingLabel = QtWidgets.QLabel(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.callingLabel.sizePolicy().hasHeightForWidth())
        self.callingLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.callingLabel.setFont(font)
        self.callingLabel.setWordWrap(True)
        self.callingLabel.setObjectName("callingLabel")
        self.horizontalLayout.addWidget(self.callingLabel)
        self.BtnAccept = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BtnAccept.sizePolicy().hasHeightForWidth())
        self.BtnAccept.setSizePolicy(sizePolicy)
        self.BtnAccept.setMinimumSize(QtCore.QSize(35, 25))
        self.BtnAccept.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnAccept.setStyleSheet("QPushButton{background-color:#ffffff;border-radius:10px;}")
        self.BtnAccept.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/sources/phone-call-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnAccept.setIcon(icon)
        self.BtnAccept.setObjectName("BtnAccept")
        self.horizontalLayout.addWidget(self.BtnAccept)
        self.Btndecline = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btndecline.sizePolicy().hasHeightForWidth())
        self.Btndecline.setSizePolicy(sizePolicy)
        self.Btndecline.setMinimumSize(QtCore.QSize(35, 25))
        self.Btndecline.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btndecline.setStyleSheet("QPushButton{background-color:#ffffff;border-radius:10px;}")
        self.Btndecline.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/sources/0094_005_phone_decline_hangup_hang_up-512.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btndecline.setIcon(icon1)
        self.Btndecline.setObjectName("Btndecline")
        self.horizontalLayout.addWidget(self.Btndecline)
        self.horizontalLayout_4.addWidget(self.groupBox_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.callingLabel.setText(_translate("Form", "Calling KİSİ"))
import sources_rc