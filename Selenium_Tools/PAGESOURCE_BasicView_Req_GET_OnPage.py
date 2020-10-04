__author__ = 'cromox'
'''
to show the PageSource view of specific page or site.
Example how to run :

$ python PAGESOURCE_BasicView_Req_GET_OnPage.py
Python Version = 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)]

Put URL = mengkome.pythonanywhere.com
URL = https://mengkome.pythonanywhere.com

(will give the output - in Basic View style)

(This is using OOP (Object-Oriented Programming) with simple Polymorphism style of the Requests's GET output)
'''
from sys import version as pythonversion
from html.parser import HTMLParser
from html.entities import name2codepoint
from requests.api import get as req_get

### GET python version
print('Python Version = ' + pythonversion)
print()
base_url = input('Put URL = ')
# base_url = 'mengkome.pythonanywhere.com'
if base_url.split('://')[0] == base_url and base_url is not None:
    base_url = 'https://' + base_url
print('URL = ' + base_url)

class ReadableHTML(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.maxword = 150

    def handle_starttag(self, tag, attrs):
        print("START tag: " + str(tag))
        for attr in attrs:
            print("    Attr : " + str(attr))
        return 'START'

    def handle_endtag(self, tag):
        print("END tag  : " + str(tag))
        return 'END'

    def handle_data(self, data):
        if len(data) > self.maxword:
            endone = ' ...(cont)...'
        else:
            endone = ''
        print("    Data : " + str(data.replace('\n', '\ENTER\ ').replace('  ', ' ').replace('   ', ' ')[:self.maxword]) + endone)

    def handle_comment(self, data):
        if len(data) > self.maxword:
            endone = ' ...(cont)...'
        else:
            endone = ''
        print(" Comment : " + str(data.replace('\n', '\ENTER\ ').replace('  ', ' ').replace('   ', ' ')[:self.maxword]) + endone)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent: " + str(c))

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print(" Num ent : " + str(c))

    def handle_decl(self, data):
        if len(data) > self.maxword:
            endone = ' ...(cont)...'
        else:
            endone = ''
        print("DECL     : " + str(data.replace('\n', '\ENTER\ ').replace('  ', ' ').replace('   ', ' ')[:self.maxword]) + endone)

print()
data1 = req_get(base_url)._content
# data2 = data1.decode("cp1250", 'ignore')
data2 = data1.decode("ascii", 'ignore')
ReadableHTML().feed(data2)
