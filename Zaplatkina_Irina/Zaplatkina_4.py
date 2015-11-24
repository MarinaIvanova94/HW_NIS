__author__ = 'admin'
import lxml.html as html
from lxml import etree

page = html.parse('http://www.kinomania.ru/people/417286/')
root = page.getroot()
tag = root.find_class('layout').pop()
url_list = []
for i in tag.iterlinks():
    if i[2].find('http://www.kinomania.ru/film/') != -1:
        url_list.append(i[2])
#print('\n'.join(url_list))

annotation_list = []
year_list = []
director_list = []

for url in url_list:
    page1 = html.parse(url)
    root1 = page1.getroot()
    tag1 = root1.find_class('l-side-in review').pop()
    tag2 = root1.xpath('/html/body/div[3]/div[4]/div/div[1]/div[1]/div[1]/div[2]/ul[1]/li[2]/span').pop()
    tag3 = root1.xpath('/html/body/div[3]/div[4]/div/div[1]/div[1]/div[1]/div[3]/ul/li[1]/a').pop()
    an = tag1.text_content().strip()
    annotation_list.append(an)
    year_list.append(tag2.text_content())
    director_list.append(tag3.text_content())

#print('\n'.join(annotation_list))
#print('\n'.join(year_list))
#print('\n'.join(director_list))

import pickle
f = open('output.pickle', 'wb')
pickle.dump('asd', f)
f.close()
f = open('output.pickle', 'rb')
top_words = pickle.load(f)
f.close()

root = etree.Element("Films")
for i in range(len(annotation_list)):
    Films = etree.SubElement(root, "film")
    etree.SubElement(Films, "url").text = url_list[i]
    etree.SubElement(Films, "annotation").text = annotation_list[i]
    etree.SubElement(Films, "year").text = year_list[i]
    etree.SubElement(Films, "director").text = director_list[i]

output = etree.tostring(root, pretty_print = True, encoding = 'UTF-8')
f1 = open('output.xml', 'wb')
f1.write(output)
f1.close()
