import pygame as pg
import player
from settings import *

class game:
    def __init__(self):
        self.running = True
        self.lockMouse = False
        self.screen = pg.display.set_mode((largura, altura))
        self.character = player.player(self)
        self.mode = 0
    
    def inputFunctions(self, mapa):
        global running, lockMouse
        delta = pg.time.Clock().tick(fps)
        teclas = pg.key.get_pressed()
        #key_down
        if teclas[pg.K_w]:
            self.character.move(mapa, 0, 20, delta)
        if teclas[pg.K_s]:
            self.character.move(mapa, 0, -20, delta)
        if teclas[pg.K_a]:
            self.character.move(mapa, -20, 0, delta)
        if teclas[pg.K_d]:
            self.character.move(mapa, 20, 0, delta)
        #----

        #key_press
        for event in pg.event.get():
            
            if event.type == pg.QUIT:
                self.running = False
                
            # ---MOUSE---
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 3:
                    self.lockMouse =  True
                    pg.mouse.set_visible(False)
            if event.type == pg.MOUSEMOTION:
                self.character.rotate(event.rel[0] / 100, delta)

            # ---TECLADO---
            if event.type == pg.KEYDOWN:
                match event.key:
                    case pg.K_ESCAPE:
                        self.lockMouse = False
                        pg.mouse.set_visible (True)
                    case pg.K_r:
                        if self.mode == 0:
                            self.mode = 1
                        else:
                            self.mode = 0
    
        if self.lockMouse:
            pg.mouse.set_pos((largura/2,altura/2))

    def drawCharacters(self):
        self.character.draw()


