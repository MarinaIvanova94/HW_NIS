import lxml
from lxml import etree

tree = etree.parse('nis1.xml')
root1 = tree.getroot()

for element in root1.iter('creator'):
    attributes = element.attrib
    if attributes:
        attributes["sex"] = "male"

m=etree.tostring(root1, pretty_print=True)
print(m.decode().encode())
f = open('nis2.xml', 'w')
f.write(m.decode())
f.close()