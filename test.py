#coding=utf8
import unittest

import duang

class PareserHtml(unittest.TestCase):
    def checkParse(self, context, result, pre='The', post='Chater'):
        d = duang.Duang(pre, post)
        r = d.parseIndex(context)
        
        for i in r.items():
            self.assertEquals(r[i[0]], i[1])

    def testIndexToLink(self):
        context = '<a href="a_href">The 1234 Chater Hello world</a>' 
        result = {'link':"a_href", 'index':1234, 'title':"Hello world"}
        self.checkParse(context, result)

    def testIndexToLinkCN(self):
        result = { 'link' : r"/8/8208/10024409.html",
                  'index' : 1093, 'title' : r'大结局'}
        context = r'<dd><a href ="/8/8208/10024409.html">第1093章大结局</a></dd>'
        self.checkParse(context, result, pre = r'第', post = r'章')

if __name__=='__main__':
    unittest.main()
