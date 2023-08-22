import pygame

pygame.init()

# screen size setting
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# set screentitle
pygame.display.set_caption("Nado Game")

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
# event roop
running = True
while running:
    for event in pygame.event.get():  # do any event happen:
        if event.type == pygame.QUIT:  # do the event which close the window happen?
            running = False  # not runnning
    screen.blit(background, (0, 0))  # draw background
    # draw character
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()  # redraw screen
# end pygame
pygame.quit()
