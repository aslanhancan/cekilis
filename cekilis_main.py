# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cekilis.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(562, 399)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(340, 309, 222, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.btnEkle = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnEkle.setObjectName("btnEkle")
        self.horizontalLayout.addWidget(self.btnEkle)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 281, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.verticalLayout.addWidget(self.listWidget)
        self.lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl.setObjectName("lbl")
        self.verticalLayout.addWidget(self.lbl)
        self.btnSil = QtWidgets.QPushButton(self.centralwidget)
        self.btnSil.setGeometry(QtCore.QRect(150, 370, 71, 23))
        self.btnSil.setObjectName("btnSil")
        self.btnSec = QtWidgets.QPushButton(self.centralwidget)
        self.btnSec.setGeometry(QtCore.QRect(220, 370, 75, 23))
        self.btnSec.setObjectName("btnSec")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(380, 10, 160, 91))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lblUser = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblUser.setObjectName("lblUser")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblUser)
        self.lineUser = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineUser.setObjectName("lineUser")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineUser)
        self.lblPass = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblPass.setObjectName("lblPass")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblPass)
        self.linePass = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.linePass.setInputMethodHints(QtCore.Qt.ImhNone)
        self.linePass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.linePass.setObjectName("linePass")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.linePass)
        self.btnGiris = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btnGiris.setObjectName("btnGiris")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.btnGiris)
        self.btnList = QtWidgets.QPushButton(self.centralwidget)
        self.btnList.setGeometry(QtCore.QRect(460, 110, 75, 23))
        self.btnList.setObjectName("btnList")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnEkle.setText(_translate("MainWindow", "Ekle"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "asdad"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.lbl.setText(_translate("MainWindow", "asdasd"))
        self.btnSil.setText(_translate("MainWindow", "Sil"))
        self.btnSec.setText(_translate("MainWindow", "Seç"))
        self.lblUser.setText(_translate("MainWindow", "Kullanıcı Adı:"))
        self.lblPass.setText(_translate("MainWindow", "Şifre:"))
        self.btnGiris.setText(_translate("MainWindow", "Instagram Giriş"))
        self.btnList.setText(_translate("MainWindow", "listeyi ekle"))