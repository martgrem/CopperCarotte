import pygame
from pygame.locals import *
pygame.init()


import random
import math
import sys

fenetre = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

class letters :



    def __init__(self, lettre) :
        
        self.nom = "btn" + str(lettre)
        self.img = pygame.image.load("CopperCarotte/dossier top secret/jeu pygame/play/lettres/" + self.nom + ".png").convert_alpha()
        self.pos = self.img.get_rect()





class guessing :

    def __init__(self, nb) :
        print(self)

        self.nom = "lettre" + str(nb)
        self.pos = 0 # un truc du genre : pos du 1er carré + (nb - 1) * (largeur d'un carré + espace entre chaque carré)
        self.img = pygame.image.load("CopperCarotte/dossier top secret/jeu pygame/play/lettres/noletter.png").convert_alpha() # charge une image vide au début
        self.img = pygame.transform.scale(self.img, (100, 100))  # resize à la taille de lettre voulue
        self.pos = self.img.get_rect()


letter1 = guessing(1)