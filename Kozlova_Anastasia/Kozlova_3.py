#расширение списка оценочной лексики посредством извлечения синонимов

import urllib
import lxml.html as html
from  lxml.html import *
from urllib import *

basic_wordlist = ["хороший","плохой", "вкусный"]
dev_wordlist=[]

def syn_finder(i):
    try:
        page = html.parse("http://slova.zkir.ru/dict/{}".format(i))
        root = page.getroot()
        words = root.find_class("synonim")
        for i in range(len(words)):
            if words[i].text_content() not in dev_wordlist:
                dev_wordlist.append(words[i].text_content())
    except OSError: pass
               
               
               
for i in basic_wordlist:
    syn_finder(i)
    
    
print (dev_wordlist)   
