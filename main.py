import pygame

pygame.init()

# config for screen
size = width, height = 800, 500
screen_color = a, b, c = 255, 255, 255
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ratnik doline")
icon = pygame.image.load("assets/icon.png")
clock = pygame.time.Clock()
pygame.display.update()
pygame.display.set_icon(icon)

#################################
# player images of different position
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
player_is_jumping = [pygame.image.load("assets/tile012.png"),
                     pygame.image.load("assets/tile013.png"),
                     pygame.image.load("assets/tile014.png"),
                     pygame.image.load("assets/tile015.png")]
# speed and position of player
speed = 8
playerX = 370
playerY = 400
# all possible direction for player :)
listOfDirection = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
# default is moving right
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
    elif dire == pygame.K_UP:
        screen.blit(player_is_jumping[walkCount // 8], (x, y))
        walkCount += 2
    else:
        screen.blit(player_not_moving[walkCount // 8], (x, y))
        walkCount += 2


def move_player():
    global playerX
    global playerY
    if direction == pygame.K_RIGHT:
        playerX += speed
    elif direction == pygame.K_LEFT:
        playerX -= speed
    elif direction == pygame.K_UP:
        playerY -= speed
    elif direction == pygame.K_DOWN:
        playerY += speed


def change_direction(event_value):
    global direction
    if event_value == pygame.K_LEFT:
        direction = listOfDirection[0]
    elif event_value == pygame.K_RIGHT:
        direction = listOfDirection[1]
    elif event_value == pygame.K_UP:
        direction = listOfDirection[2]
    elif event_value == pygame.K_DOWN:
        direction = listOfDirection[3]


isRunning = True
while isRunning:
    clock.tick(32)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:
            change_direction(event.key)
        else:
            direction = 0
    move_player()
    screen.fill(screen_color)
    draw_player(playerX, playerY, direction)
    pygame.display.update()
