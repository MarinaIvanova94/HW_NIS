+__author__='admin'
+from lxml import etree
+tree = etree.parse('Sergeeva1.xml')
+list = tree.getroot()
+
+for elem in list.iter('price'):
+  newcount = elem.get('price')
+  newline = newcount.split('-')
+  
+  for product in newline:
+    subelement = etree.SubElement(elem, 'discount')
+    subelement.text = product
+    print(product + 'discount' + '%')
+    
+text = etree.tostring(list, pretty_print=True, encoding='UTF-8')
+function = open('Sergeeva1.xml', 'w')
+function.write(text)
+function.close()