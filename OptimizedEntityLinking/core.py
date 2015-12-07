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

class EntityLinker(object):
    """Implements the base entity linking class
    that can be called at runtime"""

    def link(self, words):
        print 'Preprocessing Input...'
        processedWords = self.preprocess(words)
        print 'Linking Input...'
        searchAgent = search.LocalSearch(processedWords)
        result = searchAgent.run()
        print self.prettify(result)
        print 'Finished in 10 seconds'

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
        return words.split()


if __name__ == '__main__':
    el = EntityLinker()
    el.link('airplane aircraft')
