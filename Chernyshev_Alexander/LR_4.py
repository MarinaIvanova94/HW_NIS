__author__ = 'asus'
import lxml.html as html
#it gets info about available hotels in Arzamas or near to it
page = html.parse('http://www.booking.com/searchresults.ru.html?src=index&nflt=&ss_raw=fhpfvfc&error_url=http%3A%2F%2Fwww.booking.com%2Findex.ru.html%3Faid%3D388513%3Blabel%3Dyandex-index-Hotels-5V%252A81YcrGaQhmOwBNu3v_g-408311907%3Bsid%3D564fb73aaca5d4f28e228f0d7df54ce4%3Bdcid%3D4%3Bbb_ltbi%3D0%3Bsb_price_type%3Dtotal%26%3B&aid=388513&dcid=4&label=yandex-index-Hotels-5V*81YcrGaQhmOwBNu3v_g-408311907&sid=564fb73aaca5d4f28e228f0d7df54ce4&si=ai%2Cco%2Cci%2Cre%2Cdi&ss=%D0%90%D1%80%D0%B7%D0%B0%D0%BC%D0%B0%D1%81%2C+%D0%9D%D0%B8%D0%B6%D0%B5%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%B0%D1%8F+%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C&checkin_monthday=24&checkin_year_month=2015-11&checkout_monthday=25&checkout_year_month=2015-11&room1=A%2CA&no_rooms=1&group_adults=2&group_children=0&dest_type=city&ac_pageview_id=1d5e5c41275400ad&ac_position=0&ac_suggestion_list_length=5&ss_short=%D0%90%D1%80%D0%B7%D0%B0%D0%BC%D0%B0%D1%81&place_id=ChIJ171wqO94T0ER8KVSPbvsoRk&place_id_lat=55.39646090000001&place_id_lon=43.829917499999965&place_types=locality%2Cpolitical#hotel_1169617-back').getroot()
tag = page.find_class('hotellist').pop()

urllist = []

for i in tag.iterlinks():
    if i[2].find('/hotel/ru/') != -1:
        urllist.append("http://www.booking.com" + i[2])
#print (urllist)



name_list = []
adress_list = []
summary_list = []

for url in urllist:
    page1 = html.parse(url)
    root1 = page1.getroot()
    tag1 = root1.xpath('//*[@id="hp_hotel_name"]').pop()
    tag2 = root1.xpath('//*[@id="hp_address_subtitle"]').pop()
    tag3 = root1.xpath('//*[@id="hotel_main_content"]/div[2]/div[1]/p[3]').pop()


    name_list.append(tag1.text_content())
    adress_list.append(tag2.text_content())
    summary_list.append(tag3.text_content())

#print(summary_list)

f = open('output_Hotel.txt', 'w')

for i in range(len(urllist)):
    f.write(name_list[i] + '\t')
    f.write(adress_list[i] + '\t')
    f.write(summary_list[i]  + '\t')
f.close()



