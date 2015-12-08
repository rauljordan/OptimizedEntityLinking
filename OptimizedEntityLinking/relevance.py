from __future__ import division
import wikipedia as wk
import numpy as np
import random
import nltk
import matplotlib.pyplot as plt
from util import similarity


def newTFIDF(keyword, content):
    # total number of wikipedia pages
    D = 5021719
    # approximates number of pages in all of wikipedia
    # in which the keyword appears.
    numberOfSearchResults = len(wk.search(keyword))
    TF = np.sqrt(content.count(keyword))
    IDF = np.log(D / numberOfSearchResults)
    return TF * IDF

def candidateLinkTFIDF(keywords, link):
    """
    Do the for loop, for each keyword. Return list of
    TFIDF values
    """
    TFIDFvals = []
    try:
        page = wk.page(link, auto_suggest=True).content.lower()
    except wk.exceptions.DisambiguationError as e:

        options = filter(lambda x: "(disambiguation)" not in x, e.options)
        print options
        page = wk.page(random.choice(options), auto_suggest=True).content.lower()

    for keyword in keywords:
        TFIDFvals.append(newTFIDF(keyword, page))
    return TFIDFvals

def keywordsTFIDF(keywords):
    text = ' '.join(keywords).lower()
    TFIDFvals = []
    for keyword in keywords:
        score = newTFIDF(keyword, text)
        TFIDFvals.append(score)
    return TFIDFvals



class RelevanceModel(object):
    """
    Given a link, a keyword, and a current state, how do we figure out if that link is the best fit for that keyword effectively using the context given to us? In our implementation, there is a crucial consideration: we must be able to somehow use previous assigned keywords as factors in our score. This means that given the content of a wikipedia link, we must use the current keyword and the keywords around it to gauge how good of a match that link is to our current keyword.
    This class implements multiple approaches described from literature and
    explained in detail in the report
    """

    @classmethod
    def relevance(self, keywords, link):
        A = candidateLinkTFIDF(keywords, link)
        B = keywordsTFIDF(keywords)
        return similarity(A, B)


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
