import pygame
from pygame.locals import *
pygame.init()


import random
import math
import sys





def menu() :



    fenetre = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pos_fenetre = fenetre.get_rect()
    fond = pygame.image.load("CopperCarotte/dossier top secret/menu/fond d'écran menu.jpg").convert()
    fond = pygame.transform.scale(fond, pos_fenetre.size)

    playbtn = pygame.image.load("CopperCarotte/dossier top secret/menu/boutons menu/Bouton Jouer.png").convert()
    pos_playbtn = playbtn.get_rect()
    playbtn = pygame.transform.scale(playbtn, (588, 232))
    pos_playbtn[0], pos_playbtn[1] = pos_fenetre.size[0]/2 - pos_playbtn[2]/2, pos_fenetre.size[1]/2 - pos_playbtn[3]/2 - 200

    #setbtn = 


    fenetre.blit(fond, (0, 0))
    fenetre.blit(playbtn, (pos_playbtn[0], pos_playbtn[1]))
    pygame.display.flip()






    cont = True
    while cont:    

        fenetre.blit(fond, (0, 0))
        fenetre.blit(playbtn, (pos_playbtn[0], pos_playbtn[1]))
        pygame.display.flip()


        for event in pygame.event.get():
            if event.type == QUIT:
                cont=False
                pygame.display.quit()
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :
                    cont=False
                    pygame.display.quit()
                        



menu()

























