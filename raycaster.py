import math
import random
import pygame as pg
from settings import *

def drawLineCentered(screen, color, x ,y ,size, width):
    initY = y + size
    finalY = y - size
    pg.draw.line(screen, color, (x, initY), (x, finalY), width)

def distance(positionA : pg.Vector2, positionB : pg.Vector2):
    distanceX = positionB.x - positionA.x
    distanceY = positionA.y - positionB.y
    return math.sqrt((distanceX ** 2) + (distanceY ** 2))


class raycaster:
    def __init__(self, character, resolution=4, fov=60, maxDistance=20):
        self.maxDistance = maxDistance
        self.fov = math.radians(fov)
        self.character = character
        self.resolution = resolution
        self.numberOfRays = fov * resolution
        self.raysRadian = [0] * self.numberOfRays
        self.raysSize = [0] * self.numberOfRays
        self.rayWidth = int(largura/self.numberOfRays)

    def calculateRays(self):
        firstAngle = self.character.angle - self.fov / 2
        for ray in range(self.numberOfRays):
            self.raysRadian[ray] = firstAngle + math.radians(self.fov / self.resolution) * ray

    def calculateDistances(self, map):
        for ray in range(self.numberOfRays):
            sinAngle = math.sin(self.raysRadian[ray])
            cosAngle = math.cos(self.raysRadian[ray])
            expandX = expandY = True
            mapBorderPosition = map.get_MapPosition(self.character.position) * map.squareSize
            directionX = 1 if cosAngle > 0 else -1
            directionY = 1 if sinAngle > 0 else -1

            rayPositionX = mapBorderPosition.copy()
            rayPositionX.x += map.squareSize if cosAngle > 0 else -0.00001
            rayPositionX.y = self.character.position.y + ((rayPositionX.x - self.character.position.x)/cosAngle * sinAngle) 

            rayPositionY = mapBorderPosition.copy()
            rayPositionY.y += map.squareSize if sinAngle > 0 else -0.00001
            rayPositionY.x = self.character.position.x + ((rayPositionY.y - self.character.position.y)/sinAngle * cosAngle) 
            
            XAmmount = map.squareSize / sinAngle * cosAngle
            YAmmount = map.squareSize / cosAngle * sinAngle
            for value in range(self.maxDistance):
                if map.testColision(rayPositionY) and expandY:
                    distanceY = distance(self.character.position, rayPositionY)
                    expandY = False
                if map.testColision(rayPositionX) and expandX:
                    distanceX = distance(self.character.position, rayPositionX)
                    expandX = False
                
                if expandX:
                    rayPositionX += (
                        map.squareSize * directionX,
                        YAmmount * directionX
                    )
                if expandY:
                    rayPositionY += (
                        XAmmount * directionY,
                        map.squareSize * directionY
                    )
                if not(expandX or expandY):
                    break
            rayDistance = distanceX if distanceX < distanceY else distanceY
            self.raysSize[ray] = rayDistance

    def drawRays(self):
        for ray in range(self.numberOfRays):
            pg.draw.line(self.character.screen, "yellow", self.character.position,
                         (self.character.position.x + math.cos(self.raysRadian[ray])*self.raysSize[ray],
                         self.character.position.y + math.sin(self.raysRadian[ray])*self.raysSize[ray]
                         ))

    def draw3D(self):
        for ray in range(self.numberOfRays):
            intense = self.maxDistance/self.raysSize[ray] * 500
            if intense > 255:
                intense = 255
            if intense < 0:
                intense = 0
            intense = int(intense)
            tamanhoLinha = 30000/self.raysSize[ray]
            
            drawLineCentered(self.character.screen, pg.Color(intense,intense,intense), ray * self.rayWidth, altura / 2, tamanhoLinha, self.rayWidth)
