# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created: Fri Jun  8 21:48:52 2012
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
        MainForm.resize(450, 250)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainForm.sizePolicy().hasHeightForWidth())
        MainForm.setSizePolicy(sizePolicy)
        MainForm.setMinimumSize(QtCore.QSize(450, 250))
        MainForm.setMaximumSize(QtCore.QSize(450, 250))
        self.formLayout = QtGui.QFormLayout(MainForm)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.line_2 = QtGui.QFrame(MainForm)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 4, 0, 1, 4)
        self.line = QtGui.QFrame(MainForm)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 0, 1, 4)
        self.line_3 = QtGui.QFrame(MainForm)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 6, 0, 1, 4)
        self.btnExport = QtGui.QPushButton(MainForm)
        self.btnExport.setObjectName(_fromUtf8("btnExport"))
        self.gridLayout.addWidget(self.btnExport, 0, 1, 1, 1)
        self.txtLink = QtGui.QLineEdit(MainForm)
        self.txtLink.setObjectName(_fromUtf8("txtLink"))
        self.gridLayout.addWidget(self.txtLink, 2, 1, 1, 3)
        self.btnView = QtGui.QPushButton(MainForm)
        self.btnView.setObjectName(_fromUtf8("btnView"))
        self.gridLayout.addWidget(self.btnView, 7, 3, 1, 1)
        self.lblName = QtGui.QLabel(MainForm)
        self.lblName.setObjectName(_fromUtf8("lblName"))
        self.gridLayout.addWidget(self.lblName, 3, 0, 1, 1)
        self.lblAdd = QtGui.QLabel(MainForm)
        self.lblAdd.setObjectName(_fromUtf8("lblAdd"))
        self.gridLayout.addWidget(self.lblAdd, 2, 0, 1, 1)
        self.txtName = QtGui.QLineEdit(MainForm)
        self.txtName.setObjectName(_fromUtf8("txtName"))
        self.gridLayout.addWidget(self.txtName, 3, 1, 1, 3)
        self.rbText = QtGui.QRadioButton(MainForm)
        self.rbText.setObjectName(_fromUtf8("rbText"))
        self.gridLayout.addWidget(self.rbText, 7, 1, 1, 1)
        self.lblView = QtGui.QLabel(MainForm)
        self.lblView.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblView.setObjectName(_fromUtf8("lblView"))
        self.gridLayout.addWidget(self.lblView, 7, 0, 1, 1)
        self.btnDelete = QtGui.QPushButton(MainForm)
        self.btnDelete.setObjectName(_fromUtf8("btnDelete"))
        self.gridLayout.addWidget(self.btnDelete, 0, 3, 1, 1)
        self.rbHtml = QtGui.QRadioButton(MainForm)
        self.rbHtml.setObjectName(_fromUtf8("rbHtml"))
        self.gridLayout.addWidget(self.rbHtml, 7, 2, 1, 1)
        self.btnImport = QtGui.QPushButton(MainForm)
        self.btnImport.setObjectName(_fromUtf8("btnImport"))
        self.gridLayout.addWidget(self.btnImport, 0, 0, 1, 1)
        self.btnAdd = QtGui.QPushButton(MainForm)
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.gridLayout.addWidget(self.btnAdd, 0, 2, 1, 1)
        self.listFeeds = QtGui.QListWidget(MainForm)
        self.listFeeds.setEditTriggers(QtGui.QAbstractItemView.CurrentChanged|QtGui.QAbstractItemView.SelectedClicked)
        self.listFeeds.setWordWrap(True)
        self.listFeeds.setObjectName(_fromUtf8("listFeeds"))
        self.gridLayout.addWidget(self.listFeeds, 5, 0, 1, 4)
        self.formLayout.setLayout(0, QtGui.QFormLayout.SpanningRole, self.gridLayout)

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QtGui.QApplication.translate("MainForm", "RSS reader", None, QtGui.QApplication.UnicodeUTF8))
        self.btnExport.setText(QtGui.QApplication.translate("MainForm", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.btnView.setText(QtGui.QApplication.translate("MainForm", "View feed", None, QtGui.QApplication.UnicodeUTF8))
        self.lblName.setText(QtGui.QApplication.translate("MainForm", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblAdd.setText(QtGui.QApplication.translate("MainForm", "RSS link:", None, QtGui.QApplication.UnicodeUTF8))
        self.rbText.setText(QtGui.QApplication.translate("MainForm", "Text", None, QtGui.QApplication.UnicodeUTF8))
        self.lblView.setText(QtGui.QApplication.translate("MainForm", "View in:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDelete.setText(QtGui.QApplication.translate("MainForm", "Delete feed", None, QtGui.QApplication.UnicodeUTF8))
        self.rbHtml.setText(QtGui.QApplication.translate("MainForm", "HTML", None, QtGui.QApplication.UnicodeUTF8))
        self.btnImport.setText(QtGui.QApplication.translate("MainForm", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAdd.setText(QtGui.QApplication.translate("MainForm", "Add feed", None, QtGui.QApplication.UnicodeUTF8))

