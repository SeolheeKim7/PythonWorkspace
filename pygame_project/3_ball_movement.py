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

# moving position
character_to_x = 0

# speed
character_speed = 5

# weapon
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
# weapon can be fired multiple times
weapons = []

# weapon speed
weapon_speed = 10

# ball
ball_images = [pygame.image.load(os.path.join(image_path, "balloon1.png")),
               pygame.image.load(os.path.join(image_path, "balloon2.png")),
               pygame.image.load(os.path.join(image_path, "balloon3.png")),
               pygame.image.load(os.path.join(image_path, "balloon4.png"))]

# ball speed
ball_speed_y = [-18, -15, -12, -9]  # index 0, 1, 2, 3

# balls
balls = []

# first ball
balls.append({
    "pos_x": 50,  # x position
    "pos_y": 50,  # y position
    "img_idx": 0,  # image index
    "to_x": 3,  # x direction
    "to_y": -6,  # y direction
    "init_spd_y": ball_speed_y[0]})  # y speed

# 1. user game initialization (background, game image, position, speed, font, etc.)


running = True
while running:
    dt = clock.tick(60)  # set frame per second

    # 2. handling event (keyboard, mouse, etc.)
    for event in pygame.event.get():  # do any event happen:
        if event.type == pygame.QUIT:  # do the event which close the window happen?
            running = False  # not runnning

        if event.type == pygame.KEYDOWN:  # check if key is pressed
            if event.key == pygame.K_LEFT:  # move character to left
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:  # move character to right
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + character_width / 2 - weapon_width / 2
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
    # 3. character position update
    character_x_pos += character_to_x

    # check character position
    if character_x_pos < 0:  # left end of screen
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:  # right end of screen
        character_x_pos = screen_width - character_width

    # weapon position
    weapons = [[w[0], w[1] - weapon_speed]
               for w in weapons]  # weapon position up
    # remove weapon when it reaches top
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]

    # ball position
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]  # x position
        ball_pos_y = ball_val["pos_y"]  # y position
        ball_img_idx = ball_val["img_idx"]  # image index

        ball_size = ball_images[ball_img_idx].get_rect().size  # ball size
        ball_width = ball_size[0]  # ball width
        ball_height = ball_size[1]  # ball height
        # ball bounce when it hits the wall
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1

        # ball bounce when it hits the stage
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else:  # speed increase when it goes up
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]  # x position update
        ball_val["pos_y"] += ball_val["to_y"]  # y position update
    # 4. collision handling

    # 5. draw on screen
    screen.blit(background, (0, 0))  # draw background
    # draw weapon
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    # draw ball
    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))
    screen.blit(stage, (0, screen_height - stage_height))  # draw stage
    # draw character
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()  # redraw screen

pygame.quit()
