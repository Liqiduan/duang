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
        context = r' <dd><a href ="/8/8208/10024409.html">第1093章大结局</a></dd> <dd><a href ="/8/8208/10024408.html">第1092章杨川（10）</a></dd> <dd><a href ="/8/8208/10024407.html">第1091章杨川（9）</a></dd>'
        result = [
            {'link':"/8/8208/10024409.html", 'index':1093, 'title':'大结局'},
            {'link':"/8/8208/10024408.html", 'index':1092, 'title':r'杨川（10）'},
            {'link':"/8/8208/10024407.html", 'index':1091, 'title':r'杨川（9）'} ]

        self.checkParse(context, result, pre=r'第', post = r'章')

    def testParseIndexHtml(self):
        with open("test_index.html", "r") as f:
            context = f.read()

        d = duang.Duang()
        s = d.parseIndex(context)
    

if __name__=='__main__':
    unittest.main()
