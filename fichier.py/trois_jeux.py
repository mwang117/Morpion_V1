from fonction_mor import morpions
from fonction_allu import allumettes
from fonction_dev import devinettes
from fonction_puiss import puissance
from fonction_tri import tri_bulle

if __name__ == "__main__" :
    """
    #-------------------------------------------------------------------------------------
    Fonction : fonction morpions, fonction allumettes, fonction devinettes et fonction
    puissance 4
    Programme qui va faire office de menu afin d'accéder aux différents jeux comme le 
    morpion, la devinette, les allumettes ou bien le puissance quatre.
    #-------------------------------------------------------------------------------------
    """
    
    score1 : int            #score après la fin d'un seul jeu du joueur 1
    score2 : int            #score après la fin d'un seul jeu du joueur 1
    score1_dev : int        #score du joueur 1 pour la Devinette
    score2_dev : int        #score du joueur 2 pour la Devinette
    score1_all : int        #score du joueur 1 pour l'Allumette
    score2_all : int        #score du joueur 2 pour l'Allumette
    score1_mor : int        #score du joueur 1 pour le Morpion
    score2_mor : int        #score du joueur 2 pour le Morpion
    score1_pui : int        #score du joueur 1 pour le Puissance 4
    score2_pui : int        #score du joueur 2 pour le Puissance 4
    score1_final : int      #score final du joueur 1
    score2_final : int      #score final du joueur 2
    saisi : int
    jouer : int
    liste : list[int]       #liste commençant par le score du jeu Devinette, Allumette, Morpion puis Puissance 4
    liste_nom : list[str]   #liste 
    
    jouer = 1
    liste = [0, 0, 0, 0]
    liste_nom = ["Devinette", "Allumette", "Morpion", "Puissance 4"]
    score1_dev = 0
    score2_dev = 0
    score1_all = 0
    score2_all = 0
    score1_mor = 0
    score2_mor = 0
    score1_pui = 0
    score2_pui = 0
    score1_final = 0
    score2_final = 0
    
    print("\nMenu")
    
    #permet de savoir si l'utilisateur veut encore jouer ou non, on part du principe que l'utilisateur joue à au moins un jeu 
    while jouer == 1 :
        score1 = 0
        score2 = 0
        
        print("\n- Taper 1 pour jouer au Devinette")
        print("- Taper 2 pour jouer à l'Allumettes")
        print("- Taper 3 pour jouer au Morpion")
        print("- Taper 4 pour jouer au Puissance Quatre")
        saisi = int(input("Votre saisi :"))

        #condition pour les choix des jeux, soit 1, 2, 3 ou 4
        while (saisi != 1) and (saisi != 2) and (saisi != 3) and (saisi != 4):
            print("\n" * 50, "Votre saisi est fausse")
            print("- Taper 1 pour jouer au Devinette")
            print("- Taper 2 pour jouer à l'Allumettes")
            print("- Taper 3 pour jouer au Morpion")
            print("- Taper 4 pour jouer au Puissance Quatre")
            saisi = int(input("Votre saisi :"))
        
        #choix des jeux avec 
        if saisi == 1 :
            score1, score2 = devinettes(score1_dev, score2_dev)
            score1_dev = score1_dev + score1
            score2_dev = score2_dev + score2
        else :
            if saisi == 2 :
                score1, score2 = allumettes(score1_all, score2_all)
                score1_all = score1_all + score1
                score2_all = score2_all + score2
            else :
                if saisi == 3 :
                    score1, score2 = morpions(score1_mor, score2_mor)
                    score1_mor = score1_mor + score1
                    score2_mor = score2_mor + score2
                else : 
                    if saisi == 4 :                       
                        score1, score2 = puissance(score1_pui, score2_pui)
                        score1_pui = score1_pui + score1
                        score2_pui = score2_pui + score2
        
        #score final
        score1_final = score1_all + score1_dev + score1_mor + score1_pui
        score2_final = score2_all + score2_dev + score2_mor + score2_pui
        
        if score1_final > score2_final :
            #liste des scores du joueur 1 des différents jeux
            liste[0] = score1_dev
            liste[1] = score1_all
            liste[2] = score1_mor
            liste[3] = score1_pui
        else :
            #liste des scores du joueur 2 des différents jeux
            liste[0] = score2_dev
            liste[1] = score2_all
            liste[2] = score2_mor
            liste[3] = score2_pui
        
        print("\n" * 3, "Taper 1 pour si vous voulez continuer à jouer")
        print("Taper 2 pour si vous ne voulez plus jouer")
        jouer = int(input("Votre saisi :"))
    
        #condition l'utilisateur doit taper 1 ou 2, 1 s'il veut continuer à jouer et 2 s'il veut arrêter 
        while (jouer != 1) and (jouer != 2) :
            print("\n" * 50, "Votre saisi est fausse")
            print("Taper 1 pour si vous voulez jouer")
            print("Taper 2 pour si vous ne voulez plus jouer")
            jouer = int(input("Votre saisi :"))
     
               
    #tri des scores des différents jeux pour le joueur gagnant final
    liste, liste_nom = tri_bulle(liste, liste_nom)
    
    if (score1_final > score2_final) :
        print("\nLe classement du joueur 1")
        print("\n" * 3, "classement", 4,":", liste_nom[0], ":", liste[0])
        print("classement", 3,":", liste_nom[1], ":", liste[1])
        print("classement", 2,":", liste_nom[2], ":", liste[2])
        print("classement", 1,":", liste_nom[3], ":", liste[3])
    else :
        if (score2_final > score1_final) :
            print("\nLe classement du joueur 2")
            print("\n" * 3, "classement", 4,":", liste_nom[0], ":", liste[0])
            print("classement", 3,":", liste_nom[1], ":", liste[1])
            print("classement", 2,":", liste_nom[2], ":", liste[2])
            print("classement", 1,":", liste_nom[3], ":", liste[3])
        else :
            print("Match nul")