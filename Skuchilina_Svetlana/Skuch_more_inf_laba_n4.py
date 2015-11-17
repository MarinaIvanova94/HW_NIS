# -*- coding: utf-8 -*-
import lxml.html as html
from xml.etree.ElementTree import Element, SubElement, ElementTree
from lxml import etree
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
#for i in range(len(url_list)):
#    print url_list[i]
#    print title_list[i]

rating_list = []
story_list = []
screens = ""
screen_list = []
for ind, url in enumerate(url_list):
    page1 = html.parse(url)
    root1 = page1.getroot()
    tag1 = root1.find_class('current-rating')
    rating = tag1[0].text_content().strip()
    rating_list.append(rating)
    for y in root1.find_class('screens').pop().iterlinks():
        if 'kinogo' in y[2] and 'jpg' in y[2]:
            screens += y[2]+ '\n'
    screen_list.append(screens)
    screens = ''
    #tag2 = root1.find_class('fullimg').pop()
    #story = tag2.text_content().strip()
    #story_list.append(story)

#for i in range(len(url_list)):
#    print(url_list[i] + '\n' + title_list[i] + '\n' + u'Рейтинг: ' + rating_list[i] + '\n' + \
#          #story_list[i] + '\n' +
#          u'Кадры:\n' + screen_list[i] + '\n')
import pickle
f=open('output.pickle', 'wb')
pickle.dump('asd', f)
f.close()
f=open('output.pickle', 'rb')
top_words=pickle.load(f)
f.close()

from lxml.etree import Element, SubElement, Comment, ElementTree
from lxml import etree
films = Element('films')
for i in range(0, len(url_list)):
    film = SubElement(films, 'film')
    title = SubElement(film, 'title', href=url_list[i], title = title_list[i])
    rating = SubElement(film, 'rating').text = rating_list[i]
    screens = SubElement(film, 'screens')
    for y in screen_list[i].split():
        screen = SubElement(screens, 'screen', href = y)
output = etree.tostring(films, pretty_print=True, encoding='UTF-8')
f.close()
f = open('E:\HW_NIS\Skuchilina_Svetlana\skuch_more_inf_lba_n4.xml', 'wb')
f.write(output)
f.close()
