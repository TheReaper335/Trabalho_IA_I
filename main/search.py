# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from builtins import object
import util
import copy


class SearchProblem(object):
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
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def uniformCostSearch(problem, heuristic=None):
    # Realiza inicialmente um busca pelo no com menor custo

    #print("Iniciando em:", problem.getStartState())
    #print("O inicio e o objetivo?", problem.isGoalState(problem.getStartState()))
    #print("Iniciar os sucessores:", problem.getSuccessors(problem.getStartState()))

    # Variaveis para verificar se o objetivo foi ou nao atingido
    objectivo = False
    exploredStatesDictionary = util.Counter()  #Dicionario para contabilizar o os estados visitados
    exploredStatesDictionary[0] = problem.getStartState()  #adiciona na posição 0, a posição inicial
    frontierList = problem.getSuccessors(problem.getStartState())  #lista dos estados adjacentes

    # Vetor para listas de chaves
    vectorDictionary = {}
    frontierQueue = util.PriorityQueue()  #Heap dos nós - ordena os estados em ordem crescente do custo(FIFO)
    actionsQueue = []
    addedNodes = []


    for i in frontierList:
        actionsThisFar = copy.deepcopy(actionsQueue)
        successor = str(i[0])
        vectorDictionary[successor] = actionsThisFar

    # Preenchimento da fila com os adjacentes
    for i in frontierList:
        fNode = i        #fNode assume o valor do estado sucessor do actual
        frontierQueue.push(fNode, i[2])
        addedNodes.append(fNode[0])

    seenAlready = 1

    # Ciclo para visitar estados
    while (objectivo == False):
        for i in addedNodes:
            popped = addedNodes.pop()
            exploredStatesDictionary[seenAlready] = popped
            seenAlready = seenAlready + 1

        tempState = frontierQueue.pop()  #retorna o estado com menor custo
        previousCost = tempState[2]
        nextState = tempState[0]    #O próximo estado será o estado com menor custo


        # Salva os estados ja explorados
        exploredStatesDictionary[seenAlready] = nextState #Se adiciona o estado com menor custo ao dicionário de estados visitados
        seenAlready = seenAlready + 1

        reset = str(tempState[0])

        newActionsList = vectorDictionary[reset]
        newActionsList.append(tempState[1])

        # Esvazia a lista de acoes antigas
        actionsQueue = copy.deepcopy(newActionsList)
        currentState = nextState


        # Checa se a meta ja foi atingida
        if (problem.isGoalState(currentState)):
            objectivo = True

        else:
            frontierList = problem.getSuccessors(currentState)
            for i in frontierList:
                explored = False
                counter = 0
                for k in exploredStatesDictionary:
                    stateCo = exploredStatesDictionary[k]

                    if ((i[0] == stateCo)):

                        explored = True
                        counter = counter + 1

                    elif ((explored == False) and (k == ((len(exploredStatesDictionary))) - 1)):

                        actionsThisFar = copy.deepcopy(actionsQueue)
                        successor = str(i[0])
                        vectorDictionary[successor] = actionsThisFar
                        fNode = i
                        newCost = i[2] + previousCost
                        fNode = list(fNode)

                        # update
                        fNode[2] = newCost

                        # back to tuple
                        fNode = tuple(fNode)
                        frontierQueue.push(fNode, newCost)
                        addedNodes.append(fNode[0])

    length = len(actionsQueue)
    return actionsQueue
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
