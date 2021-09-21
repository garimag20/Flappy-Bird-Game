import random #For generating random numbers
import sys #will use sys.exit to exit game
import pygame 
from pygame.locals import * #basi pygame imports

#Global variables for the game
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511

SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'Gallery/Sprites/bird.png'
BACKGROUND = 'Gallery/Sprites/bg.png'
PIPE = 'Gallery/Sprites/pipe.png'

#Main function from where game starts
if __name__ == "__main__":
    pygame.init() #To initialize all pygame's module
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird')
    GAME_SPRITES['numbers'] = (
        pygame.image.load('Gallery/Sprites/0.png').convert_alpha(),
        pygame.image.load('Gallery/Sprites/1.png').convert_alpha(),
        pygame.image.load('Gallery/Sprites/2.png').convert_alpha(),
        pygame.image.load('Gallery/Sprites/3.png').convert_alpha(),
        pygame.image.load('Gallery/Sprites/4.png').convert_alpha(),
        pygame.image.load('Gallery/Sprites/5.png').convert_alpha(),
        pygame.image.load('Gallery/Sprites/6.png').convert_alpha(),
        pygame.image.load('Gallery/Sprites/7.png').convert_alpha(),
        pygame.image.load('Gallery/Sprites/8.png').convert_alpha(),
        pygame.image.load('Gallery/Sprites/9.png').convert_alpha()
        
    )

    GAME_SPRITES['base'] = pygame.image.load('Gallery/Sprites/base.png').convert_alpha()
    GAME_SPRITES['pipe'] = (
        pygame.image.load('Gallery/Sprites/0.png').convert_alpha(),
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
        pygame.image.load(PIPE).convert_alpha()
    )

    #Game Sounds
    GAME_SOUNDS['die'] = pygame.mixer.Sound('Gallery/Audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('Gallery/Audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('Gallery/Audio/point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('Gallery/Audio/swoosh.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('Gallery/Audio/wing.wav')

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

    while True:
        welcomeScreen()
        mainGame() #This is main game function
