grille = [[" "," "," "," "," "," "," "],
               [" "," "," "," "," "," "," "],
               [" "," "," "," "," "," "," "],
               [" "," "," "," "," "," "," "],
               [" "," "," "," "," "," "," "],
               [" "," "," "," "," "," "," "]]

def verif():
    #check horizontal
    for i in range(6):
        for j in range(4):
            if (grille[i][j] == grille[i][j+1] == grille[i][j+2] == grille[i][j+3]) and (grille[i][j] != " "):
                return True
    #check vertical
    for i in range(3):
        for j in range(7):
            if (grille[i][j] == grille[i+1][j] == grille[i+2][j] == grille[i+3][j]) and (grille[i][j] != " "):
                return True
    #check diagonal desendant
    for i in range(3):
        for j in range(4):
            if (grille[i][j] == grille[i+1][j+1] == grille[i+2][j+2] == grille[i+3][j+3]) and (grille[i][j] != " "):
                return True
    
    #check diagonal montant
    for i in range(3,6):
        for j in range(4):
            if (grille[i][j] == grille[i-1][j+1] == grille[i-2][j+2] == grille[i-3][j+3]) and (grille[i][j] != " "):
                return True
    return False

def Affichage(tab):
    print("  1   2   3   4   5   6   7") #Afficghe le nom de la colonne
    for i in range(6):
        for j in range(7):
            if j == 0 :
                print("|",tab[i][j],end=" | ") #permet a chaque nouvelle ligne d'avoir une barre vertical
            else:
                print(tab[i][j],end=" | ")
        print("")

def tombe(colonne,jeton):
    for i in range(5):
        if grille[i+1][colonne-1] != grille[i][colonne-1]:
            grille[i][colonne-1] = jeton


def Jouer():
    Joueur1 = input("Entrez le nom du Joueur 1 :")
    Joueur2 = input("Entrez le nom du joueur 2 :")

    while Joueur1 == Joueur2:
        print("Le nom des Joueurs est le meme saisir deux nom different")
        Joueur1 = input("Entrez le nom du Joueur 1 :")
        Joueur2 = input("Entrez le nom du joueur 2 :")

    couleurInvalide = True
    while couleurInvalide:
        couleurJ1 = input(Joueur1 + " Choissisez une couleur entre Rouge et Jaune" + "\n")
        if couleurJ1 == "Jaune":
            jeton =  "\U0001f7e1"
            couleurInvalide = False
        elif couleurJ1 == "Rouge":
            jeton = "\U0001f534"
            couleurInvalide = False

    while not(verif()):
        print("Au tour de",Joueur1,"de jouer")
        choix = input("Dans quelle colonne shouaitez vous mettre le jeton ?" + "\n")
        if choix.isdigit():
            choix = int(choix)
        while choix != int:
            print(choix != int)
            choix = input("Saisir un entier")
            if choix.isdigit():
                choix = int(choix)
                print(choix == 1)
        while choix > 7 or choix < 1 or choix != int:
                choix = input("Saisir un entier compris entre 1 et 7 inclus")
        choix = int(choix)
        if grille[0][choix-1] != " ":
            print("Cette colonne est deja pleine")
        else:
            tombe(choix,jeton)
            Affichage(grille)
            if verif() == False:
                chamgementJoueur = Joueur1
                Joueur1 = Joueur2
                Joueur2 = chamgementJoueur
            else:
                print(Joueur1,"a gagner")
            if jeton == "\U0001f7e1":
                jeton = "\U0001f534"
            else:
                jeton = "\U0001f7e1"

Jouer()