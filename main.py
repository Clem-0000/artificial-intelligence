default_actions = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]  # contient les actions des joueurs
lines_win = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]  # contient les positions permettant la victoire d'un joueur


def encore_case_vide(actions):
    """
    Question 1 :
    Permet de savoir s'il y a une case vide ou non, la case vide est défini par "_"
    :return: true s'il y a une case vide sinon false
    """
    return "_" in actions


def etat_final(actions):
    """
    Question 2
    Fonction permettant de déterminer s'il y a un gagnant
    :param actions: contient les actions jouées par les joueurs
    :return: -1 si le joueur min gagne, 1 si le joueur max gagne, 0 si c'est une égalité et -2 si ce n'est pas un état final
    """
    for line in lines_win:
        pose_a, pose_b, pose_c = line
        if actions[pose_a] != "_" and actions[pose_a] == actions[pose_b] and actions[pose_b] == actions[pose_c]:
            if actions[pose_a] == "O":
                return 1
            elif actions[pose_a] == "X":
                return -1
    if not encore_case_vide(actions):
        return 0
    return -2


def minmax(actions, joueur):
    """
    Question 3
    Fonction testant pour chaque case la valeur de la fonction d'évaluation et renvoie en fonction du joueur cette valeur.
    :param actions: Contient une version de la grille courante (il ne faut pas ovveride notre grille donc on en créé une nouvelle)
    :param joueur: Contient quel est le joueur actuel : "O" ou "X"
    :return: 1 / 0 / -1 en fonction de si le coup est bon ou non
    """
    final_state = etat_final(actions)
    if final_state != -2:
        return final_state
    if joueur == "O":
        # max
        meilleur_valeur = -10000
        for i in range(len(actions)):
            if actions[i] == "_":
                nouvelles_actions = list(actions)
                nouvelles_actions[i] = "O"
                valeur = minmax(nouvelles_actions, "X")
                meilleur_valeur = max(meilleur_valeur, valeur)
        return meilleur_valeur
    else:
        # min
        meilleur_valeur = 10000
        for i in range(len(actions)):
            if actions[i] == "_":
                nouvelles_actions = list(actions)
                nouvelles_actions[i] = "X"
                valeur = minmax(nouvelles_actions, "O")
                meilleur_valeur = min(meilleur_valeur, valeur)
        return meilleur_valeur


def affichage(actions):
    """
    Question 4
    Fonction permettant d'afficher la grille du morpion
    :param actions: Contient l'état actuel de la grille de la partie
    :return: none
    """
    print(actions[0] + ' | ' + actions[1] + ' | ' + actions[2])
    print("----------")
    print(actions[3] + ' | ' + actions[4] + ' | ' + actions[5])
    print("----------")
    print(actions[6] + ' | ' + actions[7] + ' | ' + actions[8])
    print("\n")


def trouverAction(actions, joueur):
    """
    Question 5
    Permet de définir quel est la meilleure action à jouer pour le joueur courant
    :param actions: Contient l'état actuel de la grille de la partie
    :param joueur: Contient le joueur qui doit jouer
    :return: L'indice du meilleur coup à jouer
    """
    meilleure_valeur = -10000 if joueur == "O" else 10000
    meilleure_action = None
    for i in range(len(actions)):
        if actions[i] == "_":
            nouvelles_actions = list(actions)
            nouvelles_actions[i] = joueur
            valeur = minmax(nouvelles_actions, "X" if joueur == "O" else "O")
            print("valeur", valeur)
            if valeur > meilleure_valeur and joueur == "O":
                meilleure_valeur = valeur
                meilleure_action = i
            if valeur < meilleure_valeur and joueur == "X":
                meilleure_valeur = valeur
                meilleure_action = i
    return meilleure_action


# Boucle de jeu 2 ordinateurs
def computers_fight():
    """
    Question 6
    Boucle de jeu permetttant de faire s'affronter un ordinateur contre un autre ordinateur et
     déclaré le vainqueur ou l'égalité entre eux.
    :return: none
    """
    grille = ["_"] * 9
    joueur_actuel = "O"  # représente le joueur max qui commence toujours en premier

    while etat_final(grille) == -2:
        print(f"C'est au tour de {joueur_actuel} : ")
        coup = trouverAction(grille, joueur_actuel)
        grille[coup] = joueur_actuel
        affichage(grille)
        joueur_actuel = "X" if joueur_actuel == "O" else "O"

    # Afficher le résultat final
    affichage(grille)
    resultat = etat_final(grille)
    if resultat == 0:
        print("Match nul")
    elif resultat == 1:
        print("le gagnant est 0")
    elif resultat == -1:
        print("le gagnant est X")


def player_vs_computer():
    """
    Question 7
    Boucle de jeu permetttant de faire s'affronter un joueur contre un ordinateur et
     déclaré le vainqueur ou l'égalité entre eux.
    :return: none
    """
    grille = ["_"] * 9
    joueur_actuel = "O"

    while etat_final(grille) == -2:
        if joueur_actuel == "X":
            # Tour de l'utilisateur : joueur min
            print("C'est à votre tour de jouer (X).")
            affichage(grille)

            coup = None
            while coup is None:
                coup = int(input("Entrez le numéro de la case où vous voulez jouer (0-8): "))
                if coup > 8:
                    print("Veuillez saisir un nombre entre 0 et 8.")
                    coup = None
                elif grille[coup] != "_":
                    print("Case déjà remplie, veuillez choisir une autre case.")
                    coup = None

            grille[coup] = "X"
        else:
            # Tour de l'ordinateur : joueur max
            print("C'est au tour de l'ordinateur (O).")
            coup = trouverAction(grille, "O")
            grille[coup] = "O"
        joueur_actuel = "X" if joueur_actuel == "O" else "O"

    # Afficher le résultat final
    affichage(grille)
    resultat = etat_final(grille)
    if resultat == 0:
        print("Match nul")
    elif resultat == 1:
        print("le gagnant est 0")
    elif resultat == -1:
        print("le gagnant est X")


computers_fight()  # permet de lancer la simulation de combat entre les deux ordinateurs
