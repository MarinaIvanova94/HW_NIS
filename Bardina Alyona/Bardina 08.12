__author__ = 'Alena'
from lxml import etree
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import fetch_20newsgroups
from sklearn.decomposition import TruncatedSVD
tfidf_ngrams = TfidfVectorizer()
dataset = fetch_20newsgroups(categories = ['alt.atheism','talk.religion.misc', 'sci.space'])
print(len(dataset.data))
labels = dataset.target
X = tfidf_ngrams.fit_transform(dataset.data).toarray()
print(X)
from sklearn.pipeline import make_pipeline
def cosine_daistance(u,v):
    import math, numpy
    g = numpy.dot(u,v)/(math.sqrt(numpy.dot(u,u)*math.sqrt(numpy.dot(v,v))))
    return g
res=X.transpose()
dist=[]
for i in res:
    for j in res:
        dist.append(cosine_daistance(i,j))
        print (cosine_daistance(i,j))
print (dist)
