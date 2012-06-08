# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created: Fri May  4 19:59:06 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName(_fromUtf8("MainForm"))
        MainForm.setWindowModality(QtCore.Qt.ApplicationModal)
        MainForm.resize(450, 240)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainForm.sizePolicy().hasHeightForWidth())
        MainForm.setSizePolicy(sizePolicy)
        MainForm.setMinimumSize(QtCore.QSize(450, 240))
        MainForm.setMaximumSize(QtCore.QSize(450, 240))
        self.gridLayoutWidget = QtGui.QWidget(MainForm)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 431, 221))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.listFeeds = QtGui.QListWidget(self.gridLayoutWidget)
        self.listFeeds.setEditTriggers(QtGui.QAbstractItemView.CurrentChanged|QtGui.QAbstractItemView.SelectedClicked)
        self.listFeeds.setWordWrap(True)
        self.listFeeds.setObjectName(_fromUtf8("listFeeds"))
        self.gridLayout.addWidget(self.listFeeds, 3, 1, 1, 4)
        self.btnView = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnView.setObjectName(_fromUtf8("btnView"))
        self.gridLayout.addWidget(self.btnView, 5, 3, 1, 2)
        self.line_2 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 4, 1, 1, 4)
        self.line = QtGui.QFrame(self.gridLayoutWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 2, 1, 1, 4)
        self.lblAdd = QtGui.QLabel(self.gridLayoutWidget)
        self.lblAdd.setObjectName(_fromUtf8("lblAdd"))
        self.gridLayout.addWidget(self.lblAdd, 0, 1, 1, 1)
        self.txtLink = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txtLink.setObjectName(_fromUtf8("txtLink"))
        self.gridLayout.addWidget(self.txtLink, 0, 2, 1, 1)
        self.txtName = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txtName.setObjectName(_fromUtf8("txtName"))
        self.gridLayout.addWidget(self.txtName, 1, 2, 1, 1)
        self.lblName = QtGui.QLabel(self.gridLayoutWidget)
        self.lblName.setObjectName(_fromUtf8("lblName"))
        self.gridLayout.addWidget(self.lblName, 1, 1, 1, 1)
        self.btnAdd = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.gridLayout.addWidget(self.btnAdd, 0, 3, 1, 1)
        self.btnDelete = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnDelete.setObjectName(_fromUtf8("btnDelete"))
        self.gridLayout.addWidget(self.btnDelete, 1, 3, 1, 1)

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QtGui.QApplication.translate("MainForm", "RSS reader", None, QtGui.QApplication.UnicodeUTF8))
        self.btnView.setText(QtGui.QApplication.translate("MainForm", "View feed", None, QtGui.QApplication.UnicodeUTF8))
        self.lblAdd.setText(QtGui.QApplication.translate("MainForm", "RSS link:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblName.setText(QtGui.QApplication.translate("MainForm", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAdd.setText(QtGui.QApplication.translate("MainForm", "Add feed", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDelete.setText(QtGui.QApplication.translate("MainForm", "Delete feed", None, QtGui.QApplication.UnicodeUTF8))

