import unittest
import xml.etree.ElementTree as etree
from lib.RssFeed import RssFeed
from lib.FeedItem import FeedItem

class RssFeedTest(unittest.TestCase):
    def test_rss_feed(self):
        rss_feed = RssFeed('testFeed.xml')
        test_feed = etree.parse('testFeed.xml').getroot()
        test_feed_channel = test_feed.find('channel')
        self.assertEqual(rss_feed.version, test_feed.attrib['version'])
        self.assertEqual(rss_feed.title, test_feed_channel.find('title').text)
        self.assertEqual(rss_feed.link, test_feed_channel.find('link').text)
        self.assertEqual(rss_feed.description, test_feed_channel.find('description').text)
        self.assertEqual(rss_feed.pub_date, test_feed_channel.find('pubDate').text)
        self.assertEqual(rss_feed.language, test_feed_channel.find('language').text)
        self.assertEqual(rss_feed.items_count, len(test_feed_channel.findall('item')))

    def test_rss_items(self):
        rss_feed = RssFeed('testFeed.xml')
        test_feed = etree.parse('testFeed.xml').getroot()
        test_feed_channel = test_feed.find('channel')
        test_feed_items = test_feed_channel.findall('item')
        self.assertEqual(rss_feed.items_count, len(test_feed_items))
        counter = 0
        for item in rss_feed.items:
            self.assertEqual(item.title, test_feed_items[counter].find('title').text)
            self.assertEqual(item.description, test_feed_items[counter].find('description').text)
            self.assertEqual(item.author, test_feed_items[counter].find('author').text)
            self.assertEqual(item.pub_date, test_feed_items[counter].find('pubDate').text)
            self.assertEqual(item.enclosure, test_feed_items[counter].find('enclosure').attrib['url'])
            self.assertEqual(item.link, test_feed_items[counter].find('link').text)
            counter += 1

    def test_rss_item(self):
        rss_feed = RssFeed('testFeed.xml')
        test_feed = etree.parse('testFeed.xml').getroot()
        test_feed_channel = test_feed.find('channel')
        test_feed_items = test_feed_channel.findall('item')
        test_feed_item = test_feed_items[0]
        feed_item = FeedItem(test_feed_item)
        self.assertEqual(feed_item.title, test_feed_item.find('title').text)
        self.assertEqual(feed_item.description, test_feed_item.find('description').text)
        self.assertEqual(feed_item.author, test_feed_item.find('author').text)
        self.assertEqual(feed_item.pub_date, test_feed_item.find('pubDate').text)
        self.assertEqual(feed_item.enclosure, test_feed_item.find('enclosure').attrib['url'])
        self.assertEqual(feed_item.link, test_feed_item.find('link').text)

		
if __name__ == "__main__":
    unittest.main()
