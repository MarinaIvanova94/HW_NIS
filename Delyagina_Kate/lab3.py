import lxml.html as html
url = []
artists = []
songs = []
tags = []
page = html.parse('http://www.last.fm/ru/music').getroot()
tag = page.find_class('globalchart').pop()

for i in tag.iterlinks():
    if i[2].find('/ru/music/') != -1:
        url.append('http://www.last.fm'+i[2])

for i in url:
    page1 = html.parse(i)
    root1 = page1.getroot()
    tag1 = root1.find_class('header-title').pop()
    for j in root1.iterlinks():
        if j[2].find('/ru/tag/')!=-1:
            tags.append(j[2])
            break
    artists.append(tag1.text_content().strip())


artists = list(set(artists))
artists.sort()
url = list(set(url))
url.sort()
print artists
print url
print tags