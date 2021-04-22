import random
import math
import functools

BOT_NAME = "Astrominimax"


class RandomAgent:
    """Agent that picks a random available move.  You should be able to beat it."""
    def __init__(self, sd=None):
        if sd is None:
            self.st = None
        else:
            random.seed(sd)
            self.st = random.getstate()

    def get_move(self, state):
        if self.st is not None:
            random.setstate(self.st)
        return random.choice(state.successors())


class HumanAgent:
    """Prompts user to supply a valid move."""
    def get_move(self, state, depth=None):
        move__state = dict(state.successors())
        prompt = "Kindly enter your move {}: ".format(sorted(move__state.keys()))
        move = None
        while move not in move__state:
            try:
                move = int(input(prompt))
            except ValueError:
                continue
        return move, move__state[move]


class MinimaxAgent:
    """Artificially intelligent agent that uses minimax to optimally select the best move."""
    
    def get_move(self, state):
        """Select the best available move, based on minimax value."""
        nextp = state.next_player()
        best_util = -math.inf if nextp == 1 else math.inf
        best_move = None
        best_state = None

        for move, state in state.successors():
            util = self.minimax(state)
            if ((nextp == 1) and (util > best_util)) or ((nextp == -1) and (util < best_util)):
                best_util, best_move, best_state = util, move, state
        return best_move, best_state

    def minimax(self, state):
        """Determine the minimax utility value of the given state.
        Args:
            state: a connect383.GameState object representing the current board
        Returns: the exact minimax utility value of the state
        """
        if len(state.successors()) == 0:
            return state.utility()
        optimal_utility = -math.inf if state.next_player() == 1 else math.inf
        for successor in map(lambda x: x[1], state.successors()):
            successor_utility = self.minimax(successor)
            if (state.next_player() == 1 and successor_utility > optimal_utility) or (state.next_player() == -1 and successor_utility < optimal_utility):
                optimal_utility = successor_utility
        return optimal_utility

class MinimaxHeuristicAgent(MinimaxAgent):
    """Artificially intelligent agent that uses depth-limited minimax to select the best move."""

    def __init__(self, depth_limit):
        self.depth_limit = depth_limit

    def minimax(self, state):
        """Determine the heuristically estimated minimax utility value of the given state.
        The depth data member (set in the constructor) determines the maximum depth of the game 
        tree that gets explored before estimating the state utilities using the evaluation() 
        function.  If depth is 0, no traversal is performed, and minimax returns the results of 
        a call to evaluation().  If depth is None, the entire game tree is traversed.
        Args:
            state: a connect383.GameState object representing the current board
        Returns: the minimax utility value of the state
        """
        return self.evaluation(state) if self.depth_limit == 0 else self.recursive_helper_minimax(state, 0)

    
    def recursive_helper_minimax(self, state, depth):
        if depth == self.depth_limit:
            return self.evaluation(state)
        
        if len(state.successors()) == 0:
            return state.utility()
        
        optimal_utility = -math.inf if state.next_player() == 1 else math.inf
        for successor in map(lambda x: x[1], state.successors()):
            successor_utility = self.recursive_helper_minimax(successor, depth + 1)
            if (state.next_player() == 1 and successor_utility > optimal_utility) or (state.next_player() == -1 and successor_utility < optimal_utility):
                optimal_utility = successor_utility
        return optimal_utility
    
    def evaluation(self, state):
        """Estimate the utility value of the game state based on features.
        N.B.: This method must run in O(1) time!
        Args:
            state: a connect383.GameState object representing the current board
        Returns: a heuristic estimate of the utility value of the state
        """
        def adjacency_check(tile_list, player_number, player_value):
            if len(tile_list) == 0 or tile_list.count(0) == 0:
                return 0
            zero = tile_list.index(0)
            left, right = {"index": zero - 1, "count": 0}, {"index": zero + 1, "count": 0}
            while (left["index"] >= 0):
                if tile_list[left["index"]] != player_number:
                    break;
                left["count"] += 1
                left["index"] -= 1
            while (right["index"] < len(tile_list)):
                if tile_list[right["index"]] != player_number:
                    break;
                right["count"] += 1
                right["index"] += 1
            cost = 0 if (left["count"]+right["count"] < 2) else pow(left["count"]+right["count"]+1, 2)
            return cost + adjacency_check(tile_list[zero+1:len(tile_list)],player_number,sum)
        
        state_potential = 0         
        for row in state.get_rows():
            state_potential += adjacency_check(row, 1, 0) - adjacency_check(row, -1, 0)
        for column in state.get_cols():
            state_potential += adjacency_check(column, 1, 0) - adjacency_check(column, -1, 0)
        for diagonal in state.get_diags():
            state_potential += adjacency_check(diagonal, 1, 0) - adjacency_check(diagonal, -1, 0)
            
        state_cost = state.scores()[0] - state.scores()[1]
        
        return 0.5*state_potential + 0.5*state_cost

class MinimaxHeuristicPruneAgent(MinimaxHeuristicAgent):
    """Smarter computer agent that uses minimax with alpha-beta pruning to select the best move."""
        
    def minimax(self, state):
        """Determine the minimax utility value the given state using alpha-beta pruning.

        The value should be equal to the one determined by MinimaxAgent.minimax(), but the 
        algorithm should do less work.  You can check this by inspecting the value of the class 
        variable GameState.state_count, which keeps track of how many GameState objects have been 
        created over time.  This agent should also respect the depth limit like HeuristicAgent.

        N.B.: When exploring the game tree and expanding nodes, you must consider the child nodes
        in the order that they are returned by GameState.successors().  That is, you cannot prune
        the state reached by moving to column 4 before you've explored the state reached by a move
        to to column 1.

        Args: 
            state: a connect383.GameState object representing the current board

        Returns: the minimax utility value of the state
        """
        if self.depth_limit == 0:
            return self.evaluation(state)
        
        return self.recursive_helper_minimax_pruned(state, 0, -math.inf, math.inf)
    
    def recursive_helper_minimax_pruned(self, state, depth, alpha, beta):
        if depth == self.depth_limit:
            return self.evaluation(state)
        
        if len(state.successors()) == 0:
            return state.utility()
        
        optimal_utility = -math.inf if state.next_player() == 1 else math.inf
        for successor in map(lambda x: x[1], state.successors()):
            successor_utility = self.recursive_helper_minimax_pruned(successor, depth + 1, alpha, beta)
            if (state.next_player() == 1 and successor_utility > optimal_utility) or (state.next_player() == -1 and successor_utility < optimal_utility):
                optimal_utility = successor_utility
            if state.next_player() == 1 and alpha < optimal_utility:
                alpha = optimal_utility
            elif state.next_player() == -1 and beta > optimal_utility:
                beta = optimal_utility
            if beta <= alpha:
                break
        return optimal_utility


