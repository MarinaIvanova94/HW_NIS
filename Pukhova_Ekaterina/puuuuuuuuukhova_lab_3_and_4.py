# encoding=utf-8
import lxml.html as html

page = html.parse('http://news.sportbox.ru/Vidy_sporta/Futbol/Bubnov')
root = page.getroot()
tag = root.find_class('list').pop()

urllist = []

for i in tag.iterlinks():
    if i[2].find('png') == -1:
        urllist.append(i[2])

smekh = []
dates = []

for url in urllist:
    page1 = html.parse('http://news.sportbox.ru'+url)
    root1 = page1.getroot()
    tag1 = root1.find_class('node-header__title').pop()
    an = tag1.text_content().strip()
    smekh.append(an)
    tag2 = root1.find_class('b-author__date').pop()
    ben = tag2.text_content().strip()
    dates.append(ben)

for i in range(len(urllist)):
    print(urllist[i], '/n', smekh[i], '/n', dates[i])

from lxml import etree
root = etree.Element('bubnov_articles')
for i in range(len(urllist)):
    tag = etree.SubElement(root, 'article')
    subtag = etree.SubElement(tag, 'url').text = urllist[i]
    subtag2 = etree.SubElement(tag, 'title').text = smekh[i]
    subtag3 = etree.SubElement(tag, 'date').text = dates[i]

new_xml = etree.tostring(root, pretty_print=True, encoding='utf-8')
a = open('puuuuuuukhova.xml', 'wb')
a.write(new_xml)
a.close()