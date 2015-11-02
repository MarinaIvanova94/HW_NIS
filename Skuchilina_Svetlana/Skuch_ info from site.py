# -*- coding: utf-8 -*-

import lxml.html as html
tag=[]
url_list=[]
article_list=[]
root = html.parse("http://rusrep.ru/authors/199670/").getroot()
tag.extend(root.find_class("left"))
for i in tag:
    for j in i.iterlinks():
        if j[2] == "/search_tags/176309/":
            for y in i.find_class('title').pop().iterlinks():
                if 'article' in y[2]:
                    url_list.append('http://rusrep.ru' + y[2])
            article_list.append(i.find_class('sub_title').pop().text_content().strip())
for i in range(len(url_list)):
    print url_list[i]
    print article_list[i]
