import pygame
from pygame.locals import *
import time
import sys

# colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
NAVY_BLUE = (0, 0, 100)

# informations
width = 300
height = 300

# intialize the pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((width, height + 50), 0, 32)

# setting fps
fps = 30
CLOCK = pygame.time.Clock()

# title and icon
pygame.display.set_caption("Tic Tac Toe")
icon = pygame.image.load("tic-tac-toe 1.png")
pygame.display.set_icon((icon))

# game info
XO = "X"
grid = [[None, None, None], \
        [None, None, None], \
        [None, None, None]]
winner = None
draw = None

# loading the images as python object
xxx = pygame.image.load('-x-hiclipart.com.png')
ooo = pygame.image.load('-o-PinClipart.com_free-printable-clip-art_487240.png')

# resizing images
imgX = pygame.transform.scale(xxx, (80, 80))
imgO = pygame.transform.scale(ooo, (80, 80))


def gameBeginScreen():
    screen1 = pygame.display.set_mode((400, 400), 0, 32)

    game_start_screen = pygame.image.load('GAME START.png')

    screen1.fill(NAVY_BLUE, (0, 0, 400, 400))
    screen1.blit(game_start_screen, (0, 0))

    pygame.display.update()

    endgame = True
    while endgame:
        for event in pygame.event.get():
            if event.type is pygame.KEYUP:
                if event.key is K_SPACE:
                    endgame = False
                    screen = pygame.display.set_mode((width, height + 50), 0, 32)
            if event.type is QUIT:
                sys.exit()


def gameInitiatingWindow():
    screen.blit(screen, (0, 0))

    screen.fill(WHITE)

    # vertical lines
    pygame.draw.line(screen, BLACK, (100, 0), (100, 300), 3)
    pygame.draw.line(screen, BLACK, (200, 0), (200, 300), 3)

    # horizontal lines
    pygame.draw.line(screen, BLACK, (0, 100), (300, 100), 3)
    pygame.draw.line(screen, BLACK, (0, 200), (300, 200), 3)
    drawingStatus()
    pygame.display.update()


def drawingStatus():
    global XO, winner, draw

    if (winner is None):
        message = XO + "'s turn."
    else:
        message = "Congratulations. Winner is {}!".format(winner)

    if draw:
        message = "Game Draw!"

    font = pygame.font.SysFont("Viner Hand ITC", 20)
    text = font.render(message, True, BLACK)

    screen.fill((NAVY_BLUE), (0, 300, 300, 50))
    screen.blit(text, (10, 310))

    pygame.display.update()


def divideScreen(mouseX, mouseY):
    # rows
    if (mouseY < 100):
        row = 0
    elif (mouseY < 200):
        row = 1
    elif (mouseY < 300):
        row = 2

    # columns
    if (mouseX < 100):
        col = 0
    elif (mouseX < 200):
        col = 1
    else:
        col = 2

    return (row, col)


def drawingMove(screen, screenRow, screenCol, Piece):
    centerX = (screenCol * 100) + 50
    centerY = (screenRow * 100) + 50

    if (Piece == "X"):
        screen.blit(imgX, (centerX - 40, centerY - 40))
    else:
        screen.blit(imgO, (centerX - 40, centerY - 40))
    pygame.display.update()

    grid[screenRow][screenCol] = Piece


def clickScreen(screen):
    global XO, grid

    (mouseX, mouseY) = pygame.mouse.get_pos()
    (row, col) = divideScreen(mouseX, mouseY)

    if (grid[row][col] == "X" or grid[row][col] == "O"):
        return

    drawingMove(screen, row, col, XO)

    if XO == "X":
        XO = "O"
    else:
        XO = "X"


def gameWon(screen):
    global winner, grid, draw

    for row in range(0, 3):
        if ((grid[row][0] == grid[row][1] == grid[row][2]) and (grid[row][0] is not None)):
            winner = grid[row][0]
            pygame.draw.line(screen, RED, (0, (row + 1) * 100 - 50), (300, (row + 1) * 100 - 50), 4)
            break

    for col in range(0, 3):
        if ((grid[0][col] == grid[1][col] == grid[2][col]) and (grid[0][col] is not None)):
            winner = grid[0][col]
            pygame.draw.line(screen, RED, ((col + 1) * 100 - 50, 0), ((col + 1) * 100 - 50, 300), 4)
            break

    if ((grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] is not None)):

        winner = grid[0][0]
        pygame.draw.line(screen, RED, (0, 0), (300, 300), 4)

    elif ((grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] is not None)):

        winner = grid[0][2]
        pygame.draw.line(screen, RED, (300, 0), (0, 300), 4)

    if (all([all(row) for row in grid]) and winner is None):
        draw = True

    pygame.display.update()


def endgameWon():
    global XO, grid, winner, draw

    time.sleep(1)

    screen1 = pygame.display.set_mode((400, 400), 0, 32)
    game_start_screen = pygame.image.load('GAME START.png')
    screen1.blit(game_start_screen, (0, 0))

    pygame.display.update()

    endgame = True
    while endgame:
        for event in pygame.event.get():
            if event.type is pygame.KEYUP:
                if event.key is K_SPACE:
                    endgame = False
                    screen = pygame.display.set_mode((width, height + 50), 0, 32)
            if event.type is QUIT:
                sys.exit()
    gameInitiatingWindow()
    XO = "X"
    grid = [[None, None, None], \
            [None, None, None], \
            [None, None, None]]
    winner = None
    draw = False


def endgameDraw():
    global XO, grid, draw, winner

    time.sleep(1)

    screen1 = pygame.display.set_mode((400, 400), 0, 32)
    game_start_screen = pygame.image.load('GAME DRAW.png')
    screen1.blit(game_start_screen, (0, 0))

    pygame.display.update()

    endgame = True
    while endgame:
        for event in pygame.event.get():
            if event.type is pygame.KEYUP:
                if event.key is K_SPACE:
                    endgame = False
                    screen = pygame.display.set_mode((width, height + 50), 0, 32)
            if event.type is QUIT:
                sys.exit()

    gameInitiatingWindow()
    XO = "X"
    grid = [[None, None, None], \
            [None, None, None], \
            [None, None, None]]
    winner = None
    draw = False


# game loop
running = True

gameBeginScreen()
gameInitiatingWindow()

while running:
    for event in pygame.event.get():
        if event.type is QUIT:
            running = False
        elif event.type is MOUSEBUTTONDOWN:
            clickScreen(screen)
    gameWon(screen)
    drawingStatus()
    if winner:
        endgameWon()
    elif draw:
        endgameDraw()
    pygame.display.update()
    CLOCK.tick(fps)

pygame.quit()
