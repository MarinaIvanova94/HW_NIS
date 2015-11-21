__author__ = 'work'
#coding: utf-8

#извлекаем ссылки на новостные статьи одного автора (Наталья Зотеева) с нижегородского сайта Биржа.ру
import lxml.html as html
page = html.parse('http://www.birzha.ru/authors/authors/25628/')
root = page.getroot()
tag = root.find_class('materials-list').pop()

url_list = []
for i in tag.iterlinks():
    if i[2].find('/news/')!=-1:
        url_list.append(i[2])

print(url_list)
