__author__ = 'work'
#coding: utf-8

from lxml import etree
tree = etree.parse('Zaplatkina.xml')
root1 = tree.getroot()

#create new subelement
for element in root1:
    new = etree.SubElement(element, "comments")
    new.text = "Посмотрите комментарии и отзывы"

#change element text
for element in tree.iter('title3'):
    element.text = "Салат 'Оливье'"

output = etree.tostring(root1, pretty_print=True, encoding='UTF-8')
f = open('Zaplatkina_changed.xml', 'w')
f.write(output.decode())
f.close()