import pygame
import math
import random

# Set up display

pygame.init()
WIDTH, HEIGHT = (1200, 600)
window = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("SPELLING BEE!")

FPS = 60
clock = pygame.time.Clock()

# FONTS

LETTER_FONT = pygame.font.SysFont("comicsans", 40)
WORD_FONT = pygame.font.SysFont("comicsans", 60)
TITLE_FONT = pygame.font.SysFont("comicsans", 70)

# LOAD IMAGES

images = []
for i in range(6):
    image = pygame.image.load("images/Bee" + str(i) + ".png")
    images.append(image)

# BUTTON VARIABLES

RADIUS = 20
GAP = 10
letters = []
#startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
startx = 400
starty = 440
A = 65

for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# GAME VARIABLES

bee_status = 0
words = ["CODING", "OBJECT", "ENCAPSULATION", "POLYMORPHISM", "INHERITANCE", "BLIMEY",
         "FIDGETTY", "MAKERS", "LIMPET", "SECURITY", "INTERCONNECTIVITY", "ABSOLUTELY", ]
word = random.choice(words)
guessed = []

# COLOURS

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# GAME FUNCTIONS


def draw():

    # DRAW BEE
    window.blit(images[bee_status], (-20, 100))
    pygame.display.update()

    window.fill(WHITE)

    

    # DRAW TITLE
    text = TITLE_FONT.render("DEADLY SPELLING BEE!", 1, BLACK)
    window.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    

    # DRAW WORD
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    window.blit(text, (500, 200))

    
    
    # DRAW BUTTONS
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(window, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            window.blit(text, (x - text.get_width() /
                        2, y - text.get_height()/2))
    
   


def display_message(colour, message):
    pygame.time.delay(2000)
    window.fill(colour)
    text = WORD_FONT.render(message, 1, BLACK)
    window.blit(text, (WIDTH/2 - text.get_width() /
                       2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)


# MAIN GAME LOOP
run = True

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()

            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                    if dis < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            bee_status += 1

    draw()

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break

    if won:
        display_message(BLUE, "YOU WON")
        break

    if bee_status == 5:
        display_message(RED, "YOU LOST")
        break

pygame.quit()
