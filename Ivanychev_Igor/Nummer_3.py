import lxml.html as html

page = html.parse('http://www.topgearrussia.ru/cars/brends/')
root = page.getroot()
tag = root.find_class('TG-all-breand').pop()
#print(tag.text_content())

url_list = []

for i in tag.iterlinks():
    url_list.append('http://www.topgearrussia.ru'+i[2])
#print (url_list)

for url in url_list:
    page1 = html.parse(url)
    root1 = page1.getroot()
    tag1 = root1.find_class('TG-FONT-STYLE-6 t10 b10').pop()
    an = tag1.text_content().strip()
    #print (an)
    tag2 = root1.find_class('TG-anons-material anons-only-h1').pop()
    news = tag2.text_content().strip()
    #print(news)