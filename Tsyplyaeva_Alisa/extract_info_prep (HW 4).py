# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 00:10:39 2015

@author: Alisa
"""

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
title_list = []
year_list = []

for url in url_list:
    page1 = html.parse(url)
    root1 = page1.getroot()
    tag1 = root1.find_class('plot').pop()
    tag2 = root1.xpath('/html/body/div[2]/div/h3').pop()    
    tag3 = root1.xpath('/html/body/div[3]/div/div/div[1]/div[2]/div/div[2]/span[1]').pop()


    annonce_list.append(tag1.text_content()) 
    title_list.append(tag2.text_content()) 
    year_list.append(tag3.text_content()) 


f = open('output_Disney.txt', 'w')    

for i in range(len(url_list)):
    f.write(url_list[i] + '\t')
    f.write(title_list[i] + '\t')
    f.write(year_list[i]  + '\t')
    try:
        f.write(annonce_list[i].decode() + '\n')
    except:
        f.write('\n')
        continue
f.close()



