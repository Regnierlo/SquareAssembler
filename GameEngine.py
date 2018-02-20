def CalculScore(score,nombreCouleurADetruire):
    score+=nombreCouleurADetruire   
    return score

def VerificationFinJeu(plateau):
    nombreCouleurPouvantEtreDetruit = 0
    i = 0
    j = 0
    taillePlateau = len(plateau)
    #tant que le tableau n'est pas entierement parcouru ou qu'on n'a pas trouvé une combinaison d'au moins 3 blocs on continue
    while (i < taillePlateau & j < taillePlateau) | (nombreCouleurPouvantEtreDetruit < 3):
        #on récupère le nombre de bloc pouvant etre détruit
        nombreCouleurPouvantEtreDetruit = VerificationDestruction(i, j, plateau,False)
        
        #on avance dans le tableau
        j += 1
        if j >= taillePlateau:
            j = 0
            i += 1
    
    #on regarde si on peut détruire les blocs
    fin = PeutOnDetruire(nombreCouleurPouvantEtreDetruit)
    
    #si on peut détruire c'est que ce n'est pas encore la fin du jeu
    if fin == True:
        fin = False
    else: #si on ne peut pas détruire c'est que c'est la fin du jeu
        fin = True
    
    return fin
    
    
def ReplacementDesCubes(plateau):
    #on parcourt le tableau en sens inverse
    for i in range(len(plateau)-1,0,-1):
        for j in range(len(plateau)-1,-1,-1):
            #si on n'est pas à la 1ere ligne on peut inverser
            if i > 0:
                #si on a une case vide on inverse avec la valeur du dessus
                if plateau[i][j] == 0:
                    plateau[i][j] = plateau[i-1][j]
                    plateau[i-1][j] = 0
    
def DestructionCube(plateau, positionCouleurADetruire):
    for i in range(len(plateau)):
        for j in range(len(plateau)):
            #si dans le tableau positionCouleurADetruire on n'a pas de 0 alors c'est que c'est la position de la couleur a détruire
            if positionCouleurADetruire[i][j] != 0:
                plateau[i][j] = 0
    
    

def VerificationDestructionGauche(numLigne, numColonne, plateau, couleurADetruire, nombreDeCouleurAGauche, positionCouleurADetruire):
    if numColonne >= 0:    
        if plateau[numLigne][numColonne] == couleurADetruire:
            if positionCouleurADetruire[numLigne][numColonne]!= couleurADetruire:
                positionCouleurADetruire[numLigne][numColonne] = couleurADetruire
                nombreDeCouleurAGauche += 1
                if numColonne-1 >= 0:
                    #verification à gauche
                    nombreDeCouleurAGauche = VerificationDestructionGauche(numLigne, numColonne-1, plateau, couleurADetruire, nombreDeCouleurAGauche, positionCouleurADetruire)
                    #Plus vérification en haut
                    nombreDeCouleurAGauche += VerificationDestructionHaut(numLigne-1, numColonne, plateau, couleurADetruire, 0, positionCouleurADetruire)
                    #Plus vérification en bas
                    nombreDeCouleurAGauche += VerificationDestructionBas(numLigne+1, numColonne, plateau, couleurADetruire, 0, positionCouleurADetruire)
            
    return nombreDeCouleurAGauche

def VerificationDestructionBas(numLigne, numColonne, plateau, couleurADetruire, nombreDeCouleurEnBas, positionCouleurADetruire):
    if numLigne < len(plateau):
        if plateau[numLigne][numColonne] == couleurADetruire:
            if positionCouleurADetruire[numLigne][numColonne] != couleurADetruire:
                positionCouleurADetruire[numLigne][numColonne] = couleurADetruire
                nombreDeCouleurEnBas += 1
                if numLigne+1 < len(plateau):
                    #verification en bas
                    nombreDeCouleurEnBas = VerificationDestructionBas(numLigne+1, numColonne, plateau, couleurADetruire, nombreDeCouleurEnBas, positionCouleurADetruire)
                    #Plus verification a gauche
                    nombreDeCouleurEnBas += VerificationDestructionGauche(numLigne+1, numColonne, plateau, couleurADetruire, 0, positionCouleurADetruire)
                    #Plus verification à droite
                    nombreDeCouleurEnBas += VerificationDestructionDroite(numLigne, numColonne+1, plateau, couleurADetruire, 0, positionCouleurADetruire)
    
    return nombreDeCouleurEnBas

def VerificationDestructionHaut(numLigne, numColonne, plateau, couleurADetruire,nombreCouleurEnHaut,positionCouleurADetruire):
    if numLigne >= 0:
        if plateau[numLigne][numColonne] == couleurADetruire:
            if positionCouleurADetruire[numLigne][numColonne] != couleurADetruire:
                positionCouleurADetruire[numLigne][numColonne] = couleurADetruire
                nombreCouleurEnHaut += 1
                if numLigne-1 >= 0:#verification sur les bords
                    #verification en haut
                    nombreCouleurEnHaut = VerificationDestructionHaut(numLigne-1, numColonne, plateau, couleurADetruire, nombreCouleurEnHaut, positionCouleurADetruire)
                    #Plus verification a droite
                    nombreCouleurEnHaut += VerificationDestructionDroite(numLigne, numColonne+1, plateau, couleurADetruire, 0, positionCouleurADetruire)
                    #Plus verification a gauche
                    nombreCouleurEnHaut += VerificationDestructionGauche(numLigne, numColonne-1, plateau, couleurADetruire, 0, positionCouleurADetruire)
    
    return nombreCouleurEnHaut

def VerificationDestructionDroite(numLigne, numColonne,plateau,couleurADetruire,nombreCouleurADroite,positionCouleurADetruire):
    if numColonne < len(plateau):
        if plateau[numLigne][numColonne] == couleurADetruire:
            #si la position à regarder n'a pas déjà été fait alors on le fait
            if positionCouleurADetruire[numLigne][numColonne] != couleurADetruire:
                positionCouleurADetruire[numLigne][numColonne] = couleurADetruire
                nombreCouleurADroite += 1
                if numColonne+1 < len(plateau):#verification sur les bords
                    #verification a droire
                    nombreCouleurADroite = VerificationDestructionDroite(numLigne,numColonne+1,plateau,couleurADetruire,nombreCouleurADroite,positionCouleurADetruire)
                    #Plus vérification en haut
                    nombreCouleurADroite += VerificationDestructionHaut(numLigne-1, numColonne, plateau, couleurADetruire, 0, positionCouleurADetruire)
                    #Plus verification en bas
                    nombreCouleurADroite += VerificationDestructionBas(numLigne+1, numColonne, plateau, couleurADetruire, 0, positionCouleurADetruire)
            
    return nombreCouleurADroite

def VerificationDestruction(numLigne, numColonne,plateau,detruireSiPossible):
    #recuperation de la couleur a détruire
    couleurADetruire = plateau[numLigne][numColonne]
    
    #On recensera les positions des couleurs à détruire ici
    positionCouleurADetruire = [[0 for j in range(len(plateau))] for i in range(len(plateau))]
    #On recense la couleur à détruire
    positionCouleurADetruire[numLigne][numColonne] = couleurADetruire
    
    #permet de savoir si la destruction se fera ou non
    destructionOK = False
    nombreCouleurADetruire = 1 #1 car il y a la couleur sélectionner à prendre en compte
    
    if numColonne+1 < len(plateau):#verification sur les bords
        #On commence à regarder si à droite c'est la meme couleur
        nombreCouleurADetruire += VerificationDestructionDroite(numLigne,numColonne+1,plateau,couleurADetruire,0,positionCouleurADetruire)
    if numColonne-1 >= 0:
        #Puis à gauche
        nombreCouleurADetruire += VerificationDestructionGauche(numLigne, numColonne-1, plateau, couleurADetruire, 0, positionCouleurADetruire)
    if numLigne+1 < len(plateau):
        #En bas
        nombreCouleurADetruire += VerificationDestructionBas(numLigne+1, numColonne, plateau, couleurADetruire, 0, positionCouleurADetruire)
    if numLigne-1 >= 0:
        #Et enfin en haut
        nombreCouleurADetruire += VerificationDestructionHaut(numLigne-1, numColonne, plateau, couleurADetruire, 0, positionCouleurADetruire)
    
    #Si on trouve plus de 3 blocs de la même couleur collé et à détruire alors on peut détruire
    if nombreCouleurADetruire >= 3:
        destructionOK = True
    
    #Si on peut détruire et qu'on est dans une optique de destruction alors on détruit
    if destructionOK == True & detruireSiPossible == True:
        DestructionCube(plateau, positionCouleurADetruire)
        
    #On retourne le nombre de blocs a détruire pour l'utiliser sur le score plus tard
    return nombreCouleurADetruire

def PeutOnDetruire(nombreCouleurADetruire):
    destruction = False
    #Si on peut détruire plus de 3 blocs alors on dis que c'est vrai
    if nombreCouleurADetruire >= 3:
        destruction = True
    return destruction