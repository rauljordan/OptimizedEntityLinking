from __future__ import division
import wikipedia as wk
import numpy as np
import random
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

def similarity(A, B):
    """Computes the cosine similarity of two vectors
    :param A, B n-dimensional vectors represented as numpy arrays
    :return value between 0 and 1
    """
    a = np.array(A)
    b = np.array(B)

    return np.dot(a, b) / (np.linalg.norm(a)*np.linalg.norm(b))


def TFIDF(state, currentKeyword, link):
    """
    k = currentKeyword
    p = wikipedia.page(link).content
    state = {"airplane":(None, 0),"wing":(None, 0)}
    """
	# TF = sqrt(frequency of k in p)
    p = wk.page(link).content.encode('utf-8').split()
    TF = np.sqrt(p.count(currentKeyword))

    context = [keyword for keyword in state.keys() if keyword != currentKeyword]
    D = 0
    relevants = 0
    for key in context:
        candidateLinks = wk.search(key)
        D = len(candidateLinks)
        for candidate in candidateLinks:
            try:
                page = wk.page(candidate, auto_suggest=True)
            except wk.exceptions.DisambiguationError as e:
                page = wk.page(random.choice(e.options))

            if key in page.content.encode('utf-8').split():
                relevants += 1

    # add 1 to relevants and D to prevent log of -inf
    IDF = np.log((D + 1 ) / (relevants + 1))


    return TF * IDF




class RelevanceModel(object):
    """
    Given a link, a keyword, and a current state, how do we figure out if that link is the best fit for that keyword effectively using the context given to us? In our implementation, there is a crucial consideration: we must be able to somehow use previous assigned keywords as factors in our score. This means that given the content of a wikipedia link, we must use the current keyword and the keywords around it to gauge how good of a match that link is to our current keyword.

    This class implements multiple approaches described from literature and
    explained in detail in the report
    """

    @classmethod
    def finalRelevance(self, keyword, link):
        tfidf = TfidfVectorizer(stop_words='english')

        weightedInput = tfidf.transform([keyword])
        #weightedPage = tfidfvectorizer(page(keyword).content)
        print weightedInput
        #return similarity(weightedInput, weightedPage)


    @classmethod
    def naiveRelevance(self, state, keyword, link):
        # get associated page:
    	p = wikipedia.page(link)

    	# get content as a list of all words in page
    	content = p.content.encode('utf-8').split()

    	# get number of times keyword and other keywords appear
        # in the cintent
    	appears = content.count(keyword)

    	# return ratio of how often word appears to total length
    	# of the content. Will always return a very small relevance
    	return appears / len(content)

    @classmethod
    def fname(arg):
        pass

if __name__ == '__main__':
    """Including some simple unit tests for naive relevance"""
    print TFIDF({"airplane":None, "wing":None}, 'airplane', 'Airplane')
    #print TFIDF('airplane', None)
