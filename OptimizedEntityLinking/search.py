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
        print "Running Local Search for " + str(iterations) + " iterations..."
        for i in range(iterations):
            for keyword in self.keywords:
                print
                print "Analyzing the keyword " + keyword
                candidateLinks = [k[0] for k in self.cachedPages[keyword]]
                assignedLink = state[keyword][0]

                for candidateLink in candidateLinks:
                    # Use Cache. duh.
                    assignedPage = self.retrieveCachedPage(assignedLink)
                    candidatePage = self.retrieveCachedPage(candidateLink)

                    candidateDocumentRelevances = []
                    currentLinkDocumentRelevances = []
                    context = [v[0] for k, v in state.items() if k != keyword]
                    print "entering loop"
                    for otherAssignedLink in context:
                        # get cached page
                        otherAssignedPage = self.retrieveCachedPage(candidateLink)

                        # Obtain the Document Relevances as a list
                        candidateScore = RelevanceModel.documentRelevance(candidatePage, otherAssignedPage)
                        candidateDocumentRelevances.append(candidateScore)

                        currentLinkScore = RelevanceModel.documentRelevance(candidatePage, assignedPage)
                        currentLinkDocumentRelevances.append(currentLinkScore)

                    # Obtain the LinkRelevances
                    print "getting link relevances"
                    assignedPage = self.retrieveCachedPage(assignedLink)
                    candidatePage = self.retrieveCachedPage(candidateLink)
                    currentLinkRelevance = RelevanceModel.linkRelevance(self.keywords, assignedPage)
                    candidateLinkRelevance = RelevanceModel.linkRelevance(self.keywords, candidatePage)
                    # Obtain a convex combination of the link relevances and the
                    # sum of the document relevances
                    candidatePsi = (1 - alpha)*candidateLinkRelevance + alpha*sum(candidateDocumentRelevances)
                    currentPsi = (1 - alpha)*currentLinkRelevance + alpha*sum(currentLinkDocumentRelevances)
                    print
                    print "Current Psi Value " + str(currentPsi) + " For " + assignedLink
                    print "Candidate Link Psi Value " + str(candidatePsi) + " For " + candidateLink

                    # If the candidate link's convex combination is greater than the current
                    # link's convex combination, we replace that assignment
                    if candidatePsi > currentPsi:
                        state[keyword] = (candidateLink, candidateLinkRelevance)
                        print "Replaced Link"
            print str(i + 1) + "/" + str(iterations) + " iterations complete"


        return state

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
