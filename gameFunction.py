import sys
import pygame


def checkEvents(settings, player, walls):
    checkCollisions(settings, player, walls)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            checkKeyDown(event, player)
        elif event.type == pygame.KEYUP:
            checkKeyUp(event, player)


# checks collisions between player and wall
def checkCollisions(settings, player, walls):
    # for checking if going right
    numR = 10
    for x in walls:
        if x.leftEdge <= player.rightEdge and player.rightEdge - x.leftEdge <= 5:
            if (x.topEdge < player.bottomEdge < x.bottomEdge) or (x.topEdge < player.topEdge < x.bottomEdge) or \
                    (x.topEdge == player.topEdge and player.bottomEdge == x.bottomEdge):
                numR = x.leftEdge - player.rightEdge
                if numR != 0:
                    player.rightV = numR
                    player.update(walls)
                    player.movingRight = False
                    player.canMoveRight = False
                else:
                    player.rightV = numR
                    player.movingRight = False
                    player.canMoveRight = False

    if numR == 10:
        player.canMoveRight = True
        player.rightV = settings.playerSpeed

    # for checking if going left
    numL = 10
    for x in walls:
        if x.rightEdge <= player.leftEdge and abs(player.leftEdge - x.rightEdge) <= 5:
            if (x.topEdge < player.bottomEdge < x.bottomEdge) or (x.topEdge < player.topEdge < x.bottomEdge) or \
                    (x.topEdge == player.topEdge and player.bottomEdge == x.bottomEdge):
                numL = player.leftEdge - x.rightEdge
                if numL != 0:
                    player.leftV = numL
                    player.update(walls)
                    player.movingLeft = False
                    player.canMoveLeft = False
                else:
                    player.leftV = numL
                    player.movingLeft = False
                    player.canMoveLeft = False
    if numL == 10:
        player.canMoveLeft = True
        player.leftV = settings.playerSpeed

    # for checking if runner is pressed on the ground- if not- falls until reaches ground
    canMoveDown1 = True
    for x in walls:
        if x.topEdge == player.bottomEdge:
            if (x.leftEdge <= player.leftEdge <= x.rightEdge) or (x.leftEdge <= player.rightEdge <= x.rightEdge):
                canMoveDown1 = False
                player.canMoveDown = False
    if canMoveDown1 and not player.jumping:
        player.falling = True
        player.canMoveDown = True
    if not canMoveDown1:
        player.falling = False

    # for checking to see that, if while jumping, player hits a ceiling/wall
    for x in walls:
        if x.bottomEdge == player.topEdge:
            if (x.leftEdge <= player.leftEdge <= x.rightEdge) or (x.leftEdge <= player.rightEdge <= x.rightEdge):
                player.falling = True
                player.jumping = False


# checks for if player is moving/presses quit
def checkKeyDown(event, player):
    if event.key == pygame.K_RIGHT:
        player.movingRight = True
    if event.key == pygame.K_LEFT:
        player.movingLeft = True
    if event.key == pygame.K_UP:
        player.movingUp = True
    if event.key == pygame.K_DOWN:
        player.movingDown = True
        player.jumping = False

    if event.key == pygame.K_ESCAPE:
        sys.exit()


# for if player stops moving
def checkKeyUp(event, player):
    if event.key == pygame.K_RIGHT:
        player.movingRight = False
    elif event.key == pygame.K_LEFT:
        player.movingLeft = False
    elif event.key == pygame.K_UP:
        player.movingUp = False
    elif event.key == pygame.K_DOWN:
        player.movingDown = False
        
