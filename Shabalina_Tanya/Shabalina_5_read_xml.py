from lxml import etree

tree = etree.parse('Shabalina_4_html_xml.xml')
root = tree.getroot()
print('URLs: ')
for element in root.iter('url'):
    print(element.text)
print('DATEs: ')
for element1 in root.iter('date'):
    print(element1.text)
