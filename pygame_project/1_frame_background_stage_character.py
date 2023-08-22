import pygame
import os
#################################################
# basic initialization
pygame.init()

# screen size setting
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# set screentitle
pygame.display.set_caption("TT Pang")

# FPS
clock = pygame.time.Clock()
#################################################
current_path = os.path.dirname(__file__)  # return current file path
image_path = os.path.join(current_path, "images")  # return image folder path

# background
background = pygame.image.load(os.path.join(image_path, "background.png"))
# stage
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]  # put character on stage

# character
character = pygame.image.load(os.path.join(image_path, "character.png"))
chracter_size = character.get_rect().size
character_width = chracter_size[0]
character_height = chracter_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height
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
    screen.blit(background, (0, 0))  # draw background
    screen.blit(stage, (0, screen_height - stage_height))  # draw stage
    # draw character
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()  # redraw screen

pygame.quit()
