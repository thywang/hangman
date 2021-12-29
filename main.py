import pygame
import os

pygame.init()
WIDTH, HEIGHT = 800, 500
pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

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
    # check for mouseclick events
    # any event that happens will be stored in pygame.event.get()
    for event in pygame.event.get():
        # click red 'x' button
        if event.type == pygame.QUIT:
            run = False

# out of the game loop
# quit the game
pygame.quit()
