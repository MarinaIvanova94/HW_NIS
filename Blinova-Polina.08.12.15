__author__ = 'Polina'
from sklearn.datasets import fetch_20newsgroups
dataset=fetch_20newsgroups()
from sklearn.feature_extraction.text import TfidfVectorizer

vect = TfidfVectorizer()
tok=vect.build_tokenizer()
texts=[]

Y=vect.fit_transform(dataset.data)
first=Y.getcol(0)
second=Y.getcol(1)
word1=[]
for i, el in enumerate(first):
    word1.append(first._get_single_element(i,0))
    word2=[]
for i, el in enumerate(second):
    word2.append(second._get_single_element(i,0))

distance=0
for i in range(len(word2)):
    
    distance+=absmod=word1[i]-word2[i](mod)
print(distance)
