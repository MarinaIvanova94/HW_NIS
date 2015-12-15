from lxml import etree
tree = etree.parse('Bazanova.xml')
root1 = tree.getroot()
for element in root1.iter('education'):
    attr_val = element.get('university')
    attribute_list = attr_val.split(',')
    for attrib in attribute_list:
        sub_elem = etree.SubElement(element, 'average_mark')
        specis = sub_elem.text =''
resultat = etree.tostring(root1, pretty_print=True)
print(resultat.decode().encode())
f = open('RESULT.xml', 'w')
f.write(resultat.decode())
print(resultat.decode())
f.close()

