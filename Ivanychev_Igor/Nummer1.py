__author__ = 'Сергей'

from lxml import etree
tree = etree.parse('Ivanychev_1.xml')
root1 = tree.getroot()

for element in tree.iter('title'):
	element.text=" Top 10 Batman's foes "

m=etree.tostring(root1, pretty_print=True)
print(m.decode().encode())
f = open('Ivanychev_2.xml', 'w')
f.write(m.decode())
f.close()