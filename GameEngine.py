'''
    Calcul le score en fonction du nombre de couleur détruite
    
    @param score: Score actuel
    @param nombreCouleurADetruire: Nombre additionné au score actuel
    
    @return: Le nouveau score
'''
def CalculScore(score,nombreCouleurADetruire):
    score+=nombreCouleurADetruire   
    return score


'''
    Vérifie le plateau pour savoir si une combinaison est encore possible.

    @param plateau: plateau du jeu
    @return: True si aucune combinaison est possible (donc fin du jeu) False sinon
'''
def VerificationFinJeu(plateau):
    nombreCouleurPouvantEtreDetruit = 0
    i = 0
    j = 0
    tailleGrille = len(plateau)
    finVerification = False
    #tant que le tableau n'est pas entierrement parcouru ou qu'on n'a pas trouvé une combinaison d'au moins 3 blocs on continue
    while finVerification == False:
        #on récupère le nombre de bloc pouvant etre détruit
        nombreCouleurPouvantEtreDetruit = VerificationDestruction(i, j, plateau,False)
        
        #on avance dans le tableau
        j += 1
        if j >= tailleGrille:
            j = 0
            i += 1
            
        if nombreCouleurPouvantEtreDetruit >= 3:
            finVerification = True
        elif i >= tailleGrille:
            finVerification = True
    
    #on regarde si on peut détruire les blocs
    fin = PeutOnDetruire(nombreCouleurPouvantEtreDetruit)
    
    #si on peut détruire c'est que ce n'est pas encore la fin du jeu
    if fin == True:
        fin = False
    else: #si on ne peut pas détruire c'est que c'est la fin du jeu
        fin = True
    
    return fin
    
'''
    Effectue un replacement des cubes horizontaux
    
    @param plateau: Plateau qui subira les modifications 
'''
def ReplacementDesCubesHorizontal(plateau):
    size = len(plateau)-1
    for i in range(size+1):
        if plateau[size][i] == 0:
            for j in range(size+1):
                if i+1 <= size:
                    plateau[j][i] = plateau[j][i+1]
                    plateau[j][i+1] = 0
    
'''
    Intervertie les cubes détruits pour les replacer
    
    @param plateau: Plateau qui subira les modifcations 
'''
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
  
'''
    Detruit les cubes du plateau grâce au tableau indiquant lesquels il faut détruire
    
    @param plateau: Plateau qui fera ses cubes détruires
    @param positionCouleurADetruire: Tableau avec les positions des cubes à détruires
'''  
def DestructionCube(plateau, positionCouleurADetruire):
    for i in range(len(plateau)):
        for j in range(len(plateau)):
            #si dans le tableau positionCouleurADetruire on n'a pas de 0 alors c'est que c'est la position de la couleur a détruire
            if positionCouleurADetruire[i][j] != 0:
                plateau[i][j] = 0
    
'''
    Vérifie si le cube est à détruire, si oui, on l'ajoute au nombreDeCouleurAGauche  
    
    @param numLigne: Numéro de la ligne à vérifier
    @param numColonne: Numéro de la colonne à vérifier
    @param plateau: Plateau où l'action sera effectuée
    @param couleurADetruire: Couleur à détruire permettant d'effectuer la conparaison
    @param nombreDeCouleurAGauche: Nombre de couleur à détruire déjà reconnu sur la gauche
    @param positionCouleurADetruire: Tableau permettant de recenser les cubes à détruire
    
    @return Retourne le nombre de couleur à détruire
'''
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

'''
    Vérifie si le cube est à détruire, si oui, on l'ajoute au nombreDeCouleurEnBas  
    
    @param numLigne: Numéro de la ligne à vérifier
    @param numColonne: Numéro de la colonne à vérifier
    @param plateau: Plateau où l'action sera effectuée
    @param couleurADetruire: Couleur à détruire permettant d'effectuer la conparaison
    @param nombreDeCouleurEnBas: Nombre de couleur à détruire déjà reconnu sur le bas
    @param positionCouleurADetruire: Tableau permettant de recenser les cubes à détruire
    
    @return Retourne le nombre de couleur à détruire
'''
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

'''
    Vérifie si le cube est à détruire, si oui, on l'ajoute au nombreCouleurEnHaut  
    
    @param numLigne: Numéro de la ligne à vérifier
    @param numColonne: Numéro de la colonne à vérifier
    @param plateau: Plateau où l'action sera effectuée
    @param couleurADetruire: Couleur à détruire permettant d'effectuer la conparaison
    @param nombreCouleurEnHaut: Nombre de couleur à détruire déjà reconnu sur le haut
    @param positionCouleurADetruire: Tableau permettant de recenser les cubes à détruire
    
    @return Retourne le nombre de couleur à détruire
'''
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

'''
    Vérifie si le cube est à détruire, si oui, on l'ajoute au nombreCouleurADroite  
    
    @param numLigne: Numéro de la ligne à vérifier
    @param numColonne: Numéro de la colonne à vérifier
    @param plateau: Plateau où l'action sera effectuée
    @param couleurADetruire: Couleur à détruire permettant d'effectuer la conparaison
    @param nombreCouleurADroite: Nombre de couleur à détruire déjà reconnu sur la droite
    @param positionCouleurADetruire: Tableau permettant de recenser les cubes à détruire
    
    @return Retourne le nombre de couleur à détruire
'''
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

'''
    Verifie si la couleur sélectionnée peut être détruite en vérifiant ses voisins
    
    @param numLigne: Numéro de la ligne sélectionnée
    @param numColonne: Numéro de la colonne sélectionnée
    @param plateau: Plateau où la vérification se fera
    @param detruireSiPossible: Boolean pour savoir si on doit détruire si possible

    @return: Le nombre de couleur à détruire
'''
def VerificationDestruction(numLigne, numColonne,plateau,detruireSiPossible):
    nombreCouleurADetruire = 1 #1 car il y a la couleur sélectionner à prendre en compte

    #recuperation de la couleur a détruire
    couleurADetruire = plateau[numLigne][numColonne]
    
    #On recensera les positions des couleurs à détruire ici
    positionCouleurADetruire = [[0 for j in range(len(plateau))] for i in range(len(plateau))]
    #On recense la couleur à détruire
    positionCouleurADetruire[numLigne][numColonne] = couleurADetruire
    
    #permet de savoir si la destruction se fera ou non
    destructionOK = False
    
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

'''
    Vérifie si c'est possible de détruire les blocs
    
    @param nombreCouleurADetruire: Nombre de couleur à détruire
    
    @return: True si la destruction est autorisé, False sinon
'''
def PeutOnDetruire(nombreCouleurADetruire):
    destruction = False
    #Si on peut détruire plus de 3 blocs alors on dis que c'est vrai
    if nombreCouleurADetruire >= 3:
        destruction = True
    return destruction