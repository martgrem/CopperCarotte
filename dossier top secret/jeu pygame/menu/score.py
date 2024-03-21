import pygame
from pygame.locals import *
pygame.init()


import random
import math
import sys


from pathlib import Path
path = Path(__file__).resolve()

fenetre = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)




class score :
    
    def __init__(self,nb, val = "") :
        self.val = val
        if val == "" :
            self.img = pygame.image.load(str(path.parent) + "/lettres/chiffres/" + "chiffrevide" + ".png").convert()
        elif val == "-" :
            self.img = pygame.image.load(str(path.parent) + "/lettres/chiffres/" + "chiffremoins" + ".png").convert()
        else :
            self.img = pygame.image.load(str(path.parent) + "/lettres/chiffres/chiffre" + str(val) + ".png").convert()
        self.img = pygame.transform.scale(self.img, (300,300))
        self.wanted_pos = (2240/2 - 150 + 300 + 100 - (nb - 1)*(300 + 100), 1260/2 - 150)





    def write(self, newval) :
        self.val = newval
        if newval == "" :
            self.img = pygame.image.load(str(path.parent) + "/lettres/chiffres/" + "chiffrevide" + ".png").convert()
        elif newval == "-" :
            self.img = pygame.image.load(str(path.parent) + "/lettres/chiffres/" + "chiffremoins" + ".png").convert()
        else :
            self.img = pygame.image.load(str(path.parent) + "/lettres/chiffres/chiffre" + str(newval) + ".png").convert()
        self.img = pygame.transform.scale(self.img, (300,300))


















