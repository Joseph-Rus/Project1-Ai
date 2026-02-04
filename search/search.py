# search.py
# ---------
# Worked on by: Elijah Tabor and Joey Russell


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from util import Stack  # Use the provided Stack


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    from util import Stack  # Use the provided Stack

    explored = []
    unexpanded = Stack()
    Start = problem.getStartState()

    # this will get the start sate like (5,4) and then it will get the action like north or south
    unexpanded.push((Start,[]))
    
    
    while not unexpanded.isEmpty():
        # this will pop the last element in the stack and remove the state and the action from it
        state, actions = unexpanded.pop()
        
        if problem.isGoalState(state):
            # we will return the path that we took like the in the [] actions so we are storing the actions in a list
            return actions
        if state in explored: # if we have already been to this state, skip it
            continue
        explored.append(state)
        
        ## we need to store the successors of the current state so we will call the getSuccessors function on the problem
        successors = problem.getSuccessors(state)
        for successor in successors:
            nextState = successor[0]
            action = successor[1]
            #cost = successor[2]
            
            if nextState not in explored:
                newActions = actions + [action]
                unexpanded.push((nextState, newActions))
    return []
    
    # print("Start State: " + str(problem.getStartState()))
    # print("Is the start state ( " + str(problem.getStartState()) + " ) a goal?: " + str(problem.isGoalState(problem.getStartState()))) 
    
    # print("Successor function of initial start state ( " + str(problem.getStartState()) + " ) yields a tuple with 3 pieces:")
    # print("\t(nextState, actionFromCurrStateToNextState, costToGetFromCurrStateToNextState)")
    # for statePortion in problem.getSuccessors(problem.getStartState()):
    #     print("\t" + str(statePortion))
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start State: " + str(problem.getStartState()))
    print("Is the start state ( " + str(problem.getStartState()) + " ) a goal?: " + str(problem.isGoalState(problem.getStartState())))
    
    # Demonstrate how successor function works
    print("Successor function of initial start state ( " + str(problem.getStartState()) + " ) yields a tuple with 3 pieces:")
    print("\t(nextState, actionFromCurrStateToNextState, costToGetFromCurrStateToNextState)")
    for statePortion in problem.getSuccessors(problem.getStartState()):
        print("\t" + str(statePortion))
    """
    
    
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    from util import Queue  # Use the provided Queue
    
    explored = []
    unexpanded = Queue()
    Start = problem.getStartState()
    
    # Push the start state with an empty action list
    unexpanded.push((Start, []))
    
    while not unexpanded.isEmpty():
        # Pop the first element in the queue
        state, actions = unexpanded.pop()
        
        if problem.isGoalState(state):
            return actions
        
        if state in explored:
            continue
            
        explored.append(state)
        
        # Get successors of the current state
        successors = problem.getSuccessors(state)
        for successor in successors:
            nextState = successor[0]
            action = successor[1]
            
            if nextState not in explored:
                newActions = actions + [action]
                unexpanded.push((nextState, newActions))
    
    return []

def uniformCostSearch(problem):
    from util import PriorityQueue  # Use the provided Queue
    
    # Initialize
    explored = []  # or set()
    unexplored = PriorityQueue()
    totalCost = 0
    
    startState = problem.getStartState()
    unexplored.push((startState, [], 0), 0)  # (state, path, cost) - path starts empty
    
    while not unexplored.isEmpty():
        # Pop current node
        currentState, currentPath, currentCost = unexplored.pop()
        
        # Check if goal
        if problem.isGoalState(currentState):
            return currentPath  # Return the path of actions!
        
        # Skip if already explored
        if currentState in explored:
            continue
            
        # Mark as explored
        explored.append(currentState)
        
        # Get successors
        successors = problem.getSuccessors(currentState)
        
        # THIS IS WHERE YOUR CODE GOES:
        for successor in successors:
            nextState = successor[0]
            action = successor[1]
            cost = successor[2] # Added for UCS
            
            if nextState not in explored:
                newPath = currentPath + [action] # Build the path
                newCost = currentCost + cost  # Add to queue
                unexplored.push((nextState, newPath, newCost), newCost)  # Add to priority queue with cost
    
    return []  # No solution found

    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    from util import PriorityQueue  # Use the provided Queue
    
    # Initialize
    explored = []  # or set()
    unexplored = PriorityQueue()
    
    startState = problem.getStartState()
    heuristicCost = heuristic(startState, problem)
    unexplored.push((startState, [], 0), heuristicCost)  # (state, path, cost) - path starts empty
    
    while not unexplored.isEmpty():
        # Pop current node
        currentState, currentPath, currentCost = unexplored.pop()
        
        # Check if goal
        if problem.isGoalState(currentState):
            return currentPath  # Return the path of actions!
        
        # Skip if already explored
        if currentState in explored:
            continue
            
        # Mark as explored
        explored.append(currentState)
        
        # Get successors
        successors = problem.getSuccessors(currentState)
        
        # THIS IS WHERE YOUR CODE GOES:
        for successor in successors:
            nextState = successor[0]
            action = successor[1]
            cost = successor[2] # Added for UCS
            
            if nextState not in explored:
                newPath = currentPath + [action] # Build the path
                newCost = currentCost + cost  # Add to queue
                heuristicCost = newCost + heuristic(nextState, problem)  # f(n) = g(n) + h(n)
                unexplored.push((nextState, newPath, newCost), heuristicCost)  # Add to priority queue with f(n)
    
    return []  # No solution found
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
