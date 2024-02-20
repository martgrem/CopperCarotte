from pathlib import Path
#Ici nous faisons un système de point qui récompense plus le faite de trouver un long mot avec des lettres peu commune, 
#plutôt qu'un mot court qui est composé de lettres très présente.
scrabble = [" ", "aeilnorstu", "dgmé", "bccpè", "fhv","","àê-","âîôû","jq", "", "kwxyzç", "", "", "", "", "ïöüÿùòä"]
lettres = set("qwertzuiopasdfghjklyxcvbnméèêëàäâîìïôöòûüùÿç-")





def diffletters(x : (str or list)) :
    '''
    Compter le nombre de lettre différent
    '''
    y = []
    for i in x :
        if i in lettres and i not in y :
            y.append(i)
    return y



def pseudo() :
    pseudo = input("Choisissez un pseudonyme à utiliser lors de vos aventures dans le monde fascinant de l'éxecution publique.")
    return pseudo
    

def score(mot, nbessais) :   
    '''
    Cette fonction fait gagner 2x plus de points, si le joueur a découvert le mot en entier
    '''
    score = 0
    x = diffletters(mot)
    for i in x :
        for indj, j in enumerate(scrabble) :
            if i in j :
                score += indj
                break
    score -= (nbessais-1)
    if "_" not in mot :
        score *= 2
    return score


def highscore(pseudo, score) :
    '''
    Ce code remplace les noms des anciens 3 meilleurs joueurs, qui ont fait moins de points que le joueur qui vient de jouer
    '''
    # Obtenir le chemin complet vers le script courant
    script_path = Path(__file__).resolve()

    #récupérer le chemin vers le dossier parent du script courant
    script_dir = script_path.parent

    #On ajoute le nom de notre fichier
    path = str(script_dir)+ "/leaderboard.txt"

    #on ouvre le fichier file.txt
    f = open(path, "r")
    
    lines = f.readlines()
    nom3, best3score = lines[2].split(",")
    best3score = int(best3score)
    if score > best3score :
        f.close()
        f = open(path, "w")
        nom1, best1score = lines[0].split(",")
        nom2, best2score = lines[1].split(",")
        best1score = int(best1score)
        best2score = int(best2score)
        if best1score < score :
            f.write(str(pseudo) + ", " + str(score) + "\n" + str(nom1) + ", " + str(best1score) + "\n" + str(nom2) + ", " + str(best2score))
        elif best2score < score :
            f.write(str(nom1) + ", " + str(best1score) + "\n" + str(pseudo) + ", " + str(score) + "\n"  + str(nom2) + ", " + str(best2score))
        else :
            f.write(str(nom1) + ", " + str(best1score) + "\n" + str(nom2) + ", " + str(best2score) + "\n" + str(pseudo) + ", " + str(score))
    f.close()
            
