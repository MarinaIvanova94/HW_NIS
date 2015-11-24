# -*- coding: utf-8 -*-
from lxml import etree
f = open('D:\NIS\HW_NIS\Skuchilina_Svetlana\skuchilina_svetlana.xml')
tree = etree.parse(f)
root = tree.getroot()
for element in root.iter('film'):
    element.set('country',u'СССР')
for element in root.iter('actor'):
    mylist=element.get('name').split()
    etree.SubElement(element,'first_name').text=mylist[0]
    etree.SubElement(element,'last_name').text=mylist[1]
    #element.set('first_name',mylist[0])
    #element.set('last_name',mylist[1])

output = etree.tostring(root, pretty_print=True, encoding='UTF-8')
f1 = open('D:\NIS\HW_NIS\Adzhigitova_Yulia\Adzhigitova(skuchilina2).xml', 'w')
f1.write(output)
print(output)
f1.close()
