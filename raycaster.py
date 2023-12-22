import math
import random
import pygame as pg
from settings import *

def drawLineCentered(screen, color, x ,y ,size, width):
    initY = y + size
    finalY = y - size
    pg.draw.line(screen, color, (x, initY), (x, finalY), width)

def distance(positionA : pg.Vector2, positionB : pg.Vector2):
    print("a")


class raycaster:
    def __init__(self, character, resolution=4, fov=60, maxDistance=500):
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
            for value in range(self.maxDistance):
                RayPosition = pg.Vector2(
                self.character.position.x
                + math.cos(self.raysRadian[ray]) * value * map.squareSize,
                self.character.position.y
                + math.sin(self.raysRadian[ray]) * value * map.squareSize,)
                if map.testColision(RayPosition):
                    self.raysSize[ray] = value
                    break
        

    def drawRays(self):
        for ray in range(self.numberOfRays):
            pg.draw.line(self.character.screen, "yellow", self.character.position,
                         (self.character.position.x + math.cos(self.raysRadian[ray])*self.raysSize[ray],
                         self.character.position.y + math.sin(self.raysRadian[ray])*self.raysSize[ray]
                         ))

    def draw3D(self):
        for ray in range(self.numberOfRays):
            intense = self.maxDistance/self.raysSize[ray] * 15
            if intense > 255:
                intense = 255
            if intense < 0:
                intense = 0
            intense = int(intense)
            tamanhoLinha = 30000/self.raysSize[ray]
            
            drawLineCentered(self.character.screen, pg.Color(intense,intense,intense), ray * self.rayWidth, altura / 2, tamanhoLinha, self.rayWidth)
