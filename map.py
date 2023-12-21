import pygame as pg
import math
from settings import *


class map:
    def __init__(self, map, squareSize=150):
        self.map = map
        self.sizeY = len(map)
        self.sizeX = len(map[0])
        self.squareSize = squareSize

    def draw(self, screen):
        squareSize = self.squareSize
        for line in range(self.sizeY):
            for pixel in range(self.sizeX):
                rectangle = pg.rect.Rect(
                    pixel * squareSize, line * squareSize, squareSize, squareSize
                )
                if self.map[line][pixel] == 1:
                    pg.draw.rect(screen, "white", rectangle)
                else:
                    pg.draw.rect(screen, "black", rectangle)

    def get_MapPosition(self, position):
        mapPosition = pg.Vector2(math.floor(position.x / self.squareSize),math.floor(position.y / self.squareSize))
        if mapPosition.x >= self.sizeX:
            mapPosition.x = self.sizeX - 1
        if mapPosition.y >= self.sizeY:
            mapPosition.y = self.sizeY - 1
        return mapPosition
