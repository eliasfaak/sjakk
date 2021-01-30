import os
import chess
import chess.pgn
pgn = open("/Users/eliasfakvam/Desktop/AI/gitrepo/gamefiles/{0}game.pgn".format(1))
game = chess.pgn.read_game(pgn)
board = game.board()
for move in game.mainline_moves():
    board.push(move)
    #print(board)
result = game.headers["Result"]
shred = board.shredder_fen()
noshred = board.fen()
print(result, shred, noshred)
