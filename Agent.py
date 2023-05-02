from Tile import Tile


class Agent:
    MIN_VALUE = -1000000
    MAX_VALUE = 1000000

    def __init__(self, game, color, max_depth):
        self.game = game
        self.color = color
        self.max_depth = max_depth

    def do_min_max(self, current_board):
        move, value = self.max(current_board, self.color, 0)
        return move

    def max(self, current_board, current_color, depth):
        NotImplemented

    def min(self, current_board, current_color, depth):
        NotImplemented
