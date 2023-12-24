import pygame as pg
import math
from settings import *

def drawLineAngle(screen, color, initalPos : pg.Vector2, angle, size):
    pg.draw.line(screen, color, initalPos, (
        initalPos.x + math.cos(angle) * size,
        initalPos.y + math.sin(angle) * size
    ))
class map:
    def __init__(self, map, screen, squareSize=150):
        self.screen = screen
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
        mapPosition = pg.Vector2(
            math.floor(position.x / self.squareSize),
            math.floor(position.y / self.squareSize),
        )
        
        if mapPosition.x >= self.sizeX:
            mapPosition.x = self.sizeX - 1
        if mapPosition.y >= self.sizeY:
            mapPosition.y = self.sizeY - 1
        if mapPosition.x < 0:
            mapPosition.x = 0
        if mapPosition.y < 0:
            mapPosition.y = 0
        return mapPosition

    def testColision(self, objPosition):
        
        position = self.get_MapPosition(objPosition)
        if self.map[int(position.y)][int(position.x)] == 1:
            return True
        else:
            return False
        
    def NextXBorder(self, position : pg.Vector2, angle):
        mapBorder = self.get_MapPosition(position)
        position.y -= (position.x - mapBorder.x)/math.cos(angle) * math.sin(angle)
        position.x += mapBorder.x + self.squareSize
        return position