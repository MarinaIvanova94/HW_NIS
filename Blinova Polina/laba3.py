import lxml.html as html
tag=[]
url_list=[]
title_list=[]
for i in range(1,137):
    root = html.parse('http://gidonline.club/genre/melodrama/page/{0}/'.format(i)).getroot()
    tag.extend(root.find_class('mainlink'))
for i in tag:
    try:
        y = i.find_class('mqn').pop().text_content()
        if y == '2010':
            for y in i.find_class('mainlink').pop().iterlinks():
                if y[1] == 'href':
                    url_list.append(y[2])
            title_list.append(i.text_content().split('\n')[0])
    except IndexError:
        y = i.find_class('mqx').pop().text_content()
for i in range(len(url_list)):
    print "Title: ", title_list[i]
    print "URL: ", url_list[i], '\n'
