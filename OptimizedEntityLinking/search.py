import util
import random
from copy import deepcopy
from relevance import RelevanceModel
import wikipedia as wk

class LocalSearch(object):
    """Implements a local search algorithm"""
    def __init__(self, keywords):
        self.keywords = keywords
        self.cachedPages = {}

    def run(self):
        return self.getInitialState()

    def getInitialState(self):
        """
        This returns an complete initial assignment by assigning each
        keyword a link with the highest relevance score between the link's
        content and the input text
        """
        initialState = {}
        for keyword in self.keywords:
            (link, score) = self.getMaxRelevance(keyword.lower())
            initialState[keyword.lower()] = (link, score)
        return initialState

    def getMaxRelevance(self, keyword):
        """For every possible candidate link for a keyword, obtain the link's
        relevance score to the keyword's context and return the highest
        scoring link along with its relevance score"""
        relevances = []
        for candidateLink in wk.search(keyword):
            score = RelevanceModel.relevance(self.keywords, candidateLink)
            relevances.append((candidateLink, score))

        # Returns the tuple with the highest relevance score in the array
        return max(relevances, key=lambda x:x[1])
