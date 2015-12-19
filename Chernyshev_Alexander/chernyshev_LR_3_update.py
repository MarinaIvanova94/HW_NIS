import lxml.html as html
#it gets info about available hotels in Arzamas or near to it
page = html.parse('http://www.booking.com/searchresults.en-us.html?city=20033173&ssne=Chicago&ssne_untouched=Chicago&error_url=http%3A%2F%2Fwww.booking.com%2Fhotel%2Fus%2Fbridgestreet-at-state-and-grand.en-us.html%3Faid%3D375440%3Blabel%3Dyandex-index-bookings-name-lttij8FYuObcClf%252APD6hNg-416097532%3Bsid%3D564fb73aaca5d4f28e228f0d7df54ce4%3Bdcid%3D4%3Bdist%3D0%3Bgroup_adults%3D2%3Broom1%3DA%252CA%3Bsb_price_type%3Dtotal%3Bsrfid%3Da8a657794e08709f307c400b0bc4b552990c5830X1%3Btype%3Dtotal%3Bucfs%3D1%26%3B&highlighted_hotels=352558&src=hotel&hp_sbox=1&aid=375440&dcid=4&label=yandex-index-bookings-name-lttij8FYuObcClf*PD6hNg-416097532&lang=en-us&sid=564fb73aaca5d4f28e228f0d7df54ce4&si=ai%2Cco%2Cci%2Cre%2Cdi&ss=Arzamas%2C+Nizhny+Novgorod+Oblast%2C+Russia&checkin_monthday=17&checkin_year_month=2015-11&checkout_monthday=18&checkout_year_month=2015-11&room1=A%2CA&no_rooms=1&group_adults=2&group_children=0&ss_raw=arza&dest_type=city&dest_id=-2879690&ac_pageview_id=192f62a8234402ae&ac_position=1&ac_langcode=en&ac_suggestion_list_length=8&place_types=').getroot()
tag = page.find_class('hotellist').pop()

urllist = []

for i in tag.iterlinks():
    if i[2].find('/hotel/ru/') != -1:
        urllist.append("http://www.booking.com" + i[2])
#print (urllist)
hotels = []
for ind, url in enumerate(urllist):
    page1 = html.parse(url)
    root1 = page1.getroot()
    tag1 = root1.find_class('hotel_description_wrapper_exp').pop()
    an = tag1.text_content().strip()
    hotels.append(an)
    print(an)





