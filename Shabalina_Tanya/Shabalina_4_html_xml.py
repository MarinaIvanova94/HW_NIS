import lxml.html as html
from lxml import etree

str = 'http://vsekakuzverei.com/category/%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D1%8B-%D0%B2%D1%81%D0%B5-%D0%BA%D0%B0%D0%BA-%D1%83-%D0%B7%D0%B2%D0%B5%D1%80%D0%B5%D0%B9/'
page = html.parse(str)
root = page.getroot()
tag_num = root.find_class('pagenavi').pop()

url_list = []
article_list = []
num_list = []
title_list = []
date_list = []
tag_list = []
entry_list = []
num_list.append(str)

#извлекаем ссылку на каждую страницу
for j in tag_num.iterlinks():
    if j[2].find('vsekakuzverei.com/category'):
        num_list.append(j[2])
num_list.pop()

#извлекаем ссылки на видео из всех страниц
for m in num_list:
    page = html.parse(m)
    root = page.getroot()
    tag = root.find_class('entry-container list-view').pop()
    for i in tag.iterlinks():
        if i[2].find('vsekakuzverei.com/20') != -1:
            url_list.append(i[2])

#удаляем повторяющиеся ссылки
k = 0
for l in url_list:
    if l == url_list[k+1] and k < len(url_list)-1:
        url_list.pop(k+1)
    k += 1

#получаем описание всех видео
for url in url_list:
    temp = []
    page1 = html.parse(url)
    root1 = page1.getroot()
    tag1 = root1.find_class('entry-content').pop()
    article = tag1[0].text_content().strip().encode()
    article_list.append(article)

#получаем название статьи
    tag2 = root1.find_class('entry-title').pop()
    title = tag2.text_content().strip().encode()
    title_list.append(title)

#получаем дату публикации статьи
    tag3 = root1.find_class('entry-date').pop()
    date = tag3.text_content().strip().encode()
    date_list.append(date)

#получаем для каждой статьи тэг
    tag4 = root1.find_class('entry-utility').pop()
    t_list = []
    for i in tag4.iterlinks():
        if i[2].find('vsekakuzverei.com/tag/') != -1:
            tagged = i[0].text_content().encode()
            t_list.append(tagged)
    tag_list.append(t_list)

#получаем список entry_list, элементами которого являются списки, содержащие информацию о каждой статье
    temp.append(title_list[-1])
    temp.append(url_list[-1])
    temp.append(article_list[-1])
    temp.append(date_list[-1])
    temp.append(tag_list[-1])
    entry_list.append(temp)

#создаем xml
root2 = etree.Element('main')
for i in entry_list:
    main = etree.SubElement(root2, 'entry')
    etree.SubElement(main, 'title').text = i[0].decode()
    etree.SubElement(main, 'url').text = i[1]
    etree.SubElement(main, 'article').text = i[2].decode()
    etree.SubElement(main, 'date').text = i[3]
    tagg = ''
    for j in i[4]:
        tagg += j.decode()
    etree.SubElement(main,'tagged').text = tagg
xml = etree.tostring(root2, pretty_print=True)
f = open('Shabalina_4_html_xml.xml', 'w')
f.write(xml.decode())
f.close()
