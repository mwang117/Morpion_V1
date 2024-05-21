def morpions(score1 : int, score2 : int) -> int :
    """
    #-------------------------------------------------------------------------------------
    Fonction qui va prendre en paramètre d'entrée, les scores des deux joueurs. Et
    va renvoyer en paramètre de sortie, les scores des deux joueurs après avoir terminés
    les parties. JEU DE MORPION
    #-------------------------------------------------------------------------------------
    """

    table : list[list[str]]     #liste à double dimension afin d'avoir 3 lignes et 3 colonnes
    nb_colonne : int
    nb_ligne : int
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
    print("Jeu de Morpion simple")
    print("X pour le joueur 1")
    print("O pour le joueur 2")
            
    nb_partie = int(input("\nVeuilez saisir le nombre de partie que vous voulez jouer :"))

    while nb_partie != 0 :
        nb_partie = nb_partie - 1
        table = [
          ['-', '-', '-'],
          ['-', '-', '-'],
          ['-', '-', '-']
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
        
        #affichage de la matrice, pour qu'il ressemble à un morpion
        for i in range(0, 3) :
            print("\n")
            for j in range(0, 3) :
                print(table[i][j], end="  ")
                
        while (compteur != 9) and ((gagne_diago == 0) and (gagne_horizontale == 0) and (gagne_verticale == 0)) :
            print("\n" * 2, "Joueur", k,"Veuillez choisir le numéro de la ligne puis le numéro de la colonne !")
            
            
            nb_ligne = int(input("\nVeuillez saisir la ligne :"))
            #condition de la ligne, soit 1, 2 ou 3
            while (nb_ligne != 1) and (nb_ligne != 2) and (nb_ligne !=3) :
                print("Veuillez choisir entre 1, 2 ou 3 !!!")
                nb_ligne = int(input("Veuillez saisir la ligne :"))
            
            
            nb_colonne = int(input("\nVeuillez saisir la colonne :"))
            #condition de la colonne, soit 1, 2 ou 3
            while (nb_colonne != 1) and (nb_colonne != 2) and (nb_colonne !=3) :
                print("Veuillez choisir entre 1, 2 ou 3 !!!")
                nb_colonne = int(input("Veuillez saisir la colonne :"))
            
            
            #condition pour voir si la case est déjà prise ou non
            #moins 1 sur tout puisque la table commence à 0
            while (table[nb_ligne - 1][nb_colonne - 1] == "O") or (table[nb_ligne - 1][nb_colonne - 1] == "X") :
                
                
                #affichage de la matrice, pour qu'il  ressemble à un morpion
                print("\n" * 50)
                for i in range(0, 3) :
                    print("\n")
                    for j in range(0, 3) :
                        print(table[i][j], end="  ")
                 
                        
                print("\n" * 2, "Votre case choisie est déjà prise !!!")
                nb_ligne = int(input("Veuillez saisir la ligne :"))
                
                #condition de la ligne, soit 1, 2 ou 3
                while (nb_ligne != 1) and (nb_ligne != 2) and (nb_ligne !=3) :
                    print("Veuillez choisir entre 1, 2 ou 3 !!!")
                    nb_ligne = int(input("Veuillez saisir la ligne :"))
            
            
                nb_colonne = int(input("Veuillez saisir la colonne :"))
                
                #condition de la colonne, soit 1, 2 ou 3
                while (nb_colonne != 1) and (nb_colonne != 2) and (nb_colonne !=3) :
                    print("Veuillez choisir entre 1, 2 ou 3 !!!")
                    nb_colonne = int(input("Veuillez saisir la colonne :"))
            
            
            if (k) == 1 :
                table[nb_ligne - 1][nb_colonne - 1] = "X"
            else : 
                table[nb_ligne - 1][nb_colonne - 1] = "O"
            
            
            compteur = compteur + 1    
            gagne_verticale = gagne_vertical(table)
            gagne_diago = gagne_dia(table)
            gagne_horizontale = gagne_horizontal(table)
            
            
            #permuter entre joueur 1 et 2    
            k3 = k
            k = k2
            k2 = k3
            
            
            #affichage de la matrice, pour qu'il  ressemble à un morpion
            print("\n" * 50)
            for i in range(0, 3) :
                print("\n")
                for j in range(0, 3) :
                    print(table[i][j], end="  ")


        #condition match nul ou non
        #voir quel joueur a gagné
        if compteur == 9 :
            print("\n" * 2, "C'est match nul")
        else:
            print("\n" * 2, "Joueur", k, "a perdu")
            
            
        #condition si k = 2 puisque lors de la fin du boucle while, c'est le dernier joueur qui a joué qui gagne
        #mais juste avant la fin de cette boucle while, le 'k' change, per exemple, joueur 1 gagne, k = 2 à la fin
        if k == 2 :
            score1 = score1 + 1
        else : 
            score2 = score2 + 1
            
            
        print("\nle score du joueur 1 :", score1)
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
    
    i = 0
    valid = 0  
    
    for i in range(0, 3) :
        valid = 0
        if (table[0][i] == table[1][i]) and (table[1][i] == table[2][i]) and table[0][i] != "-" :
            valid = valid + 1 
            return valid
        
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
    
    i = 0
    valid = 0
    
    for i in range(0, 3) :
        valid = 0
        if ((table[i][0] == table[i][1]) and (table[i][1] == table[i][2]) and table[i][0] != "-") :
            valid = valid + 1
            return valid
        
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
    i : int
    
    i = 0
    valid = 0
    
    for i in range(0, 1) :
        valid = 0
        if ((table[i][0] == table[1][1]) and (table[1][1] == table[2][2]) and (table[i][0] != "-")) or ((table[i][2] == table[1][1]) and (table[1][1] == table[2][0]) and (table[i][2] != "-")) :
            valid = valid + 1
            return valid
        
    return valid