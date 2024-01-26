import math as m
import random as aleajactaest
import time as t

#Cela nous permet de voir si le code fonctionne
#réponses = ["cool", "paradisiaque", "détergent", "ratatouille", "caribou", "notamment", "ridicule", "pastèque", "illustré", "justification"]
lettres = set("qwertzuiopasdfghjklyxcvbnméèêëàäâîìïôöòûüùÿ")
nb_chances = 10
hard = False
nb_mots = 1
dico = open("dossier top secret/liste.de.mots.francais.frgut.txt", "r")
réponses = dico.readlines()
dico.close()


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


def diffletters(x : (str or list)) :
    '''
    Compter le nombre de lettre différent
    '''
    y = []
    for i in x :
        if i in lettres and i not in y :
            y.append(i)
    return len(y)






def setup() :
    '''
    Choisis la difficulté
    '''
    global hard
    global nb_chances
    global nb_mots
    if input("Mode difficile ?").lower in {"oui","yes", "ouais", "avec plaisir", "je vous en saurais fort gré"} :
        hard = True
    else :
        hard = False        #valeur par défaut
    try :
        nb_chances = int(input("Nombre d'erreurs maximum ?"))
    except :
        nb_chances = 10     #valeur par défaut
    try :
        nb_mots = int(input("Nombre de mots à deviner ?"))
    except :
        nb_mots = 1           #valeur par défaut






def pendu(x : list) :

    #choisis un mot aléatoire à faire deviner
    #answer = ltostr(aleajactaest.sample(x, nb_mots))
    answer = ltostr(aleajactaest.sample(réponses, nb_mots))
    answer = answer.strip()
    
    #ajoute le nombre de "_" correspondant au nombre de lettre du mot
    motvide = "_ "*(len(answer)-1) + "_"
    oùilenest = ["_"]*len(answer)
    
    #print(answer)
    nb_essai = 1
    essayés = []
    
    #Petite intro
    print("Bonjour !")
    t.sleep(0.5)
    print("Bonne chance !")
    t.sleep(0.5)
    print("Le mot est", motvide)
    t.sleep(0.5)

    #Boucle qui vérifie que le nombre d'essai effectué par le joueur ne dépasse pas le nombre d'essai maximu autorisé par de niveau de difficulté
    while "_" in oùilenest and nb_essai <= nb_chances :
        essai = input("Une lettre ?").lower()
        t.sleep(0.5)
        print(".")
        t.sleep(0.5)
        print(". .")
        t.sleep(0.5)
        print(". . .")
        t.sleep(0.5)
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
        p("Vous n'avez trouvé que " + ltostr(oùilenest) + ", soit " + str(diffletters(oùilenest)) + " lettres différentes sur " + str(diffletters(answer)) + "!")
        input()
        print("Le mot était...")
        input()
        p(str(answer) + "!")
    else :
        print("Le mot était bien " +  str(answer) + "\nBravo !!!")
    
    

#setup()
pendu(réponses)



