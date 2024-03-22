import pygame
from pygame.locals import *
pygame.init()


import random as aleajactaest
import math
import os
import sys

from pathlib import Path
script_path = Path(__file__).resolve()
import lettres
import game
import skinpendu
import devinage
#import leaderboard
import score
import boutonssettings


hard = False
bordel = aleajactaest.choice([True, False, False])
nb_essais = 20




def menu() :
    '''
    Créé le menu avec tous les bouttons
    '''
    global script_path

    fenetre = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pos_fenetre = fenetre.get_rect()
    #print(pos_fenetre)
    fond = pygame.image.load(str(script_path.parent)+"/fond d'écran menu.jpg").convert()
    fond = pygame.transform.scale(fond, pos_fenetre.size)

    playbtn = pygame.image.load(str(script_path.parent)+"/boutons menu/Bouton Jouer.png").convert()
    pos_playbtn = playbtn.get_rect()
    playbtn = pygame.transform.scale(playbtn, (588, 232))
    pos_playbtn[0], pos_playbtn[1] = pos_fenetre.size[0]/2 - pos_playbtn[2]/2, pos_fenetre.size[1]/2 - pos_playbtn[3]/2 - 200

    setbtn = pygame.image.load(str(script_path.parent)+"/boutons menu/Bouton Paramètres.png").convert()
    pos_setbtn = setbtn.get_rect()
    setbtn = pygame.transform.scale(setbtn, (744, 232))
    pos_setbtn[0], pos_setbtn[1] = pos_fenetre.size[0]/2 - pos_setbtn[2]/2, pos_fenetre.size[1]/2 - pos_setbtn[3]/2 + 100

    compbtn = pygame.image.load(str(script_path.parent)+"/boutons menu/Bouton Compétition.png").convert()
    compbtn = pygame.transform.scale(compbtn, (135*5, 29*5))
    pos_compbtn = compbtn.get_rect()
    pos_compbtn[0], pos_compbtn[1] = pos_fenetre.size[0]/2 - pos_compbtn[2]/2, pos_fenetre.size[1]/2 - pos_compbtn[3]/2 + 350

    hsbtn = pygame.image.load(str(script_path.parent)+"/boutons menu/Leaderboard.png").convert()
    hsbtn = pygame.transform.scale(hsbtn, (135*5, 29*5))
    pos_hsbtn = hsbtn.get_rect()
    pos_hsbtn[0], pos_hsbtn[1] = pos_fenetre.size[0]/2 - pos_hsbtn[2]/2, pos_fenetre.size[1]/2 - pos_hsbtn[3]/2 + 550

    fenetre.blit(fond, (0, 0))
    fenetre.blit(playbtn, (pos_playbtn[0], pos_playbtn[1]))
    fenetre.blit(setbtn, (pos_setbtn[0], pos_setbtn[1]))
    fenetre.blit(compbtn, (pos_compbtn[0], pos_compbtn[1]))
    fenetre.blit(hsbtn, (pos_hsbtn[0], pos_hsbtn[1]))

    pygame.display.flip()






    cont = True
    while cont:    

        fenetre.blit(fond, (0, 0))
        fenetre.blit(playbtn, (pos_playbtn[0], pos_playbtn[1]))
        fenetre.blit(setbtn, (pos_setbtn[0], pos_setbtn[1]))
        fenetre.blit(compbtn, (pos_compbtn[0], pos_compbtn[1]))
        fenetre.blit(hsbtn, (pos_hsbtn[0], pos_hsbtn[1]))
        
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
                    elif pos_setbtn[0] <= pos[0] <= pos_setbtn[0] + pos_setbtn[2] and pos_setbtn[1] <= pos[1] <= pos_setbtn[1] + pos_setbtn[3] :
                        settings(fenetre)
                    elif pos_compbtn[0] <= pos[0] <= pos_compbtn[0] + pos_compbtn[2] and pos_compbtn[1] <= pos[1] <= pos_compbtn[1] + pos_compbtn[3] :
                        compétition(fenetre)
                    elif pos_hsbtn[0] <= pos[0] <= pos_hsbtn[0] + pos_hsbtn[2] and pos_hsbtn[1] <= pos[1] <= pos_hsbtn[1] + pos_hsbtn[3] :
                        leaderboard(fenetre)




def jeu(fenetre) :
    cont = True
    global hard
    global nb_essais
    nbessai = 0
    global script_path
    essayés = []
    countdown = -1
    ended = False

    if hard :
        f = open(str(script_path.parent.parent.parent)+"/liste_de_mots_francais_frgut.txt")
    else :
        f = open(str(script_path.parent.parent.parent)+"/listemotscourants.txt")
    réponses = f.readlines()
    f.close()
    answer, oùilenest = game.init(réponses)
    while len(answer) > 20 :
        answer, oùilenest = game.init(réponses)
    #answer, oùilenest = game.init(["testabab"])    # pour les tests
    #print(answer,oùilenest)
    #fenetre = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pos_fenetre = fenetre.get_rect()
    #print(pos_fenetre.size)
    fond = pygame.image.load(str(script_path.parent) + "/fond d'écran menu.jpg").convert()
    fond = pygame.transform.scale(fond, pos_fenetre.size)
        
    lettre = {}
    if bordel :
        for j, i in enumerate(aleajactaest.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZéèêëàäâîìïôöòûüùÿç-", len("ABCDEFGHIJKLMNOPQRSTUVWXYZéèêëàäâîìïôöòûüùÿç-"))) :
            lettre[i] = lettres.letters(i, j)
    else :
        for j, i in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZéèêëàäâîìïôöòûüùÿç-") :
            lettre[i] = lettres.letters(i, j)

    #print(lettre["-"])
    
    skin = {}
    for j, i in enumerate(skinpendu.skinchoice(nb_essais)) :
        skin[j] = skinpendu.skins(i)
    indskin = 0

    devining = {}
    for i in range(1, 21) :
        devining[i] = devinage.deviningletters(i)

    pygame.display.flip()


    while cont:    
        
        fenetre.blit(fond, (0, 0))

        for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZéèêëàäâîìïôöòûüùÿç-" :
            if not lettre[i].guess : #si la lettre n'est pas encore essayée        (à faire pour toutes les lettres)
                fenetre.blit(lettre[i].img, lettre[i].wanted_pos)
            elif lettre[i].guess : #si la lettre n'est pas encore essayée        (à faire pour toutes les lettres)
                fenetre.blit(lettre[i].usedimg, lettre[i].wanted_pos)

        fenetre.blit(skin[indskin].img, (1400, 100))

        for i in range(1, len(answer)+1) :
            fenetre.blit(devining[i].img, devining[i].wanted_pos)

            # exemple pour une seule lettre
        # if not guessA : #si a n'est pas encore essayé        (à faire pour toutes les lettres)
        #     fenetre.blit(btn, (pos_btnA[0] + pos_btnA[2]/2 - pos_btn[2]/2, pos_btnA[1] + pos_btnA[3]/2 - pos_btn[3]/2 + 8))
        #     fenetre.blit(btnA, (pos_btnA[0], pos_btnA[1]))
        # else :
        #     fenetre.blit(usedbtn, (pos_btnA[0] + pos_btnA[2]/2 - pos_usedbtn[2]/2, pos_btnA[1] + pos_btnA[3]/2 - pos_usedbtn[3]/2 + 8))
        #     fenetre.blit(btnA, (pos_btnA[0], pos_btnA[1]))
        

        pygame.display.flip()

        if countdown > 0 :
            countdown -= 1
        if countdown == 0 :
            if indskin == 20 :
                loose(fenetre, answer, finalguess, finaltries)
                return
            elif not "_" in oùilenest :
                win(fenetre, answer, finalguess, finaltries)
                return

        for event in pygame.event.get():
            if event.type == QUIT:
                cont=False
                pygame.display.quit()

            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :
                    #cont = False
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
                if lettre[i].justguessed and not ended :
                    lettre[i].justguessed = False
                    justesse, pénalité, oùilenest, essayés = game.deviner(answer, oùilenest, essayés, i.lower())
                    if pénalité :
                        if indskin < len(skin) - 2 :
                            indskin+= 1
                            nbessai += 1
                        else :
                            indskin+= 1
                            nbessai += 1
                            countdown = 250      # attends un peu avant les résultats
                            finalguess = oùilenest
                            finaltries = nbessai
                            ended = True
                    elif not "_" in oùilenest:
                        countdown = 250     # attends un peu avant les résultats
                        finalguess = oùilenest
                        finaltries = nbessai
                        ended = True
                    if not justesse :
                        pass
                    
                    for i in range(1, len(answer)+1) :
                        devining[i].write(oùilenest[i-1])






def loose(fenetre, answer, oùilenest, nbessai) :
    #print("loss")
    cont = True
    global script_path

    scorr = score.scorr(oùilenest, nbessai)
    #print(scorr)
    scorr =str(scorr)[::-1]
    #print(scorr)
    uscore ={}
    for j in range(3) :
        try :
            uscore[j+1] = score.score(j+1, scorr[j])
        except :
            uscore[j+1] = score.score(j+1, "")

    pos_fenetre = fenetre.get_rect()
    fond = pygame.image.load(str(script_path.parent)+"/fond d'écran menu.jpg").convert()
    fond = pygame.transform.scale(fond, pos_fenetre.size)
    points = pygame.image.load(str(script_path.parent)+"/boutons menu/Bouton Points.png").convert()
    pos_points = points.get_rect()
    points = pygame.transform.scale(points, pos_points.size)

    pygame.display.flip()

    while cont:

        fenetre.blit(fond, (0, 0))
        fenetre.blit(points, (pos_fenetre.size[0]/2 - pos_points.size[0]/2, 50))
        for i in range(3) :
            fenetre.blit(uscore[i+1].img, uscore[i+1].wanted_pos)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                cont=False
                pygame.display.quit()
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :
                    cont=False
                    return   
    

def win(fenetre, answer, oùilenest, nbessai) :
    #print("win")
    cont = True
    global script_path

    scorr = score.scorr(oùilenest, nbessai)
    #print(scorr)
    scorr =str(scorr)[::-1]
    #print(scorr)
    uscore ={}
    for j in range(3) :
        try :
            uscore[j+1] = score.score(j+1, scorr[j])
        except :
            uscore[j+1] = score.score(j+1, "")

    pos_fenetre = fenetre.get_rect()
    fond = pygame.image.load(str(script_path.parent)+"/fond d'écran menu.jpg").convert()
    fond = pygame.transform.scale(fond, pos_fenetre.size)
    points = pygame.image.load(str(script_path.parent)+"/boutons menu/Bouton Points.png").convert()
    pos_points = points.get_rect()
    points = pygame.transform.scale(points, pos_points.size)

    pygame.display.flip()

    while cont:

        fenetre.blit(fond, (0, 0))
        fenetre.blit(points, (pos_fenetre.size[0]//2 - pos_points.size[0]//2, 50))    
        for i in range(3) :
            fenetre.blit(uscore[i+1].img, uscore[i+1].wanted_pos)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                cont=False
                pygame.display.quit()
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :
                    cont=False
                    return   



def settings(fenetre) :
    cont = True
    global script_path
    global hard
    global nb_essais
    #fenetre = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pos_fenetre = fenetre.get_rect()
    fond = pygame.image.load(str(script_path.parent)+"/fond d'écran menu.jpg").convert()
    fond = pygame.transform.scale(fond, pos_fenetre.size)

    noteasy = pygame.image.load(str(script_path.parent)+"/boutons settings/Bouton Difficile.png").convert()
    noteasy = pygame.transform.scale(noteasy, (135*5, 29*5))

    easy = pygame.image.load(str(script_path.parent)+"/boutons settings/Bouton Facile.png").convert()
    easy = pygame.transform.scale(easy, (135*5, 29*5))

    pos_noteasy = noteasy.get_rect()
    pos_noteasy[0], pos_noteasy[1] = pos_fenetre.size[0]/2 - pos_noteasy[2]/2, pos_fenetre.size[1]/2 - pos_noteasy[3]/2 - 200

    pos_diff = pos_fenetre.size[0]/2 - pos_noteasy[2]/2, pos_fenetre.size[1]/2 - pos_noteasy[3]/2 - 200, pos_noteasy[2], pos_noteasy[3]

    lbtn = pygame.image.load(str(script_path.parent)+"/boutons settings/Bouton Gauche.png").convert()
    lbtn = pygame.transform.scale(lbtn, (31*5, 29*5))
    pos_lbtn = pos_diff[0] - 50 - 31*5, pos_diff[1], 31*5, 29*5

    rbtn = pygame.image.load(str(script_path.parent)+"/boutons settings/Bouton Droite.png").convert()
    rbtn = pygame.transform.scale(rbtn, (31*5, 29*5))
    pos_rbtn = pos_diff[0] + pos_diff[2] + 50, pos_diff[1], 31*5, 29*5

    essaisbtn = pygame.image.load(str(script_path.parent)+"/boutons settings/Bouton Essais.png").convert()
    essaisbtn = pygame.transform.scale(rbtn, (116*5, 26*5))
    
    nbessais = {}
    for i in ["05", "10", "15", "20"] :
        nbessais[i] = boutonssettings.essaisnb(i)

    if hard :
        difficulté = noteasy
    else :
        difficulté = easy



    fenetre.blit(fond, (0, 0))
    fenetre.blit(difficulté, (pos_diff))
    fenetre.blit(lbtn, (pos_lbtn[0], pos_lbtn[1]))
    fenetre.blit(rbtn, (pos_rbtn[0], pos_rbtn[1]))

    pygame.display.flip()

    while cont:    
            
        fenetre.blit(fond, (0, 0))
        fenetre.blit(difficulté, (pos_diff))
        fenetre.blit(lbtn, (pos_lbtn[0], pos_lbtn[1]))
        fenetre.blit(rbtn, (pos_rbtn[0], pos_rbtn[1]))
        for i in nbessais.keys() :
             fenetre.blit(nbessais[i].img1, nbessais[i].wanted_pos[0])
             fenetre.blit(nbessais[i].img2, nbessais[i].wanted_pos[1])

        pygame.display.flip()
        

        for event in pygame.event.get():
            if event.type == QUIT:
                cont=False
                pygame.display.quit()
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :
                    cont=False
                    return   
            
            if event.type == MOUSEBUTTONDOWN :
                if pygame.mouse.get_pressed()[0] :
                    pos = pygame.mouse.get_pos()
                    if pos_lbtn[0] <= pos[0] <= pos_lbtn[0] + pos_lbtn[2] and pos_lbtn[1] <= pos[1] <= pos_lbtn[1] + pos_lbtn[3] :
                        hard = False
                        difficulté = easy
                    elif pos_rbtn[0] <= pos[0] <= pos_rbtn[0] + pos_rbtn[2] and pos_rbtn[1] <= pos[1] <= pos_rbtn[1] + pos_rbtn[3] :
                        hard = True
                        difficulté = noteasy


def compétition(fenetre) :
    cont = True
    global script_path
    #fenetre = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pos_fenetre = fenetre.get_rect()
    fond = pygame.image.load(str(script_path.parent)+"/fond d'écran menu.jpg").convert()
    fond = pygame.transform.scale(fond, pos_fenetre.size)

    fenetre.blit(fond, (0, 0))

    pygame.display.flip()

    while cont:    
        
        fenetre.blit(fond, (0, 0))
        pygame.display.flip()
        

        for event in pygame.event.get():
            if event.type == QUIT:
                cont=False
                pygame.display.quit()
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :
                    cont=False
                    return   
            

def leaderboard(fenetre) :
    cont = True
    global script_path
    #fenetre = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pos_fenetre = fenetre.get_rect()
    fond = pygame.image.load(str(script_path.parent)+"/fond d'écran menu.jpg").convert()
    fond = pygame.transform.scale(fond, pos_fenetre.size)

    fenetre.blit(fond, (0, 0))

    pygame.display.flip()

    while cont:    
        
        fenetre.blit(fond, (0, 0))
        pygame.display.flip()
        

        for event in pygame.event.get():
            if event.type == QUIT:
                cont=False
                pygame.display.quit()
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :
                    cont=False
                    return  



menu()








 










