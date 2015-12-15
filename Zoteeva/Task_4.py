__author__ = 'work'
#coding: utf-8

import lxml.html as html
from lxml import etree

#извлекаем ссылки на новостные статьи одного автора (Наталья Зотеева) с нижегородского сайта Биржа.ру
page = html.parse('http://www.birzha.ru/authors/authors/25628/')
root = page.getroot()
tag = root.find_class('materials-list').pop()

urls = []
for i in tag.iterlinks():
    if i[2].find('/news/')!= -1:
        urls.append('http://www.birzha.ru' + i[2])

#удаляем повторяющиеся ссылки
k = 0
for l in urls:
    if l == urls[k+1] and k < len(urls)-1:
        urls.pop(k+1)
    k += 1

#выводим аннотации статей
annotations = []
sections = []
dates = []
t_list = []
main_list = []

for url in urls:
    page_1 = html.parse(url)
    root_1 = page_1.getroot()
    tag_1 = root_1.find_class('news-preview-text').pop()
    annot = tag_1.text_content().strip()
    annotations.append(annot)

#получаем темы статей
    tag_2 = root_1.find_class('news-section').pop()
    section = tag_2.text_content().strip()
    sections.append(section)

#получаем даты публикаций статей
    tag_3 = root_1.find_class('news-date').pop()
    date = tag_3.text_content().strip()
    dates.append(date)

#создаем main_list, в котором содержатся списки: sections, dates, annotations, urls
    t_list.append(sections[-1])
    t_list.append(dates[-1])
    t_list.append(annotations[-1])
    t_list.append(urls[-1])
    main_list.append(t_list)

#создаем xml
root_2 = etree.Element('main')
for i in main_list:
    main = etree.SubElement(root_2, 'my_articles')
    etree.SubElement(main, 'topic').text = i[0]
    etree.SubElement(main, 'date').text = i[1]
    etree.SubElement(main, 'annotation').text = i[2]
    etree.SubElement(main, 'url').text = i[3]

xml = etree.tostring(root_2, pretty_print = True)
f = open('Task_4.xml', 'wb')
f.write(xml)
f.close()
