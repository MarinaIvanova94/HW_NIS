import lxml.html as html

page = html.parse('http://www.sports.ru/rfpl/table/').getroot()
tag = page.find_class('table').pop()
#print(tag.text_content())

urllist = []

for i in tag.iterlinks():
    if i[2].find('http://www.sports.ru/') != -1:
        urllist.append(i[2])

teams = []

for ind, url in enumerate(urllist):
    page1 = html.parse(url)
    root1 = page1.getroot()
    tag1 = root1.find_class('descr').pop()
    an = tag1.text_content().strip()
    teams.append(an)
    print(an+' '+urllist[ind])