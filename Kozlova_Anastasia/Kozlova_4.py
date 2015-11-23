
import lxml.html as html
from  lxml.html import *
links=[]

#достаем ссылки на все кафэ с главной страницы
lis = [i for i in range(1,18)]
for i in lis:
    page = html.parse(r"http://cafe-nn.ru/cafe?page={}&cat=All&kitchen=All&area=All&check[min]=&check[max]=".format(i))
    root = page.getroot()
    link_list = root.iterlinks()
    for i in link_list:
        if ".html" in i[2] and "kafe" in i[2] and i[2] not in links:
            links.append(i[2])                      
print ("Ссылки на рестораны: ", links)

#создаем структуру, где будет храниться извлеченная информация
from lxml import etree
myroot = etree.Element("root")

des = []
rev = []
au = []
for i in links:
    try:
        page=html.parse("http://cafe-nn.ru{}".format(i))
        root = page.getroot()
        name = root.xpath('//*[@id="content"]/div[4]/h2/text()') #извлекаем название ресторана
        item =  etree.SubElement(myroot, "place")#записываем инф-ю
        try:
            item.text = name.pop()
        except:pass
        
           
        adddescrip = root.xpath('//*[@id="content"]/div[4]/div[1]/p[4]/text()[1]') #извлекаем  описание ресторана
        adddes =  etree.SubElement(item, "additional_description")
        try:
            adddes.text = adddescrip[-1]
        except:pass
        
        
        k=1
        review = root.find_class("testimonial") #получаем отзывы
        for i in review:
            rev = etree.SubElement(item, "review{}".format(k))
            rev.text = i.text_content()
            try:
                rev.set("author", root.xpath('//*[@id="reports"]/div[2]/b/text()').pop()) #добавляем атрибуты : имя автора отзыва и дата
                rev.set("date",root.xpath('//*[@id="reports"]/div[2]/span/text()').pop() ) # и дата написания
            except:pass
            k=k+1
        
        
        
    except:pass

    
txt = etree.tostring(myroot,pretty_print = True, encoding = 'utf8')


f = open("C:\\Users\\Anastasia\\Documents\\Dutch2\\outtF.xml",'wb')
f.write(txt)
f.close()


#читаем файл, который только что записали
my_tree = etree.parse("C:\\Users\\Anastasia\\Documents\\Dutch2\\outtF.xml")
my_root = my_tree.getroot()
print (my_root.tag)


txt = etree.tostring(my_root,pretty_print = True, encoding = 'utf8', method = 'text')
print (txt.decode())


