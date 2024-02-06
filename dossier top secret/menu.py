import pygame
from pygame.locals import *
pygame.init()


import random
import math


fenetre = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pos_fenetre = fenetre.get_rect()





pygame.display.flip()

def menu() :
    cont = True
    while cont:    
        for event in pygame.event.get():
            if event.type == QUIT:
                cont=False






























