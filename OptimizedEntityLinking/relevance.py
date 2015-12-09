import wikipedia as wk
import numpy as np
import random
import matplotlib.pyplot as plt
import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer


stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))


class RelevanceModel(object):
    """
    Given a link, a keyword, and a current state, how do we figure out if that link is the best fit for that keyword effectively using the context given to us? In our implementation, there is a crucial consideration: we must be able to somehow use previous assigned keywords as factors in our score. This means that given the content of a wikipedia link, we must use the current keyword and the keywords around it to gauge how good of a match that link is to our current keyword.
    This class implements multiple approaches described from literature and
    explained in detail in the report
    """

    @classmethod
    def linkRelevance(self, inputKeywords, page):
        inputText = ' '.join(inputKeywords)

        # try:
        #     linkText = wk.page(link, auto_suggest=False).content.lower()
        # except wk.exceptions.DisambiguationError as e:
        #     options = filter(lambda x: "(disambiguation)" not in x, e.options)
        #     linkText = wk.page(options[0], auto_suggest=False).content.lower()
        linkText = page
        vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')
        tfidf = vectorizer.fit_transform([inputText, linkText])
        return ((tfidf * tfidf.T).A)[0,1]

    @classmethod
    def documentRelevance(self, page1, page2):

        # try:
        #     linkText1 = wk.page(link1, auto_suggest=False).content.lower()
        # except wk.exceptions.DisambiguationError as e:
        #     options = filter(lambda x: "(disambiguation)" not in x, e.options)
        #     linkText1 = wk.page(options[0], auto_suggest=False).content.lower()

        # try:
        #     linkText2 = wk.page(link2, auto_suggest=False).content.lower()
        # except wk.exceptions.DisambiguationError as e:
        #     options = filter(lambda x: "(disambiguation)" not in x, e.options)
        #     linkText2 = wk.page(options[0], auto_suggest=False).content.lower()
        linkText1 = page1
        linkText2 = page2
        vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')
        tfidf = vectorizer.fit_transform([linkText1, linkText2])
        return ((tfidf * tfidf.T).A)[0,1]
