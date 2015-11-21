"""
Raul Jordan, Sameer Mehra, Melissa Lee
Optimized Entity Linking
core.py

Contains all core logic and entry to the entity-linking
system and provides a class that encapsulates the logic
of the classical search formulation, as well as
access to the different relevance function classes
"""

import search
import relevance

class EntityLinker(object):
    """Implements the base entity linking class
    that can be called at runtime"""
    def __init__(self, searchFun='bfs'):
        self.searchFun = searchFun

    def link(self, words):
        print 'Preprocessing Input...'
        self.words = self.preprocess(words)
        print 'Linking Input...'
        if self.searchFun == 'bfs':
            searchAgent = search.SearchAgent(self.words)
            result = searchAgent.breadthFirstSearch()
            print result
        if self.searchFun == 'dfs':
            searchAgent = search.SearchAgent(self.words)
            result = searchAgent.depthFirstSearch()
            print result
        print 'Finished in 10 seconds'

    def preprocess(self, words):
        """Preprocesses the input string to obtain an array
        of tuples where each word is initially linked to None.
        This is the initial state of our classical search problem formulation.

        This needs to find the keywords in our phrase! We need to address this
        issue
        """
        return {word: None for word in words.split()}


if __name__ == '__main__':
    el = EntityLinker('dfs')
    el.link('airplane wing dog')
