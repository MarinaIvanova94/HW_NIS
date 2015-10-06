from lxml import etree

tree = etree.parse('yanap.xml')
root = tree.getroot()

for element1 in root.iter('printBook'):
    element1.set("place", "N.Novgorod")#adds a new attribute
    a = etree.SubElement(root,'comments')#adds a new subelement
    l = root[0]
    root[0] = root[-1] # moves the last element to the place of the element[0]
    root.append(l) #we save the element[0]

for elem in root.iter('comments'):
    t = elem.text = 'How to print a book! We know for sure!'

for element2 in root.iter('title'):
    sub = etree.SubElement(root,'advice')#new subelement
    txt = sub.text = 'Leave your comment,please:)'#text, which new subelement contains

for element3 in root.iter('part1'):
    attr = element3.attrib
    if attr: attr["colour"] = "white"#new attribute

for element in root.iter():
    print("%s - %s" % (element.tag, element.text))

n = etree.tostring(root, pretty_print=True)
f = open('yanap.xml', 'w')
f.write(n.decode())
f.close()
