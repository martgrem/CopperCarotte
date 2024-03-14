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







def position(n : int, lx, ly) :
    '''
    calculer les coordonées du bouton correspondant à chaque lettre
    n = nombre de la lettre
    lx, ly = dimensions de la lettre
    '''
    ox, oy = 75, 63
    xspace = lx/3
    yspace = ly/3

    xpos, ypos = calcpos(n)    # position ou 1 lettre = 1 unité

    vx = ox + xpos*(lx + xspace) # position en pixels
    vy = oy + ypos*(ly + yspace)
    if ypos%2 == 0 :
        vx += lx/2
    return vx, vy






def calcpos(n : int) :
    '''
    renvoie la ligne et la colonnne sur lesquelles se trouve la n-ème lettre (part de 0)
    '''
    c = 0
    l = -1 #no de ligne
    while True :
        n -= 6 + c
        l += 1
        if n < 0 :
            return n + 6 + c, l
        
        c = (c+1)%2










class letters :

    def __init__(self, lettre, nb) :
        
        self.nom = "lettre" + str(lettre)
        self.ln = 125
        self.guess = False
        self.justguessed = False
        self.img = pygame.image.load(str(script_path.parent) + "/lettres/newletters/" + str(self.nom) + ".png").convert()
        self.img = pygame.transform.scale(self.img, (125, 125))
        self.usedimg = pygame.image.load(str(script_path.parent) + "/lettres/usedletters/" + str(self.nom) + ".png").convert()
        self.usedimg = pygame.transform.scale(self.usedimg, (125, 125))
        self.pos = self.img.get_rect() #non utilisé
        self.usedpos = self.usedimg.get_rect() #non utilisé
        self.wanted_pos = position(nb, self.ln, self.ln)


lettre = {}
for j, i in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZéèêëàäâîìïôöòûüùÿç-") :
    lettre[i] = letters(i, j)

# print(lettre["-"])

# print(lettre["-"].wanted_pos)


 












































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