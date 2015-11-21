# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 20:10:45 2015

@author: Alisa
"""

from lxml import etree
#root = etree.Element('team_info')
movie_list = open('output_Disney.txt').readlines()
root = etree.Element('Disney_movies')

for i, movie in enumerate(movie_list):
    
    s = movie.split('\t')
    
    SubEl = etree.SubElement(root, 'movie')
    
    tag1 = etree.SubElement(SubEl, 'link')
    tag1.text = s[0]
    
    tag2 = etree.SubElement(SubEl, 'title')
    tag2.text = s[1]
    
    tag3 = etree.SubElement(SubEl, 'year')
    tag3.text = s[2]
    
    tag4 = etree.SubElement(SubEl, 'plot_summary')
    tag4.text = s[3].decode()
    

Disney_xml = etree.tostring(root, pretty_print=True)

f = open('Tsyplyaeva_xml (HW 4).xml', 'w')
f.write(Disney_xml)
f.close() 