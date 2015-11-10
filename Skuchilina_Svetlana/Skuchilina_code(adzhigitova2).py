from lxml import etree
f = open('E:/HW_NIS/Adzhigitova_Yulia/Adzhigitova.xml')
tree = etree.parse(f)
root = tree.getroot()
for element in root.iter('actor'):
    mylist=element.get('born').split(', ')
    element.set('town',mylist[0])
    if len(mylist)==2:
        element.set('country',mylist[1])
    else:        
        element.set('state',mylist[1])
        element.set('country',mylist[2])
    
output = etree.tostring(root, pretty_print=True, encoding='UTF-8')
f1 = open('E:/HW_NIS/Adzhigitova_Yulia/Adzhigitova(skuchilina2).xml', 'w')
f1.write(output)
print(output)
f1.close()
