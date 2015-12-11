"""
Raul Jordan, Sameer Mehra, Melissa Lee
Optimized Entity Linking
core.py

Contains all core logic and entry to the entity-linking
system and provides a class that encapsulates the logic
of the classical search formulation, as well as
access to the different relevance function classes
"""

from search import LocalSearch
import nltk
import cache
import argparse

class EntityLinker(object):
    """Implements the base entity linking class
    that can be called at runtime"""
    def __init__(self, alpha, iterations):
        self.alpha = alpha
        self.iterations = iterations

    def link(self, words):
        print 'Preprocessing Input...'
        processedWords = self.preprocess(words)
        print 'Caching Possible Wikipedia Pages For Faster Runtime...'
        c = cache.getCache(processedWords)
        print 'Linking Initial Input...'
        searchAgent = LocalSearch(processedWords, c)
        result = searchAgent.runLocalSearch(self.alpha, self.iterations)
        #print self.prettify(result)
        print result
        return result

    def prettify(self, state):
        """Prettifies the links in a terminal state"""
        for k, v in state.items():
            wikipediaLink = 'en.wikipedia.org/wiki/' + v[0]
            state[k] = (wikipediaLink, v[1])
        return state

    def preprocess(self, words):
        """Preprocesses the input string to obtain an array
        of tuples where each word is initially linked to None.
        This is the initial state of our classical search problem formulation.

        This needs to find the keywords in our phrase! We need to address this
        issue
        """
        self.raw_words = words

        pos = nltk.pos_tag(words.split())
        keywords = [noun[0] for noun in pos
                    if (noun[1] == 'NNP' or noun[1] == 'NN'
                                        or noun[1] == 'NNS')]

        return keywords


if __name__ == '__main__':
    #el = EntityLinker(0.1, 1)
    #el.link("Thermodynamics is the study of heat")
    parser = argparse.ArgumentParser(description='Link entities to wikipedia pages')
    parser.add_argument('text', metavar='text', type=str,
                   help='input text you wish to provide')
    parser.add_argument('--alpha', default=0.9, type=float,
                   help='optimization parameter alpha (default: 0.9). Try different values to obtain better accuracy of your text linking')
    parser.add_argument('--iterations', default=1, type=int,
                   help='iterations: number of local search iterations to run search for. Default and recommended is 1 for speed purposes')

    args = parser.parse_args()
    el = EntityLinker(args.alpha, args.iterations)
    el.link(args.text)
