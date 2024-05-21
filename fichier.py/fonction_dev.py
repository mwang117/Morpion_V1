def devinettes(score1 : int, score2 : int) -> int :
    """
    #-------------------------------------------------------------------------------------
    Fonction qui va prendre en paramètre d'entrée, les scores des deux joueurs. Et
    va renvoyer en paramètre de sortie, les scores des deux joueurs après avoir terminés
    les parties. JEU DE DEVINETTE
    #-------------------------------------------------------------------------------------
    """
    
    nb_J1 : int
    nb_J2 : int
    Max : int
    tentative : int
    rejouer : str
    reponse : int

    nb_J1 = 0
    nb_J2 = 0
    Max = 0
    rejouer = ""
    tentative = 5
    reponse = 0

    print("\n" *100)
    while True :
        print("\n" * 10)
        
        tentative = 5
        
        #règle
        print("Le joueur 1 choisi un entier et une intervalle")
        print("Le joueur 2 a 5 essais et s'il réussit à deviner l'entier, il gagne")
        print("Sinon le joueur 1 gagne")
        print("\n" *5)
        nb_J1 = 0
        while (nb_J1 < 1 or nb_J1 > Max and Max < 1):
            Max = int(input("Joueur1, choisissez la limite maximale : "))
            nb_J1 = int(input("Choisissez votre nombre entier entre 1 et " + str(Max) + " : "))
            

        
        
        print("\n" * 100)
        while (tentative > 0) :
            
            nb_J2 = 0
            while(nb_J2 > Max or nb_J2 < 1) :
                print("\n" * 3)
                print("Joueur2, vous devez choisir un nombre entre 1 et "+ str(Max))
                nb_J2 = int(input("Joueur2 choisissez un nombre : "))
                
                if (nb_J2 > Max or nb_J2 < 1):
                    print("Vous devez choisir un nombre dans la limite indiqué")
                else :
                    break
                
                
            tentative = tentative - 1
            
            print("\n" * 100)
            
            
            while reponse != 1 or reponse != 2 or reponse != 3 :
                print("Joueur1, le nombre choisi par le Joueur2 est :", nb_J2)
                reponse = int(input(print(nb_J2," est :"
                    "\n1. Plus petit que votre nombre"
                    "\n2. Plus grand que votre nombre"
                    "\n3. Egale à votre nombre")))

                print("\n" * 20)    
                if reponse == 1 :                    
                    if nb_J2 < nb_J1 :
                        print("Le nombre du Joueur2 est bien trop petit")
                        break
                    else :
                        print("Menteur! Le nombre du Joueur2 n'est pas plus petit")
                if reponse == 2 :  
                    if nb_J2 > nb_J1 :
                        print("Le nombre du Joueur2 est bien trop grand")
                        break
                    else :
                        print("Menteur! Le nombre du Joueur2 n'est pas plus grand")
                if reponse == 3 :
                    if nb_J2 == nb_J1 :
                        print("C'est gagné !!")
                        break
                    else :
                        print("Menteur! Le Joueur2 n'a pas donné la bonne réponse")

            if nb_J2 == nb_J1:
                break    
            print("il vous reste ",tentative, " tentatives")

                
            
        if nb_J1 == nb_J2:
            print("Le joueur2 a remporté la partie")
            score2 = score2 + 1
        else :
            print("Le joueur 1 a remporté la partie ")
            score1 = score1 + 1
        rejouer = str(input("Voulez vous rejouer ? (oui/non) : "))
        
        if rejouer != "oui" :
            break
    
    return score1, score2