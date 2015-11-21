import util

class SearchAgent(object):
    """breadth first search algorithm for entity linking"""
    def __init__(self, words):
        self.words = words

    def breadthFirstSearch(self):
        """
        Search the shallowest nodes in the search tree first.
        """
        start_node = (self.getStartState(), [], 0)
        explored = []
        frontier = util.Queue()
        frontier.push(start_node)

        if self.isGoalState(self.getStartState()):
            return []

        while not frontier.isEmpty():
            (current_state, actions, costs) = frontier.pop()
            if current_state not in explored:
                explored.append(current_state)
                if problem.isGoalState(current_state):
                    return actions
                for child_node in self.getSuccessors(current_state):
                    next_state = child_node[0]
                    next_action = child_node[1]
                    next_cost = child_node[2]

                    next_node = (next_state, actions + [next_action], costs + next_cost)
                    frontier.push(next_node)
        return []

    def depthFirstSearch(self):
        """
        Search the deepest nodes in the search tree first
        """
        start_node = (self.getStartState(), [], 0)
        explored = []
        frontier = util.Stack()
        frontier.push(start_node)

        if self.isGoalState(self.getStartState()):
            return []

        while not frontier.isEmpty():
            (current_state, actions, costs) = frontier.pop()
            if current_state not in explored:

                explored.append(current_state)
                if self.isGoalState(current_state):
                    return actions
                else:
                    return []

                for child_node in self.getSuccessors(current_state):
                    next_state = child_node[0]
                    next_action = child_node[1]
                    next_cost = child_node[2]

                    next_node = (next_state, actions + [next_action], costs + next_cost)
                    frontier.push(next_node)
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
