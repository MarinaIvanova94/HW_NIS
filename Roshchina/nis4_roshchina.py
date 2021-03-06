#coding: utf-8
from lxml.html import parse
from lxml import etree

"""Создание XML на основе данных, извлеченных с сайта www.qwrt.ru"""
pages = []
u = parse('http://www.qwrt.ru/').getroot()

for p in range(1, 69):
    page = parse('http://www.qwrt.ru/'+str(p)).getroot()
    pages.append(page)

titles = []
taglists = []
links = []
num_of_pages = []

for i in range(len(pages)):
    hrefs = pages[i].cssselect("a._title")
    tags = pages[i].cssselect("div.sm_tags")
    authors = pages[i].cssselect("div.art_autor")
    for j in range(len(tags)):
        if "кино" in tags[j].text_content() and "США" in tags[j].text_content():
            titles.append(hrefs[j].text_content())
            taglists.append(tags[j].text_content())
            links.append("http://www.qwrt.ru"+hrefs[j].get('href'))
            num_of_pages.append(i+1)

root = etree.Element("chosen_articles")
for i, w in enumerate(num_of_pages):
        child = etree.SubElement(root, "article", page="%s" % w)
        child1 = etree.SubElement(child, "title").text = titles[i]
        child2 = etree.SubElement(child, "link").text = links[i]
        child3 = etree.SubElement(child, "list_of_tags").text = taglists[i]


xml = etree.tostring(root, pretty_print=True, encoding='utf-8')
f = open('nis4_roshchina2.xml', 'wb')
f.write(xml)
f.close()

"""Работа с XML - извлечение данных """
tree = etree.parse('nis4_roshchina2.xml')
root = tree.getroot()

for element in root.iter('title'):
    print(element.text)

for element in root.iter('article'):
    print(element.attrib)
