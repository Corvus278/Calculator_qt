# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\PycharmProjects\Calculator_Qt\calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(682, 562)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Button_sqrt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_sqrt.sizePolicy().hasHeightForWidth())
        self.Button_sqrt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_sqrt.setFont(font)
        self.Button_sqrt.setObjectName("Button_sqrt")
        self.horizontalLayout.addWidget(self.Button_sqrt)
        self.Button_qrt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_qrt.sizePolicy().hasHeightForWidth())
        self.Button_qrt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_qrt.setFont(font)
        self.Button_qrt.setObjectName("Button_qrt")
        self.horizontalLayout.addWidget(self.Button_qrt)
        self.Button_C = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_C.sizePolicy().hasHeightForWidth())
        self.Button_C.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_C.setFont(font)
        self.Button_C.setObjectName("Button_C")
        self.horizontalLayout.addWidget(self.Button_C)
        self.Button_del = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_del.sizePolicy().hasHeightForWidth())
        self.Button_del.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_del.setFont(font)
        self.Button_del.setObjectName("Button_del")
        self.horizontalLayout.addWidget(self.Button_del)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Button_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_7.sizePolicy().hasHeightForWidth())
        self.Button_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_7.setFont(font)
        self.Button_7.setObjectName("Button_7")
        self.horizontalLayout_2.addWidget(self.Button_7)
        self.Button_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_8.sizePolicy().hasHeightForWidth())
        self.Button_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_8.setFont(font)
        self.Button_8.setObjectName("Button_8")
        self.horizontalLayout_2.addWidget(self.Button_8)
        self.Button_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_9.sizePolicy().hasHeightForWidth())
        self.Button_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_9.setFont(font)
        self.Button_9.setObjectName("Button_9")
        self.horizontalLayout_2.addWidget(self.Button_9)
        self.Button_div = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_div.sizePolicy().hasHeightForWidth())
        self.Button_div.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_div.setFont(font)
        self.Button_div.setObjectName("Button_div")
        self.horizontalLayout_2.addWidget(self.Button_div)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Button_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_4.sizePolicy().hasHeightForWidth())
        self.Button_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_4.setFont(font)
        self.Button_4.setObjectName("Button_4")
        self.horizontalLayout_3.addWidget(self.Button_4)
        self.Button_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_5.sizePolicy().hasHeightForWidth())
        self.Button_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_5.setFont(font)
        self.Button_5.setObjectName("Button_5")
        self.horizontalLayout_3.addWidget(self.Button_5)
        self.Button_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_6.sizePolicy().hasHeightForWidth())
        self.Button_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_6.setFont(font)
        self.Button_6.setObjectName("Button_6")
        self.horizontalLayout_3.addWidget(self.Button_6)
        self.Button_mul = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_mul.sizePolicy().hasHeightForWidth())
        self.Button_mul.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_mul.setFont(font)
        self.Button_mul.setObjectName("Button_mul")
        self.horizontalLayout_3.addWidget(self.Button_mul)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Button_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_1.sizePolicy().hasHeightForWidth())
        self.Button_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_1.setFont(font)
        self.Button_1.setObjectName("Button_1")
        self.horizontalLayout_4.addWidget(self.Button_1)
        self.Button_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_2.sizePolicy().hasHeightForWidth())
        self.Button_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_2.setFont(font)
        self.Button_2.setObjectName("Button_2")
        self.horizontalLayout_4.addWidget(self.Button_2)
        self.Button_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_3.sizePolicy().hasHeightForWidth())
        self.Button_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_3.setFont(font)
        self.Button_3.setObjectName("Button_3")
        self.horizontalLayout_4.addWidget(self.Button_3)
        self.Button_sub = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_sub.sizePolicy().hasHeightForWidth())
        self.Button_sub.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_sub.setFont(font)
        self.Button_sub.setObjectName("Button_sub")
        self.horizontalLayout_4.addWidget(self.Button_sub)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Button_pm = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_pm.sizePolicy().hasHeightForWidth())
        self.Button_pm.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_pm.setFont(font)
        self.Button_pm.setObjectName("Button_pm")
        self.horizontalLayout_5.addWidget(self.Button_pm)
        self.Button_0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_0.sizePolicy().hasHeightForWidth())
        self.Button_0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_0.setFont(font)
        self.Button_0.setObjectName("Button_0")
        self.horizontalLayout_5.addWidget(self.Button_0)
        self.Button_row = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_row.sizePolicy().hasHeightForWidth())
        self.Button_row.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_row.setFont(font)
        self.Button_row.setObjectName("Button_row")
        self.horizontalLayout_5.addWidget(self.Button_row)
        self.Button_sum = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_sum.sizePolicy().hasHeightForWidth())
        self.Button_sum.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_sum.setFont(font)
        self.Button_sum.setObjectName("Button_sum")
        self.horizontalLayout_5.addWidget(self.Button_sum)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Button_parenthesisLeft = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_parenthesisLeft.sizePolicy().hasHeightForWidth())
        self.Button_parenthesisLeft.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_parenthesisLeft.setFont(font)
        self.Button_parenthesisLeft.setObjectName("Button_parenthesisLeft")
        self.horizontalLayout_7.addWidget(self.Button_parenthesisLeft)
        self.Button_parenthesisRight = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_parenthesisRight.sizePolicy().hasHeightForWidth())
        self.Button_parenthesisRight.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_parenthesisRight.setFont(font)
        self.Button_parenthesisRight.setObjectName("Button_parenthesisRight")
        self.horizontalLayout_7.addWidget(self.Button_parenthesisRight)
        self.Button_eq = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_eq.sizePolicy().hasHeightForWidth())
        self.Button_eq.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_eq.setFont(font)
        self.Button_eq.setObjectName("Button_eq")
        self.horizontalLayout_7.addWidget(self.Button_eq)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 682, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.label.setText(_translate("MainWindow", "0"))
        self.Button_sqrt.setText(_translate("MainWindow", "_/x"))
        self.Button_qrt.setText(_translate("MainWindow", "x^y"))
        self.Button_C.setText(_translate("MainWindow", "С"))
        self.Button_del.setText(_translate("MainWindow", "<<"))
        self.Button_7.setText(_translate("MainWindow", "7"))
        self.Button_8.setText(_translate("MainWindow", "8"))
        self.Button_9.setText(_translate("MainWindow", "9"))
        self.Button_div.setText(_translate("MainWindow", "/"))
        self.Button_4.setText(_translate("MainWindow", "4"))
        self.Button_5.setText(_translate("MainWindow", "5"))
        self.Button_6.setText(_translate("MainWindow", "6"))
        self.Button_mul.setText(_translate("MainWindow", "*"))
        self.Button_1.setText(_translate("MainWindow", "1"))
        self.Button_2.setText(_translate("MainWindow", "2"))
        self.Button_3.setText(_translate("MainWindow", "3"))
        self.Button_sub.setText(_translate("MainWindow", "-"))
        self.Button_pm.setText(_translate("MainWindow", "+/-"))
        self.Button_0.setText(_translate("MainWindow", "0"))
        self.Button_row.setText(_translate("MainWindow", ","))
        self.Button_sum.setText(_translate("MainWindow", "+"))
        self.Button_parenthesisLeft.setText(_translate("MainWindow", "("))
        self.Button_parenthesisRight.setText(_translate("MainWindow", ")"))
        self.Button_eq.setText(_translate("MainWindow", "="))