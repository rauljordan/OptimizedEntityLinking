
# from sklearn.feature_extraction.text import TfidfVectorizer

# vect = TfidfVectorizer(sublinear_tf=True, analyzer='word',
#            stop_words='english')

# documents = ["hello world this is awesome", "this is another page of wikipedia hello so awesome"]

# response = vect.fit_transform(documents)

# doc1 = response[0]
# doc2 = response[1]

# print doc1.getnnz()
# print "Now Doc2"
# print doc2.getnnz()

# import numpy as np


import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer


stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]

# import wikipedia as wk 
# inc = wk.page('Apple Inc.').content
# fruit = wk.page('Apple (Fruit)').content
# print cosine_sim('Steve Jobs was a great leader at Apple', inc)
# print cosine_sim('Steve Jobs was a great leader at Apple', fruit)
# print cosine_sim(inc, fruit)






