import pygame
import os

# set up display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

# button variables
RADIUS = 20
GAP = 15
# store [x, y, letter] in each element of letters
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
# ASCII value
A = 65
# determine position of each button
for i in range(26):
    # two rows of buttons
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    # convert ASCII value to character
    letters.append([x, y, chr(A + i)])

print(letters)

# load images
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

# game variables
hangman_status = 4

# fonts
LETTER_FONT = pygame.font.SysFont('helveticaneue', 30)

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# set up game loop
# define max FPS: 60 frames per second
FPS = 60
# clock object to make sure our loop runs at this speed
clock = pygame.time.Clock()
# controls the game loop
run = True

# function to draw


def draw():
    # window background
    win.fill(WHITE)
    # draw buttons
    for letter in letters:
        # unpacking the variable
        x, y, ltr = letter
        # where, what color, position of centre, radius, thickness
        pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
        # render text (what we want to render, anti-aliasing, color)
        text = LETTER_FONT.render(ltr, 1, BLACK)
        # draw the text
        win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))
    # draw hangman image
    win.blit(images[hangman_status], (150, 100))
    # update display
    pygame.display.update()


# the game loop
while run:
    # to make sure our loop runs at predefined speed
    clock.tick(FPS)

    draw()

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
