# extracting links and plot summaries of Disney movies

import lxml.html as html

page = html.parse('http://www.movieinsider.com/c2/walt-disney-pictures/')
root = page.getroot()
tag = root.find_class("phase5")

url_list = []

for i in tag:    
    for j in i.iterlinks():
        if (('movies' not in j[2]) and ('page_offset' not in j[2]) 
        and ('status' not in j[2]) and ('videos' not in j[2])):
            url_list.append(j[2])


annonce_list = []

for url in url_list:
    page1 = html.parse(url)
    root1 = page1.getroot()
    tag1 = root1.find_class('plot')#.pop()
    
    for i in tag1:
        an = i.text_content().strip()
        annonce_list.append(an)
        
for index, url in url_list:
    print (url, annonce_list[index])
