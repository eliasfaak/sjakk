import pygame as p
import chessengine
WIDTH = HEIGHT  = 512
DIMENSION = 8
SQ_SIZE = HEIGHT//DIMENSION
MAX_FPS = 15
IMAGES = {}

"""
Metode for å ikke hente bilder flere ganger.
"""
def loadimages():
    pieces = ["wP", "wR", "wN", "wB", "wQ", "wK", "bP", "bR", "bQ", "bB", "bN", "bK"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("/Users/eliasfakvam/Desktop/gitrepo/brikker/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


"""
skal håndtere brukerinput og grafikk
"""
def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = chessengine.GameState()
    loadimages()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

        clock.tick(MAX_FPS)
        p.display.flip()
        drawgamestate(screen, gs)

"""
grafikken
"""
def drawgamestate(screen, gs):
    drawboard(screen) #lager bretter
    drawpieces(screen, gs.board) #lager brikker


def drawboard(screen):
    colors =[p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r+c)%2]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def drawpieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
    main()
