class FeedItem:
    def __init__(self, item):
        self.title = self._get_item_title(item).strip()
        self.description = self._get_item_description(item).strip()
        self.link = self._get_item_link(item).strip()
        self.author = self._get_item_author(item).strip()
        self.enclosure = self._get_item_enclosure(item).strip()
        self.pub_date = self._get_item_pub_date(item)

    def _get_item_title(self, item):
        return item.find('title').text

    def _get_item_description(self, item):
        description = item.find('description')
        if description != None:
            return description.text
        else:
            return ""

    def _get_item_link(self, item):
        link = item.find('link')
        if link != None:
            return link.text
        else:
            return ""

    def _get_item_author(self, item):
        author = item.find('author')
        if author != None:
            return author.text
        else:
            return ""

    def _get_item_enclosure(self, item):
        enclosure = item.find('enclosure')
        if enclosure != None:
            return enclosure.attrib['url']
        else:
            return ""

    def _get_item_pub_date(self, item):
        pub_date = item.find('pubDate')
        if pub_date != None:
            return pub_date.text
        else:
            return ""
