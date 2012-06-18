import sys, os.path
import urllib.request
from PyQt4.QtGui import *
from ui.MainFormUI import Ui_MainForm
from ui.FeedForm import FeedForm
from lib.RssFeed import RssFeed as rss_feed
from lib.OpmlParser import OpmlParser

class MainForm(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_MainForm()
        self.ui.setupUi(self)

        self.file_path = 'feeds/Links.txt'

        self.ui.btnAdd.clicked.connect(self._btn_add_clicked)
        self.ui.btnDelete.clicked.connect(self._btn_delete_clicked)
        self.ui.btnView.clicked.connect(self._btn_view_feed_clicked)
        self.ui.btnImport.clicked.connect(self._btn_import_clicked)
        self.ui.btnExport.clicked.connect(self._btn_export_clicked)
        self.ui.rbText.setChecked(True)

        self._init_listFeeds_items()

    def _btn_add_clicked(self):
        name = self.ui.txtName.text()
        link = self.ui.txtLink.text()
        if name != "" and link != "":
            with open(self.file_path, 'r') as file:
                rss = name + ', ' + link
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
            rss = name + ', ' + link
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
                feed_form = FeedForm(feed, self.ui.rbHtml.isChecked())
                feed_form.exec()
            except ValueError:
                self._throw_link_error()
        else:
            self._throw_select_feed_error()

    def _btn_import_clicked(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Text files (*.txt), OPML Files (*.opml)")
        
        if file_dialog.exec():
            selected_file = file_dialog.selectedFiles()[0]
            if os.path.exists(selected_file):
                if '.txt' in selected_file:
                    self._import_txt(selected_file)
                if '.opml' in selected_file:
                    self._import_opml(selected_file)
            else:
                self._throw_file_error()

        self._init_listFeeds_items()

    def _import_txt(self, selected_file):
        with open(selected_file, 'r') as import_file:
            with open(self.file_path, 'a+') as links_file:
                for line in import_file.read().splitlines():
                    links_file.write(line + '\n')

    def _import_opml(self, selected_file):
        opml_parser = OpmlParser()
        opml_parser.parse(selected_file)
        with open(self.file_path, 'a+') as links_file:
            for feed in opml_parser.feeds:
                links_file.write(feed + '\n')
        
    def _btn_export_clicked(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilters(["Text files (*.txt)", "OPML files (*.opml)"])

        if file_dialog.exec():
            selected_file = file_dialog.selectedFiles()[0]
            selected_name_filter = file_dialog.selectedNameFilter()
            
            if os.path.exists(selected_file):
                if self._confirmation_dialog() == QMessageBox.Ok:
                    if '.txt' in selected_file:
                        self._export_txt(selected_file)
                    if '.opml' in selected_file:
                        self._export_opml(selected_file)                   
            else:
                if '.txt' in selected_name_filter:
                    self._export_new_txt(selected_file)
                if '.opml' in selected_name_filter:
                    self._export_new_opml(selected_file)
                

    def _export_txt(self, selected_file):
        with open(selected_file, 'w') as new_file:
            with open(self.file_path, 'r') as links_file:
                new_file.write(links_file.read())

    def _export_new_txt(self, selected_file):
        with open(selected_file + '.txt', 'w') as new_file:
            with open(self.file_path, 'r') as links_file:
                new_file.write(links_file.read())

    def _export_opml(self, selected_file):
        opml_parser = OpmlParser()       
        with open(selected_file, 'w') as new_file:
            with open(self.file_path, 'r') as links_file:
                links = links_file.read()
                opml = opml_parser.build_opml(links)
                new_file.write(opml)

    def _export_new_opml(self, selected_file):
        opml_parser = OpmlParser()       
        with open(selected_file + '.opml', 'w') as new_file:
            with open(self.file_path, 'r') as links_file:
                links = links_file.read()
                opml = opml_parser.build_opml(links)
                new_file.write(opml)

    def _init_listFeeds_items(self):
        self.ui.listFeeds.clear()
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w+') as file:
                pass
        else:
            with open(self.file_path, 'r+') as file:
                for line in file.read().splitlines():
                    feed_info = line.split(', ')
                    if len(feed_info) > 1:
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

    def _throw_file_error(self):
        error = QMessageBox()
        error.setWindowTitle("Error!")
        error.setIcon(QMessageBox.Critical)
        error.setText("File doesn`t exist!")
        error.exec()

    def _confirmation_dialog(self):
        confirmation = QMessageBox()
        confirmation.setWindowTitle("Are you sure?")
        confirmation.setIcon(QMessageBox.Question)
        confirmation.setText("This file will be overwritten. Are you sure?")
        confirmation.addButton(QMessageBox.Cancel)
        confirmation.addButton(QMessageBox.Ok)
        return confirmation.exec()
