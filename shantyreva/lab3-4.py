#Извлечем новости с указанием их источника
# encoding=utf-8
#import urllib.request
import lxml.html as html

page = html.parse('http://www.championat.com/other/_biathlon.html')
root = page.getroot()
tag = root.find_class('news__items').pop()
#print(tag.text_content())

url_list = []

for i in tag.iterlinks():
    if i[2].find('news') != -1:
        if i[2].find('comments') == -1:
            url_list.append(i[2])

title = []
source = []

for url in url_list:
    page1 = html.parse('http://www.championat.com/'+url)
    root1 = page1.getroot()
    tag1 = root1.find_class('article__head__title').pop()
    an = tag1.text_content().strip()
    title.append(an)
    tag2 = root1.find_class('article__source').pop()
    ben = tag2.text_content().strip()
    source.append(ben)

from lxml import etree
root = etree.Element('article_supply')
tag = etree.SubElement(root, 'article')
for i in range(len(url_list)):
    subtag = etree.SubElement(tag, 'url').text = url_list[i]
    subtag2 = etree.SubElement(tag, 'title').text = title[i]
    subtag3 = etree.SubElement(tag, 'source').text = source[i]

new_xml = etree.tostring(root, pretty_print=True, encoding='utf-8')
a = open('news.xml', 'wb')
a.write(new_xml)
a.close()