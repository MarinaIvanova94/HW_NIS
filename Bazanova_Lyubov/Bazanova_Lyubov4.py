from lxml import etree
import lxml.html as html


page = html.parse("http://wellcomebookprize.org/past-prizes/2015").getroot()
winner = page.find_class("book-highlight book-preview book-winner").pop()

winner_author = winner.xpath('//*[@id="main"]/div/div[2]/h2/a').pop()
print("*******THE WINNER*******\n", winner_author.text_content())
winner_book = winner.xpath('//*[@id="main"]/div/div[2]/p[1]/a').pop()
print("By ", winner_book.text_content())
winner_publisher = winner.xpath('//*[@id="main"]/div/div[2]/p[3]').pop()
print(winner_publisher.text_content().strip())


tag = page.find_class('list-books').pop()
url_list = []
for i in tag.iterlinks():
    if i[2].find('/book/') != -1:
        url_list.append(i[2])

url_list.remove('/book/iceberg')

print("*******SHORTLISTED BOOKS*******")
for url in url_list:
    page1 = html.parse('http://wellcomebookprize.org/{}'.format(url))
    root1 = page1.getroot()
    print(root1.find_class('title').pop().text_content())
    print(root1.find_class('author').pop().text_content())
    print(root1.find_class('publisher').pop().text_content())


titles = root1.find_class('title').pop().text_content()
authors = root1.find_class('author').pop().text_content()
publishers = root1.find_class('publisher').pop().text_content()
root_elem = etree.Element("books")
root = etree.Element("books")

for i in range(len(titles)):
    book = etree.SubElement(root, "book")
    etree.SubElement(book, "title").text = titles[i]
    etree.SubElement(book, "author").text = authors[i]
    etree.SubElement(book, "publisher").text = publishers[i]
output = etree.tostring(root, pretty_print=True, encoding='UTF-8')
f1 = open('output.xml', 'w')
f1.write(output.decode('utf-8'))
print(output)
f1.close()
