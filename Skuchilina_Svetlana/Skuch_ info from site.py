# -*- coding: utf-8 -*-
import lxml.html as html
tag=[]
url_list=[]
title_list=[]
for i in range(1,493):
    root = html.parse('http://kinogo.co/page/{0}/'.format(i)).getroot()
    tag.extend(root.find_class('shortstory'))
for i in tag:
    for j in i.iterlinks():
        if 'indijskie_filmy' in j[2]:
            for y in i.find_class('zagolovki').pop().iterlinks():
                if '2010' in y[2]:
                    url_list.append(y[2])
                    title_list.append(i.find_class('zagolovki').pop().text_content())
for i in range(len(url_list)):
    print url_list[i]
    print title_list[i]
