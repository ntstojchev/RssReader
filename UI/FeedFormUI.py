# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FeedForm.ui'
#
# Created: Sat May  5 15:27:57 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FeedForm(object):
    def setupUi(self, FeedForm):
        FeedForm.setObjectName(_fromUtf8("FeedForm"))
        FeedForm.resize(680, 470)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FeedForm.sizePolicy().hasHeightForWidth())
        FeedForm.setSizePolicy(sizePolicy)
        FeedForm.setMinimumSize(QtCore.QSize(680, 470))
        FeedForm.setMaximumSize(QtCore.QSize(680, 470))
        self.gridLayoutWidget = QtGui.QWidget(FeedForm)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 661, 451))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lblVersion = QtGui.QLabel(self.gridLayoutWidget)
        self.lblVersion.setWordWrap(True)
        self.lblVersion.setObjectName(_fromUtf8("lblVersion"))
        self.gridLayout.addWidget(self.lblVersion, 5, 0, 1, 1)
        self.lblLanguage = QtGui.QLabel(self.gridLayoutWidget)
        self.lblLanguage.setObjectName(_fromUtf8("lblLanguage"))
        self.gridLayout.addWidget(self.lblLanguage, 5, 1, 1, 1)
        self.lblTitle = QtGui.QLabel(self.gridLayoutWidget)
        self.lblTitle.setWordWrap(True)
        self.lblTitle.setObjectName(_fromUtf8("lblTitle"))
        self.gridLayout.addWidget(self.lblTitle, 0, 0, 1, 1)
        self.lblItems = QtGui.QLabel(self.gridLayoutWidget)
        self.lblItems.setObjectName(_fromUtf8("lblItems"))
        self.gridLayout.addWidget(self.lblItems, 5, 2, 1, 1)
        self.btnSortByTitle = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnSortByTitle.setObjectName(_fromUtf8("btnSortByTitle"))
        self.gridLayout.addWidget(self.btnSortByTitle, 5, 3, 1, 1)
        self.txtFeedItems = QtGui.QTextEdit(self.gridLayoutWidget)
        self.txtFeedItems.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.txtFeedItems.setObjectName(_fromUtf8("txtFeedItems"))
        self.gridLayout.addWidget(self.txtFeedItems, 3, 0, 1, 4)
        self.line = QtGui.QFrame(self.gridLayoutWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 4, 0, 1, 4)
        self.line_2 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 2, 0, 1, 4)
        self.lblDescription = QtGui.QLabel(self.gridLayoutWidget)
        self.lblDescription.setWordWrap(True)
        self.lblDescription.setObjectName(_fromUtf8("lblDescription"))
        self.gridLayout.addWidget(self.lblDescription, 1, 0, 1, 4)
        self.lblLink = QtGui.QLabel(self.gridLayoutWidget)
        self.lblLink.setObjectName(_fromUtf8("lblLink"))
        self.gridLayout.addWidget(self.lblLink, 0, 2, 1, 2)

        self.retranslateUi(FeedForm)
        QtCore.QMetaObject.connectSlotsByName(FeedForm)

    def retranslateUi(self, FeedForm):
        FeedForm.setWindowTitle(QtGui.QApplication.translate("FeedForm", "Feed", None, QtGui.QApplication.UnicodeUTF8))
        self.lblVersion.setText(QtGui.QApplication.translate("FeedForm", "Version: ", None, QtGui.QApplication.UnicodeUTF8))
        self.lblLanguage.setText(QtGui.QApplication.translate("FeedForm", "Language: ", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTitle.setText(QtGui.QApplication.translate("FeedForm", "Title: ", None, QtGui.QApplication.UnicodeUTF8))
        self.lblItems.setText(QtGui.QApplication.translate("FeedForm", "Items: ", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSortByTitle.setText(QtGui.QApplication.translate("FeedForm", "Sort by title", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDescription.setText(QtGui.QApplication.translate("FeedForm", "Description: ", None, QtGui.QApplication.UnicodeUTF8))
        self.lblLink.setText(QtGui.QApplication.translate("FeedForm", "Link: ", None, QtGui.QApplication.UnicodeUTF8))

