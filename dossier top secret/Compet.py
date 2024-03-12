import math as m
import random as aleajactaest
import time as t
import leaderboard
from pathlib import Path
#Cela nous permet de voir si le code fonctionne
#réponses = ["cool", "paradisiaque", "détergent", "ratatouille", "caribou", "notamment", "ridicule", "pastèque", "illustré", "justification"]
lettres = set("qwertzuiopasdfghjklyxcvbnméèêëàäâîìïôöòûüùÿç-")
nb_chances = 10
hard = False
nb_mots = 1




# Obtenir le chemin complet vers le script courant
script_path = Path(__file__).resolve()

#récupérer le chemin vers le dossier parent du script courant
script_dir = script_path.parent

#On ajoute le nom de notre fichier
path = str(script_dir)+ "/listemotscourants.txt"

#on ouvre le fichier file.txt
f = open(path)

réponses = f.readlines()


def ltostr(x : list) :
    '''
    convertit une liste en string
    '''
    z = ""
    for i in x :
        z += str(i)
    return z

#raccourci
def p(x) :
    print(x)
def p05(x) :
    print(x)
    t.sleep(0.5)
def p1(x) :
    print(x)
    t.sleep(1)


def lendiffletters(x : (str or list)) :
    '''
    Compter le nombre de lettre différent
    '''
    y = []
    for i in x :
        if i in lettres and i not in y :
            y.append(i)
    return len(y)


def entertospace(x : str) :
    y = list(x)
    for i, j in enumerate(y) :
        if j == "\n" :
            y[i] = " "
    return ltostr(y)
            



def setup() :
    '''
    Choisis la difficulté
    '''
    global nb_chances
    global nb_mots
    nb_chances =8
    nb_mots = 1


    
def intro () :
    print("Bonjour !")
    t.sleep(0.5)
    print("Bonne chance !")
    t.sleep(0.5)   

    







def pendu(réponse_dans_la_fonction) :

    global nb_essai
    global oùilenest

    #choisis un mot aléatoire à faire deviner
    #answer = ltostr(aleajactaest.sample(x, nb_mots))
    answer =("test")
    #answer = ltostr(aleajactaest.sample(réponse_dans_la_fonction, nb_mots))
    answer = answer.strip()
    answer = entertospace(answer)
    
    #ajoute le nombre de "_" correspondant au nombre de lettre du mot
    motvide = "_ "*(len(answer)-1) + "_"
    oùilenest = ["_"]*len(answer)
    
    #print(answer)
    nb_essai = 1
    essayés = []
    
    

    #Petite intro
  
    print("Le mot est", motvide)
    t.sleep(0.5)

    #Boucle qui vérifie que le nombre d'essai effectué par le joueur ne dépasse pas le nombre d'essai maximu autorisé par de niveau de difficulté
    while "_" in oùilenest and nb_essai <= nb_chances :
        essai = input("Une lettre ?").lower()
       # t.sleep(0.5)
        #print(".")
        #t.sleep(0.5)
        #print(". .")
        #t.sleep(0.5)
       # print(". . .")
    
        #t.sleep(0.5)
        if essai == answer :
            for numlettre, lettre in enumerate(answer) :
                oùilenest[numlettre] = lettre
        elif essai not in lettres :
            print("Ceci n'est pas une lettre.")
            t.sleep(1)
            if hard :
                nb_essai += 1
        
        #Commande qui ne pénalise pas le fait qu'un joueur réessaie une lettre
        elif essai in essayés :
            print("Déjà mise !")
            t.sleep(1)
            if hard :
                nb_essai += 1
        else :
            essayés.append(essai)
            if essai in answer :
                for pos, letter in enumerate(answer) :
                    if essai == letter :
                        oùilenest[pos] = essai
                print("Good Guess !")
                t.sleep(0.55)
                if "_" in oùilenest :
                    print("Le mot est", ltostr(oùilenest))
                t.sleep(1)
            else :
                print("Raté...")
                t.sleep(0.55)
                if "_" in oùilenest :
                    print("Le mot est", ltostr(oùilenest))
                    t.sleep(1)
                nb_essai += 1
        
    if nb_essai > nb_chances :
        print("Dommage !")
        input()
        p("Vous n'avez trouvé que " + ltostr(oùilenest) + ", soit " + str(lendiffletters(oùilenest)) + " lettres différentes sur " + str(lendiffletters(answer)) + "!")
        input()
        print("Le mot était...")
        input()
        p(str(answer) + "!")
    else :
        print("Le mot était bien " +  str(answer) + "\nBravo !!!")
    
    
    
    
    
    
    
def competition () :
    
    
    global compet
    global réponses
    global v
    compet = True
    v=0  
    if compet == True :  
         for i in range(10) :
            pendu(réponses)
            x = leaderboard.score(ltostr(oùilenest), nb_essai)
            print(leaderboard.score(ltostr(oùilenest), nb_essai))
            v = v+x
            print(v)


            
    else :
        pendu(réponses)
    return v
    
 
setup()
intro()
leaderboard.highscore(leaderboard.pseudo(),competition())
    



#print(entertospace("abc\nefg"))




