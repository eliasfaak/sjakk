import numpy as np
import os
import chess.pgn
import chess
from state import State
path = "/Users/eliasfakvam/Desktop/AI/gitrepo/gamefiles"
games = os.listdir(path)

print(len(games))
def create_dataset(size):
    X,Y = [], []
    game_number = 0
    for game_name in games:
        pgn = open(os.path.join(path,game_name))
        try:
            game = chess.pgn.read_game(pgn)
        except:
            print(game_name)
            break
        if game is None:
            break
        board = game.board()
        for move in game.mainline_moves():
            pos = State(board).serialize()
            board.push(move)
            mov = State(board).serialize()
            X.append(pos)
            Y.append(mov)
        print("now have {} examples from {} games".format(len(X), game_number))
        print("latest game was{}".format(game_name))
        if len(X) > size:
            return X,Y
        game_number+=1
    X = np.array(X)
    Y = np.array(Y)
    return X,Y

create_dataset(10000000000000)
