import lxml
from lxml import etree
my_tree = etree.parse("C:\\Users\\Anastasia\\Documents\\Dutch\\Dmitrieva_nis.xml")
my_root = my_tree.getroot()

#удаляем один из атрибутов - название издателя
for element in my_root: 
    for sub_el in element:
        if sub_el.tag=='dateline':
            ##print (sub_el.get("author"))
            dateline_attr = sub_el.attrib
            del dateline_attr['publisher']
            ##print (dateline_attr)
            
# добавляем новую сущность       
for element in my_root:
    new_sub_elem = etree.SubElement(element, "price")
    price = input("Введи цену")
    new_sub_elem.text = price
    
txt = etree.tostring(my_root,encoding = 'utf8')
f = open("C:\\Users\\Anastasia\\Documents\\Dutch\\Dmitrieva_nis_changed444.xml",'w')
f.write(txt.decode())
f.close()
