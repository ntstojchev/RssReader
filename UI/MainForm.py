import sys, os.path
import urllib.request
from PyQt4.QtGui import *
from UI.MainFormUI import Ui_MainForm
from UI.FeedForm import FeedForm
from lib.RssFeed import RssFeed as rss_feed

class MainForm(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_MainForm()
        self.ui.setupUi(self)

        self.file_path = 'UI/Links.txt'

        self.ui.btnAdd.clicked.connect(self._btn_add_clicked)
        self.ui.btnDelete.clicked.connect(self._btn_delete_clicked)
        self.ui.btnView.clicked.connect(self._btn_view_feed_clicked)

        self._init_listFeeds_items()

    def _btn_add_clicked(self):
        name = self.ui.txtName.text()
        link = self.ui.txtLink.text()
        if name != "" and link != "":
            with open(self.file_path, 'r') as file:
                rss = name + ',' + link
                if rss not in file.read():
                    file.close()
                    with open(self.file_path, 'a+') as file:
                        file.write(rss + '\n')
                        self.ui.txtName.setText("")
                        self.ui.txtLink.setText("")
                        self._add_list_item(name, link)
                else:
                    self.ui.txtName.setText("")
                    self.ui.txtLink.setText("")
        else:
            self._throw_empty_fields_error()

    def _btn_delete_clicked(self):
        if self.ui.listFeeds.currentItem() != None:
            name = self.ui.listFeeds.currentItem().text()
            link = self.ui.listFeeds.currentItem().toolTip()
            rss = name + ',' + link
            new_feed = ''
            with open(self.file_path, 'r') as file:
                new_feed = file.read().replace(rss + '\n', '')
            with open(self.file_path, 'w+') as file:
                file.write(new_feed)
            self._init_listFeeds_items()
        else:
            self._throw_select_feed_error()
            

    def _btn_view_feed_clicked(self):
        if self.ui.listFeeds.currentItem() != None:
            try:
                feed = rss_feed(urllib.request.urlopen(self.ui.listFeeds.currentItem().toolTip()))
                feed_form = FeedForm(feed)
                feed_form.exec()
            except ValueError:
                self._throw_link_error()
        else:
            self._throw_select_feed_error()

    def _init_listFeeds_items(self):
        self.ui.listFeeds.clear()
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w+') as file:
                pass
        else:
            with open(self.file_path, 'r+') as file:
                for line in file.read().splitlines():
                    feed_info = line.split(',')
                    self._add_list_item(feed_info[0], feed_info[1])

    def _add_list_item(self, name, link):
        item = QListWidgetItem(name)
        item.setToolTip(link)
 
        self.ui.listFeeds.addItem(item)

    def _throw_empty_fields_error(self):
        error = QMessageBox()
        error.setWindowTitle("Error!")
        error.setIcon(QMessageBox.Critical)
        error.setText("Fill the empty fields!")
        error.exec()

    def _throw_select_feed_error(self):
        error = QMessageBox()
        error.setWindowTitle("Error!")
        error.setIcon(QMessageBox.Critical)
        error.setText("Select feed first!")
        error.exec()

    def _throw_link_error(self):
        error = QMessageBox()
        error.setWindowTitle("Error!")
        error.setIcon(QMessageBox.Critical)
        error.setText("Feed link error!")
        error.exec()
