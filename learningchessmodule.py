import os
import io
import chess
import chess.pgn
from state import State
#pgn = io.StringIO("8/8/8/8/8/8/8/8")
#game = chess.pgn.read_game("8/8/8/8/8/8/8/8")
board = chess.Board("8/8/8/8/8/8/8/8")
fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

#result = game.headers["Result"]

dicttensortofen = {1: "p", 2: "P", 3: "b", 4: "B", 5: "n", 6: "N",
                7: "r", 8: "R", 9: "q", 10: "Q", 11: "k", 12: "K"}
noshred = board.fen()
def fentotensor(fen):
    dictfentotensor = {"p": [1], "P": [2], "b": [3], "B": [4], "n": [5], "N": [6],
                "r": [7], "R": [8], "q" : [9], "Q": [10], "k": [11], "K": [12], "1": [0],
                "2": [0,0], "3": [0,0,0], "4": [0,0,0,0], "5": [0,0,0,0,0], "6": [0,0,0,0,0,0], "7": [0,0,0,0,0,0,0], "8":[0,0,0,0,0,0,0,0]}
    tensor = []
    rows = list(fen.split("/"))
    for row in rows:
        rw = []
        for square in list(row):
            rw = rw+dictfentotensor[square]
        tensor.append(rw)
    return tensor

"""
def tensortofen(tensor):
    fen = " "
    for row in tensor:
        fenrow = " "
        blanks = 0
        for i in range(len(row)):
            if row[i] == 0:
                blanks+=1
            elif blanks > 0:
                fenrow + str(blanks)
                print(fenrow)
            else:
                fenrow + dicttensortofen[row[i]]
                print(fenrow)
        print(fenrow)
        fen = "/"+fenrow
    return fen
test2 = tensortofen(test)
print(test2)
"""
