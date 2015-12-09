import util
import random
from copy import deepcopy
from relevance import RelevanceModel
import wikipedia as wk

class LocalSearch(object):
    """Implements a local search algorithm"""
    def __init__(self, keywords, cache):
        self.keywords = keywords
        self.cachedPages = cache

    def retrieveCachedPage(self, link):
        for keyword in self.cachedPages.keys():
            for pageTup in self.cachedPages[keyword]:
                if pageTup[0] == link:
                    return pageTup[1]

    def runLocalSearch(self, alpha, iterations):
        state = self.getInitialState()
        print "Initial State Obtained!"
        print state
        print "Running Local Search..."
        for i in range(iterations):
            for keyword in self.keywords:
                candidateLinks = [k[0] for k in self.cachedPages[keyword]]
                assignedLink = state[keyword][0]

                for candidateLink in candidateLinks:
                    candidateDocumentRelevances = []
                    currentAssignmentDocumentRelevances = []
                    context = [v[0] for k, v in state if k != keyword]
                    for otherAssignedLink in context:
                        # Obtain the Document Relevances as a list
                        candidateScore = RelevanceModel.documentRelevance(candidateLink, otherAssignedLink)
                        candidateDocumentRelevances.append(candidateScore)

                        currentLinkScore = RelevanceModel.documentRelevance(candidateLink, assignedLink)
                        currentLinkDocumentRelevances.append(currentLinkScore)

                    # Obtain the LinkRelevances
                    currentLinkRelevance = RelevanceModel.linkRelevance(self.keywords, assignedLink)
                    candidateLinkRelevance = linkRelevance(self.keywords, candidateLink)

                    # Obtain a convex combination of the link relevances and the
                    # sum of the document relevances
                    candidatePsi = (1 - alpha)*candidateLinkRelevance + alpha*sum(candidateDocumentRelevances)
                    currentPsi = (1 - alpha)*currentLinkRelevance + alpha*sum(currentLinkDocumentRelevances)


                    # If the candidate link's convex combination is greater than the current
                    # link's convex combination, we replace that assignment
                    if candidatePsi > currentPsi:
                        state[keyword] = (candidateLink, candidateLinkRelevance)
                        print "Replaced Link"
            print str(i) + "/" + str(iterations) + " iterations complete


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
        candidateLinks = [k[0] for k in self.cachedPages[keyword]]
        for candidateLink in candidateLinks:
            score = RelevanceModel.linkRelevance(self.keywords, candidateLink)
            relevances.append((candidateLink, score))

        # Returns the tuple with the highest relevance score in the array
        return max(relevances, key=lambda x:x[1])
