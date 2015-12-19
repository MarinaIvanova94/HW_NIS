__author__ = 'work'
#coding: utf-8

#извлекаем ссылки на новостные статьи одного автора (Наталья Зотеева) с нижегородского сайта Биржа.ру
import lxml.html as html
page = html.parse('http://www.birzha.ru/authors/authors/25628/')
root = page.getroot()
tag = root.find_class('materials-list').pop()

url_list = []
for i in tag.iterlinks():
    if i[2].find('/news/')!= -1:
        url_list.append('http://www.birzha.ru' + i[2])

#удаление повторяющихся ссылок
k = 0
for l in url_list:
    if l == url_list[k+1] and k < len(url_list)-1:
        url_list.pop(k+1)
    k += 1
print('\n'.join(url_list))

#выводим аннотации статей
annotations = []
sections = []
dates = []
for url in url_list:
    page_1 = html.parse(url)
    root_1 = page_1.getroot()
    tag_1 = root_1.find_class('news-preview-text').pop()
    annot = tag_1.text_content().strip()
    annotations.append(annot)

#получаем темы статей
    tag_2 = root_1.find_class('news-section').pop()
    section = tag_2.text_content().strip()
    sections.append(section)

#получаем даты публикаций статей
    tag_3 = root_1.find_class('news-date').pop()
    date = tag_3.text_content().strip()
    dates.append(date)

print('\n'.join(annotations))
print('\n'.join(sections))
print('\n'.join(dates))
