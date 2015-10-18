__author__ = 'Nikola Karpov'
from lxml import etree

tree=etree.parse('HW_NIS/NIS_HW1_Bazanova.xml')
root=tree.getroot()
#for element in root:
#    for s_el in element:
#        print(s_el.tag, s_el.text)

for element in root.iter('skills'):
    #print("%s - %s" % (element.tag, element.text))
    val=element.get('keySkills')
    for sk in val.split(','):
        etree.SubElement(element, 'skill').text=sk
    element.set('keySkills', '')

    #for key, val in element.items():
    #    if key=='keySkills':
    #        for sk in val.split(','):
    #            etree.SubElement(element, 'skill').text=sk
            #print(val.split(','))

s=etree.tostring(root, xml_declaration=True, pretty_print=False, encoding='UTF-8')
f=open('HW_NIS/NIS_HW1_Bazanova1.xml', 'w')
f.write(s)
f.close()
print('OK')