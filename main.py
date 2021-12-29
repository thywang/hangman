import pygame
import os

# set up display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

# load images
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

# game variables
hangman_status = 4

# colors
WHITE = (255, 255, 255)

# set up game loop
# define max FPS: 60 frames per second
FPS = 60
# clock object to make sure our loop runs at this speed
clock = pygame.time.Clock()
# controls the game loop
run = True

# the game loop
while run:
    # to make sure our loop runs at predefined speed
    clock.tick(FPS)

    # window background
    win.fill(WHITE)
    # draw hangman image
    win.blit(images[hangman_status], (150, 100))
    # update display
    pygame.display.update()

    # check for mouseclick events
    # any event that happens will be stored in pygame.event.get()
    for event in pygame.event.get():
        # click red 'x' button
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # get (x, y) position of mouse
            # for comparing position of mouse to positions of buttons
            pos = pygame.mouse.get_pos()
            print(pos)

# out of the game loop
# quit the game
pygame.quit()
