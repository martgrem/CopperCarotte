#Ici nous faisons un système de point qui récompense plus le faite de trouver un long mot avec des lettres peu commune, 
#plutôt qu'un mot court qui est composé de lettres très présente.
scrabble = [" ", "aeilnorstu", "dgmé", "bccpè", "fhv","","àê","âîôû","jq", "", "kwxyzç", "", "", "", "", "ïöüÿùòä"]
lettres = set("qwertzuiopasdfghjklyxcvbnméèêëàäâîìïôöòûüùÿç")


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
    return

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
    f = open("leaderboard.txt", "r")
    lines = f.readlines()
    nom3, best3score = lines[3].split(",")
    if score >= best3score :
        f.close()
        f = open("leaderboard.txt", "w")
        nom1, best1score = lines[1].split(",")
        nom2, best2score = lines[2].split(",")
        if best1score < score :
            f.write(str(pseudo) + ", " + str(score) + "\n" + str(nom1) + ", " + str(best1score) + "\n" + str(nom2) + ", " + str(best2score))
        elif best2score < score :
            f.write(str(nom1) + ", " + str(best1score) + "\n" + str(pseudo) + ", " + str(score) + "\n"  + str(nom2) + ", " + str(best2score))
        else :
            f.write(str(nom1) + ", " + str(best1score) + "\n" + str(nom2) + ", " + str(best2score) + "\n" + str(pseudo) + ", " + str(score))
    f.close()
            

