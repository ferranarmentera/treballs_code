# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/fcolell/Documents/Python_vstudio/Calculadora_simple.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(550, 358)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 150, 381, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.boton_suma = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.boton_suma.setObjectName("boton_suma")
        self.horizontalLayout.addWidget(self.boton_suma)
        self.boton_resta = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.boton_resta.setObjectName("boton_resta")
        self.horizontalLayout.addWidget(self.boton_resta)
        self.boton_mul = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.boton_mul.setObjectName("boton_mul")
        self.horizontalLayout.addWidget(self.boton_mul)
        self.boton_div = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.boton_div.setObjectName("boton_div")
        self.horizontalLayout.addWidget(self.boton_div)
        self.salida = QtWidgets.QLabel(Form)
        self.salida.setGeometry(QtCore.QRect(80, 250, 381, 31))
        self.salida.setAlignment(QtCore.Qt.AlignCenter)
        self.salida.setObjectName("salida")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(190, 40, 160, 80))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.num_1 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.num_1.setObjectName("num_1")
        self.gridLayout_2.addWidget(self.num_1, 0, 1, 1, 1)
        self.num_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.num_2.setObjectName("num_2")
        self.gridLayout_2.addWidget(self.num_2, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.boton_suma.setText(_translate("Form", "+"))
        self.boton_resta.setText(_translate("Form", "-"))
        self.boton_mul.setText(_translate("Form", "*"))
        self.boton_div.setText(_translate("Form", "/"))
        self.salida.setText(_translate("Form", "TextLabel"))
        self.label.setText(_translate("Form", "Número 1:"))
        self.label_2.setText(_translate("Form", "Número 2:"))


