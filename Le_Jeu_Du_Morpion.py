#------------------------------------------------------------------------------------------#
# 
# ## initialisation de l'air du jeu en affichant le tableau

tableau = [" " for _ in range(9)] 

#on creer un tableau de 9 caractere espace 
#pour le jeu qu on remplacera plutard par les symboles du jeu durant la partie.

#------------------------------------------------------------------------------------------#

## affichage du tableau 

def afficherTableau (p, gagnant = None): 
    print(" " + p[0] + " | " + p[1] + " | " + p[2] + " ")
    print("---+---+---")
    print(" " + p[3] + " | " + p[4] + " | " + p[5] + " ")
    print("---+---+---")
    print(" " + p[6] + " | " + p[7] + " | " + p[8] + " ")
    if gagnant:
        print("""* Partie terminee : le joueur {0} a gagne. *""".format(gagnant))


#------------------------------------------------------------------------------------------#

##prgrammation du jeu 

def morpion():
    joueur = "X"
    tour = 0

    while True:
        afficherTableau(tableau)
        print("> Tour du joueur " + joueur + ". Entrez un nombre de 1 à 9.")

        move = int(input()) - 1  # notre tableau est de 0 à 8, donc on retire 1

        if tableau[move] == " ":
            tableau[move] = joueur
            tour += 1
        else:
            print("! Case déjà occupée, choisissez-en une autre.")
            continue  # on passe au prochain passage de boucle sans exécuter le code ci-dessous

        if tableau[0] == tableau[1] == tableau[2] != " " \
        or tableau[3] == tableau[4] == tableau[5] != " " \
        or tableau[6] == tableau[7] == tableau[8] != " " \
        or tableau[0] == tableau[3] == tableau[6] != " " \
        or tableau[1] == tableau[4] == tableau[7] != " " \
        or tableau[2] == tableau[5] == tableau[8] != " " \
        or tableau[0] == tableau[4] == tableau[8] != " " \
        or tableau[2] == tableau[4] == tableau[6] != " ":
            afficherTableau(tableau, joueur)
            break

        if tour == 9:
            print("Égalité")
            break

        joueur = "O" if joueur == "X" else "X"  # on change de joueur


if __name__ == "__main__":
    morpion()