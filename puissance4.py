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

def jouerTour(matrix, joueur):
    error = True
    if(joueur == 1):    
        print("Joueur 1, dans quelle case voulez-vous mettre votre jeton ?")
        while(error == True):
            error = False
            colonne = int(input("Veuillez entrer le numéro de colonne\n"))
            colonne -= 1
            ligne = trouverLigne(matrix, colonne)
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
                affichage(matrix)
                if(victoire(matrix, colonne, ligne) == True or testMatrixPleine(matrix) == False):
                    conditionFinPartie = True
                    print("GGGGGGGGGGGGGGGGGGGGG")
    else:
        while(conditionFinPartie == False):
            print("")
            #implémenter joueur vs IA
    conditionRejouer = rejouer()
    if(conditionRejouer == True):
        matrix = viderMatrix()
        conditionFinPartie = False