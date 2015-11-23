from lxml import etree
strings = open('output.txt').read()
list = strings.split(',')
list.remove('')
root = etree.Element('popular_singers')
print list
for i in range(0, len(list), 3):

   tag = etree.SubElement(root, 'singer')
   subtag = etree.SubElement(tag, 'name').text = list[i]
   subtag2 = etree.SubElement(tag, 'link').text = list[i+1]
   subtag3 = etree.SubElement(tag, 'tag').text = list[i+2]

new_xml = etree.tostring(root, pretty_print=True, encoding='utf-8')
a = open('new_xml_output.xml', 'wb')
a.write(new_xml)
a.close()
