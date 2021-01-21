import pygame as pg
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
    IMAGES[piece] = p.transform.slace(p.image.load("brikker/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
