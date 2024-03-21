import pygame
from pygame.locals import *
pygame.init()


import random
import math
import sys


from pathlib import Path
path = Path(__file__).resolve()

fenetre = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)




def skinchoice(nb_essai) :
    
    if nb_essai== 20 :
        return range(0, 21)
    elif nb_essai == 15 :
        return (0,2,3,5,7,8,9,11,13,14,15,16,17,18,19,20)
    elif nb_essai == 10 :
        return (0,3,5,7,9,11,13,15,18,19,20)
    elif nb_essai ==5 :
        return (0,7,11,15,19,20)

            



class skins :

    def __init__(self, nb) :

        self.img = pygame.image.load(str(path.parent) + "/lettres/Pendu sprite/lettre" + str(nb) + ".png").convert()
        self.img = pygame.transform.scale(self.img, (162,170))
        self.nb = nb+1




# skin = {}
# for i in range(19) :
#     skin[i+1] = skins(i)

























