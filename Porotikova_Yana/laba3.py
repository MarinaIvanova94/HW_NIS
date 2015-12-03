#вывести на экран ссылки на часы в электронном каталоге маказина "ЭЛЕКТРА"
import lxml.html as html
page = html.parse('http://www.electra.ru/reluce/CHasy/')
root = page.getroot()
tag = root.find_class('sneha-catalog-tile').pop()
url_list=[]

for i in tag.iterlinks():
        if i[2].find('electra.ru') != -1 and i[2] not in url_list and i[2].find("1"):
            url_list.append(i[2])
print('\n'.join(url_list))
