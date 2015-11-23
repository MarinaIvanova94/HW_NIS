import lxml.html as html

page = html.parse('http://www.sports.ru/rfpl/table/').getroot()
tag = page.find_class('table').pop()
#print(tag.text_content())

urllist = []

for i in tag.iterlinks():
    if i[2].find('http://www.sports.ru/') != -1:
        urllist.append(i[2])


teams = []
flags = []

for ind, url in enumerate(urllist):
    page1 = html.parse(url)
    root1 = page1.getroot()
    tag1 = root1.find_class('descr').pop()
    name = tag1.text_content().strip()
    tag2 = root1.find_class('profile-table').pop()
    flag = tag2.text_content().strip()
    teams.append(name)
    flags.append(flag)

for i in range(len(urllist)):
    print(urllist[i])
    print(teams[i])
    print(flags[i])
#import pickle
#f = open('output','wb')
#pickle.dump(urllist, f)
#f.close()

#d = ('output','rb')
#ssilki = pickle.load(d)
#d.close()
#print(ssilki)