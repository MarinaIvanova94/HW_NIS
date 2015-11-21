__author__ = 'admin'
import lxml.html as html

#из текста (биографии актрисы) извлекаем ссылки на фильмы
page = html.parse('http://www.kinomania.ru/people/417286/')
root = page.getroot()
tag = root.find_class('layout').pop()
url_list = []
for i in tag.iterlinks():
    if i[2].find('http://www.kinomania.ru/film/') != -1:
        url_list.append(i[2])
print('\n'.join(url_list))

#выводим краткую информацию о фильме
annot_list = []
for url in url_list:
    page1 = html.parse(url)
    root1 = page1.getroot()
    tag1 = root1.find_class('l-side-in review').pop()
    an = tag1.text_content().strip()
    annot_list.append(an)
print('\n'.join(annot_list))
