__author__ = '315-9'

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import fetch_20newsgroups
t_ngrams = TfidfVectorizer()
dataset = fetch_20newsgroups(categories = ['alt.atheism', 'talk.religion.misc', 'sci.space'])
print(len(dataset.data))
labels = dataset.target
X = t_ngrams.fit_transform(dataset.data).toarray()
print (X)
def cosine_distance(t, p):
    import math,numpy
    n = numpy.dot(t, p) / (math.sqrt(numpy.dot(t, t)) * math.sqrt(numpy.dot(p, p)))
    return n
res = X.transpose()
dist = []
for i in res:
    for j in res:
        print (cosine_distance(i,j))
        dist.append(cosine_distance(i,j))
print (dist)
