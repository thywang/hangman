import pygame
import math

# set up display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

# button variables
RADIUS = 20
GAP = 15
# store [x, y, letter, boolean value (if clicked or not)] in each element of letters
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
    letters.append([x, y, chr(A + i), True])

print(letters)

# load images
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

# game variables
hangman_status = 0
# word to be guessed
word = "BLUENOSE"
# letters guessed
guessed = []

# fonts
LETTER_FONT = pygame.font.SysFont('helveticaneue', 30)
WORD_FONT = pygame.font.SysFont('comicsans', 50)

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

    # draw word
    display_word = ""
    for letter in word:
        # check if letter has been guessed
        if letter in guessed:
            # space added for readability
            display_word += letter + " "
        else:
            display_word += "_ "
    # render the word
    text = WORD_FONT.render(display_word, 1, BLACK)
    # display on screen
    win.blit(text, (400, 200))

    # draw buttons
    for letter in letters:
        # unpacking the variable
        x, y, ltr, visible = letter
        if visible:
            # where, what color, position of centre, radius, thickness
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            # render text (what we want to render, anti-aliasing, color)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            # draw the text
            win.blit(text, (x - text.get_width() /
                     2, y - text.get_height() / 2))

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
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                # unpacking
                x, y, ltr, visible = letter
                if visible:
                    # check for collision
                    # Pythagoras to determine the distance between mouse and centre of button
                    dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                    if dis < RADIUS:
                        # because 'visible' is actually a copy of letter[3]
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1
 # check if user won
    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break
# out of the game loop
# quit the game
pygame.quit()
