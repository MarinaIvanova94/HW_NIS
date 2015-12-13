# -*- coding: UTF-8 -*-
import lxml.html as html
from lxml.etree import Element, SubElement, ElementTree
from lxml import etree
tag = []
url_list = []
title_list = []
country_list = []
time_list = []
for i in range(1,225):
    root = html.parse('http://gidonline.club/genre/komediya/page/{0}/'.format(i)).getroot()
    tag.extend(root.find_class('mainlink'))
for i in tag:
    try:
        y = i.find_class('mqn').pop().text_content()
        if y == '2013':
            for y in i.find_class('mainlink').pop().iterlinks():
                if y[1] == 'href':
                    url_list.append(y[2])
            title_list.append(i.text_content().split('\r')[0])
    except IndexError:
        y = i.find_class('mqx').pop().text_content()

for ind, url in enumerate(url_list):
    page1 = html.parse(url)
    root1 = page1.getroot()
    tag1 = root1.find_class('t-row').pop().text_content().strip().split('\n')
    country_list.append(tag1[2].strip()[len(u'страна'):])
    time_list.append(tag1[4].strip()[len(u'время'):])

import pickle
f = open('output.pickle', 'wb')
pickle.dump('asd', f)
f.close()
f = open('output.pickle', 'rb')
top_words = pickle.load(f)
f.close()

root = Element('list_of_comedies')
for i in range(0, len(url_list)):
    comedy = SubElement(root, 'comedy')
    SubElement(comedy, 'title', href = url_list[i]).text = title_list[i]
    SubElement(comedy, 'country').text = country_list[i]
    time = SubElement(comedy, 'time')
    time.text = time_list[i]
    t = time_list[i].split()
    try:
        if len(t) == 4:
            min = SubElement(time, 'minutes', number = str(int(t[0]) * 60+ int(t[2])))
        else:
            min = SubElement(time, 'minutes', number = t[0])
    except IndexError:
        #не указано время на сайте
        print title_list[i], url_list[i], time_list[i]
output = etree.tostring(root, pretty_print=True, encoding='UTF-8')
f1 = open(r'D:\HW_NIS\Bardina Alyona\4 laba (site_xml).xml', 'wb')
f1.write(output)
print(output)
f1.close()
