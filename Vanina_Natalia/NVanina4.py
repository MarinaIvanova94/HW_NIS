__author__ = 'Natu'

#создадим словарь политических терминов и список книг по теме

import lxml.html as html
from lxml import etree

page = html.parse('http://politike.ru/dictionary/275')
root = page.getroot()
tag=root.find_class('component').pop()
url_list=[]
for i in tag.iterlinks():
    if i[2].find('politike.ru')!=-1:
        url_list.append(i[2])
print(url_list)
annonce_list=[]
for url in url_list:
    p = html.parse(url)
    r = p.getroot()
    t = r.find_class('term').pop()
    a = (t.text_content().strip())
    annonce_list.append(a)
    print(a)

#создаем словари для данных
term = []
determination = []
book = []
tm = []


for url in url_list:
    page1 = html.parse(url)
    root1 = page1.getroot()

#термин
    tag1 = root1.find_class('m-title').pop()
    a = tag1.text_content().strip()
    tm.append(a)
    term.append(a)

#определение
    tag2 = root1.find_class('m-block').pop()
    a1 = tag2.text_content().strip()
    tm.append(a1)
    determination.append(a1)


#из класса 'abook book' получим весь список книг по теме 
    tag4 = root1.find_class('abook book')
    for i in tag4:
        book = i.getchildren()[0]
    a3 = book.text_content().strip()
    tm.append(a3)
    book.append(a3)

#создание xml с полученными данными
root8 = etree.Element("political_terms")
for i in range(len(term)):
    child1 = etree.SubElement(root8, "term")
    child2 = etree.SubElement(child1, "word").text = term[i]
    child3 = etree.SubElement(child1, "determination").text = determination[i]
    child4 = etree.SubElement(child1, "books").text = book[i]

out = etree.tostring(root8, pretty_print = True, encoding = 'utf-8')
f = open('res4.xml', 'wb')
f.write(out)
f.close()
