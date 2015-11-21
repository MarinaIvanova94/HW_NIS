import lxml.html as html

str = 'http://vsekakuzverei.com/category/%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D1%8B-%D0%B2%D1%81%D0%B5-%D0%BA%D0%B0%D0%BA-%D1%83-%D0%B7%D0%B2%D0%B5%D1%80%D0%B5%D0%B9/'
page = html.parse(str)
root = page.getroot()
tag_num = root.find_class('pagenavi').pop()

url_list = []
article_list = []
num_list = []
num_list.append(str)

#извлекаем ссылку на каждую страницу
for j in tag_num.iterlinks():
    if j[2].find('vsekakuzverei.com/category'):
        num_list.append(j[2])
num_list.pop()

#извлекаем ссылки на видео из всех четырех страниц
for m in num_list:
    page = html.parse(m)
    root = page.getroot()
    tag = root.find_class('entry-container list-view').pop()
    for i in tag.iterlinks():
        if i[2].find('vsekakuzverei.com/20') != -1:
            url_list.append(i[2])

#удаляем повторяющиеся ссылки
k = 0
for l in url_list:
    if l == url_list[k+1] and k < len(url_list)-1:
        url_list.pop(k+1)
    k += 1
print('\n'.join(url_list))
print(len(url_list))

#получаем описание всех видео
for url in url_list:
    page1 = html.parse(url)
    root1 = page1.getroot()
    tag1 = root.find_class('entry-content').pop()
    article = tag1.text_content().strip().encode()
    article_list.append(article)
print(article_list)