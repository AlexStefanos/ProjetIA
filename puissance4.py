matrix = [[0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0]]
ligne = 0
colonne = 0
conditionFinPartie = False
conditionRejouer = True

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
            print(matrix)
            print("Joueur 2 ?")
            ligne = int(input("Veuillez entrer le numéro de ligne\n"))
            ligne -= 1
            colonne = int(input("Veuillez entrer le numéro de colonne\n"))
            colonne -= 1
            matrix[ligne][colonne] = 2
            print(matrix)
    else:
        while(conditionFinPartie == False):
            print("Joueur 1, dans quelle case voulez-vous mettre votre jeton ?")
    conditionRejouer = False

def victoire(matrix, colonne, ligne):
    compteurJ1 = 0
    compteurJ2 = 0
    for i in range(matrix[ligne][i]):
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
    for i in range(matrix[i][colonne]):
        if(matrix[i][colonne] == 1):
            compteurJ1 += 1
        else:
            compteurJ1 = 0
        if(matrix[ligne[i]] == 2):
            compteurJ2 += 1
        else:
            compteurJ2 = 0
    if(compteurJ1 >= 4 or compteurJ2 >= 4):
        return(True)
    if((ligne + 4 < 5) and (colonne + 4 < 6)):
        for i in range(matrix[ligne + i][colonne + i]):
            if(matrix[ligne + i][colonne + i] == 1):
                compteurJ1 += 1
            else:
                compteurJ1 = 0
            if(matrix[ligne + i][colonne + i] == 2):
                compteurJ2 += 1
            else:
                compteurJ2 = 0
    if(compteurJ1 >= 4 or compteurJ2 >= 4):
        return(True)
    if((ligne - 4 > 0) and (colonne - 4 > 0)):
        for i in range(matrix[ligne - i][colonne - i]):
            if(matrix[ligne - i][colonne - i] == 1):
                compteurJ1 += 1
            else:
                compteurJ1 = 0
            if(matrix[ligne - i][colonne - i] == 2):
                compteurJ2 += 1
            else:
                compteurJ2 = 0
    if(compteurJ1 >= 4 or compteurJ2 >= 4):
        return(True)
    #il manque la diagonale en haut à gauche et en bas à droite
    if(compteurJ1 >= 4 or compteurJ2 >= 4):
        return(True)
    else:
        return(False)
