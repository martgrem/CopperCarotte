import pygame
from pygame.locals import *
pygame.init()


import random
import math
import sys


from pathlib import Path
script_path = Path(__file__).resolve()

script_dir = str(script_path.parent) + "/fond d'écran menu.png"



fenetre = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

class letters :



    def __init__(self, lettre) :
        
        self.nom = "lettre" + str(lettre)
        self.img = pygame.image.load(str(script_path.parent) + "/lettres/newletters/" + str(self.nom) + ".png").convert()
        self.img = pygame.transform.scale(self.img, (125, 125))
        self.usedimg = pygame.image.load(str(script_path.parent) + "/lettres/usedletters/" + str(self.nom) + ".png").convert()
        self.img = pygame.transform.scale(self.usedimg, (125, 125))
        self.pos = self.img.get_rect()
        self.usedpos = self.usedimg.get_rect()
        self.usedpos = self.pos


lettre = {}
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZéèêëàäâîìïôöòûüùÿç-" :
    lettre[i] = letters(i)

print(lettre["-"])




 


























































class guessing :

    def __init__(self, nb) :

        self.nom = "lettre" + str(nb)
        self.pos = 0 # un truc du genre : pos du 1er carré + (nb - 1) * (largeur d'un carré + espace entre chaque carré)  pour X
        self.img = pygame.image.load("CopperCarotte/dossier top secret/jeu pygame/play/lettres/noletter.png").convert_alpha() # charge une image vide au début
        self.img = pygame.transform.scale(self.img, (125, 125))  # resize à la taille de lettre voulue
        self.pos = self.img.get_rect()
        self.pos[0], self.pos[1] = 150 - self.pos[2]/2 + (self.pos[2]+100)*(nb%7), 650 - self.pos[3]/2 + (self.pos[3]+75)*(nb//7)





"""

pour toutes les utiliser de manière efficace

guessingletter = {}
for i in range(1,27) :
    guessingletter[i] = "lettre" + str(i)
    guessingletter[i] = guessing(i)
"""


# guessingletter = {}
# for i in range(0,13) :
#     guessingletter[i] = guessing(i)



class guessed :

    def __init__(self, nb) :

        self.nom = "guessedletter" + str(nb)
        self.pos = 0 # un truc du genre : pos du 1er carré + ( (nb - 1) % (nblettre/ligne) ) * (largeur d'un carré + espace entre chaque carré) pour X et ( nb // (nblettre/ligne) ) * (largeur d'un carré + espace entre chaque carré)
        self.img = pygame.image.load("CopperCarotte/dossier top secret/jeu pygame/play/lettres/noletter.png").convert_alpha() # charge une image vide au début
        self.img = pygame.transform.scale(self.img, (75, 75))  # resize à la taille de lettre voulue
        self.pos = self.img.get_rect()
        self.pos[0], self.pos[1] = 125 - self.pos[2]/2 + (self.pos[2]+50)*(nb%7), 175 - self.pos[3]/2 + (self.pos[3]+25)*(nb//7)




        """

pour toutes les utiliser de manière efficace

guessedletter = {}
for i in range(1,27) :
    guessedletter[i] = "lettre" + str(i)
    guessedletter[i] = guessed(i)
"""

# guessedletter = {}
# for i in range(0,43) :
#     guessedletter[i] = guessed(i)

# print(guessingletter[5])