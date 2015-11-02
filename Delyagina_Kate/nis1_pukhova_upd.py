from lxml import etree
tree = etree.parse('Pukhova.xml')
root1 = tree.getroot()

for element in tree.iter('price'):
	element.text="Price"

newfile = etree.tostring(root1, pretty_print=True)
a = open('nis1_pukhova_upd.xml','w')
a.write(newfile.decode())
a.close()
