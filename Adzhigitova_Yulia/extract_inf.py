# -*- coding: utf-8 -*-
#Вывод ссылок на новость и текста новости, где упоминается (есть ссылка) на актера Логана Лермана (просматривается весь архив новостей кинопоиска)
import lxml.html as html
tag=[]
url_list=[]
news_list=[]
for i in range(1,67):
    root = html.parse('http://www.kinopoisk.ru/news/perpage/200/page/{0}/'.format(i)).getroot()
    tag.extend(root.find_class('item'))
for i in tag:
    for j in i.iterlinks():
        if j[2] == '/name/7418/' or 'id_actor=7418' in j[2]:
            for y in i.find_class('title').pop().iterlinks():
                if 'news' in y[2]:
                    url_list.append('http://www.kinopoisk.ru'+y[2])
            news_list.append(i.find_class('descr').pop().text_content())
for i in range(len(url_list)):
    print url_list[i], news_list[i]
