__author__ = '123'
import lxml.html as html
from lxml import etree

other_words = ["egypt_a321_not_terror_attack", "venediktov_ryabtseva_apology", "latvia_russia_border", "oil_price_37",
               "ruble_dollar_rate_70"]
page = html.parse("http://www.bbc.com/russian/topics/russia").getroot()


for url in other_words:
    for i in other_words:
        page1 = html.parse('http://www.bbc.com/russian/news/2015/12/151214_{}'.format(i))

titles = page.find_class('story-body__h1').pop().text_content()
dates = page.find_class('date date--v2').pop().text_content()
info = page.find_class('story-body__introduction').pop().text_content()

root_elem = etree.Element("events")
root = etree.Element("events")

for i in range(len(titles)):
    book = etree.SubElement(root, "event")
    etree.SubElement(book, "title").text = titles[i]
    etree.SubElement(book, "date").text = dates[i]
    etree.SubElement(book, "info").text = info[i]

resultat = etree.tostring(root, pretty_print=True, encoding='UTF-8')
targetxml = open('result.xml', 'w')
targetxml.write(resultat)

targetxml.close()
