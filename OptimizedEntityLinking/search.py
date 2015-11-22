import util
import random
from copy import deepcopy
import relevance
import wikipedia as wk

class SearchAgent(object):
    """breadth first search algorithm for entity linking"""
    def __init__(self, words):
        self.initialState = words

    def isGoalState(self, state):
        """
        A goal state is reached when every word has a link that has at least
        0.5 relevance
        """
        assignments = state.values()
        for link, relevanceScore in state.values():
            if relevanceScore < 0.5:
                return False
        return True


    def mostConstrained(self, state):
        """Gets the variable with the most assignments constraining it.
        the one that has the smallest state space of possible links it could
        take"""
        keywords = state.keys()
        return random.choice(keywords)

    def getSuccessors(self, state):
        """
        Returns a list of successors where each item is a triple containing
        the most constrained keyword in the state, a wikipedia page that could be
        assigned to it, and the relevance score of that wikipedia page to that
        keyword

        Example: state = {'airplane':(None, 0)}
        return [('airplane', 'www.wikipedia.org/Airplane', 0.9),
                ('airplane', 'www.wikipedia.org/Jefferson_Airplane_Accident', 0.3)]
        """
        mostConstrained = self.mostConstrained(state)

        successors = []
        for wikipediaPage in wk.search(mostConstrained):
            relevanceScore = relevance.relevanceFunction(mostConstrained, wikipediaPage)
            assignment = (mostConstrained, wikipediaPage, relevanceScore)
            successors.append(assignment)

        return successors

    def depthFirstSearch(self):
        """
        Search the deepest nodes in the search tree first
        """
        initialState = self.initialState
        explored = []
        frontier = []
        frontier.append(initialState)


        while frontier:
            currentState = frontier.pop()
            if currentState not in explored:

                explored.append(currentState)

                if self.isGoalState(currentState):
                    return currentState

                # Gets the possible actions for the most constrained word
                for successor in self.getSuccessors(currentState):

                    nextState = deepcopy(currentState)
                    mostConstrained = successor[0]
                    assignment = successor[1]
                    relevanceScore = successor[2]

                    nextState[mostConstrained] = (assignment, relevanceScore)
                    if nextState not in frontier:
                        frontier.append(nextState)
        return []


    def breadthFirstSearch(self):
        """
        Search the shallowest nodes in the search tree first.
        """
        initialState = self.initialState
        explored = []
        frontier = []
        frontier.insert(0, initialState)

        while len(frontier) != 0:
            currentState = frontier.pop()

            if currentState not in explored:

                explored.append(currentState)

                if self.isGoalState(currentState):
                    return currentState

                # Gets the possible actions for the most constrained word
                for successor in self.getSuccessors(currentState):

                    nextState = deepcopy(currentState)
                    mostConstrained = successor[0]
                    assignment = successor[1]

                    nextState[mostConstrained] = (assignment, 0)


                    frontier.insert(0, nextState)
                    print frontier
        return []


    def uniformCostSearch(self):
        "Search the node of least total cost first. "
        start_node = (self.getStartState(), [], 0)
        explored = []
        frontier = util.PriorityQueue()
        start_cost = 0
        frontier.push(start_node, start_cost)

        if self.isGoalState(self.getStartState()):
            return []

        while not frontier.isEmpty():
            (current_state, actions, costs) = frontier.pop()

            if current_state not in explored:
                explored.append(current_state)
                if self.isGoalState(current_state):
                    return actions
                for child_node in self.getSuccessors(current_state):
                    next_state = child_node[0]
                    next_action = child_node[1]
                    next_cost = child_node[2]

                    g = self.getCostOfActions(actions + [next_action])

                    next_node = (next_state, actions + [next_action], g)
                    frontier.push(next_node, g)
        return []

    def aStarSearch(self, heuristic=util.nullHeuristic):
        "Search the node that has the lowest combined cost and heuristic first."

        start_node = (self.getStartState(), [], 0)
        explored = []
        frontier = util.PriorityQueue()
        start_cost = heuristic(self.getStartState(), problem)
        frontier.push(start_node, start_cost)

        if self.isGoalState(self.getStartState()):
            return []

        while not frontier.isEmpty():
            (current_state, actions, costs) = frontier.pop()
            if current_state not in explored:
                explored.append(current_state)
                if self.isGoalState(current_state):
                    return actions
                for child_node in self.getSuccessors(current_state):
                    next_state = child_node[0]
                    next_action = child_node[1]
                    next_cost = child_node[2]

                    g = problem.getCostOfActions(actions + [next_action])
                    h = heuristic(next_state, problem)
                    g_h = g + h

                    next_node = (next_state, actions + [next_action], costs + next_cost)
                    frontier.push(next_node, g_h)
        return []
