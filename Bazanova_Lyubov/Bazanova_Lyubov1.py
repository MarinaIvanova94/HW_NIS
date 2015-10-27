'''Вывести все сссылки со страницы и весь текст'''
import urllib2
from bs4 import BeautifulSoup

soup = BeautifulSoup(urllib2.urlopen('http://heroesch.ru/tablitsa-geroev/').read())
print("*All links of this page*")
for link in soup.find_all('a'):
    print(link.get('href'))
print("*All text of this page")
for text in soup.body.findAll(text=True):
    print(text.rstrip())
