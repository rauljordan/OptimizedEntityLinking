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
        A goal state is reached when every word is assigned a link
        """
        assignments = state.values()
        if all(assignments):
            # Checks that every word has a relevance above 0.5
            for word, assignment in state.items():
                if relevance.relevanceFunction(word, assignment) < 0.5:
                    return False
            return True
        return False

    def mostConstrained(self, state):
        """Gets the variable with the most assignments constraining it.
        the one that has the smallest state space of possible links it could
        take"""
        notAssigned = state.keys()
        return random.choice(notAssigned)

    def getSuccessors(self, state):

        mostConstrained = self.mostConstrained(state)

        successors = []
        for wikipediaPage in wk.search(mostConstrained):
            assignment = (mostConstrained, wikipediaPage)
            successors.append(assignment)

        return successors

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

                    nextState[mostConstrained] = assignment


                    frontier.insert(0, nextState)
                    print frontier
        return []

    def depthFirstSearch(self):
        """
        Search the deepest nodes in the search tree first
        """
        initialState = self.initialState
        explored = []
        frontier = []
        frontier.append(initialState)


        while len(frontier) != 0:
            currentState = frontier.pop()
            if currentState not in explored:

                explored.append(currentState)

                print frontier
                if self.isGoalState(currentState):
                    return currentState

                # Gets the possible actions for the most constrained word
                for successor in self.getSuccessors(currentState):

                    nextState = deepcopy(currentState)
                    mostConstrained = successor[0]
                    assignment = successor[1]

                    nextState[mostConstrained] = assignment

                    frontier.append(nextState)

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
