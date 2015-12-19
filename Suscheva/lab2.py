from lxml import etree
tree = etree.parse('Shantyreva.xml')
root1 = tree.getroot()

for element in tree.iter('description'):
        element.text="Plot"

newfile = etree.tostring(root1, pretty_print=True)
a = open('Shantyreva_2.xml','w')
a.write(newfile.decode())
a.close()
