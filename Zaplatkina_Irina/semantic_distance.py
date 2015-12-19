__author__ = 'admin'
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidVectorizer
from math import fabs

i = 2
j = 1
dataset = fetch_20newsgroups(categories = ['alt.atheism', 'talk.religion.misc', 'sci.space'])
vector = TfidVectorizer()
X = vector.fit_transform(dataset.data).toarray()
a = []
for c in range(X.shape[0]):
    a.append(fabs(X[c][i] - X[c][j]))
result = 0
for x in a:
    result += x
print (result)