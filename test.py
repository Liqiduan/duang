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

if __name__=='__main__':
    unittest.main()
