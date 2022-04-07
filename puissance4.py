import random

matrix=[[0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0]]

#           0  1  2  3  4  5  6
#    5    [[0, 0, 0, 0, 0, 0, 0], 
#    4    [0, 0, 0, 0, 0, 0, 0], 
#    3    [0, 0, 0, 0, 0, 0, 0], 
#    2    [0, 0, 0, 0, 0, 0, 0], 
#    1    [0, 0, 0, 0, 0, 0, 0], 
#    0    [0, 0, 0, 0, 0, 0, 0]]

#               EN JEU
#           1  2  3  4  5  6  7
#    6    [[0, 0, 0, 0, 0, 0, 0], 
#    5    [0, 0, 0, 0, 0, 0, 0], 
#    4    [0, 0, 0, 0, 0, 0, 0], 
#    3    [0, 0, 0, 0, 0, 0, 0], 
#    2    [0, 0, 0, 0, 0, 0, 0], 
#    1    [0, 0, 0, 0, 0, 0, 0]]
ligne = 0
colonne = 0
dernierTour = [[],[]]
conditionFinPartie = False
conditionRejouer = True
print("Salut à tous")

def affichage(matrix):
    for i in range(6):
        print("[", end='')
        for j in range(7):
            print(matrix[5 - i][j], end=' ')
        print("]")

def victoire(matrix, colonne, ligne):
    compteurJ1 = 0
    compteurJ2 = 0
    i = 0
    tmpLigne = 0
    tmpColonne = 0
    while(tmpLigne < 6):
        while(tmpColonne < 7):
            if(matrix[tmpLigne][tmpColonne] == 1):
                compteurJ1 += 1
            else:
                compteurJ1 = 0
            if(matrix[tmpLigne][tmpColonne] == 2):
                compteurJ2 += 1
            else:
                compteurJ2 = 0
            if(compteurJ1 >= 4 or compteurJ2 >= 4):
                return(True)
            tmpColonne += 1
        tmpLigne += 1
        tmpColonne = 0
    tmpLigne = 0
    tmpColonne = 0
    while(tmpLigne < 6):
        if(matrix[tmpLigne][colonne] == 1):
            compteurJ1 += 1
        else:
            compteurJ1 = 0
        if(matrix[tmpLigne][colonne] == 2):
            compteurJ2 += 1
        else:
            compteurJ2 = 0
        if(compteurJ1 >= 4 or compteurJ2 >= 4):
            return(True)
        tmpLigne += 1
    tmpLigne = ligne
    tmpColonne = colonne
    while(tmpLigne > 0 and tmpColonne > 0):
        tmpLigne -= 1
        tmpColonne -= 1
    while(tmpLigne < 6 and tmpColonne < 7):
        if(matrix[tmpLigne][tmpColonne] == 1):
            compteurJ1 += 1
        else:
            compteurJ1 = 0
        if(matrix[tmpLigne][tmpColonne] == 2):
            compteurJ2 += 1
        else:
            compteurJ2 = 0
        if(compteurJ1 >= 4 or compteurJ2 >= 4):
            return(True)
        tmpLigne += 1
        tmpColonne += 1
    tmpLigne = ligne
    tmpColonne = colonne
    while(tmpLigne > 0 and tmpColonne < 6):
        tmpLigne -= 1
        tmpColonne += 1
    while(tmpLigne < 6 and tmpColonne >= 0):
        if(matrix[tmpLigne][tmpColonne] == 1):
            compteurJ1 += 1
        else:
            compteurJ1 = 0
        if(matrix[tmpLigne][tmpColonne] == 2):
            compteurJ2 += 1
        else:
            compteurJ2 = 0
        if(compteurJ1 >= 4 or compteurJ2 >= 4):
            return(True)
        tmpLigne += 1
        tmpColonne -= 1

def trouverLigne(matrix, colonne):
    ligne = 0
    while(matrix[ligne][colonne] != 0):
        ligne += 1
    return(ligne)

def colonneVide(matrix):
    colVide = []
    tmp = 0
    for i in range (7):
        for j in range (6):
            if(matrix[j][i] == 0 and tmp == 0):
                colVide.append(i)
                tmp = 1
        tmp = 0
    return(colVide)

def finDePartie(matrix, dernierTour):
    return victoire(matrix,dernierTour[0][1],dernierTour[0][0]) or victoire(matrix,dernierTour[1][1],dernierTour[1][0]) or testMatrixPleine(matrix)

def scoreDernierTour(matrix, dernierTour, joueur):
    score = 0
    jetons = 0
    jetonsAdv = 0
    if(joueur == 1):
        jetons = 1
        jetonsAdv = 2
    else:
        jetons = 2
        jetonsAdv = 1
    
    if(victoire(matrix, dernierTour[0][1], dernierTour[0][0])):
    



def minmax(matrix, profondeur, maximinzingPlayer, dernierTour):
    colVide = colonneVide(matrix)
    if profondeur == 0 or finDePartie(matrix, colonne,ligne):
        if finDePartie(matrix, dernierTour):
            if victoire(matrix,dernierTour[0][1],dernierTour[0][0]):
                return -100000000000
            if victoire(matrix,dernierTour[1][1],dernierTour[1][0]):
                return -100000000000
            else:
                return 0
        else :
            return 

def jouerTour(matrix, joueur):
    error = True
    if(joueur == 1):    
        print("Joueur 1, dans quelle case voulez-vous mettre votre jeton ?")
        while(error == True):
            error = False
            colonne = int(input("Veuillez entrer le numéro de colonne\n"))
            colonne -= 1
            ligne = trouverLigne(matrix, colonne)
            dernierTour[0] = [ligne,colonne]
            if(matrix[ligne][colonne] == 1 or matrix[ligne][colonne] == 2):
                error = True
                print("Il y a déjà un jeton dans cette case, veuillez rejouer votre tour")
        matrix[ligne][colonne] = 1
    else:
        print("Joueur 2, dans quelle case voulez-vous mettre votre jeton ?")
        while(error == True):
            error = False
            colonne = int(input("Veuillez entrer le numéro de colonne\n"))
            colonne -= 1
            ligne = trouverLigne(matrix, colonne)
            dernierTour[1] = [ligne,colonne]
            if(matrix[ligne][colonne] == 1 or matrix[ligne][colonne] == 2):
                error = True
                print("Il y a déjà un jeton dans cette case, veuillez rejouer votre tour")
        matrix[ligne][colonne] = 2

def choixModeDeJeu():
    print("Explication des règles")
    print("Choisir un mode de jeu parmis :")
    print("- Joueur contre Joueur (tapez 0)")
    print("- Joueur contre IA (tapez 1)")
    mode = int(input(""))
    while(mode != 0 and mode != 1):
        if(mode == 0):
            print("Vous avez choisi le mode Joueur contre Joueur")
        elif(mode == 1):
            print("Vous avez choisi le mode Joueur contre IA")
        else:
            print("Veuillez choisir entre les 2 modes de jeux disponibles")
    return(mode)

def rejouer():
    rejouer = 9
    while(rejouer != 0 and rejouer != 1):
        rejouer = int(input("Voulez-vous relancer une partie ? 1 si oui, 0 sinon\n"))
    if(rejouer == 1):
        return(True)
    else:
        return(False)

def testMatrixPleine(matrix):
    tmpLigne = 0
    caseVide = False
    while(tmpLigne < 6):
        tmpColonne = 0
        while(tmpColonne < 7):
            if(matrix[tmpLigne][tmpColonne] == 0):
                caseVide = True
            tmpColonne += 1
        tmpLigne += 1
    if(caseVide == False):
        print("Il n'y a plus de cases disponibles")
    return(caseVide)

def viderMatrix():
    matrix = [[0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0]]
    return(matrix)

def tourIAFacile(matrix):
    tmpColonne = random.randint(0, 6)
    tmpLigne = trouverLigne(matrix, tmpColonne)
    error = True
    while(error == True):
        error = False
        if(matrix[tmpLigne][tmpColonne] == 1 or matrix[tmpLigne][tmpColonne] == 2):
            error = True
            print(error)
    matrix[tmpLigne][tmpColonne] = 2

while(conditionRejouer == True): #ou que la grille soit pleine
    mode = choixModeDeJeu()
    if(mode == 0):
        while(conditionFinPartie == False):
            jouerTour(matrix, 1)
            affichage(matrix)
            if(victoire(matrix, colonne, ligne) == True or testMatrixPleine(matrix) == False):
                conditionFinPartie = True
                print("GGGGGGGGGGGGGGGGG")
            if(conditionFinPartie == False):
                jouerTour(matrix, 2)
                if(victoire(matrix, colonne, ligne) == True or testMatrixPleine(matrix) == False):
                    conditionFinPartie = True
                    print("GGGGGGGGGGGGGGGGGGGGG")
            affichage(matrix)
    else:
        print("Veuillez choisir le niveau de difficulté")
        diff = -1
        while(diff != 0 and diff != 1 and diff != 2):
            diff = int(input("Tapez 0 : Facile, 1 : Moyen, 2 : Difficile"))
        while(conditionFinPartie == False):
            if(diff == 0):
                print("Vous avez choisi la difficulté Facile")
                jouerTour(matrix, 1)
                if(victoire(matrix, colonne, ligne) == True or testMatrixPleine(matrix) == False):
                    conditionFinPartie = True
                    print("GGGGGGGGGGGGGGGGG")
                if(conditionFinPartie == False):
                    tourIAFacile(matrix)
                    print("L'IA a joué")
                    if(victoire(matrix, colonne, ligne) == True or testMatrixPleine(matrix) == False):
                        conditionFinPartie = True
                        print("GGGGGGGGGGGGGGGGGGGGG")
                affichage(matrix)
            elif(diff == 1):
                print("Vous avez choisi la difficulté Moyenne")
            else:
                print("Vous avez choisi la difficulté Difficile")  
    conditionRejouer = rejouer()
    if(conditionRejouer == True):
        matrix = viderMatrix()
        conditionFinPartie = False