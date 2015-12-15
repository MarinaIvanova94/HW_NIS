# -*- coding: UTF-8 -*-
from lxml import etree, html
f = open('C:\Users\евросеть\Documents\GitHub\HW_NIS\Bardina Alyona\Bardina.xml')
tree = etree.parse(f)
root = tree.getroot()
for element in root.iter('director'):
    mylist = element.text.split()
    etree.SubElement(element,'first_name').text = " ".join(mylist[:-1])
    etree.SubElement(element,'last_name').text = " ".join(mylist[-1])
for element in root.iter('genres'):
    my_list = element.text.split(', ')
    print my_list
    for i in my_list:
        etree.SubElement(element, 'genre', name = i)
output = etree.tostring(root, pretty_print=True, encoding='UTF-8')
f1 = open('C:\Users\евросеть\Documents\GitHub\HW_NIS\Blinova Polina\Blinova(Bardina).xml', 'w')
f1.write(output)
f1.close()
f.close()
