import pygame
from pygame.locals import *
pygame.init()


import random
import math
import sys


from pathlib import Path
path = Path(__file__).resolve()

fenetre = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)




def calcpos(n : int) :
    '''
    renvoie la ligne et la colonnne sur lesquelles se trouve la n-ème lettre du mot (part de 0) (affichée ou non)
    '''

    lnx = 5 #longueur d'une ligne

    # c = 0
    # l = -1 #no de ligne
    # while True :
    #     n -= lnx
    #     l += 1
    #     if n < 0 :
    return n%lnx , n//lnx
        
        #c = (c+1)%2





def position(n : int, lx, ly) :
    '''
    calculer les coordonées de la lettre du mot (affichée ou non)
    n = nombre de la lettre
    lx, ly = dimensions de la lettre
    '''
    ox, oy = 1480, 800
    xspace = lx/3
    yspace = ly/3

    xpos, ypos = calcpos(n-1)    # position ou 1 lettre = 1 unité

    vx = ox + xpos*(lx + xspace) # position en pixels
    vy = oy + ypos*(ly + yspace)
    # if ypos%2 == 0 :
    #     vx += lx/2 + xspace/2
    return vx, vy







class deviningletters :

    def __init__(self, nb) :
        self.nom = "lettre" +str(nb)
        self.nb = nb
        self.img = pygame.image.load(str(path.parent) + "/lettres/lettrevide/" + "lettre_" + ".png").convert()
        self.img = pygame.transform.scale(self.img, (75, 75))
        self.status = ""
        self.ln = 75
        self.wanted_pos = position(self.nb, self.ln, self.ln)

    def write(self, newstatus) :
        self.status = newstatus
        if newstatus == "_" :
            self.img = pygame.image.load(str(path.parent) + "/lettres/lettrevide/" + "lettre_" + ".png").convert()
            self.img = pygame.transform.scale(self.img, (75, 75))
        elif newstatus == "" :
            self.img = pygame.image.load(str(path.parent) + "/lettres/lettrevide/" + "lettrevide" + ".png").convert()
            self.img = pygame.transform.scale(self.img, (75, 75))
        else :
            self.img = pygame.image.load(str(path.parent) + "/lettres/newletters/lettre" + str(newstatus) + ".png").convert()
            self.img = pygame.transform.scale(self.img, (75, 75))
        


# x = deviningletters(1)

# devining = {}
# for i in range(19) :
#     devining[i+1] = deviningletters(i+1)

# print(x.wanted_pos)






