"""
Raul Jordan, Sameer Mehra, Melissa Lee
Optimized Entity Linking
core.py

Contains all core logic and entry to the entity-linking
system and provides a class that encapsulates the logic
of the classical search formulation, as well as
access to the different relevance function classes
"""

# import nltk

class BreadthFirstSearchLinker(object):
    """breadth first search algorithm for entity linking"""
    def __init__(self, words):
        self.words = words

    def search(self):
        frontier = []
        explored = []
        frontier.append(self.words)
        while frontier:
            node = frontier.pop()
            for child in self.relevance(node):
                



class EntityLinker(object):
    """Implements the base entity linking class
    that can be called at runtime"""
    def __init__(self, relevanceFun=None, searchFun='bfs'):
        self.relevanceFun = relevanceFun
        self.searchFun = searchFun

    def link(self, words):
        print 'Preprocessing Input...'
        self.words = self.preprocess(words)
        print 'Linking Input...'
        if self.searchFun == 'bfs':
            bfsLinker = BreadthFirstSearchLinker(words)
            result = bfsLinker.search()
            print result
        print 'Finished in 10 seconds'

    def preprocess(self, words):
        """Preprocesses the input string to obtain an array
        of tuples where each word is initially linked to None. This is the initial state of our classical search problem formulation
        """
        return [(word, None) for word in words.split()]


if __name__ == '__main__':
    el = EntityLinker('bfs')
    el.link('airplanes are wonderful')
