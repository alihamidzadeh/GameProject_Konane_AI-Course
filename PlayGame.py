from PlayKonane import PlayKonane
from Tile import Tile
from Agent import Agent
from Board import Board
from KonaneGame2 import KonaneGame2 as KonaneGame


class PlayGame:

    def __init__(self):
        NotImplemented

    def play(self):
        size = 4
        game = KonaneGame()
        initial_board = Board(size, game.initialize_board(size))
        agent1 = Agent(game, color=Tile.P_Black, max_depth=6)
        agent2 = Agent(game, color=Tile.P_White, max_depth=6)
        # bot vs bot
        play = PlayKonane(initial_board, game, agent1=agent1, agent2=agent2)

        # player vs bot
        #play = PlayKonane(initial_board, game, agent1=agent2)


if __name__ == '__main__':
    PlayGame().play()
