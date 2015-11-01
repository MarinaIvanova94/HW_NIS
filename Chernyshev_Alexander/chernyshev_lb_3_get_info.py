__author__ = 'asus'

#извлекаем ссылки на всевозможную информацию о штате Айдахо без лишнего мусора
import lxml.html as html
page = html.parse('http://prousa.info/idaho')
root = page.getroot()
tag = root.find_class('c_node_content content').pop()
url_list=[]

for i in tag.iterlinks():
        if i[2].find("png")== -1 and  i[2].find("jpg")== -1:#go throuh all things u contain
            url_list.append(i[2])
print(url_list)


