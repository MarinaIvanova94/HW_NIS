from lxml import etree

tree = etree.parse('nis1_roshchina.xml')
root1 = tree.getroot()
# for child in root1:
#    for sub in child:
#        for element in sub:
#            attr_val = element.get('amount')

for element in root1.iter('part'):
    #    attr_val = element.get('material')
    attributes = element.attrib
    if attributes:
        attributes["quality"] = "good"
# print attributes
#    part_list = attr_val.split(',')
#    for skill in skill_list:
#        sub_elem = etree.SubElement(element, 'part')
#        sub_elem.text = skill
#        print('Part = ' + skill)

newfile = etree.tostring(root1, pretty_print=True, encoding='utf-8')
a = open('Roshchina_upd.xml', 'wb')
a.write(newfile)
a.close()