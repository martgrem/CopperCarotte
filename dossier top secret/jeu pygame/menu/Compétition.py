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
    for j, i in enumerate(skinpendu.skinchoice(10)) :
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
            return score.scorr(oùilenest, nbessai)

        for event in pygame.event.get():
            if event.type == QUIT:
                cont=False
                pygame.display.quit()

            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :
                    #cont = False
                    return "closed"

 
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



def win(fenetre, scorr) :
    #print("win")
    cont = True
    global script_path

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



def tronul(fenetre) :
    cont = True

    pos_fenetre = fenetre.get_rect()
    fond = pygame.image.load(str(script_path.parent)+"/fond d'écran menu.jpg").convert()
    fond = pygame.transform.scale(fond, pos_fenetre.size)
    tronul = pygame.image.load(str(script_path.parent)+"/boutons menu/Bouton erreur.png").convert()
    tronul = pygame.transform.scale(tronul, (926, 367))
    pos_tronul = tronul.get_rect()

    pygame.display.flip()

    while cont:

        fenetre.blit(fond, (0, 0))
        fenetre.blit(tronul, (pos_fenetre.size[0]/2 - pos_tronul.size[0]/2, pos_fenetre.size[1]/2 - pos_tronul.size[1]/2))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                cont=False
                pygame.display.quit()
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :
                    cont=False
                    return   


def pseudo(fenetre) :
    cont = True
    global script_path
    cd = 0
    endcd = -1
    name = ""

    lettre = {}
    for j, i in enumerate(aleajactaest.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZéèêëàäâîìïôöòûüùÿç-", len("ABCDEFGHIJKLMNOPQRSTUVWXYZéèêëàäâîìïôöòûüùÿç-"))) :
        lettre[i] = lettres.letters(i, j)

    nom = {}
    for i in range(3) :
        nom[i+1] = devinage.deviningletters(i+1)

    pos_fenetre = fenetre.get_rect()
    fond = pygame.image.load(str(script_path.parent)+"/fond d'écran menu.jpg").convert()
    fond = pygame.transform.scale(fond, pos_fenetre.size)
    demande = pygame.image.load(str(script_path.parent)+"/boutons menu/Bouton Pseudo.png").convert()
    demande = pygame.transform.scale(demande, (80*5, 17*5))

    fenetre.blit(fond, (0, 0))

    pygame.display.flip()

    while cont:    
        for j, i in enumerate(name) :
            nom[j+1].write(i)

        if cd != 0 :
            cd -= 1
        fenetre.blit(fond, (0, 0))
        fenetre.blit(demande, (1400, 350))

        for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZéèêëàäâîìïôöòûüùÿç-" :
            fenetre.blit(lettre[i].img, lettre[i].wanted_pos)

        for i in nom.keys() :
            fenetre.blit(nom[i].img, (nom[i].wanted_pos[0] - 15, nom[i].wanted_pos[1] - 300))

        pygame.display.flip()
        
        if len(name) == 3 :
            if cd == 0 :
                return name
            elif cd > 0 :
                cd -= 1
            else :
                cd = 300

        for event in pygame.event.get():
            if event.type == QUIT:
                cont=False
                pygame.display.quit()
            if event.type == KEYDOWN :
                # if event.key == K_ESCAPE :
                #     cont=False
                #     return
                
                if cd == 0 :
                    if event.key == K_a :
                        name += "A"
                        cd = 100
                    elif event.key == K_b :
                        name += "B"
                        cd = 100
                    elif event.key == K_c :
                        name += "C"
                        cd = 100
                    elif event.key == K_d :
                        name += "D"
                        cd = 100
                    elif event.key == K_e :
                        name += "E"
                        cd = 100
                    elif event.key == K_f :
                        name += "F"
                        cd = 100
                    elif event.key == K_g :
                        name += "G"
                        cd = 100
                    elif event.key == K_h :
                        name += "H"
                        cd = 100
                    elif event.key == K_i :
                        name += "I"
                        cd = 100
                    elif event.key == K_j :
                        name += "J"
                        cd = 100
                    elif event.key == K_k :
                        name += "K"
                        cd = 100
                    elif event.key == K_l :
                        name += "L"
                        cd = 100
                    elif event.key == K_m :
                        name += "M"
                        cd = 100
                    elif event.key == K_n :
                        name += "N"
                        cd = 100
                    elif event.key == K_o :
                        name += "O"
                        cd = 100
                    elif event.key == K_p :
                        name += "P"
                        cd = 100
                    elif event.key == K_q :
                        name += "Q"
                        cd = 100
                    elif event.key == K_r :
                        name += "X"
                        cd = 100
                    elif event.key == K_s :
                        name += "R"
                        cd = 100
                    elif event.key == K_t :
                        name += "S"
                        cd = 100
                    elif event.key == K_u :
                        name += "T"
                        cd = 100
                    elif event.key == K_v :
                        name += "U"
                        cd = 100
                    elif event.key == K_w :
                        name += "V"
                        cd = 100
                    elif event.key == K_x :
                        name += "W"
                        cd = 100
                    elif event.key == K_y :
                        name += "Y"
                        cd = 100
                    elif event.key == K_z :
                        name += "Z"
                        cd = 100


            if event.type == MOUSEBUTTONDOWN and cd == 0:
                if pygame.mouse.get_pressed()[0] :
                    mspos = pygame.mouse.get_pos()


                    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZéèêëàäâîìïôöòûüùÿç-" :
                        if lettre[i].wanted_pos[0] <= mspos[0] <= lettre[i].wanted_pos[0] + lettre[i].ln and lettre[i].wanted_pos[1] <= mspos[1] <= lettre[i].wanted_pos[1] + lettre[i].ln :
                            name += str(i)
                            cd = 100


def compétition(fenetre) :
    scorr = 0
    for _ in range(1) :
         c = jeu(fenetre)
         if c == "closed" :
             return
         scorr += c
    if scorr < -99 :
        tronul(fenetre)
        return
    else :
        win(fenetre, scorr)
        f = open(str(script_path.parent.parent.parent) + "/leaderboard.txt", "r")
        lines = f.readlines()
        f.close()
        a, b = lines[2].split(", ")
        if a == "None" or int(b.strip()) < scorr :
            name = pseudo(fenetre)
            f = open(str(script_path.parent.parent.parent) + "/leaderboard.txt", "w")
            a, b = lines[0].split(", ")
            if a == "None" or int(b.strip()) < scorr :
                f.write(str(name) + ", " + str(scorr) + "\n" + lines[0] + lines[1].strip())
            else :
                a, b = lines[1].split(", ")
                if a == "None" or int(b.strip()) < scorr :
                    f.write(lines[0] + str(name) + ", " + str(scorr) + "\n" + lines[1].strip())
                else :
                    f.write(lines[0] + lines[1] + str(name) + ", " + str(scorr))
            f.close()
            return




    
        
     
def fenetrevide(fenetre) :
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


#compétition()

