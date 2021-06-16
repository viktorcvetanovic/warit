import pygame

pygame.init()

size = width, height = 800, 500
screen_color = a, b, c = 255, 255, 255
# config for screen#
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ratnik doline")
icon = pygame.image.load("assets/icon.png")
clock = pygame.time.Clock()
pygame.display.update()
pygame.display.set_icon(icon)

#################################
# player#
player_right_image = [pygame.image.load("assets/tile008.png"),
                      pygame.image.load("assets/tile009.png"),
                      pygame.image.load("assets/tile010.png"),
                      pygame.image.load("assets/tile011.png")]
player_left_image = [pygame.image.load("assets/tile004.png"),
                     pygame.image.load("assets/tile005.png"),
                     pygame.image.load("assets/tile006.png"),
                     pygame.image.load("assets/tile007.png")]
player_not_moving = [pygame.image.load("assets/tile000.png"),
                     pygame.image.load("assets/tile001.png"),
                     pygame.image.load("assets/tile002.png"),
                     pygame.image.load("assets/tile003.png")]
speed = 8
playerX = 370
playerY = 400
listOfDirection = [pygame.K_LEFT, pygame.K_RIGHT]
direction = listOfDirection[0]
walkCount = 0


def draw_player(x, y, dire):
    global walkCount
    if walkCount >= 32:
        walkCount = 0
    if dire == pygame.K_RIGHT:
        screen.blit(player_right_image[walkCount // 8], (x, y))
        walkCount += 2
    elif dire == pygame.K_LEFT:
        screen.blit(player_left_image[walkCount // 8], (x, y))
        walkCount += 2
    else:
        screen.blit(player_not_moving[walkCount // 8], (x, y))
        walkCount += 1


def move_player():
    global playerX
    global playerY
    if direction == pygame.K_RIGHT:
        playerX += speed
    elif direction == pygame.K_LEFT:
        playerX -= speed


isRunning = True
while isRunning:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = listOfDirection[0]
            elif event.key == pygame.K_RIGHT:
                direction = listOfDirection[1]
            elif event.key == pygame.K_UP:
                pass
        else:
            direction = 0
    move_player()
    screen.fill(screen_color)
    draw_player(playerX, playerY, direction)
    pygame.display.update()
