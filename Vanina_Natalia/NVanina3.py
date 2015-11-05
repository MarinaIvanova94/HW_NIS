#список популярных политических статей

import lxml.html as html
page = html.parse('http://www.lgz.ru/policy/')
root = page.getroot()
tag = root.find_class('articles-list clearfix').pop()
url_list = []
for i in tag.iterlinks():
    if i[2].find('http://www.lgz.ru/')!=-1:
        url_list.append(i[2])
print(url_list)
annonce_list=[]
for url in url_list:
    p = html.parse(url)
    r = p.getroot()
    t = r.find_class('article-block clearfix').pop()
    a = (t.text_content().strip())
    annonce_list.append(a)
    print(a)
