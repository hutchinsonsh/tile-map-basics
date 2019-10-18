import pygame
from pygame.sprite import Sprite

class Player(Sprite):
    def __init__(self, game, x, y, settings, screen, ai_settings):
        super(Player, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.game = game
        self.image = pygame.Surface((settings.tileSize, settings.tileSize))
        self.image.fill(settings.red)
        self.rect = self.image.get_rect()
        self.x = x * settings.tileSize
        self.y = y * settings.tileSize

        self.rect.x = self.x
        self.rect.y = self.y

        # for finding the edges of the player rect
        self.leftEdge = self.rect.x
        self.rightEdge = self.rect.x + settings.tileSize
        self.topEdge = self.rect.y
        self.bottomEdge = self.rect.y + settings.tileSize

        # for moving right/if user is pressing on a key
        self.movingRight = False
        self.movingLeft = False
        self.movingUp = False
        self.movingDown = False

        # if collision, by how much can user move
        self.rightV = ai_settings.playerSpeed
        self.leftV = ai_settings.playerSpeed

        # this makes sense to have in my head
        self.canMoveRight = True
        self.canMoveLeft = True
        self.canMoveUp = True
        self.canMoveDown = True

        self.jumpCount = 0      # goes up to 92
        self.jumping = False

        self.fallCount = 0
        self.falling = False

    def update(self, wall):
        # for moving right
        if self.movingRight and self.canMoveRight:
            self.rect.x += self.rightV
            self.leftEdge = self.rect.x
            self.rightEdge = self.rect.x + self.ai_settings.tileSize

        # for moving left
        if self.movingLeft and self.canMoveLeft:
            self.rect.x -= self.leftV
            self.leftEdge = self.rect.x
            self.rightEdge = self.rect.x + self.ai_settings.tileSize

        # for the jumping part
        if self.movingUp and not self.jumping and not self.falling:
            self.jumping = True

        # for the falling part
        if self.movingDown and self.canMoveDown:
            self.jumping = False
            self.falling = True

        # jumping part 2
        if self.jumping:
            self.rect.y -= self.ai_settings.playerJumping[self.jumpCount]
            self.topEdge = self.rect.y
            self.bottomEdge = self.rect.y + self.ai_settings.tileSize
            if self.jumpCount > 46 or self.falling:
                self.jumping = False
                self.jumpCount = 0
            else:
                self.jumpCount += 1

        if not self.jumping:
            self.jumpCount = 0

        # falling part 2
        num = self.ai_settings.playerFalling[self.fallCount]
        num2 = 5
        if self.falling:
            for x in wall:
                if x.topEdge >= self.bottomEdge and x.topEdge - self.bottomEdge <= 5:
                    if (x.leftEdge <= self.leftEdge <= x.rightEdge) or (
                            x.leftEdge <= self.rightEdge <= x.rightEdge):
                        num2 = x.topEdge - self.bottomEdge
            if num2 == 0:
                self.falling = False
                self.fallCount = 0
            elif num2 < num:
                self.rect.y += num2
                self.falling = False
                self.fallCount = 0
            else:
                self.rect.y += self.ai_settings.playerFalling[self.fallCount]
                self.fallCount += 1

            self.topEdge = self.rect.y
            self.bottomEdge = self.rect.y + self.ai_settings.tileSize

        if not self.canMoveDown:
            self.falling = False
            self.fallCount = 0

    # sets image to the right position
    def draw(self, screen):
        screen.blit(self.image, self.rect)
