import pygame
from pygame.locals import *
pygame.init()


import random
import math
import os
import sys





def menu() :



    fenetre = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pos_fenetre = fenetre.get_rect()
    fond = pygame.image.load("CopperCarotte/dossier top secret/jeu pygame/menu/fond d'écran menu.jpg").convert()
    fond = pygame.transform.scale(fond, pos_fenetre.size)

    playbtn = pygame.image.load("CopperCarotte/dossier top secret/jeu pygame/menu/boutons menu/Bouton Jouer.png").convert()
    pos_playbtn = playbtn.get_rect()
    playbtn = pygame.transform.scale(playbtn, (588, 232))
    pos_playbtn[0], pos_playbtn[1] = pos_fenetre.size[0]/2 - pos_playbtn[2]/2, pos_fenetre.size[1]/2 - pos_playbtn[3]/2 - 200

    setbtn = pygame.image.load("CopperCarotte/dossier top secret/jeu pygame/menu/boutons menu/Bouton Paramètres.png").convert()
    pos_setbtn = setbtn.get_rect()
    setbtn = pygame.transform.scale(setbtn, (744, 232))
    pos_setbtn[0], pos_setbtn[1] = pos_fenetre.size[0]/2 - pos_setbtn[2]/2, pos_fenetre.size[1]/2 - pos_setbtn[3]/2 + 100


    fenetre.blit(fond, (0, 0))
    fenetre.blit(playbtn, (pos_playbtn[0], pos_playbtn[1]))
    fenetre.blit(setbtn, (pos_setbtn[0], pos_setbtn[1]))
    pygame.display.flip()






    cont = True
    while cont:    

        fenetre.blit(fond, (0, 0))
        fenetre.blit(playbtn, (pos_playbtn[0], pos_playbtn[1]))
        fenetre.blit(setbtn, (pos_setbtn[0], pos_setbtn[1]))
        pygame.display.flip()


        for event in pygame.event.get():
            if event.type == QUIT:
                cont=False
                pygame.display.quit()
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :
                    cont=False
                    pygame.display.quit()
            if event.type == MOUSEBUTTONDOWN :
                if pygame.mouse.get_pressed()[0] :
                    pos = pygame.mouse.get_pos()
                    if pos_playbtn[0] <= pos[0] <= pos_playbtn[0] + pos_playbtn[2] and pos_playbtn[1] <= pos[1] <= pos_playbtn[1] + pos_playbtn[3] :
                        jeu(fenetre)
                    if pos_setbtn[0] <= pos[0] <= pos_setbtn[0] + pos_setbtn[2] and pos_setbtn[1] <= pos[1] <= pos_setbtn[1] + pos_setbtn[3] :
                        settings(fenetre)




def jeu(fenetre) :
    cont = True
    
    #fenetre = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pos_fenetre = fenetre.get_rect()
    fond = pygame.image.load("CopperCarotte/dossier top secret/jeu pygame/menu/fond d'écran menu.jpg").convert()
    fond = pygame.transform.scale(fond, pos_fenetre.size)

    btn = pygame.image.load("CopperCarotte/dossier top secret/jeu pygame/play/lettres/lettre vide.png").convert()
    btn = pygame.transform.scale(btn, (125, 125))
    pos_btn = btn.get_rect()

    usedbtn = pygame.image.load("CopperCarotte/dossier top secret/jeu pygame/play/lettres/lettre vide utilisée.png").convert()
    usedbtn = pygame.transform.scale(usedbtn, (125, 125))
    pos_usedbtn = usedbtn.get_rect()
    
    btnA =pygame.image.load("CopperCarotte/dossier top secret/jeu pygame/play/lettres/Letter_A.svg.png").convert_alpha()
    btnA = pygame.transform.scale(btnA, (125, 125))
    pos_btnA = btnA.get_rect()
    pos_btnA[0], pos_btnA[1] = 150 - pos_btnA[2]/2, 650 - pos_btnA[3]/2
    
    fenetre.blit(fond, (0, 0))

    fenetre.blit(btn, (pos_btnA[0] + pos_btnA[2]/2 - pos_btn[2]/2, pos_btnA[1] + pos_btnA[3]/2 - pos_btn[3]/2 + 8))
    fenetre.blit(btnA, (pos_btnA[0], pos_btnA[1]))

    pygame.display.flip()

    guessA, guessB, guessC, guessD, guessE, guessF, guessG, guessH, guessI, guessJ, guessK, guessL, guessM, guessN, guessO, guessP, guessQ, guessR, guessS, guessT, guessU, guessV, guessW, guessX, guessY, guessZ = False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False


    while cont:    
        
        fenetre.blit(fond, (0, 0))

        if not guessA : #si a n'est pas encore essayé        (à faire pour toutes les lettres)
            fenetre.blit(btn, (pos_btnA[0] + pos_btnA[2]/2 - pos_btn[2]/2, pos_btnA[1] + pos_btnA[3]/2 - pos_btn[3]/2 + 8))
            fenetre.blit(btnA, (pos_btnA[0], pos_btnA[1]))
        else :
            fenetre.blit(usedbtn, (pos_btnA[0] + pos_btnA[2]/2 - pos_usedbtn[2]/2, pos_btnA[1] + pos_btnA[3]/2 - pos_usedbtn[3]/2 + 8))
            fenetre.blit(btnA, (pos_btnA[0], pos_btnA[1]))
        

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                cont=False
                pygame.display.quit()

            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :
                    cont=False
                    return


                if event.key == K_a :
                    guessA = True

            if event.type == MOUSEBUTTONDOWN :
                if pygame.mouse.get_pressed()[0] :
                    mspos = pygame.mouse.get_pos()



                    if pos_btnA[0] + pos_btnA[2]/2 - pos_btn[2]/2 <= mspos[0] <= pos_btnA[0] + pos_btnA[2]/2 + pos_btn[2]/2 and pos_btnA[1] + pos_btnA[3]/2 - pos_btn[3]/2 <= mspos[1] <= pos_btnA[1] + pos_btnA[3]/2 + pos_btn[3]/2  :
                        guessA = True




def settings(fenetre) :
    cont = True

    #fenetre = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pos_fenetre = fenetre.get_rect()
    fond = pygame.image.load("CopperCarotte/dossier top secret/jeu pygame/menu/fond d'écran menu.jpg").convert()
    fond = pygame.transform.scale(fond, pos_fenetre.size)

    boum = pygame.image.load("neauteubouqueux/PyGame/BOUM.png").convert_alpha()
    boum = pygame.transform.scale(boum, (1000, 1000))
    fenetre.blit(fond, (0, 0))
    fenetre.blit(boum, (250, 0))
    pygame.display.flip()
    while cont:    
        

        


        for event in pygame.event.get():
            if event.type == QUIT:
                cont=False
                pygame.display.quit()
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :
                    cont=False
                    return   




menu()







def justpathing(image) :
    absolutepath = os.path.abspath(__file__)
    fileDirectory = os.path.dirname(absolutepath)
    fileDirectory = os.path.dirname(fileDirectory)
    if image == "fond" :
        newPath = os.path.join(fileDirectory, "fond d'écran menu.png")
    elif image == "Jouer" :
        newPath = os.path.join(fileDirectory, "Bouton Jouer.png")

    return newPath
















