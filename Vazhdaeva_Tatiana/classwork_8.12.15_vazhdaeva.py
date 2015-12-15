__author__ = '123'
from sklearn.database import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from math import fabs
i = 2
j = 1
dataset = fetch_20newsgroups(categories = ['alt.atheism','talk.religion.misc', 'sci.space'])
vector = TfidfVectorizer()
X = vector.fit_transform(dataset.data).toarray()
temp = []
for k in range (X.shape[0]):
    temp.append(fabs(X[k][i] - X[k][j]))
res = object
for x in temp:
    res += x
print (res)
