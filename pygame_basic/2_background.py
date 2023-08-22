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

# event roop
running = True
while running:
    for event in pygame.event.get():  # do any event happen:
        if event.type == pygame.QUIT:  # do the event which close the window happen?
            running = False  # not runnning
    screen.blit(background, (0, 0))  # draw background
    pygame.display.update()  # redraw screen
# end pygame
pygame.quit()
