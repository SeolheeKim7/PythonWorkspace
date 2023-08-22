import pygame
#################################################
# basic initialization
pygame.init()

# screen size setting
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# set screentitle
pygame.display.set_caption("GAME NAME")

# FPS
clock = pygame.time.Clock()
#################################################

# 1. user game initialization (background, game image, position, speed, font, etc.)

running = True
while running:
    dt = clock.tick(60)  # set frame per second

    # 2. handling event (keyboard, mouse, etc.)
    for event in pygame.event.get():  # do any event happen:
        if event.type == pygame.QUIT:  # do the event which close the window happen?
            running = False  # not runnning

    # 3. character position update

    # 4. collision handling

    # 5. draw on screen
    pygame.display.update()  # redraw screen

pygame.quit()
