# -*- coding: utf-8 -*-
from lxml import etree
#root = etree.Element('team_info')
strings = open('output').readlines()
root = etree.Element('team_info')
for i in range(0, len(strings), 4):

    tag = etree.SubElement(root, 'team')
    subtag = etree.SubElement(tag, 'link').text = strings[i]
    subtag2 = etree.SubElement(tag, 'name').text = strings[i+1]
    subtag3 = etree.SubElement(tag, 'country').text = strings[i+2]
    subtag4 = etree.SubElement(tag, 'coach').text = strings[i+3]

new_xml = etree.tostring(root, pretty_print=True)
a = open('new_xml_assignment4.xml', 'w')
a.write(new_xml.decode())
a.close()