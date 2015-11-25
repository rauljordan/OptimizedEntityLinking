from __future__ import division
import wikipedia


class RelevanceModel(object):
    """
    Given a link, a keyword, and a current state, how do we figure out if that link is the best fit for that keyword effectively using the context given to us? In our implementation, there is a crucial consideration: we must be able to somehow use previous assigned keywords as factors in our score. This means that given the content of a wikipedia link, we must use the current keyword and the keywords around it to gauge how good of a match that link is to our current keyword.

    This class implements multiple approaches described from literature and
    explained in detail in the report
    """
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
    def wlmRelevance(self, keyword, link):
        """
        Implements a variant of the Wikipedia Link Based Measure model as a
        driver for our relevance score as described in literature
        """

    def hmmRelevance(self, state, keyword, link):
        """
        OUR OPTIMIZATION

        Framing the relevance problem as a Hidden Markov Model
        where the emissions are the keywords and the hidden variables is a possible link. We want to find out P(X | E) where this will be our relevance score. The arrows between the values of X are a 'transition score' which will be our value of gamma in this case. We will weigh our relevance score by our transition score accordingly to obtain our final score.

        This frames our problem probabilistically and allows us to use well-understood tools to solve the problem. Also, this optimizes our algorithm from the naive implementations we had before where we picked the most constrained keyword to assign. In this case, we can simply go left to right with our input to discover the best keyword to assign 
        """

if __name__ == '__main__':
    """Including some simple unit tests for naive relevance"""
    print RelevanceModel.naiveRelevance('airplane', 'Airplane')
