import lxml.html as html
#извлекаем ссылки на видео с сайта
page = html.parse('http://www.planetaexcel.ru/video/')
root = page.getroot()
tag = root.find_class('s2u-yt-grid-collection').pop()
url_list = []

for i in tag.iterlinks():
        if i[2].find('http://www.youtube.com/') != -1:
            url_list.append(i[2])
print('\n'.join(url_list))