from lxml import etree
tree = etree.parse('Sushcheva.xml')
root1 = tree.getroot()

for element in tree.iter('ingredient'):
        element.text="Ingredient"

newfile = etree.tostring(root1, pretty_print=True)
a = open('Suscheva_2.xml','w')
a.write(newfile.decode())
a.close()
