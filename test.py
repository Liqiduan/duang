#coding=utf8
import unittest

import duang

class PareserHtml(unittest.TestCase):

    def testIndexToLink(self):
        link = "test_href"
        index = 1234
        title = "The Title"

        context = '<a href="%s">The %d Chater %s</a>' % (link, index, title)
        d = duang.Duang()
        r = d.parseIndex(context)
        
        self.assertEquals(r['link'], link)
        self.assertEquals(r['index'], index)
        self.assertEquals(r['title'], title)

    def testIndexToLinkCN(self):
        link = r"/8/8208/10024409.html"
        index = 1093
        title = r'大结局'
        context = r'<dd><a href ="/8/8208/10024409.html">第1093章大结局</a></dd>'
        d = duang.Duang(pre = r'第', post = r'章')
        r = d.parseIndex(context)
        
        self.assertEquals(r['link'], link)
        self.assertEquals(r['index'], index)
        self.assertEquals(r['title'], title)

if __name__=='__main__':
    unittest.main()
