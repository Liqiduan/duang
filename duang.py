#coding=utf8
import ssl
import urllib2

import re

class Duang():
    def __init__(self, pre=r'第', post=r'章'):
        self.__pre = pre
        self.__post = post

    def parseIndex(self, str):
        pattern_content = r'[^<>"]'
        pattern_link = r'<a\s*href\s*="(?P<link>%s*)"\s*>' % pattern_content
        pattern_index = r'\s*%s\s*(?P<index>\d+)\s*%s' \
            % (self.__pre, self.__post)
        pattern_title = r'\s*(?P<title>%s*)\s*</a>' % pattern_content
        pattern = pattern_link + pattern_index + pattern_title
        
        r = []
        for i in re.finditer(pattern, str):
            tmp = i.groupdict()
            tmp['index'] = int(tmp['index'])
            r.append(tmp)

        return r

def test():
    link = "test_href"
    index = 1234
    title = "The Title"

    context = '<a href="%s">The %d Chater %s</a>' % (link, index, title)
    return Duang.parseIndex(context)

if __name__=='__main__':
    test()

