from lib.FeedItem import *

class FeedItems:
    def __init__(self, feed_items):
        self.items = self._get_items(feed_items)
        self.length = len(feed_items)
        
    def _get_items(self, feed_items):
        items = []
        for item in feed_items:
            items.append(FeedItem(item))

        return items
