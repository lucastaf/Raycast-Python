import pygame as pg
import player
import math
import map
from game import *
import raycaster

pg.init()


newGame = game()
map1 = map.map([[1, 1, 1, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1],],
                newGame.screen)

rays = raycaster.raycaster(newGame.character)

while newGame.running:
    newGame.inputFunctions(map1)
    newGame.screen.fill("black")
    rays.calculateRays()
    rays.calculateDistances(map1)

    if newGame.mode == 0:
        map1.draw(newGame.screen)
        rays.drawRays()
        newGame.drawCharacters()
        
    else:
        rays.draw3D()

    pg.display.flip()

pg.quit()
