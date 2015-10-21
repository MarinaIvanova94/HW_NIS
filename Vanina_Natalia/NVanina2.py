__author__ = 'Vanina'

from lxml import etree
tree = etree.parse('Chernyshev2')
root1 = tree.getroot()

for element in root1.iter('information'):
    cont_val = element.get('country')
    cont_list = cont_val.split(',')
    for countries in cont_list:
       print('Country = ' +countries)

for cont in cont_list:
    sub_elem = etree.SubElement(element, 'colour')
    colour = sub_elem.text =''

output=etree.tostring(root1, encoding = 'utf8')
print(output.decode().encode())
f = open('Chernyshev_upd.xml', 'w')
f.write(output.decode())
f.close()

