# -*- coding: UTF-8 -*-
from lxml import etree, html
f = open('E:\HW_NIS\Blinova Polina\Blinova.xml')
tree = etree.parse(f)
root = tree.getroot()
for element in root.iter('author'):
    mylist = element.text.split()
    etree.SubElement(element,'first_name', name = " ".join(mylist[:-1]))
    etree.SubElement(element,'last_name', name = " ".join(mylist[-1]))
output = etree.tostring(root, pretty_print=True, encoding='UTF-8')
f1 = open('E:\HW_NIS\Bardina Alyona\Bardina(Blinova).xml', 'w')
f1.write(output)
f1.close()
f.close()
