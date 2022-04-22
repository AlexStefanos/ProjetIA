import random, math, copy

#Sommaire
#IA : Ligne 36 -> 160
#Jeu : Ligne 151 -> fin (480)

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
dernierTour = [[0,0],[0,0]]
conditionFinPartie = False
conditionRejouer = True
print("Salut à tous")

def scoreLunette(fenetre, joueur):
    scoreL = 0
    joueur_ad = 1
    if(joueur == 1):
        joueur_ad = 2
    
    if fenetre.count(joueur) == 4:
        scoreL += 100
    elif fenetre.count(joueur) == 3 and fenetre.count(0) == 1:
        scoreL += 5
    elif fenetre.count(joueur) == 2 and fenetre.count(0) == 2:
        scoreL += 2
    if fenetre.count(joueur_ad) == 3 and fenetre.count(0) == 1:
        scoreL -= 4
    return scoreL

def scoreTotal(matrix, joueur):
    score = 0
    colonneMilieu = []

    for ligne in range(6):
        colonneMilieu.append(matrix[ligne][3])   
    compteurMilieu = colonneMilieu.count(joueur)
    score += compteurMilieu * 3
    for liste in matrix:
        for colonne in range(7-3):
            fenetre = [liste[colonne],liste[colonne+1],liste[colonne+2],liste[colonne+3]]
            score += scoreLunette(fenetre, joueur)
    for colonne in range(7):
        for ligne in range(6-3):
            fenetre = [matrix[ligne][colonne],matrix[ligne + 1][colonne],matrix[ligne + 2][colonne],matrix[ligne + 3][colonne]]
            score += scoreLunette(fenetre, joueur)
    for ligne in range(6-3):
        for colonne in range(7-3):
            fenetre = [matrix[ligne][colonne],matrix[ligne + 1][colonne + 1],matrix[ligne + 2][colonne + 2],matrix[ligne + 3][colonne + 3]]
            score += scoreLunette(fenetre, joueur)
    for ligne in range(6-3):
        for colonne in range(7-3):
            fenetre = [matrix[ligne + 3][colonne],matrix[ligne + 3 - 1][colonne + 1],matrix[ligne + 3 - 2][colonne + 2],matrix[ligne + 3 - 3][colonne + 3]]
            score += scoreLunette(fenetre, joueur)
    return score

def minimax(matrix, profondeur, maximizingPlayer, dernierTour):
    if profondeur == 0 or finDePartie(matrix, dernierTour):
        if finDePartie(matrix, dernierTour):
            if victoire(matrix,dernierTour[1][1],dernierTour[1][0]):
                return (None, 100000000000000)
            elif victoire(matrix,dernierTour[0][1],dernierTour[0][0]):
                return (None, -100000000000000)
            else:
                return (None, 0)
        else :
            return (None, scoreTotal(matrix, 2))
    if maximizingPlayer:
        valeur = -math.inf
        colonne = random.choice(colonneDisponible(matrix))
        for col in colonneDisponible(matrix):
            tmpDernierTour = copy.deepcopy(dernierTour)
            tmpDernierTour[1][1] = col
            tmpDernierTour[1][0] = ligneDisponible(matrix, tmpDernierTour[1][1])
            tmpMatrix = copy.deepcopy(matrix)
            jouerTour(tmpMatrix,2, tmpDernierTour[1][0], tmpDernierTour[1][1])
            nouveauScore = minimax(tmpMatrix, profondeur-1,False,tmpDernierTour)[1]
            if nouveauScore > valeur:
                valeur = nouveauScore
                colonne = col
        return colonne, valeur
    else:
        valeur = math.inf
        colonne = random.choice(colonneDisponible(matrix))
        for col in colonneDisponible(matrix):
            tmpDernierTour = copy.deepcopy(dernierTour)
            tmpDernierTour[0][1] = col
            tmpDernierTour[0][0] = ligneDisponible(matrix, tmpDernierTour[0][1])
            tmpMatrix = copy.deepcopy(matrix)
            jouerTour(tmpMatrix,1, tmpDernierTour[0][0], tmpDernierTour[0][1])
            nouveauScore = minimax(tmpMatrix, profondeur-1,True,tmpDernierTour)[1]
            if nouveauScore < valeur:
                valeur = nouveauScore
                colonne = col
        return colonne, valeur

def elagage_alpha_beta(matrix, profondeur, maximizingPlayer, dernierTour, alpha, beta):
    if profondeur == 0 or finDePartie(matrix, dernierTour):
        if finDePartie(matrix, dernierTour):
            if victoire(matrix,dernierTour[1][1],dernierTour[1][0]):
                return (None, 100000000000000)
            elif victoire(matrix,dernierTour[0][1],dernierTour[0][0]):
                return (None, -100000000000000)
            else:
                return (None, 0)
        else :
            return (None, scoreTotal(matrix, 2))
    if maximizingPlayer:
        valeur = -math.inf
        colonne = random.choice(colonneDisponible(matrix))
        for col in colonneDisponible(matrix):
            tmpDernierTour = copy.deepcopy(dernierTour)
            tmpDernierTour[1][1] = col
            tmpDernierTour[1][0] = ligneDisponible(matrix, tmpDernierTour[1][1])
            tmpMatrix = copy.deepcopy(matrix)
            jouerTour(tmpMatrix,2, tmpDernierTour[1][0], tmpDernierTour[1][1])
            nouveauScore = elagage_alpha_beta(tmpMatrix, profondeur-1,False,tmpDernierTour,alpha,beta)[1]
            if nouveauScore > valeur:
                valeur = nouveauScore
                colonne = col
            alpha = max(alpha, valeur)
            if (alpha >= beta) :
                break 
        return colonne, valeur
    else:
        valeur = math.inf
        colonne = random.choice(colonneDisponible(matrix))
        for col in colonneDisponible(matrix):
            tmpDernierTour = copy.deepcopy(dernierTour)
            tmpDernierTour[0][1] = col
            tmpDernierTour[0][0] = ligneDisponible(matrix, tmpDernierTour[0][1])
            tmpMatrix = copy.deepcopy(matrix)
            jouerTour(tmpMatrix,1, tmpDernierTour[0][0], tmpDernierTour[0][1])
            
            nouveauScore = elagage_alpha_beta(tmpMatrix, profondeur-1,True,tmpDernierTour,alpha,beta)[1]
            if nouveauScore < valeur:
                valeur = nouveauScore
                colonne = col
            beta = min(beta, valeur)
            if (alpha >= beta) :
                break
        return colonne, valeur

def affichage(matrix):
    for i in range(6):
        print("                     [", end='')
        for j in range(7):
            if(matrix[5 - i][j] == 1):
                print('X', end='')
            elif(matrix[5 - i][j] == 2):
                print('O', end='')
            else:
                print(' ', end='')
            print(' ', end='')
        print("]")
    print("                      1 2 3 4 5 6 7\n")
    print("          Joueur 1 -> X        Joueur 2 -> O\n\n")

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
            if(compteurJ1 >= 4 and matrix[ligne][colonne] == 1):
                return(True)
            elif(compteurJ2 >= 4 and matrix[ligne][colonne] == 2):
                return(True)
            tmpColonne += 1
        tmpLigne += 1
        tmpColonne = 0
    tmpLigne = 0
    tmpColonne = 0
    compteurJ1 = 0
    compteurJ2 = 0
    while(tmpLigne < 6):
        if(matrix[tmpLigne][colonne] == 1):
            compteurJ1 += 1
        else:
            compteurJ1 = 0
        if(matrix[tmpLigne][colonne] == 2):
            compteurJ2 += 1
        else:
            compteurJ2 = 0
        if(compteurJ1 >= 4 and matrix[ligne][colonne] == 1):
                return(True)
        elif(compteurJ2 >= 4 and matrix[ligne][colonne] == 2):
            return(True)
        tmpLigne += 1
    tmpLigne = ligne
    tmpColonne = colonne
    compteurJ1 = 0
    compteurJ2 = 0
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
        if(compteurJ1 >= 4 and matrix[ligne][colonne] == 1):
                return(True)
        elif(compteurJ2 >= 4 and matrix[ligne][colonne] == 2):
            return(True)
        tmpLigne += 1
        tmpColonne += 1
    tmpLigne = ligne
    tmpColonne = colonne
    compteurJ1 = 0
    compteurJ2 = 0
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
        if(compteurJ1 >= 4 and matrix[ligne][colonne] == 1):
                return(True)
        elif(compteurJ2 >= 4 and matrix[ligne][colonne] == 2):
            return(True)
        tmpLigne += 1
        tmpColonne -= 1

def trouverLigne(matrix, colonne):
    ligne = 0
    while(matrix[ligne][colonne] != 0):
        ligne += 1
    return(ligne)


def finDePartie(matrix, dernierTour):
    return victoire(matrix,dernierTour[0][1],dernierTour[0][0]) or victoire(matrix,dernierTour[1][1],dernierTour[1][0]) or testMatrixPleine(matrix)

def jouerTour(matrix, joueur,ligne = -1,colonne = -1):
    erreur = True
    if(joueur == 1 and ligne == -1):    
        print("Joueur 1, dans quelle case voulez-vous mettre votre jeton ?")
        while(erreur == True):
            erreur = False
            colonne = input("Veuillez entrer le numéro de colonne\n")
            while(colonne != '1' and colonne != '2' and colonne != '3' and colonne != '4' and colonne != '5' and colonne != '6' and colonne != '7'):
                colonne = input("Veuillez entrer un numéro de colonne entre 1 et 7 compris\n")
            colonne = int(colonne)
            colonne -= 1
            while(colonneDisponible(matrix).count(colonne) != 1):
                print("La colonne où vous voulez jouer est pleine, veuillez choisir une autre colonne")
                colonne = input("Veuillez entrer le numéro de colonne\n")
                while(colonne != '1' and colonne != '2' and colonne != '3' and colonne != '4' and colonne != '5' and colonne != '6' and colonne != '7'):
                    colonne = input("Veuillez entrer un numéro de colonne entre 1 et 7 compris\n")
                colonne = int(colonne)
                colonne -= 1
            ligne = trouverLigne(matrix, colonne)
            dernierTour[0] = [ligne,colonne]
            if(matrix[ligne][colonne] == 1 or matrix[ligne][colonne] == 2):
                erreur = True
                print("Il y a déjà un jeton dans cette case, veuillez rejouer votre tour")
        matrix[ligne][colonne] = 1
        return dernierTour[0]
    elif(joueur == 2 and ligne == -1):
        print("Joueur 2, dans quelle case voulez-vous mettre votre jeton ?")
        while(erreur == True):
            erreur = False
            colonne = input("Veuillez entrer le numéro de colonne\n")
            while(colonne != '1' and colonne != '2' and colonne != '3' and colonne != '4' and colonne != '5' and colonne != '6' and colonne != '7'):
                colonne = input("Veuillez entrer un numéro de colonne entre 1 et 7 compris\n")
            colonne = int(colonne)
            colonne -= 1
            while(colonneDisponible(matrix).count(colonne) != 1):
                print("La colonne où vous voulez jouer est pleine, veuillez choisir une autre colonne")
                colonne = input("Veuillez entrer le numéro de colonne\n")
                while(colonne != '1' and colonne != '2' and colonne != '3' and colonne != '4' and colonne != '5' and colonne != '6' and colonne != '7'):
                    colonne = input("Veuillez entrer un numéro de colonne entre 1 et 7 compris\n")
                colonne = int(colonne)
                colonne -= 1
            ligne = trouverLigne(matrix, colonne)
            dernierTour[1] = [ligne,colonne]
            if(matrix[ligne][colonne] == 1 or matrix[ligne][colonne] == 2):
                erreur = True
                print("Il y a déjà un jeton dans cette case, veuillez rejouer votre tour")
        matrix[ligne][colonne] = 2
        return dernierTour[1]
    elif(joueur == 1 ):
        while(erreur == True):
            erreur = False
            dernierTour[0] = [ligne,colonne]
            if(matrix[ligne][colonne] == 1 or matrix[ligne][colonne] == 2):
                erreur = True
                print("Il y a déjà un jeton dans cette case, veuillez rejouer votre tour")
        matrix[ligne][colonne] = 1
        return dernierTour[0]
    else:
        while(erreur == True):
            erreur = False
            dernierTour[1] = [ligne,colonne]
            if(matrix[ligne][colonne] == 1 or matrix[ligne][colonne] == 2):
                erreur = True
                print("Il y a déjà un jeton dans cette case, veuillez rejouer votre tour")
        matrix[ligne][colonne] = 2
        return dernierTour[1]

def choixModeDeJeu():
    print("Explication des règles")
    print("Choisir un mode de jeu parmis :")
    print("- Joueur contre Joueur (tapez 0)")
    print("- Joueur contre IA (tapez 1)")
    mode = input("Veuillez choisir un mode de jeu\n")
    while(mode != '0' and mode != '1'):
        mode = input("Veuillez saisir un des modes de jeu proposés\n")
    mode = int(mode)
    if(mode == 0):
        print("Vous avez choisi le mode Joueur contre Joueur")
    elif(mode == 1):
        print("Vous avez choisi le mode Joueur contre IA")
    else:
        print("Veuillez choisir entre les 2 modes de jeux disponibles")
    return(mode)

def rejouer():
    rejouer = input("Voulez-vous relancer une partie ? 1 si oui, 0 sinon\n")
    while(rejouer != '0' and rejouer != '1'):
        rejouer = input("Voulez-vous relancer une partie ? 1 si oui, 0 sinon\n")
    rejouer = int(rejouer)
    if(rejouer == 1):
        return(True)
    else:
        return(False)

def testMatrixPleine(matrix):
    tmpLigne = 0
    plein = True
    while(tmpLigne < 6):
        tmpColonne = 0
        while(tmpColonne < 7):
            if(matrix[tmpLigne][tmpColonne] == 0):
                plein = False
            tmpColonne += 1
        tmpLigne += 1
    if(plein == True):
        print("Il n'y a plus de cases disponibles")
    return(plein)

def colonneDisponible(matrix):
    colonne_dispo = []
    for colonne in range(7):
        if matrix[5][colonne] == 0:
            colonne_dispo.append(colonne)
        
    return colonne_dispo

def ligneDisponible(board, colonne):
	for ligne in range(6):
		if board[ligne][colonne] == 0:
			return ligne

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
    erreur = True
    while(erreur == True):
        erreur = False
        if(matrix[tmpLigne][tmpColonne] == 1 or matrix[tmpLigne][tmpColonne] == 2):
            erreur = True
            print(erreur)
    matrix[tmpLigne][tmpColonne] = 2
    return [tmpLigne,tmpColonne]

def tourIAMoyen(matrix,dernierTour):
    tmpColonne, minimax_score = minimax(matrix, 3,True,dernierTour)
    if(tmpColonne != None):
        tmpLigne = trouverLigne(matrix, tmpColonne)
        matrix[tmpLigne][tmpColonne] = 2
        return [tmpLigne,tmpColonne]

def tourIADifficile(matrix,dernierTour):
    tmpColonne, minimax_score = elagage_alpha_beta(matrix, 5, True, dernierTour, -math.inf, math.inf)
    if(tmpColonne != None):
        tmpLigne = trouverLigne(matrix, tmpColonne)
        matrix[tmpLigne][tmpColonne] = 2
        return [tmpLigne,tmpColonne]

while(conditionRejouer == True): #ou que la grille soit pleine
    mode = choixModeDeJeu()
    if(mode == 0):
        while(conditionFinPartie == False):
            affichage(matrix)
            dernierTour[0] = jouerTour(matrix, 1)
            affichage(matrix)
            if(victoire(matrix, dernierTour[0][1], dernierTour[0][0]) == True or testMatrixPleine(matrix) == True):
                conditionFinPartie = True
                print("Le joueur 1 a gagné")
            if(conditionFinPartie == False):
                dernierTour[1] = jouerTour(matrix, 2)
                if(victoire(matrix, dernierTour[1][1], dernierTour[1][0]) == True or testMatrixPleine(matrix) == True):
                    conditionFinPartie = True
                    print("Le joueur 2 a gagné")
            affichage(matrix)
    else:
        print("Veuillez choisir un niveau de difficulté parmis :")
        print("Facile - Tapez 0")
        print("Moyenne - Tapez 1")
        print("Difficile - Tapez 2")
        diff = input("")
        while(diff != '0' and diff != '1' and diff != '2'):
            diff = input("Veuillez saisir un des niveaux de difficulté proposé\n")
        diff = int(diff)
        if(diff == 0):
            print("Vous avez choisi la difficulté Facile")
            affichage(matrix)
            while(conditionFinPartie == False):
                dernierTour[0] = jouerTour(matrix, 1)
                if(victoire(matrix, dernierTour[0][1], dernierTour[0][0]) == True or testMatrixPleine(matrix) == True):
                    conditionFinPartie = True
                    print("Le joueur 1 a gagné")
                if(conditionFinPartie == False):
                    dernierTour[1] = tourIAFacile(matrix)
                    print("L'IA a joué colonne : " + str(dernierTour[1][1] + 1))
                    if(victoire(matrix, dernierTour[1][1], dernierTour[1][0]) == True or testMatrixPleine(matrix) == True):
                        conditionFinPartie = True
                        print("L'IA a gagné")
                affichage(matrix)
            conditionRejouer = rejouer()
            if(conditionRejouer == True):
                matrix = viderMatrix()
                conditionFinPartie = False
        elif(diff == 1):
            print("Vous avez choisi la difficulté Moyenne")
            affichage(matrix)
            while(conditionFinPartie == False):
                dernierTour[0] = jouerTour(matrix, 1)
              
                if(victoire(matrix, dernierTour[0][1], dernierTour[0][0]) == True or testMatrixPleine(matrix) == True):
                    conditionFinPartie = True
                    print("Le joueur 1 a gagné")
                if(conditionFinPartie == False):
                    dernierTour[1] = tourIAMoyen(matrix,dernierTour)
                    print("L'IA a joué colonne : " + str(dernierTour[1][1] + 1))
                    if(victoire(matrix, dernierTour[1][1], dernierTour[1][0]) == True or testMatrixPleine(matrix) == True):
                        conditionFinPartie = True
                        print("L'IA a gagné")
                affichage(matrix)
            conditionRejouer = rejouer()
            if(conditionRejouer == True):
                matrix = viderMatrix()
                conditionFinPartie = False
        elif(diff == 2):
            print("Vous avez choisi la difficulté Difficile")
            affichage(matrix)
            while(conditionFinPartie == False):
                dernierTour[0] = jouerTour(matrix, 1)
                if(victoire(matrix, dernierTour[0][1], dernierTour[0][0]) == True or testMatrixPleine(matrix) == True):
                    conditionFinPartie = True
                    print("Le joueur 1 a gagné")
                if(conditionFinPartie == False):
                    dernierTour[1] = tourIADifficile(matrix,dernierTour)
                    print("L'IA a joué colonne : " + str(dernierTour[1][1] + 1))
                    if(victoire(matrix, dernierTour[1][1], dernierTour[1][0]) == True or testMatrixPleine(matrix) == True):
                        conditionFinPartie = True
                        print("L'IA a gagné")
                affichage(matrix)
            conditionRejouer = rejouer()
            if(conditionRejouer == True):
                matrix = viderMatrix()
                conditionFinPartie = False