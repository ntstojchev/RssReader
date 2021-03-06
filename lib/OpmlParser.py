import xml.etree.ElementTree as etree
from datetime import datetime

class OpmlParser:
    def __init__(self):
        pass
    
    def parse(self, path):
        root = etree.parse(path).getroot()
        body = root.find('body')
        outline = body.find('outline')
        self.outlines = outline.findall('outline')
        self.feeds = self._get_feeds()

    def _get_feeds(self):
        feeds = []
        for outline in self.outlines:
            feed = str(outline.attrib['title'] + ', ' + outline.attrib['xmlUrl'])
            feeds.append(feed)
        return feeds

    def build_opml(self, rss_feeds):
        opml = ''
        opml += self._generate_head()
        opml += self._generate_body(rss_feeds)
       
        return opml

    def _generate_head(self):
        head = ''
        head += '<opml version="1.1">\n'
        head += '   <head>\n'
        head += '       <title>\n'
        head += '           Generated by RssReader: ' + str(datetime.now()) + '\n'
        head += '       </title>\n'
        head += '   </head>\n'
        return head

    def _generate_body(self, rss_feeds):
        body = ''
        body += '   <body>\n'
        body += '       <outline text="RssFeeds">\n'
        body += self._generate_outline(rss_feeds)
        body += '       </outline>\n'
        body += '   </body>\n'
        body += '</opml>'
        return body

    def _generate_outline(self, rss_feeds):
        outlines = ''
        for rss_feed in rss_feeds.splitlines():
            if rss_feed != '':
                feed = rss_feed.split(', ')
                outlines += '           <outline title="' + str(feed[0]) + '" xmlUrl="' + str(feed[1]) + '"/>\n'

        return outlines

