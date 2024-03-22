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



class essaisch :

    def __init__(self, nb) :
        self.img = pygame.image.load(str(path.parent) + "/lettres/chiffres/chiffre" + str(nb) + ".png").convert()
        self.img = pygame.transform.scale(self.img, (31*5, 29*5))

        #self.wanted_pos = (2240/2 - 250, 1260/2 - 116)
        self.wanted_pos = (300, 485)


class essaisnb :

    def __init__(self, nb) :
        self.img1 = essaisch(nb[:1]).img
        self.img2 = essaisch(nb[1:]).img
        self.wanted_pos = (300,485), (300 + 155 + 50, 485)

















