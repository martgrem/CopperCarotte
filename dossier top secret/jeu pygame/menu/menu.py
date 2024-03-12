import pygame
from pygame.locals import *
pygame.init()


import random
import math
import os
import sys

from pathlib import Path
script_path = Path(__file__).resolve()
print(script_path)
import lettres
import game


hard = False






def menu() :



    fenetre = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pos_fenetre = fenetre.get_rect()
    print(pos_fenetre)
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
    global hard
    essayés = []
    if hard :
        f = open(str(script_path.parent.parent.parent)+"/liste_de_mots_français_frgut.txt")
    else :
        f = open(str(script_path.parent.parent.parent)+"/listemotscourants.txt")
    réponses = f.readlines()
    f.close()
    answer, oùilenest, nb_essais = game.init(réponses)
    
    #fenetre = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pos_fenetre = fenetre.get_rect()
    print(pos_fenetre.size)
    fond = pygame.image.load(str(script_path.parent) + "/fond d'écran menu.jpg").convert()
    fond = pygame.transform.scale(fond, pos_fenetre.size)
        
    lettre = {}
    for j, i in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZéèêëàäâîìïôöòûüùÿç-") :
        lettre[i] = lettres.letters(i, j)

    print(lettre["-"])

    pygame.display.flip()


    while cont:    
        
        fenetre.blit(fond, (0, 0))


        for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZéèêëàäâîìïôöòûüùÿç-" :
            if not lettre[i].guess : #si la lettre n'est pas encore essayée        (à faire pour toutes les lettres)
                fenetre.blit(lettre[i].img, lettre[i].wanted_pos)
            elif lettre[i].guess : #si la lettre n'est pas encore essayée        (à faire pour toutes les lettres)
                fenetre.blit(lettre[i].usedimg, lettre[i].wanted_pos)



            # exemple pour une seule lettre
        # if not guessA : #si a n'est pas encore essayé        (à faire pour toutes les lettres)
        #     fenetre.blit(btn, (pos_btnA[0] + pos_btnA[2]/2 - pos_btn[2]/2, pos_btnA[1] + pos_btnA[3]/2 - pos_btn[3]/2 + 8))
        #     fenetre.blit(btnA, (pos_btnA[0], pos_btnA[1]))
        # else :
        #     fenetre.blit(usedbtn, (pos_btnA[0] + pos_btnA[2]/2 - pos_usedbtn[2]/2, pos_btnA[1] + pos_btnA[3]/2 - pos_usedbtn[3]/2 + 8))
        #     fenetre.blit(btnA, (pos_btnA[0], pos_btnA[1]))
        

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
                    lettre["A"].guess = True
                    lettre["A"].justguessed =True
                elif event.key == K_b :
                    lettre["B"].guess = True
                    lettre["B"].justguessed =True
                elif event.key == K_c :
                    lettre["C"].guess = True
                    lettre["C"].justguessed =True
                elif event.key == K_d :
                    lettre["D"].guess = True
                    lettre["D"].justguessed =True
                elif event.key == K_e :
                    lettre["E"].guess = True
                    lettre["E"].justguessed =True
                elif event.key == K_f :
                    lettre["F"].guess = True
                    lettre["F"].justguessed =True
                elif event.key == K_g :
                    lettre["G"].guess = True
                    lettre["G"].justguessed =True
                elif event.key == K_h :
                    lettre["H"].guess = True
                    lettre["H"].justguessed =True
                elif event.key == K_i :
                    lettre["I"].guess = True
                    lettre["I"].justguessed =True
                elif event.key == K_j :
                    lettre["J"].guess = True
                    lettre["J"].justguessed =True
                elif event.key == K_k :
                    lettre["K"].guess = True
                    lettre["K"].justguessed =True
                elif event.key == K_l :
                    lettre["L"].guess = True
                    lettre["L"].justguessed =True
                elif event.key == K_m :
                    lettre["M"].guess = True
                    lettre["M"].justguessed =True
                elif event.key == K_n :
                    lettre["N"].guess = True
                    lettre["N"].justguessed =True
                elif event.key == K_o :
                    lettre["O"].guess = True
                    lettre["O"].justguessed =True
                elif event.key == K_p :
                    lettre["P"].guess = True
                    lettre["P"].justguessed =True
                elif event.key == K_q :
                    lettre["Q"].guess = True
                    lettre["Q"].justguessed =True
                elif event.key == K_r :
                    lettre["R"].guess = True
                    lettre["R"].justguessed =True
                elif event.key == K_s :
                    lettre["S"].guess = True
                    lettre["S"].justguessed =True
                elif event.key == K_t :
                    lettre["T"].guess = True
                    lettre["T"].justguessed =True
                elif event.key == K_u :
                    lettre["U"].guess = True
                    lettre["U"].justguessed =True
                elif event.key == K_v :
                    lettre["V"].guess = True
                    lettre["V"].justguessed =True
                elif event.key == K_w :
                    lettre["W"].guess = True
                    lettre["W"].justguessed =True
                elif event.key == K_x :
                    lettre["X"].guess = True
                    lettre["X"].justguessed =True
                elif event.key == K_y :
                    lettre["Y"].guess = True
                    lettre["Y"].justguessed =True
                elif event.key == K_z :
                    lettre["Z"].guess = True
                    lettre["Z"].justguessed =True

            if event.type == MOUSEBUTTONDOWN :
                if pygame.mouse.get_pressed()[0] :
                    mspos = pygame.mouse.get_pos()


                    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZéèêëàäâîìïôöòûüùÿç-" :
                        if lettre[i].wanted_pos[0] <= mspos[0] <= lettre[i].wanted_pos[0] + lettre[i].ln and lettre[i].wanted_pos[1] <= mspos[1] <= lettre[i].wanted_pos[1] + lettre[i].ln and not lettre[i].guess:
                            lettre[i].guess = True
                            lettre[i].justguessed =True

            for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZéèêëàäâîìïôöòûüùÿç-" :
                if lettre[i].justguessed :
                    lettre[i].justguessed = False
                    justesse, pénalité, oùilenest, essayés = game.deviner(answer, oùilenest, hard, essayés, lettre[i].nom)
                    if pénalité :
                        nb_essais += 1
                    if not justesse :
                        pass




def settings(fenetre) :
    cont = True

    #fenetre = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pos_fenetre = fenetre.get_rect()
    fond = pygame.image.load("CopperCarotte/dossier top secret/jeu pygame/menu/fond d'écran menu.jpg").convert()
    fond = pygame.transform.scale(fond, pos_fenetre.size)

    #boum = pygame.image.load("neauteubouqueux/PyGame/BOUM.png").convert_alpha()
    #boum = pygame.transform.scale(boum, (1000, 1000))
    fenetre.blit(fond, (0, 0))
    #fenetre.blit(boum, (250, 0))
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
















