from Tile import Tile


class Agent:
    MIN_VALUE = -1000000
    MAX_VALUE = 1000000

    def __init__(self, game, color, max_depth):
        self.game = game
        self.color = color
        self.max_depth = max_depth

    def do_min_max(self, current_board):
        alpha = self.MIN_VALUE
        beta = self.MAX_VALUE
        move, value = self.max(current_board, self.color, 0, alpha, beta)
        return move

    def max(self, current_board, current_color, depth, alpha, beta):
        if self.game.check_terminal(current_board, current_color):
            return None, self.game.evaluate(current_board, current_color, -1000)

        if depth == self.max_depth:
            return None, self.game.evaluate(current_board, current_color)

        possible_moves = self.game.generate_all_possible_moves(current_board, current_color)
        best_move = None
        best_value = self.MIN_VALUE

        for move in possible_moves:
            temporary_move, value = self.min(current_board.next_board(current_color, move),
                                             self.game.opponent(current_color), depth + 1, alpha, beta)

            if value > best_value:
                best_value = value
                best_move = move

            if best_value >= beta:
                return best_move, best_value

            if best_value > alpha:
                alpha = best_value

        return best_move, best_value

    def min(self, current_board, current_color, depth, alpha, beta):
        if self.game.check_terminal(current_board, current_color):
            return None, self.game.evaluate(current_board, current_color, 1000)

        if depth == self.max_depth:
            return None, self.game.evaluate(current_board, current_color)

        possible_moves = self.game.generate_all_possible_moves(current_board, current_color)
        best_move = None
        best_value = self.MAX_VALUE

        for move in possible_moves:
            temporary_move, value = self.max(current_board.next_board(current_color, move),
                                             self.game.opponent(current_color), depth + 1, alpha, beta)

            if value < best_value:
                best_value = value
                best_move = move

            if best_value <= alpha:
                return best_move, best_value

            if best_value < beta:
                beta = best_value

        return best_move, best_value
