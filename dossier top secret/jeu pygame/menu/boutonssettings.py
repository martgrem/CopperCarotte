import pygame
from pygame.locals import *
pygame.init()

import os
import sys

from pathlib import Path
path = Path(__file__).resolve()
# print(path)
# print(sys.path)
sys.path.append(str(path.parent.parent.parent))
# print(sys.path)



class essaisnb :

    def __init__(self, nb) :
        
        self.img = pygame.image.load(str(path.parent) + "/lettres/newletters/lettre" + str(nb) + ".png").convert()
        self.img = pygame.transform.scale(self.img, (500, 232))

        self.wanted_pos = (2240/2 - 250, 1260/2 - 116)



class arrows :

    def __init__(self, dir) :
        self.img = pygame.image.load(str(path.parent) + "/lettres/newletters/lettre" + str(dir+1) + ".png").convert()
        self.img = pygame.transform.scale(self.img, (100, 100))
        self.wantedpos = (2240/2 + 250 + 50, 1260/2 - 116 )

















