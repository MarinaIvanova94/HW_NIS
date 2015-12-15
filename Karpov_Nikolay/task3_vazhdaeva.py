__author__ = '123'

"""
импорт названия, орписания и времени выпуска статей о событиях декабря 2015 года

"""
#http://www.bbc.com/russian/news/2015/12/151214_venediktov_ryabtseva_apology
#http://www.bbc.com/russian/news/2015/12/151214_latvia_russia_border
#http://www.bbc.com/russian/news/2015/12/151214_oil_price_37
#http://www.bbc.com/russian/news/2015/12/151214_ruble_dollar_rate_70
#http://www.bbc.com/russian/news/2015/12/151214_egypt_a321_not_terror_attack

import lxml.html as html
other_words = ["egypt_a321_not_terror_attack", "venediktov_ryabtseva_apology", "latvia_russia_border", "oil_price_37",
               "ruble_dollar_rate_70",]
page = html.parse("http://www.bbc.com/russian/topics/russia").getroot()


for url in other_words:
    for i in other_words:
        page1 = html.parse('http://www.bbc.com/russian/news/2015/12/151214_{}'.format(i))
        root1 = page1.getroot()

        print(root1.find_class('story-body__h1').pop().text_content())
        print(root1.find_class('date date--v2').pop().text_content())
        print(root1.find_class('story-body__introduction').pop().text_content())
