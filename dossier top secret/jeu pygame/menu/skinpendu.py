import pygame
from pygame.locals import *
pygame.init()


import random
import math
import sys


from pathlib import Path
path = Path(__file__).resolve()

fenetre = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)




def skinchoice(n) :
    return range(1, 21)
    y =[]
    for k in [2 ,4, 5, 10] :
        if n%k == 0 :
            for i in range(k) :
                pass
            



class skins :

    def __init__(self, nb) :

        self.img = pygame.image.load(str(path.parent) + "/lettres/Pendu sprite/lettre" + str(nb) + ".png").convert()

        self.nb = nb+1




# skin = {}
# for i in range(19) :
#     skin[i+1] = skins(i)

























