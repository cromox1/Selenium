__author__ = 'cromox'
'''
get ALL tag_names on specific page of browser.
Example how to run :

$ python3 TAGNAME_ALL_PAGESOURCE_Req_GET_OnPage.py
Python Version = 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)]

Put URL = mengkome.pythonanywhere.com
URL = https://mengkome.pythonanywhere.com

(will give the output as follow)

List of tag_name ( count) :
1) html = 1
2) head = 1
3) title = 1
4) link = 3
5) meta = 2
6) body = 1
7) div = 9
8) h1 = 1
9) a = 1
10) form = 1
11) input = 5
12) label = 3
13) br = 1

Total tag_name = 30

(This is using OOP (Object-Oriented Programming) with simple Polymorphism style)
'''
from sys import version as pythonversion
from html.parser import HTMLParser
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
        self.dicttagname = {}

    def handle_starttag(self, tag, attrs):
        if tag in self.dicttagname:
            self.dicttagname[tag] += 1
        else:
            self.dicttagname[tag] = 1

    def handle_endtag(self, tag):
        totalall = 0
        if tag == list(self.dicttagname.keys())[0]:
            alltags = self.dicttagname
            alltagkeys = list(alltags.keys())
            print('List of tag_name ( count) :')
            for i in range(len(alltagkeys)):
                print(str(i+1) + ') ' + str(alltagkeys[i]) + ' = ' + str(alltags[alltagkeys[i]]))
                totalall = totalall + alltags[alltagkeys[i]]
            print()
            print('Total tag_name = ' + str(totalall))

print()
data1 = req_get(base_url)._content
data2 = data1.decode("ascii", 'ignore')
ReadableHTML().feed(data2)