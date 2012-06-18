import sys, os.path
from PyQt4.QtGui import *
from ui.FeedFormUI import Ui_FeedForm
from lib.RssFeed import RssFeed as rss_feed

class FeedForm(QDialog):
    def __init__(self, feed, html_checked):
        QDialog.__init__(self)

        self.ui = Ui_FeedForm()
        self.ui.setupUi(self)

        self.feed = feed
        self.html_checked = html_checked
        self.ui.btnSortByTitle.clicked.connect(self._btn_sort_by_title_clicked)
        self.ui.btnExport.clicked.connect(self._btn_export_clicked)

        self._init_feed_info()

    def _btn_sort_by_title_clicked(self):
        sorted_feed = self.feed.sort_feed_by_title(self.feed.items, True)
        self.feed.items = sorted_feed
        self._init_feed_items()

    def _btn_export_clicked(self):
        file_dialog = QFileDialog()
        if self.html_checked:
            file_dialog.setNameFilter("HTML files (*.html)")

            if file_dialog.exec():
                selected_file = file_dialog.selectedFiles()[0]
                
                if os.path.exists(selected_file):
                    if self._confirmation_dialog() == QMessageBox.Ok:
                        with open(selected_file, 'w') as new_file:
                            new_file.write(self.ui.txtFeedItems.toHtml())
                else:
                    with open(selected_file + '.html', 'w') as new_file:
                        new_file.write(self.ui.txtFeedItems.toHtml())
        else:
            file_dialog.setNameFilter("Text files (*.txt)")

            if file_dialog.exec():
                selected_file = file_dialog.selectedFiles()[0]
                
                if os.path.exists(selected_file):
                    if self._confirmation_dialog() == QMessageBox.Ok:
                        with open(selected_file, 'w') as new_file:
                            new_file.write(self.ui.txtFeedItems.toPlainText())
                else:
                    with open(selected_file + '.txt', 'w') as new_file:
                        new_file.write(self.ui.txtFeedItems.toPlainText())
    
    def _init_feed_info(self):
        self.ui.lblTitle.setText(self.ui.lblTitle.text() + self.feed.title)
        self.ui.lblDescription.setText(self.ui.lblDescription.text() + self.feed.description)
        self.ui.lblVersion.setText(self.ui.lblVersion.text() + self.feed.version)
        self.ui.lblLanguage.setText(self.ui.lblLanguage.text() + self.feed.language)
        self.ui.lblItems.setText(self.ui.lblItems.text() + str(self.feed.items_count))
        self.ui.lblLink.setText(self.ui.lblLink.text() + self.feed.link)
        self._init_feed_items()
        

    def _init_feed_items(self):
        self.ui.txtFeedItems.clear()

        if self.html_checked:
            for item in self.feed.items:
                self.ui.txtFeedItems.append(self._to_html(item))
        else:
            for item in self.feed.items:
                self.ui.txtFeedItems.append(self._to_str(item))

        self._set_cursor_position()

    def _set_cursor_position(self):
        cursor = self.ui.txtFeedItems.textCursor()
        cursor.movePosition(QTextCursor.Start, QTextCursor.MoveAnchor)
        self.ui.txtFeedItems.setTextCursor(cursor)
        
    def _to_html(self, feed_item):
        item = ''
        if feed_item.title != '':
            item += '<h1>' + str(feed_item.title) + '</h1>'
        else:
            item += '<h1> ' + 'N/A' + '</h1>'
        if feed_item.pub_date != '':
            item += 'PubDate: ' + str(feed_item.pub_date) + '<br />'
        else:
            item += 'PubDate: ' + 'N/A' + '<br />'
        if feed_item.author != '':
            item += 'Author: ' + str(feed_item.author) + ''
        else:
            item += 'Author: ' + 'N/A' + ''
        if feed_item.description != '':
            item += '<p> ' + str(feed_item.description) + '<br />'
        else:
            item += 'Desc: ' + 'N/A' + '<br />'      
        if feed_item.enclosure != '':
            item += '<img src="' + str(feed_item.enclosure) + '" height="70" width="70" /><br />'
        else:
            item += 'Enclosure: ' + 'N/A' + '<br />'
        if feed_item.link != '':
            item += '<a href= "' + str(feed_item.link) + '">Feed link<a/><br />'
        else:
            item += 'Link: ' + 'N/A' + '<br />'
            
        return item
    
    def _to_str(self, feed_item):
        item = ''
        item += '-----------------------' + '\n'
        if feed_item.title != '':
            item += 'Title: ' + str(feed_item.title) + '\n'
        else:
            item += 'Title: ' + 'N/A' + '\n'
        if feed_item.description != '':
            item += 'Desc: ' + str(feed_item.description) + '\n'
        else:
            item += 'Desc: ' + 'N/A' + '\n'
        if feed_item.author != '':
            item += 'Author: ' + str(feed_item.author) + '\n'
        else:
            item += 'Author: ' + 'N/A' + '\n'
        if feed_item.pub_date != '':
            item += 'PubDate: ' + str(feed_item.pub_date) + '\n'
        else:
            item += 'PubDate: ' + 'N/A' + '\n'
        if feed_item.enclosure != '':
            item += 'Enclosure: ' + str(feed_item.enclosure) + '\n'
        else:
            item += 'Enclosure: ' + 'N/A' + '\n'
        if feed_item.link != '':
            item += 'Link: ' + str(feed_item.link) + '\n'
        else:
            item += 'Link: ' + 'N/A' + '\n'
            
        return item

    def _confirmation_dialog(self):
        confirmation = QMessageBox()
        confirmation.setWindowTitle("Are you sure?")
        confirmation.setIcon(QMessageBox.Question)
        confirmation.setText("This file will be overwritten. Are you sure?")
        confirmation.addButton(QMessageBox.Cancel)
        confirmation.addButton(QMessageBox.Ok)
        return confirmation.exec()
