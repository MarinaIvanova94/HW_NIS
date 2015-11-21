from lxml import etree
tree = etree.parse('Kate_Delyagina.xml')
root1 = tree.getroot()

for country in tree.iter('people'):
    if int(country.text) > 5000000:
        country.text = "more than 5 million"

m=etree.tostring(root1, pretty_print=True, encoding='utf-8')
print(m.decode().encode())
f = open('Kate_Delyagina_2.xml', 'w')
f.write(m.decode())
f.close()