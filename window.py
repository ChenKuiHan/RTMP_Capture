# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(579, 369)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(70, 10, 421, 21))
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox.setObjectName("comboBox")
        self.startButton = QtWidgets.QPushButton(Form)
        self.startButton.setGeometry(QtCore.QRect(500, 10, 71, 21))
        self.startButton.setObjectName("startButton")
        self.stopButton = QtWidgets.QPushButton(Form)
        self.stopButton.setGeometry(QtCore.QRect(500, 10, 71, 21))
        self.stopButton.setObjectName("stopButton")
        self.clearButton = QtWidgets.QPushButton(Form)
        self.clearButton.setGeometry(QtCore.QRect(190, 40, 71, 21))
        self.clearButton.setObjectName("clearButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 40, 91, 21))
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(10, 70, 561, 291))
        self.listWidget.setObjectName("listWidget")
        self.delButton = QtWidgets.QPushButton(Form)
        self.delButton.setGeometry(QtCore.QRect(110, 40, 71, 21))
        self.delButton.setObjectName("delButton")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(500, 40, 71, 20))
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.startButton.setText(_translate("Form", "开始"))
        self.stopButton.setText(_translate("Form", "停止"))
        self.clearButton.setText(_translate("Form", "清空"))
        self.label.setText(_translate("Form", "选择网卡:"))
        self.pushButton.setText(_translate("Form", "流播放器打开"))
        self.delButton.setText(_translate("Form", "删除"))
        self.checkBox.setText(_translate("Form", "阻止睡眠"))
