# -*- coding: UTF-8 -*-
import lxml.html as html
from lxml.etree import Element, SubElement, ElementTree
from lxml import etree
tag=[]
url_list=[]
title_list=[]
country_list=[]
time_list = []
actor_list = []
for i in range(1,137):
    root = html.parse('http://gidonline.club/genre/melodrama/page/{0}/'.format(i)).getroot()
    tag.extend(root.find_class('mainlink'))
for i in tag:
    try:
        y = i.find_class('mqn').pop().text_content()
        if y == '2010':
            for y in i.find_class('mainlink').pop().iterlinks():
                if y[1] == 'href':
                    url_list.append(y[2])
            title_list.append(i.text_content().split('\r')[0])
    except IndexError:
        y = i.find_class('mqx').pop().text_content()
for i in range(len(url_list)):
    print "Title: ", title_list[i]
    print "URL: ", url_list[i], '\n'

for ind, url in enumerate(url_list):
    page1 = html.parse(url)
    root1 = page1.getroot()
    tag1 = root1.find_class('t-row').pop().text_content().strip().split('\n')
    country_list.append(tag1[2].strip()[len(u'страна'):])
    time_list.append(tag1[4].strip()[len(u'время'):])

import pickle
f=open('output.pickle', 'wb')
pickle.dump('asd', f)
f.close()
f=open('output.pickle', 'rb')
top_words=pickle.load(f)
f.close()

root = Element('list_of_melodramas')
for i in range(0, len(url_list)):
    melodrama = SubElement(root, 'melodrama')
    SubElement(melodrama, 'title', href = url_list[i]).text = title_list[i]
    SubElement(melodrama, 'country').text = country_list[i]
    time = SubElement(melodrama, 'time')
    time.text = time_list[i]
    min = SubElement(time, 'minutes', number = int(time_list[i].split()[0]) * 60+ int(time_list[i].split()[2]))
output = etree.tostring(root, pretty_print=True, encoding='UTF-8')
f1 = open(r'C:\Users\евросеть\Documents\GitHub\HW_NIS\Blinova Polina\laba4.xml', 'wb')
f1.write(output)
print(output)
f1.close()
