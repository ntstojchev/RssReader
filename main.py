import sys
from PyQt4 import QtGui, QtCore
from UI.MainForm import *
from lib.RssFeed import RssFeed as rss_feed

def main():
    app = QtGui.QApplication(sys.argv)

    main_form = MainForm()
    main_form.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
