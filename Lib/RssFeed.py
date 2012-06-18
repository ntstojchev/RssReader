import xml.etree.ElementTree as etree
from lib.FeedItems import *

class RssFeed:
    '''RssFeed.py demonstraion:
    feed = RssFeed(feed_path);
    feed.version ## Rss version
    feed.title ## Rss title
    feed.link ## Rss link
    feed.description ## Rss description
    feed.pub_date ## Rss publication date
    feed.language ## Rss language
    feed.items_count ## Rss items count
    for item in feed.items:
        item.title ## Item title
        item.description ## Item description
        item.author ## Item author
        item.pub_date ## Item publication date
        item.enclosure ## Item enclosure link
        item.link ## Item link

    sorted_feed = feed.sort_feed_by_title(feed.items, True) ## sorting feed by title
    '''
    
    def __init__(self, path):
        self.root = etree.parse(path).getroot()
        self.version = self._get_feed_version()
        channel = self.root.find('channel')
        self._get_feed_information(channel)

    def _get_feed_version(self):
        return self.root.attrib['version']

    def _get_feed_information(self, channel):
        self.title = self._get_feed_title(channel).strip()
        self.link = self._get_feed_link(channel).strip()
        self.description = self._get_feed_description(channel).strip()
        self.pub_date = self._get_feed_pub_date(channel).strip()
        self.language = self._get_feed_language(channel)
        self.items = self._get_feed_items(channel).items
        self.items_count = len(self.items)

    def _get_feed_title(self, channel):
        return channel.find('title').text

    def _get_feed_link(self, channel):
        return channel.find('link').text

    def _get_feed_description(self, channel):
        return channel.find('description').text

    def _get_feed_pub_date(self, channel):
        result = channel.find('pubDate')
        if result != None:
            return result.text
        else :
            return ""
            
    def _get_feed_language(self, channel):
        result = channel.find('language')
        if result != None:
            return result.text
        else:
            return ""

    def _get_feed_items(self, channel):
        return FeedItems(channel.findall('item'))

    def sort_feed_by_title(self, feed, rev= False):
        return sorted(feed, key=lambda item: item.title, reverse = rev)
