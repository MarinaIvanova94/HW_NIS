"""
Выбрать с сайта http://www.qwrt.ru/internet/ статьи с тегами "кино"+"США" и вывести на экран названия статей и ссылки на них
"""
from lxml.html import parse

pages = []
u = parse('http://www.qwrt.ru/').getroot()
y = u.find_class("_lists attemp_ls")
num_of_pages = int(y[0].get('data-last-page'))

for p in range(1, num_of_pages+1):
    page = parse('http://www.qwrt.ru/'+str(p)).getroot()
    pages.append(page)

for i in range(len(pages)):
    hrefs = pages[i].cssselect("a._title")
    tags = pages[i].cssselect("div.sm_tags")
    for j in range(len(tags)):
        if "кино" in tags[j].text_content() and "США" in tags[j].text_content():
            print(hrefs[j].text_content())
            print("http://www.qwrt.ru"+hrefs[j].get('href')+'\n')