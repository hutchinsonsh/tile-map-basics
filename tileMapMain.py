import pygame
import sys
import gameFunction as gf
from os import path
from pygame.sprite import Group
from settings import Settings
from wall import Wall
from player import Player
from tileMap import *


class Game:
    def __init__(self):
        self.running = True
        pygame.init()
        self.screen = pygame.display.set_mode((settings.w, settings.h))
        pygame.display.set_caption(settings.title)
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500, 100)
        self.running = True
        self.loadData()
        self.newMap = False

    def loadData(self):
        game_folder = path.dirname(__file__)
        self.map = Map(path.join(game_folder, 'map.txt'), settings)

    # creates the tileMap/player locations
    def new1(self):
        self.wallGroup = Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    wall = Wall(g, col, row, settings, '1')
                    self.wallGroup.add(wall)
                elif tile == '2':
                    wall = Wall(g, col, row, settings, '2')
                    self.wallGroup.add(wall)
                elif tile == '3':
                    wall = Wall(g, col, row, settings, '3')
                    self.wallGroup.add(wall)
                elif tile == '4':
                    wall = Wall(g, col, row, settings, '4')
                    self.wallGroup.add(wall)
                if tile == 'P':
                    self.newPlayer = Player(g, col, row, settings, self.screen, settings)
        self.camera = Camera(self.map.width, self.map.height, settings)

    def new(self):
        for x in self.wallGroup:
            if x.type == '4' and x.leftEdge == self.newPlayer.rightEdge:
                    self.newMap = True
        if self.newMap == True:
            game_folder = path.dirname(__file__)
            self.map = Map(path.join(game_folder, 'map2.txt'), settings)
            self.new1()
            self.newMap = False

    # draws the grid
    def drawGrid(self):
        for x in range(0, settings.w, settings.tileSize):
            pygame.draw.line(self.screen, settings.grey, (x, 0), (x, settings.h))
        for y in range(0, settings.h, settings.tileSize):
            pygame.draw.line(self.screen, settings.grey, (0, y), (settings.w, y))

    # draws the walls and player
    def draw(self, settings):
        self.screen.fill(settings.blue)
        #self.drawGrid()
        for x in self.wallGroup:
            self.screen.blit(x.image, self.camera.apply(x))
        self.screen.blit(self.newPlayer.image, self.camera.apply(self.newPlayer))
        pygame.display.flip()

    # checks events, updates any changes, draws events/changes
    def run(self, settings):
        self.playing = True
        while self.playing:
            self.new()
            self.dt = self.clock.tick(settings.FPS) / 1000
            gf.checkEvents(settings, self.newPlayer, self.wallGroup)
            self.update()
            self.draw(settings)

    # updates players movement
    def update(self):
        self.newPlayer.update(self.wallGroup)
        self.camera.update(self.newPlayer)

    # quits game
    def quit(self):
        pygame.quit()
        sys.exit()


settings = Settings()
g = Game()
mapData = Map('map.txt', settings)
g.new1()
while g.running:
    g.new()
    g.run(settings)
pygame.quit()

