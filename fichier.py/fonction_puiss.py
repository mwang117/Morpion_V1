def puissance(score1 : int, score2 : int) -> int :
    """
    #-------------------------------------------------------------------------------------
    Fonction qui va prendre en paramètre d'entrée, les scores des deux joueurs. Et
    va renvoyer en paramètre de sortie, les scores des deux joueurs après avoir terminés
    les parties. JEU DE PUISSANCE QUATRE
    #-------------------------------------------------------------------------------------
    """         
 
    table : list[list[str]]     #liste à double dimension afin d'avoir 3 lignes et 3 colonnes
    li_co : list[int]
    li_ligne : list[int]
    nb_colonne : int
    compteur : int
    gagne_verticale : int
    gagne_horizontale : int
    gagne_diago : int
    i : int
    j : int
    nb_partie : int
    k2 : int
    k3 : int
    k : int
    
    i = 0
    j = 0
    compteur = 0             
    gagne_verticale = 0
    gagne_horizontale = 0
    gagne_diago = 0
    
    #permuter entre joueur 1 et 2
    #joueur1 = X et joueur2 = O
    k2 = 2
    k3 = 0
    k = 1
    
    #règle
    print("Jeu de Puissance 4 simple")
    print("X pour le joueur 1")
    print("O pour le joueur 2")
            
    nb_partie = int(input("\nVeuilez saisir le nombre de partie que vous voulez jouer :"))

    while nb_partie != 0 :
        nb_partie = nb_partie - 1
        li_ligne = [0, 0, 0, 0, 0, 0, 0]
        li_co = [0, 1, 2, 3, 4, 5, 6]
        table = [
          ['-', '-', '-', '-', '-', '-', '-'],
          ['-', '-', '-', '-', '-', '-', '-'],
          ['-', '-', '-', '-', '-', '-', '-'],
          ['-', '-', '-', '-', '-', '-', '-'],
          ['-', '-', '-', '-', '-', '-', '-'],
          ['-', '-', '-', '-', '-', '-', '-']
        ]
        compteur = 0             
        gagne_verticale = 0
        gagne_horizontale = 0
        gagne_diago = 0
        
        #permuter entre joueur 1 et 2
        #joueur1 = X et joueur2 = O
        k2 = 2
        k3 = 0
        k = 1
        
        
        #affichage de la matrice, pour qu'il ressemble à un puissance 4, 6 lignes et 7 colonnes
        for i in range(5, -1, -1) :
            print("\n")
            for j in range(0, 7) :
                print(table[i][j], end="  ")
             
                
        while (compteur != 42) and ((gagne_diago == 0) and (gagne_horizontale == 0) and (gagne_verticale == 0)) :
            print("\n" * 2, "Joueur", k,"Veuillez choisir le numéro de la colonne !")            
            
            nb_colonne = int(input("\nVeuillez saisir la colonne :"))
            #condition de la colonne, soit 1, 2, 3, 4, 5, 6 ou 7
            while (nb_colonne != 1) and (nb_colonne != 2) and (nb_colonne !=3) and (nb_colonne != 4) and (nb_colonne != 5) and (nb_colonne != 6) and (nb_colonne != 7):
                print("Veuillez choisir entre 1, 2, 3, 4, 5, 6 ou 7 !!!")
                nb_colonne = int(input("Veuillez saisir la colonne :"))
            
            
            #condition pour voir si la case est déjà remplie ou non
            #moins 1 sur tout puisque la table commence à 0
            while (table[5][nb_colonne - 1] == "O") or (table[5][nb_colonne - 1] == "X") :
                
                print("\n" * 50)
                #affichage de la matrice, pour qu'il ressemble à un puissance 4, 6 lignes et 7 colonnes
                for i in range(5, -1, -1) :
                    print("\n")
                    for j in range(0, 7) :
                        print(table[i][j], end="  ")
                        
                print("\n" * 2, "Votre case choisie est déjà remplie !!!")
            
            
                nb_colonne = int(input("Veuillez saisir la colonne :"))
                #condition de la colonne, soit 1, 2, 3, 4, 5, 6 ou 7
                while (nb_colonne != 1) and (nb_colonne != 2) and (nb_colonne !=3) and (nb_colonne != 4) and (nb_colonne != 5) and (nb_colonne != 6) and (nb_colonne != 7):
                    print("Veuillez choisir entre 1, 2, 3, 4, 5, 6 ou 7 !!!")
                    nb_colonne = int(input("Veuillez saisir la colonne :"))
            
            
            #boucle for pour parcourir la liste
            for i in range(0, 7) :
                #ajoute +1 à la liste li_ligne; qui représente le nombre de jeton qu'il y a dans une colonne
                if (i == li_co[nb_colonne - 1]) :
                    li_ligne[nb_colonne - 1] = li_ligne[nb_colonne - 1] + 1
            
            
            if (k) == 1 :
                table[li_ligne[nb_colonne - 1] - 1][nb_colonne - 1] = "X"
            else : 
                table[li_ligne[nb_colonne - 1] - 1][nb_colonne - 1] = "O"
            
            
            compteur = compteur + 1    
            gagne_verticale = gagne_vertical(table)
            gagne_diago = gagne_dia(table)
            gagne_horizontale = gagne_horizontal(table)
            
            
            #permuter entre joueur 1 et 2    
            k3 = k
            k = k2
            k2 = k3
            
            print("\n" * 50)
            #affichage de la matrice, pour qu'il ressemble à un puissance 4, 6 lignes et 7 colonnes
            for i in range(5, -1, -1) :
                print("\n")
                for j in range(0, 7) :
                    print(table[i][j], end="  ")


        #condition match nul ou non
        #voir quel joueur a gagné
        if compteur == 42 :
            print("\n" * 2, "C'est match nul")
        else:
            print("\n" * 2, "Joueur", k, "a perdu")
            
            
        #condition si k = 2 puisque lors de la fin du boucle while, c'est le dernier joueur qui a joué qui gagne
        #mais juste avant la fin de cette boucle while, le 'k' change, per exemple, joueur 1 gagne, k = 2 à la fin
        if k == 2 :
            score1 = score1 + 1
        else : 
            score2 = score2 + 1
            
        print("le score du joueur 1 :", score1)
        print("le score du joueur 2 :", score2)   
    
    return(score1, score2)
        
        
def gagne_vertical(table : list[list[str]]) -> int :
    """
    #-------------------------------------------------------------------------------------
    Paramètre d'entrée : la liste à double dimension
    Paramètre de sortie : entier positif, valid, 0 ou 1
    Fonction qui va prendre en paramètre d'entrée la liste à double dimension et
    va envoyer un entier, soit 0, soit 1. 0 pour non valide et 1 pour valide. Une fonction 
    pour savoir si le joueur a gagné de manière verticale.
    #-------------------------------------------------------------------------------------
    """
    
    valid : int
    i : int
    compteur : int
    trou_1 : int
    trou_2 : int
    trou_3 : int
    trou_4 : int
    
    i = 0
    compteur = 0
    valid = 0 
    
    for i in range(0, 7) :
        valid = 0
        trou_1 = 0
        trou_2 = 1
        trou_3 = 2
        trou_4 = 3
        compteur = 0
        
        #utilisation de "for j" non possible, donc utilisation de while pour l'imiter (for i in range(0, 4))
        while (compteur != 3) :
            compteur = compteur + 1
            if ((table[trou_1][i] == table[trou_2][i]) and (table[trou_2][i] == table[trou_3][i]) and (table[trou_3][i] == table[trou_4][i]) and (table[trou_1][i] != "-")) :
                valid = valid + 1 
                return valid
            trou_1 = trou_1 + 1
            trou_2 = trou_2 + 1
            trou_3 = trou_3 + 1
            trou_4 = trou_4 + 1
    return valid
            
            
def gagne_horizontal(table : list[list[str]]) -> int :
    """
    #-------------------------------------------------------------------------------------
    Paramètre d'entrée : la liste à double dimension
    Paramètre de sortie : entier positif, valid, 0 ou 1
    Fonction qui va prendre en paramètre d'entrée la liste à double dimension et
    va envoyer un entier, soit 0, soit 1. 0 pour non valide et 1 pour valide. Une fonction 
    pour savoir si le joueur a gagné de manière horzontale.
    #-------------------------------------------------------------------------------------
    """
    
    valid : int
    i : int
    compteur : int
    trou_1 : int
    trou_2 : int
    trou_3 : int
    trou_4 : int
    
    i = 0
    compteur = 0
    valid = 0 
    
    for i in range(0, 6) :
        valid = 0
        trou_1 = 0
        trou_2 = 1
        trou_3 = 2
        trou_4 = 3
        compteur = 0
        
        #utilisation de "for j" non possible, donc utilisation de while pour l'imiter (for i in range(0, 4))
        while (compteur != 4) :
            compteur = compteur + 1
            if ((table[i][trou_1] == table[i][trou_2]) and (table[i][trou_2] == table[i][trou_3]) and (table[i][trou_3] == table[i][trou_4]) and (table[i][trou_1] != "-")) :
                valid = valid + 1
                return valid
            trou_1 = trou_1 + 1
            trou_2 = trou_2 + 1
            trou_3 = trou_3 + 1
            trou_4 = trou_4 + 1
        
    return valid
      
      
def gagne_dia(table : list[list[str]]) -> int :
    """
    #-------------------------------------------------------------------------------------
    Paramètre d'entrée : la liste à double dimension
    Paramètre de sortie : entier positif, valid, 0 ou 1
    Fonction qui va prendre en paramètre d'entrée la liste à double dimension et
    va envoyer un entier, soit 0, soit 1. 0 pour non valide et 1 pour valide. Une fonction 
    pour savoir si le joueur a gagné de manière diagonale.
    #-------------------------------------------------------------------------------------
    """
    
    valid : int
    compteur_i : int
    compteur_j : int
    trou_1_i : int            #pour les lignes du tableau
    trou_2_i : int
    trou_3_i : int
    trou_4_i : int
    trou_1 : int            #pour les colonnes du tableau
    trou_2 : int
    trou_3 : int
    trou_4 : int
    
    compteur_i = 0
    compteur_j = 0
    valid = 0 
    trou_1_i = -1
    trou_2_i = 0
    trou_3_i = 1
    trou_4_i = 2
    
    #utilisation de "for j" non possible, donc utilisation de while pour l'imiter (for i in range(0, 3))
    while (compteur_i != 3) :
        compteur_i = compteur_i + 1
        
        valid = 0
        trou_1_i = trou_1_i + 1
        trou_2_i = trou_2_i + 1
        trou_3_i = trou_3_i + 1
        trou_4_i = trou_4_i + 1
        trou_1 = 0
        trou_2 = 1
        trou_3 = 2
        trou_4 = 3
        
        #utilisation de "for j" non possible, donc utilisation de while pour l'imiter (for i in range(0, 4))
        while (compteur_j != 4) :
            compteur_j = compteur_j + 1
            if ((table[trou_1_i][trou_1] == table[trou_2_i][trou_2]) and (table[trou_2_i][trou_2] == table[trou_3_i][trou_3]) and (table[trou_3_i][trou_3] == table[trou_4_i][trou_4]) and (table[trou_1_i][trou_1] != "-")) :
                valid = valid + 1 
                return valid
            trou_1 = trou_1 + 1
            trou_2 = trou_2 + 1
            trou_3 = trou_3 + 1
            trou_4 = trou_4 + 1
            
        trou_1 = 6
        trou_2 = 5
        trou_3 = 4
        trou_4 = 3
        
        #utilisation de "for j" non possible, donc utilisation de while pour l'imiter (for i in range(0, 4))
        while (compteur_j != 4) :
            compteur_j = compteur_j + 1
            if ((table[trou_1_i][trou_1] == table[trou_2_i][trou_2]) and (table[trou_2_i][trou_2] == table[trou_3_i][trou_3]) and (table[trou_3_i][trou_3] == table[trou_4_i][trou_4]) and (table[trou_1_i][trou_1] != "-")) :
                valid = valid + 1 
                return valid
            trou_1 = trou_1 - 1
            trou_2 = trou_2 - 1
            trou_3 = trou_3 - 1
            trou_4 = trou_4 - 1
            
    return valid