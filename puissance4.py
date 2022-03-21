matrix = [[0, 0, 0, 0, 0, 0, 0], 
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
#    6    [[1, 0, 0, 0, 0, 0, 0], 
#    5    [0, 2, 0, 0, 0, 0, 0], 
#    4    [0, 0, 1, 0, 0, 0, 0], 
#    3    [0, 0, 0, 1, 0, 0, 0], 
#    2    [0, 0, 0, 0, 1, 0, 0], 
#    1    [0, 0, 0, 0, 0, 1, 0]]
ligne = 0
colonne = 0
conditionFinPartie = False
conditionRejouer = True

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
    tmpLigne = ligne
    tmpColonne = colonne
    for i in range(6):
        if(matrix[ligne][i] == 1):
            compteurJ1 += 1
        else:
            compteurJ1 = 0
        if(matrix[ligne][i] == 2):
            compteurJ2 += 1
        else:
            compteurJ2 = 0
        if(compteurJ1 >= 4 or compteurJ2 >= 4):
            return(True)
    for i in range(6):
        if(matrix[i][colonne] == 1):
            compteurJ1 += 1
        else:
            compteurJ1 = 0
        if(matrix[i][colonne] == 2):
            compteurJ2 += 1
        else:
            compteurJ2 = 0
        if(compteurJ1 >= 4 or compteurJ2 >= 4):
            return(True)
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
            print("compteurJ1 :", compteurJ1)
            print("tmpLigne :", tmpLigne)
            print("tmpColonne :", tmpColonne)
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

while(conditionRejouer == True): #ou que la grille soit pleine
    print("Salut à tous")
    print("Explication des règles")
    print("Choisir un mode de jeu parmis :")
    print("- Joueur contre Joueur (tapez 0)")
    print("- Joueur contre IA (tapez 1)")
    tmp = int(input(""))
    while(tmp != 0 and tmp != 1):
        if(tmp == 0):
            print("Vous avez choisi le mode Joueur contre Joueur")
        elif(tmp == 1):
            print("Vous avez choisi le mode Joueur contre IA")
        else:
            print("Veuillez choisir entre les 2 modes de jeux disponibles")
    #bien faire l'affichage
    if(tmp == 0):
        while(conditionFinPartie == False):
            print("Joueur 1, dans quelle case voulez-vous mettre votre jeton ? [ligne, colonne]")
            ligne = int(input("Veuillez entrer le numéro de ligne\n"))
            ligne -= 1
            colonne = int(input("Veuillez entrer le numéro de colonne\n"))
            colonne -= 1
            matrix[ligne][colonne] = 1
            affichage(matrix)
            if(victoire(matrix, colonne, ligne) == True):
                conditionFinPartie = True
                print("GGGGGGGGGGGGGGGGG")
            print("Joueur 2 ?")
            ligne = int(input("Veuillez entrer le numéro de ligne\n"))
            ligne -= 1
            colonne = int(input("Veuillez entrer le numéro de colonne\n"))
            colonne -= 1
            matrix[ligne][colonne] = 2
            affichage(matrix)
            if(victoire(matrix, colonne, ligne) == True):
                conditionFinPartie = True
                print("GGGGGGGGGGGGGGGGGGGGG")
    else:
        while(conditionFinPartie == False):
            print("Joueur 1, dans quelle case voulez-vous mettre votre jeton ?")
    conditionRejouer = False

    # à faire :
    #     - pour l'utilisateur : il ne doit mettre que les colonnes pour jouer et donc faire coulisser les pièces
    #     - ne pas pouvoir remplacer une pièce déjà mise
    #     - quand un des 2 joueurs gagnent une partie, la partie s'arrête