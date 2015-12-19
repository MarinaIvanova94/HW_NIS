__author__ = 'liubov'
from lxml import etree


tree = etree.parse('morinaU')
root1 = tree.getroot()

for element in root1.iter('ingredient'):
    attr_val = element.get('amount')
    attribute_list = attr_val.split(',')

    for attrib in attribute_list:
        sub_elem = etree.SubElement(element, 'specis')
        specis = sub_elem.text =''

output = etree.tostring(root1, pretty_print=True)
print(output.decode().encode())
f = open('morinaU1', 'w')
f.write(output.decode())
print(output.decode())
f.close()
