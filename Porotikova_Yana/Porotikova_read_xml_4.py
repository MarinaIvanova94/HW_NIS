
from lxml import etree
tree = etree.parse('Porotikova_4_xml.xml')
root = tree.getroot()
for i in root.iter('url'):
    print(i.text)
for i in root.iter('description'):
    print(i.text)
for i in root.iter('genre'):
    print(i.text)
for i in root.iter('producers'):
    print(i.text)
