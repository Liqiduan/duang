#coding=utf8
import unittest
import re
import duang

class PareserHtml(unittest.TestCase):
    def checkParse(self, context, result, pre='The', post='Chater'):
        d = duang.Duang(pre, post)
        r = d.parseIndex(context)
        
        self.assertEquals(len(r), len(result))
        for i in range(len(r)):
            self.assertDictEqual(r[i], result[i])

    def testIndexToLink(self):
        context = '<a href="a_href">The 1234 Chater Hello world</a>' 
        result = [{'link':"a_href", 'index':1234, 'title':"Hello world"}]
        self.checkParse(context, result)

    def testIndexToLinkCN(self):
        result = [{ 'link' : r"/8/8208/10024409.html",
                  'index' : 1093, 'title' : r'大结局'}]
        context = r'<dd><a href ="/8/8208/10024409.html">第1093章大结局</a></dd>'
        self.checkParse(context, result, pre = r'第', post = r'章')

    def testMixIndex(self):
        context = '<a href="a_href">abc 1234 Chater Hello world</a>' 
        result = [{'link':"a_href", 'index':1234, 'title':"Hello world"}]
        self.checkParse(context, result, pre = r'((abc)|(The))', post = r'((adf)|(Chater))')

    def testIndexToLinks(self):
        context = r'<dd><a href ="/8/8208/1001231.html">第1094章adsfdsf</a></dd>'
        context = context + r'<dd><a href ="/8/8208/10024409.html">第1093章大结局</a></dd>'
        result = []
        result.append({'link':"/8/8208/1001231.html", 'index':1094, 'title':"adsfdsf"})
        result.append({ 'link' : r"/8/8208/10024409.html", 'index' : 1093, 'title' : r'大结局'})

        self.checkParse(context, result, pre=r'第', post = r'章')

if __name__=='__main__':
    unittest.main()
