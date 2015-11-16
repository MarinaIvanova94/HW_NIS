import lxml.html as html
from xml.etree.ElementTree import Element, SubElement, ElementTree
from lxml import etree
tag=[]
url_list=[]
an_news_list=[]
newsTags_list = []
news_title_list = []
for i in range(1,10):
    root = html.parse('http://www.kinopoisk.ru/news/perpage/200/page/{0}/'.format(i)).getroot()
    tag.extend(root.find_class('item'))
for i in tag:
    for j in i.iterlinks():
        if j[2] == '/name/7418/' or 'id_actor=7418' in j[2]:
            for y in i.find_class('title').pop().iterlinks():
                if 'news' in y[2]:
                    url_list.append('http://www.kinopoisk.ru'+y[2])
            an_news_list.append(i.find_class('descr').pop().text_content())

for ind, url in enumerate(url_list):
    page1 = html.parse(url)
    root1 = page1.getroot()
    tag1 = root1.find_class('newsHeaderTitle').pop()
    news_title = tag1.text_content().strip()
    news_title_list.append(news_title)
    tag2 = root1.find_class('newsTags').pop()
    newsTags = tag2.text_content().split()
    for i in range(len(newsTags)-1):
        if u'премьер' in newsTags[i]:
            newsTags[i] = newsTags[i] + " " + newsTags.pop(i+1)
    newsTags_list.append(", ".join(newsTags))

allnews = Element('allnews')
for i in range(0, len(url_list)):
    news = SubElement(allnews, 'news')
    title = SubElement(news, 'title', href=url_list[i], title = news_title_list[i])
    summary = SubElement(news, 'summary').text = an_news_list[i]
    tagset = SubElement(news, 'tagset')
    for j in newsTags_list[i].split(", "):
        xtag = SubElement(tagset, 'xtag').text = j
tree = ElementTree(allnews)
tree.write("D:\NIS\HW_NIS\Adzhigitova_Yulia\laba4_onestring.xml", encoding='UTF-8')
f = open("D:\NIS\HW_NIS\Adzhigitova_Yulia\laba4_onestring.xml", 'r')
tree = etree.parse(f)
root = tree.getroot()
output = etree.tostring(root, pretty_print=True, encoding='UTF-8')
f1 = open('D:\NIS\HW_NIS\Adzhigitova_Yulia\laba4.xml', 'w')
f1.write(output)
print(output)
f1.close()
