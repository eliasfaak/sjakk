"""
Denne klassen lagere all informasjonen om posisjonen og lovelige trekk
"""
class GameState():
    def _init_(self):
        self.board = [
        ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"]
        ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"]
        ["--", "--", "--", "--", "--", "--", "--", "--"]
        ["--", "--", "--", "--", "--", "--", "--", "--"]
        ["--", "--", "--", "--", "--", "--", "--", "--"]
        ["--", "--", "--", "--", "--", "--", "--", "--"]
        ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"]
        ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
    self.whiteToMove = True
    self.moveLog
