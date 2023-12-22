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
        mapPosition = pg.Vector2(
            math.floor(position.x / self.squareSize),
            math.floor(position.y / self.squareSize),
        )
        if mapPosition.x >= self.sizeX:
            mapPosition.x = self.sizeX - 1
        if mapPosition.y >= self.sizeY:
            mapPosition.y = self.sizeY - 1
        return mapPosition

    def testColision(self, objPosition):
        position = self.get_MapPosition(objPosition)
        if self.map[int(position.y)][int(position.x)] == 1:
            return True
        else:
            return False

    def findSquareBorder(self, position: pg.Vector2, angle):
        pass

    def findFaceSide(self, position: pg.Vector2, angle):
        sinAngle = math.sin(angle)
        cosAngle = math.cos(angle)
        # cantos: 1 = UL+-, 2 = UR++, 3 = DL--, 4 = DR-+, 5 = nao tem
        if sinAngle > 0 and cosAngle < 0:
            canto = 1
        elif sinAngle > 0 and cosAngle < 0:
            canto = 2
        elif sinAngle < 0 and cosAngle < 0:
            canto = 3
        elif sinAngle < 0 and cosAngle > 0:
            canto = 4
        else:
            canto = 5
        
        #faces: 1 = U, 2 = R, 3 = D, 4 = L
        if canto == 5:
            if cosAngle == 0:
                if sinAngle > 0:
                    return 1 #cima
                else: #sin < 0
                    return 3 #Baixo
            else: #sin == 0
                if cosAngle > 0:
                    return 2 #Direita
                else: # cos > 0
                    return 4 #Esquerda
        
        match canto:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass


