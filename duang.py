import ssl
import urllib2

import re

class Duang():
    @staticmethod
    def parseIndex(str):
        pattern_link = r'<a\s*href="(?P<link>.*)"\s*>'
        pattern_index = r'\s*The\s*(?P<index>\d+)\s*Chater'
        pattern_title = r'\s*(?P<title>.*)\s*</a>'
        pattern = pattern_link + pattern_index + pattern_title

        item = re.search(pattern, str)
        r = item.groupdict()
        r['index'] = int(r['index'])

        return r

def test():
    link = "test_href"
    index = 1234
    title = "The Title"

    context = '<a href="%s">The %d Chater %s</a>' % (link, index, title)
    return Duang.parseIndex(context)

if __name__=='__main__':
    test()

