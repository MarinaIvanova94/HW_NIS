#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Kozlova, Bazanova
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy
from sklearn.datasets import fetch_20newsgroups
import math

dataset = fetch_20newsgroups(categories = ['alt.atheism','sci.space'])

vect = TfidfVectorizer()
M = vect.fit_transform(dataset.data).toarray()

trans = M.transpose()
distance = []

for i in range(len(trans)):
    for j in trans[i]:
        MAN = abs(trans[i][j]- trans[i][j]) + abs(trans[i][j]- trans[j][j])
print ("RESULT", MAN)
