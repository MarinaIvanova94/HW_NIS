# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 22:43:32 2015

@author: Alisa
"""

from lxml import etree

tree=etree.parse('Tsyplyaeva_xml (HW 4).xml')
root=tree.getroot()

for elem in root.iter('movie'):
    for i in elem.getchildren():
        if i==elem.find('title') or i==elem.find('year'):
            print(i.text),
    print('\n')
