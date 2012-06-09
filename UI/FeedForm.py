import sys
from PyQt4.QtGui import *
from UI.FeedFormUI import Ui_FeedForm
from Lib.RssFeed import RssFeed as rss_feed

class FeedForm(QDialog):
    def __init__(self, feed):
        QDialog.__init__(self)

        self.ui = Ui_FeedForm()
        self.ui.setupUi(self)

        self.feed = feed
        self.ui.btnSortByTitle.clicked.connect(self._btn_sort_by_title_clicked)

        self._init_feed_info()

    def _btn_sort_by_title_clicked(self):
        sorted_feed = self.feed.sort_feed_by_title(self.feed.items, True)
        self.feed.items = sorted_feed
        self._init_feed_items()
        
    
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
        for item in self.feed.items:
            self.ui.txtFeedItems.append(self._to_str(item))
        self._set_cursor_position()

    def _set_cursor_position(self):
        cursor = self.ui.txtFeedItems.textCursor()
        cursor.movePosition(QTextCursor.Start, QTextCursor.MoveAnchor)
        self.ui.txtFeedItems.setTextCursor(cursor)
        
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
            #item += 'Link: <a href=\"' + str(feed_item.link) + '\"> Click </a>\n'
            item += 'Link: ' + str(feed_item.link) + '\n'
        else:
            item += 'Link: ' + 'N/A' + '\n'
        return item
