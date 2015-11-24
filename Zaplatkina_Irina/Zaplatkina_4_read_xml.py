__author__ = 'admin'
from lxml import etree
tree = etree.parse('Zaplatkina_4_xml.xml')
root = tree.getroot()
for i in root.iter('url'):
    print(i.text)
for i in root.iter('annotation'):
    print(i.text)
for i in root.iter('year'):
    print(i.text)
for i in root.iter('director'):
    print(i.text)