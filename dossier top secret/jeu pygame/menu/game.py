import pygame
from pygame.locals import *
pygame.init()

import os
import sys

from pathlib import Path
path = Path(__file__).resolve()
# print(path)
# print(sys.path)
sys.path.append(str(path.parent.parent.parent))
# print(sys.path)
import superprojettrokouldefouavecGuillaume






import lettres

import math as m
import random as aleajactaest
import time as t
import leaderboard
#Cela nous permet de voir si le code fonctionne
#réponses = ["cool", "paradisiaque", "détergent", "ratatouille", "caribou", "notamment", "ridicule", "pastèque", "illustré", "justification"]
alphabet = set("qwertzuiopasdfghjklyxcvbnméèêëàäâîìïôöòûüùÿç-")
nb_chances = 10
hard = False


f = open(str(path.parent.parent.parent)+"/listemotscourants.txt")
réponses = f.readlines()





def ltostr(x : list) :
    '''
    convertit une liste en string
    '''
    z = ""
    for i in x :
        z += str(i)
    return z




def entertospace(x : str) :
    y = list(x)
    for i, j in enumerate(y) :
        if j == "\n" :
            y[i] = " "
    return ltostr(y)





# def setup() :
#     '''
#     Choisis la difficulté
#     '''
#     if input("Mode difficile ?").lower in {"oui","yes", "ouais", "avec plaisir", "je vous en saurais fort gré"} :
#         hard = True
#     else :
#         hard = False        #valeur par défaut
#     try :
#         nb_chances = int(input("Nombre d'erreurs maximum ?"))
#     except :
#         nb_chances = 10     #valeur par défaut
#     try :
#         nb_mots = int(input("Nombre de mots à deviner ?"))
#     except :
#         nb_mots = 1           #valeur par défaut







def init(réponses) :
            #choisis un mot aléatoire à faire deviner
    #answer = ltostr(aleajactaest.sample(x, nb_mots))
    answer = ltostr(aleajactaest.sample(réponses, 1))
    answer = answer.strip()
    answer = entertospace(answer)
    
    #ajoute le nombre de "_" correspondant au nombre de lettre du mot
    oùilenest = ["_"]*len(answer)
    for i, j in enumerate(oùilenest) :
        if answer[i] == " " :
            oùilenest[i] = " "


    return answer, oùilenest



def deviner(réponse, oùilenest,  essayés, guess) :

    #Commande qui ne pénalise pas le fait qu'un joueur réessaie une lettre (au cas où ça arrive on la laisse)
    if guess in essayés :
        return False, False, oùilenest, essayés
    else :
        essayés.append(guess)
        if guess in réponse :
            for pos, letter in enumerate(réponse) :
                if guess == letter :
                    oùilenest[pos] = guess
            return True, False, oùilenest, essayés
        else :
            return False, True, oùilenest, essayés






# print(init(["testabab"]))

# print(deviner('testabab', ['_', '_', '_', '_', '_', '_', '_', '_'], [], "a"))
















