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
        """ RUNS LOCAL SEARCH """
        psiScores = []
        initialState = self.getInitialState()


        for keyword in self.keywords:
            candidateLinks = wk.search(keyword)
            context = [v for k, v in initialState.items() if k != keyword]

            # For that candidate link, compare its page
            # to all the other assigned pages, and keep track of their
            # relevance scores inside of a relevance score
            for candidateLink in candidateLinks:
                for contextLink in context:
                    # score = getTFIDF(candidateLink, contextLink)
                    psiScores.append((candidateLink, 0.999999))

            bestCandidateLink, bestPsiScore  = max(psiScores, key=lambda x: x[1])

            relevanceOfBestCandidateLink = 0.99
            if relevanceOfBestCandidateLink > initialState[keyword][1]:
                # Replace!
                initialState[keyword] = (bestCandidateLink, relevanceOfBestCandidateLink)



        return initialState

    def getInitialState(self):
        """
        This returns an complete initial assignment by assigning each
        keyword a link with the highest relevance score between the link's
        content and the input text
        """
        initialState = {}
        for keyword in self.keywords:
            (link, score) = self.getMaxRelevance(keyword)
            initialState[keyword] = (link, score)
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
