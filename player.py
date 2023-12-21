import pygame as pg
import map
import math


class player:
    def __init__(self,game, size = 25):
        self.size = size
        self.position = pg.Vector2(500, 500)
        self.angle = 0
        self.game = game
        self.screen = game.screen

    def draw(self):
        pg.draw.line(
            self.screen,
            "blue",
            self.position,
            (
                self.position.x + math.cos(self.angle) * 100,
                self.position.y + math.sin(self.angle) * 100,
            ),
        )
        retangulo = pg.Rect(self.position.x - self.size/2, self.position.y - self.size/2, self.size, self.size)
        pg.draw.rect(self.screen, "red", retangulo)

    def move(self, mapa, x, y, delta):
        x = x * delta / 100
        y = y * delta / 100
        realAngle = self.angle
        deslocX = -(x * math.sin(realAngle)) + (y * math.cos(realAngle))
        deslocY = (x * math.cos(realAngle)) + (y * math.sin(realAngle))
        newPosition = pg.Vector2(self.position.x + deslocX, self.position.y + deslocY)
        if(self.testColisionRect(newPosition,mapa)):
            self.position = newPosition

        """
        if self.testColisionPoint(pg.Vector2(newPosition.x - self.size/2, self.position.y), mapa) and self.testColisionPoint(pg.Vector2(newPosition.x + self.size/2, self.position.y), mapa):
            self.position.x = newPosition.x
        if self.testColisionPoint(pg.Vector2(self.position.x, newPosition.y + self.size/2), mapa) and self.testColisionPoint(pg.Vector2(self.position.x, newPosition.y - self.size/2), mapa):
            self.position.y = newPosition.y
        """

    def rotate(self, angleRadian, delta):
        angleRadian = angleRadian * delta / 100
        self.angle += angleRadian
        if self.angle >= math.pi * 2:
            self.angle -= math.pi * 2

    def testColisionPoint(self, position, mapa):
        location = mapa.get_MapPosition(position)
        if mapa.map[int(location.y)][int(location.x)] == 1:
            return True
        else:
            return False

    def testColisionRect(self, position, mapa):
        pointUL = pg.Vector2(position.x - self.size/2, position.y - self.size/2)
        pointUR = pg.Vector2(position.x + self.size/2, position.y - self.size/2)
        pointDL = pg.Vector2(position.x - self.size/2, position.y + self.size/2)
        pointDR = pg.Vector2(position.x + self.size/2, position.y + self.size/2)
        if self.testColisionPoint(pointUL,mapa) or self.testColisionPoint(pointUR,mapa) or self.testColisionPoint(pointDL,mapa) or self.testColisionPoint(pointDR,mapa):
            return False
        else:
            return True