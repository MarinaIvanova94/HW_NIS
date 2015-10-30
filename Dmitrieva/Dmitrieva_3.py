#извлечение названий и кратких описаний курсов с postnauka.ru
import urllib.request
import lxml.html as html
page = html.parse('http://postnauka.ru/courses')
root = page.getroot()
tag = root.find_class('m-subt')
tag1 = root.find_class('m-title')
for i in range(len(tag1)):
    print(tag1[i].text_content())
    print(tag[i].text_content(), '\n')
