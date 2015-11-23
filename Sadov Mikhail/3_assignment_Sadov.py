# encoding=utf-8
#import urllib.request
import lxml.html as html

#html = urllib.request.urlopen()
#sel = CSSelector('div.content')

page = html.parse('http://www.hse.ru/staff/nkarpov#sci')
root = page.getroot()
tag = root.find_class('b-person-data publications printable').pop()
#print(tag.text_content().encode())

url_list = []

for i in tag.iterlinks():
    if i[2].find('hse.publications.ru') != -1:
        url_list.append(i[2])
#print(url_list)
annonce_list = []

for url in url_list:
    page1 = html.parse(url)
    root1 = page1.getroot()
    tag1 = root1.find_class('details-annonce').pop()
    an = tag1.text_content().strip()
    annonce_list.append(an)
    print(an)
#body > div.page > div.layout.wide > div.grid.grid_ > div.main > div > div.b-person-data.publications.printable > ul > li:nth-child(1) > div > a
body > div.page > div.layout.wide > div.grid.grid_ > div.main > div > div.b-person-data.publications.printable