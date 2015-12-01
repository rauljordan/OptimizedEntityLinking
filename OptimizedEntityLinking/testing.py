from __future__ import division
import wikipedia as wk
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import string
from collections import Counter

def similarity(A, B):
    """Computes the cosine similarity of two vectors
    :param A, B n-dimensional vectors represented as numpy arrays
    :return value between 0 and 1
    """
    a = np.array(A)
    b = np.array(B)

    return np.dot(a, b) / (np.linalg.norm(a)*np.linalg.norm(b))



def get_tokens(link):
    text = wk.page(link).content.encode('utf-8')
    lowers = text.lower()
    #remove the punctuation using the character deletion step of translate
    no_punctuation = lowers.translate(None, string.punctuation)
    tokens = nltk.word_tokenize(no_punctuation)
    return tokens


token_dict = {}
stemmer = PorterStemmer()

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    return tokens

if __name__ == '__main__':

    text = wk.page("Airplane").content.encode("utf-8")
    lowers = text.lower()
    token_dict["Airplane"] = lowers

    tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
    tfs = tfidf.fit_transform(token_dict.values())

    feature_names = tfidf.get_feature_names()
    for col in tfs.nonzero()[1]:
        print feature_names[col], ' - ', tfs[0, col]
