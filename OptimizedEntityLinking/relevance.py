from __future__ import division
import wikipedia as wk
import numpy as np
import random
import nltk
import matplotlib.pyplot as plt

def similarity(A, B):
    """Computes the cosine similarity of two vectors
    :param A, B n-dimensional vectors represented as numpy arrays
    :return value between 0 and 1
    """

    a = np.array(A)
    b = np.array(B)

    a_norm = np.linalg.norm(a)
    b_norm = np.linalg.norm(b)

    if a_norm == 0:
        a_norm = 100000
    if b_norm == 0:
        b_norm = 100000

    return np.dot(a, b) / (a_norm * b_norm)

def newTFIDF(keyword, content):
    # total number of wikipedia pages
    D = 5021719
    # approximates number of pages in all of wikipedia
    # in which the keyword appears.
    numberOfSearchResults = len(wk.search(keyword))
    TF = np.sqrt(content.count(keyword))
    IDF = np.log(D / numberOfSearchResults)
    return TF * IDF

def stateTFIDF(state, link):
    """
    Do the for loop, for each keyword. Return list of
    TFIDF values
    """
    keywords = state.keys()
    vals = []
    page = wk.page(link).content.lower()
    for keyword in keywords:
        vals.append(newTFIDF(keyword, page))
    return vals

def inputTFIDF(state):
    # return tfidf(keyword, state.keys())
    text = ' '.join(state.keys()).lower()
    vals = []
    for keyword in state.keys():
        vals.append(newTFIDF(keyword, text))

    return vals

"""
def TFIDF(state, currentKeyword, link):
    # k = currentKeyword
    # p = wikipedia.page(link).content
    # state = {"airplane":(None, 0),"wing":(None, 0)}
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
"""

class RelevanceModel(object):
    """
    Given a link, a keyword, and a current state, how do we figure out if that link is the best fit for that keyword effectively using the context given to us? In our implementation, there is a crucial consideration: we must be able to somehow use previous assigned keywords as factors in our score. This means that given the content of a wikipedia link, we must use the current keyword and the keywords around it to gauge how good of a match that link is to our current keyword.

    This class implements multiple approaches described from literature and
    explained in detail in the report
    """

    @classmethod
    def finalRelevance(self, state, keyword, link):
        A = stateTFIDF(state, link)
        B = inputTFIDF(state)
        return similarity(A, B)

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
    inputText = 'airplane, dog, cat, fish, man, jacket, apple, christmas, theater, pet, napkin, egg, eyebrow, juice, palm tree, island'.split(', ')
    inputLength = [i for i in range(len(inputText))]
    variance = []
    mean = []
    maxscore = []
    for i in range(len(inputText)):
        state = {k:None for k in inputText[0:i]}
        keyword = "airplane"
        scores = []
        for page in wk.search(keyword):
            scores.append(RelevanceModel.finalRelevance(state, keyword, page))
        variance.append(np.var(scores))
        mean.append(np.mean(scores))
        maxscore.append(max(scores))

    # Plotting the relevance score variance vs. input length
    plt.figure(1)
    plt.plot(inputLength, variance, color='#009688')
    plt.figure(2)
    plt.plot(inputLength, mean, color='#FF0000')
    plt.figure(3)
    plt.plot(inputLength, maxscore, color='#00FF00')
    plt.show()


    print variance
    print mean
    print maxscore
