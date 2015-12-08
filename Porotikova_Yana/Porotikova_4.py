import lxml.html as html
from lxml import etree
#get information about films from the Johnny Depp's biography and print the description about films

page = html.parse('http://www.kinomania.ru/news/53299/')
root = page.getroot()
tag = root.find_class('layout').pop()
url_list = []
for i in tag.iterlinks():
    if i[2].find('http://www.kinomania.ru/film/') != -1:
        url_list.append(i[2])
# annotation about films
description_list = []
genre_list = []
producers_list = []

for url in url_list:
    page1 = html.parse(url)
    root1 = page1.getroot()
    tag1 = root1.find_class('l-side-in review').pop()
    tag2 = root1.xpath('/html/body/div[3]/div/div/div[1]/div[1]/div[1]/div[2]/ul[1]/li[3]').pop()
    tag3 = root1.xpath('/html/body/div[3]/div/div/div[1]/div[1]/div[1]/div[3]/ul/li[3]/a[3]').pop()
    an = tag1.text_content().strip()
    description_list.append(an)
    genre_list.append(tag2.text_content())
    producers_list.append(tag3.text_content())
print('\n'.join(description_list))
print('\n'.join(genre_list))
print('\n'.join(producers_list))

import pickle
f = open('Porotikova_xml_4.pickle', 'wb')
pickle.dump('asd', f)
f.close()
f = open('Porotikova_xml_4.pickle', 'rb')
top_words = pickle.load(f)
f.close()

root = etree.Element("Films")
for i in range(len(description_list)):
    Films = etree.SubElement(root, "film")
    etree.SubElement(Films, "url").text = url_list[i]
    etree.SubElement(Films, "description").text = description_list[i]
    etree.SubElement(Films, "genre").text = genre_list[i]
    etree.SubElement(Films, "producers").text = producers_list[i]

output = etree.tostring(root, pretty_print = True, encoding = 'UTF-8')
f1 = open('Porotikova_xml_4.xml', 'wb')
f1.write(output)
f1.close()
