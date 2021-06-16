import random

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
font = pygame.font.Font("freesansbold.ttf", 26)
#################################
# player images of different position
player = {
    1: [pygame.image.load("assets/tile008.png"),
        pygame.image.load("assets/tile009.png"),
        pygame.image.load("assets/tile010.png"),
        pygame.image.load("assets/tile011.png")],
    2: [pygame.image.load("assets/tile004.png"),
        pygame.image.load("assets/tile005.png"),
        pygame.image.load("assets/tile006.png"),
        pygame.image.load("assets/tile007.png")],
    3: [pygame.image.load("assets/tile000.png"),
        pygame.image.load("assets/tile001.png"),
        pygame.image.load("assets/tile002.png"),
        pygame.image.load("assets/tile003.png")],
    4: [pygame.image.load("assets/tile012.png"),
        pygame.image.load("assets/tile013.png"),
        pygame.image.load("assets/tile014.png"),
        pygame.image.load("assets/tile015.png")]
}
enemy_one = {
    1: [pygame.image.load("assets/enemy/tile008.png"),
        pygame.image.load("assets/enemy/tile009.png"),
        pygame.image.load("assets/enemy/tile010.png"),
        pygame.image.load("assets/enemy/tile011.png")],
    2: [pygame.image.load("assets/enemy/tile004.png"),
        pygame.image.load("assets/enemy/tile005.png"),
        pygame.image.load("assets/enemy/tile006.png"),
        pygame.image.load("assets/enemy/tile007.png")],
    3: [pygame.image.load("assets/enemy/tile000.png"),
        pygame.image.load("assets/enemy/tile001.png"),
        pygame.image.load("assets/enemy/tile002.png"),
        pygame.image.load("assets/enemy/tile003.png")],
    4: [pygame.image.load("assets/enemy/tile012.png"),
        pygame.image.load("assets/enemy/tile013.png"),
        pygame.image.load("assets/enemy/tile014.png"),
        pygame.image.load("assets/enemy/tile015.png")]
}
enemy_two = {
    1: [pygame.image.load("assets/enemy_two/tile008.png"),
        pygame.image.load("assets/enemy_two/tile009.png"),
        pygame.image.load("assets/enemy_two/tile010.png"),
        pygame.image.load("assets/enemy_two/tile011.png")],
    2: [pygame.image.load("assets/enemy_two/tile004.png"),
        pygame.image.load("assets/enemy_two/tile005.png"),
        pygame.image.load("assets/enemy_two/tile006.png"),
        pygame.image.load("assets/enemy_two/tile007.png")],
    3: [pygame.image.load("assets/enemy_two/tile000.png"),
        pygame.image.load("assets/enemy_two/tile001.png"),
        pygame.image.load("assets/enemy_two/tile002.png"),
        pygame.image.load("assets/enemy_two/tile003.png")],
    4: [pygame.image.load("assets/enemy_two/tile012.png"),
        pygame.image.load("assets/enemy_two/tile013.png"),
        pygame.image.load("assets/enemy_two/tile014.png"),
        pygame.image.load("assets/enemy_two/tile015.png")]
}
# speed and position of player
speed = 8
enemy_speed = 2
score = 0
playerX = 370
playerY = 400
list_of_enemy_pos = [
    {'x': random.randint(1, 450), 'y': random.randint(1, 450), 'class': enemy_one, 'direction': pygame.K_DOWN},
    {'x': random.randint(1, 450), 'y': random.randint(1, 450), 'class': enemy_two, 'direction': pygame.K_UP}]
# all possible direction for player :)
listOfDirection = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
# default is moving right
direction = listOfDirection[0]
enemy_direction = listOfDirection[random.randint(0, 3)]
walkCount = 0


def draw_player_or_enemy(x, y, dire, array):
    global walkCount
    if walkCount >= 32:
        walkCount = 0
    if dire == pygame.K_RIGHT:
        screen.blit(array[1][walkCount // 8], (x, y))
        walkCount += 2
    elif dire == pygame.K_LEFT:
        screen.blit(array[2][walkCount // 8], (x, y))
        walkCount += 2
    elif dire == pygame.K_UP:
        screen.blit(array[4][walkCount // 8], (x, y))
        walkCount += 2
    else:
        screen.blit(array[3][walkCount // 8], (x, y))
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


def move_enemy(i):
    enemy = list_of_enemy_pos[i]
    if enemy['direction'] == pygame.K_RIGHT:
        enemy['x'] += enemy_speed
    elif enemy['direction'] == pygame.K_LEFT:
        enemy['x'] -= enemy_speed
    elif enemy['direction'] == pygame.K_UP:
        enemy['y'] -= enemy_speed
    elif enemy['direction'] == pygame.K_DOWN:
        enemy['y'] += enemy_speed


def change_direction(event_value):
    global direction
    global score
    if event_value == pygame.K_LEFT:
        direction = listOfDirection[0]
    elif event_value == pygame.K_RIGHT:
        direction = listOfDirection[1]
    elif event_value == pygame.K_UP:
        direction = listOfDirection[2]
    elif event_value == pygame.K_DOWN:
        direction = listOfDirection[3]


def call_random(func, i):
    n = random.randint(1, 15)
    if n == 2:
        func(i)


def change_enemy_direction(i):
    list_of_enemy_pos[i]['direction'] = listOfDirection[random.randint(0, 3)]


def render_score():
    text = font.render("Score:" + str(score), True, (0, 0, 0))
    screen.blit(text, (10, 10))


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
    render_score()
    draw_player_or_enemy(playerX, playerY, direction, player)
    for i in range(0, len(list_of_enemy_pos)):
        move_enemy(i)
        draw_player_or_enemy(list_of_enemy_pos[i]['x'], list_of_enemy_pos[i]['y'], enemy_direction,
                             list_of_enemy_pos[i]['class'])
        call_random(change_enemy_direction, i)
    pygame.display.update()
