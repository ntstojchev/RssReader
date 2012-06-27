import unittest
import xml.etree.ElementTree as etree
from lib.RssFeed import RssFeed
from lib.FeedItem import FeedItem
from lib.OpmlParser import OpmlParser

class RssFeedTest(unittest.TestCase):
    def setUp(self):
        self.rss_feed = RssFeed('testFeed.xml')
        self.test_feed = etree.parse('testFeed.xml').getroot()
        self.test_feed_channel = self.test_feed.find('channel')
    
    def test_rss_feed(self):
        self.assertEqual(self.rss_feed.version, self.test_feed.attrib['version'])
        self.assertEqual(self.rss_feed.title, self.test_feed_channel.find('title').text)
        self.assertEqual(self.rss_feed.link, self.test_feed_channel.find('link').text)
        self.assertEqual(self.rss_feed.description, self.test_feed_channel.find('description').text)
        self.assertEqual(self.rss_feed.pub_date, self.test_feed_channel.find('pubDate').text)
        self.assertEqual(self.rss_feed.language, self.test_feed_channel.find('language').text)
        self.assertEqual(self.rss_feed.items_count, len(self.test_feed_channel.findall('item')))

    def test_rss_items(self):
        test_feed_items = self.test_feed_channel.findall('item')
        self.assertEqual(self.rss_feed.items_count, len(test_feed_items))
        counter = 0
        for item in self.rss_feed.items:
            self.assertEqual(item.title, test_feed_items[counter].find('title').text)
            self.assertEqual(item.description, test_feed_items[counter].find('description').text)
            self.assertEqual(item.author, test_feed_items[counter].find('author').text)
            self.assertEqual(item.pub_date, test_feed_items[counter].find('pubDate').text)
            self.assertEqual(item.enclosure, test_feed_items[counter].find('enclosure').attrib['url'])
            self.assertEqual(item.link, test_feed_items[counter].find('link').text)
            counter += 1

    def test_rss_item(self):
        test_feed_items = self.test_feed_channel.findall('item')
        test_feed_item = test_feed_items[0]
        feed_item = FeedItem(test_feed_item)
        self.assertEqual(feed_item.title, test_feed_item.find('title').text)
        self.assertEqual(feed_item.description, test_feed_item.find('description').text)
        self.assertEqual(feed_item.author, test_feed_item.find('author').text)
        self.assertEqual(feed_item.pub_date, test_feed_item.find('pubDate').text)
        self.assertEqual(feed_item.enclosure, test_feed_item.find('enclosure').attrib['url'])
        self.assertEqual(feed_item.link, test_feed_item.find('link').text)

    def test_invalid_opml_feed(self):
        parser = OpmlParser()
        self.assertRaises(KeyError, parser.parse, 'invalid_opml.opml')

    def test_opml_items(self):
        parser = OpmlParser()
        parser.parse('export_feeds_opml.opml')
        self.assertEqual(len(parser.feeds), 2)

    def test_opml_item(self):
        parser = OpmlParser()
        parser.parse('export_feeds_opml.opml')
        splited_item = parser.feeds[0].split(', ')
        self.assertEqual('PC Mania', splited_item[0])
        self.assertEqual('http://pcmania.bg/feed.php', splited_item[1])
        		
if __name__ == "__main__":
    unittest.main()
