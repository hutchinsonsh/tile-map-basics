import pygame as pg

class Map:
    def __init__(self, fileName, settings):
        self.data = []
        with open(fileName, 'rt') as x:
            for line in x:
                self.data.append(line.strip())

        self.ai_settings = settings
        self.tileWidth = len(self.data[0])
        self.tileHeight = len(self.data)
        self.width = self.tileWidth * self.ai_settings.tileSize
        self.height = self.tileHeight * self.ai_settings.tileSize

class Camera:
    def __init__(self, width, height, settings):
        self.ai_settings = settings
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, player):
        return player.rect.move(self.camera.topleft)

    def update(self, player):
        x = -player.rect.x + int(self.ai_settings.w / 2)
        y = -player.rect.y + int(self.ai_settings.h / 2)

        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.width - self.ai_settings.w), x) # right
        y = max(-(self.height - self.ai_settings.h), y)  # bottom
        self.camera = pg.Rect(x, y, self.width, self.height)
        
