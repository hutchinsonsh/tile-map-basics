import pygame
from pygame.sprite import Sprite

class Wall(Sprite):
    def __init__(self, game, x, y, settings):
        super(Wall, self).__init__()
        self.game = game
        self.image = pygame.Surface((settings.tileSize, settings.tileSize))
        self.image.fill(settings.white)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

        self.rect.left = self.x * settings.tileSize
        self.rect.centery = self.y * settings.tileSize + 16

        self.leftEdge = x * settings.tileSize
        self.rightEdge = (x + 1) * settings.tileSize
        self.topEdge = y * settings.tileSize
        self.bottomEdge = (y + 1) * settings.tileSize

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, camera):
        self.x *= camera.width
        self.y *= camera.height
        
