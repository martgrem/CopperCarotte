import pygame
from pygame.locals import *
pygame.init()


import random
import math
import sys


from pathlib import Path
path = Path(__file__).resolve()

fenetre = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


class skins :

    def _init__(self, lettre, nb) :

        self.nom = "lettre" + str(lettre)

        self.img = pygame.image.load(str(path.parent) + "/lettres/newletters/" + str(self.nom) + ".png").convert()





























