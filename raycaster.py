import math
import random
import pygame as pg
from settings import *

def drawLineCentered(screen, color, x ,y ,size, width):
    initY = y + size
    finalY = y - size
    pg.draw.line(screen, color, (x, initY), (x, finalY), width)

class raycaster:
    def __init__(self, character, resolution=3, fov=90, maxDistance=500):
        self.maxDistance = maxDistance
        self.fov = math.radians(fov)
        self.character = character
        self.resolution = resolution
        self.numberOfRays = fov * resolution
        self.rays = [0] * self.numberOfRays
        self.raysSize = [0] * self.numberOfRays

    def calculateRays(self):
        firstAngle = self.character.angle - self.fov / 2
        for ray in range(len(self.rays)):
            self.rays[ray] = firstAngle + math.radians(self.fov / self.resolution) * ray

    def calculateDistances(self, map):
        for ray in range(self.numberOfRays):
            for value in range(self.maxDistance):
                RayPosition = pg.Vector2(
                self.character.position.x
                + math.cos(self.rays[ray]) * value,
                self.character.position.y
                + math.sin(self.rays[ray]) * value,)
                posmapa = map.get_MapPosition(RayPosition)
                if map.map[int(posmapa.y)][int(posmapa.x)] == 1:
                    self.raysSize[ray] = value
                    break

    def draw3D(self):
        colors = ["white", "red", "green", "yellow", "purple", "blue"]
        for ray in range(self.numberOfRays):
            tamanhoLinha = 1/self.raysSize[ray] * 20000
            drawLineCentered(self.character.screen, colors[ray%len(colors)], ray * 10, altura / 2, tamanhoLinha, 20)
