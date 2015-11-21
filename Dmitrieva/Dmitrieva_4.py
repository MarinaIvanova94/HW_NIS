import urllib.request
import lxml.html as html
from lxml import etree
page = html.parse('http://postnauka.ru/courses')
root = page.getroot()
tag = root.find_class('m-title')

url_list = []
for i in tag:
    for ii in i.iterlinks():
        if ii[2].find('postnauka.ru/courses') != -1:
            url_list.append(ii[2])
            
#добавим словари, в которые будем записывать данные по мере их получения
#при помощи них затем создадим xml-документ
courses = []
names = []
descriptions = []
texts = []

desc = []
for url in url_list:
    page1 = html.parse(url)
    root1 = page1.getroot()
    
    #получаем название курса:
    tag1 = root1.find_class('p-title').pop()
    a = tag1.text_content().strip()
    desc.append(a)
    courses.append(a)
    
    #получаем имя автора и краткую информацию о нём:
    tag2 = root1.find_class('p-name').pop()
    tag3 = root1.find_class('p-desc').pop()
    a1 = tag2.text_content().strip()
    a2 = tag3.text_content().strip()
    desc.append(a1)
    names.append(a1)
    desc.append(a2)
    descriptions.append(a2)
    
    #из тега <p> класса 'text' получаем краткое описание курса :
    tag4 = root1.find_class('text')
    for i in tag4:
        text = i.getchildren()[0]
    a3 = text.text_content().strip()
    desc.append(a3)
    texts.append(a3)
    
#создание xml с полученными данными
root8 = etree.Element("postnauka_courses")
for i in range(len(courses)):
    child1 = etree.SubElement(root8, "course")
    child2 = etree.SubElement(child1, "subject").text = courses[i]
    child3 = etree.SubElement(child1, "teacher").text = names[i]
    child3 = etree.SubElement(child1, "short_bio").text = descriptions[i]
    child4 = etree.SubElement(child1, "course_annotation").text = texts[i]
    
out = etree.tostring(root8, pretty_print = True, encoding = 'utf-8')
f = open('output5.xml', 'wb')
f.write(out)
f.close()
