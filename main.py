import pygame

pygame.init()

size = width, height = 800, 500
screen_color = a, b, c = 255, 255, 255
# config for screen#
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ratnik doline")
icon = pygame.image.load("assets/icon.png")

pygame.display.update()
pygame.display.set_icon(icon)

#################################
# player#
playerImg = pygame.image.load("assets/tile008.png")
speed = 8
playerX = 370
playerY = 400


# def move_player(playerX, playerY, a: int):
#     if (a == 1):
#         playerX += 10
#     elif (a == 2):
#         playerY += 10


def show_player(x, y):
    screen.blit(playerImg, (x, y))


isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX -= speed
            elif event.key == pygame.K_RIGHT:
                playerX += speed
            elif event.key == pygame.K_UP:
                pass
    screen.fill(screen_color)
    show_player(playerX, playerY)
    pygame.display.update()
