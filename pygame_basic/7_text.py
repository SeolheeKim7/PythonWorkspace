import pygame
#################################################
# basic initialization
pygame.init()

# screen size setting
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# set screentitle
pygame.display.set_caption("TT Game")

# FPS
clock = pygame.time.Clock()
#################################################

# 1. user game initialization (background, game image, position, speed, font, etc.)

# open background image
background = pygame.image.load(
    "C:/PythonWorkspace/pygame_basic/background.png")

# open sprite
character = pygame.image.load("C:/PythonWorkspace/pygame_basic/character.png")
character_size = character.get_rect().size  # get size of image
character_width = character_size[0]  # get width of image
character_height = character_size[1]  # get height of image
character_x_pos = (screen_width / 2) - \
    (character_width / 2)  # set x position of image
character_y_pos = screen_height - character_height  # set y position of image

# moving position
to_x = 0
to_y = 0

# speed
character_speed = 0.6

# enemy character
enemy = pygame.image.load("C:/PythonWorkspace/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size  # get size of image
enemy_width = enemy_size[0]  # get width of image
enemy_height = enemy_size[1]  # get height of image
enemy_x_pos = (screen_width / 2) - \
    (enemy_width / 2)  # set x position of image
enemy_y_pos = (screen_height / 2) - \
    (enemy_height / 2)  # set y position of image

# font definition
game_font = pygame.font.Font(None, 40)  # create font object

# total time
total_time = 10

# start time
start_ticks = pygame.time.get_ticks()  # get start tick

# event roop
running = True

while running:
    dt = clock.tick(60)  # set frame per second

    # 2. handling event (keyboard, mouse, etc.)
    for event in pygame.event.get():  # do any event happen:
        if event.type == pygame.QUIT:  # do the event which close the window happen?
            running = False  # not runnning

        if event.type == pygame.KEYDOWN:  # check if any key is pressed
            if event.key == pygame.K_LEFT:  # check if left key is pressed
                to_x -= character_speed  # move character to left  by 5
            elif event.key == pygame.K_RIGHT:  # check if right key is pressed
                to_x += character_speed  # move character to right by 5
            elif event.key == pygame.K_UP:  # check if up key is pressed
                to_y -= character_speed    # move character to up    by 5
            elif event.key == pygame.K_DOWN:  # check if down key is pressed
                to_y += character_speed    # move character to down  by 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # 3. character position update
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # set character position to be in screen
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 4. collision handling
    # collision
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # check collision
    if character_rect.colliderect(enemy_rect):
        print("Collision")
        running = False

    # 5. draw on screen
    screen.blit(background, (0, 0))  # draw background
    # draw character
    screen.blit(character, (character_x_pos, character_y_pos))
    # draw enemy
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    # timer
    # get time
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

    # render time
    timer = game_font.render(
        str(int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))
    # time out
    if total_time - elapsed_time <= 0:
        print("Time out")
        running = False

    pygame.display.update()  # redraw screen

# delay
pygame.time.delay(2000)  # 2 sec delay
# end pygame
pygame.quit()
