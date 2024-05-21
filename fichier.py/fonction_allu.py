def allumettes(score1 : int, score2 : int) -> int :
    """
    #-------------------------------------------------------------------------------------
    Fonction qui va prendre en paramètre d'entrée, les scores des deux joueurs. Et
    va renvoyer en paramètre de sortie, les scores des deux joueurs après avoir terminés
    les parties. JEU D'ALLUMETTE
    #-------------------------------------------------------------------------------------
    """
    
    #règle
    print("Il y a 20 allumettes.")
    print("Chacun son tour attrape 1, 2 ou 3 allumettes.")
    print("Le premier qui attrape la dernière allumette a gagné !")
        
    nb_allu : int
    preleve : int
    k2 : int
    k3 : int
    k : int
    nb_partie : int
    
    k2 = 2
    k3 = 0
    k = 1
    nb_partie = int(input("Veuilez saisir le nombre de partie qui vous voulez jouer :"))

    while nb_partie != 0 :
        nb_allu = 20
        
        #condition, le joueur qui doit retirer la dernière allumette a perdu 
        while nb_allu != 1 :
            print("il reste", nb_allu, "allumettes")
            print("Joueur", k, "veuillez saisir un chiffre entre 1, 2 ou 3 :")
            preleve = int(input("Votre saisi :"))
            
            #condition soit 1 ou 2 ou 3
            while (preleve != 1) and (preleve != 2) and (preleve != 3) :
                print("Vous ne pouvez pas retirer", preleve, "allumettes")
                print("Joueur", k, "veuillez saisir un chiffre entre 1, 2 ou 3 :")
                preleve = int(input("Votre saisi :"))
            
            #condition pour qu'il reste 1 allumette à la fin 
            while ((nb_allu == 3) and (preleve == 3)) or (nb_allu == 2) and ((preleve == 2) or (preleve == 3)) :
                print("Vous ne pouvez pas retirer", preleve, "allumettes")
                print("Joueur", k, "veuillez saisir un chiffre entre 1, 2 ou 3 :")
                preleve = int(input("Votre saisi :"))      
            nb_allu = nb_allu - preleve
            
            #pour permuter entre joueur 1 et joueur 2
            k3 = k
            k = k2
            k2 = k3
        print("il reste", nb_allu, "allumettes")    
        print("Joueur", k, "a perdu")
        nb_partie = nb_partie - 1
        
        #le nombre 1 c'est pour le joueur 1 mais le programme fait que k permute sur l'autre chiffre à la fin
        if k == 1 :
            score2 = score2 + 1
        else: 
            score1 = score1 + 1                
    print("le score du joueur 1 :", score1)
    print("le score du joueur 2 :", score2)

    return score1, score2 