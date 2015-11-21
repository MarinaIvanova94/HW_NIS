import urllib.request
import lxml.html as html
page = html.parse('http://postnauka.ru/courses')
root = page.getroot()
tag = root.find_class('m-title')

url_list = []
for i in tag:
    for ii in i.iterlinks():
        if ii[2].find('postnauka.ru/courses') != -1:
            url_list.append(ii[2])
            
desc = []
for url in url_list:
    page1 = html.parse(url)
    root1 = page1.getroot()
    
    #получаем название курса:
    tag1 = root1.find_class('p-title').pop()
    a = tag1.text_content().strip()
    desc.append(a)
    
    #получаем имя автора и краткую информацию о нём:
    tag2 = root1.find_class('p-name').pop()
    tag3 = root1.find_class('p-desc').pop()
    a1 = tag2.text_content().strip()
    a2 = tag3.text_content().strip()
    desc.append(a1)
    desc.append(a2)
    
    #из тега <p> класса 'text' получаем краткое описание курса :
    tag4 = root1.find_class('text')
    for i in tag4:
        text = i.getchildren()[0]
    a3 = text.text_content().strip()
    desc.append(a3)
    
for i in desc:
    print(i, '\n')
