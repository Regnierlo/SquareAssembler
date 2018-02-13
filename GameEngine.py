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

def VerificationDestruction(numLigne, numColonne,plateau):
    #recuperation de la couleur a détruire
    couleurADetruire = plateau[numLigne][numColonne]
    print("Couleur à détruire : " + str(couleurADetruire))
    
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
        nombreCouleurADetruire += VerificationDestructionGauche(numLigne, numColonne-1, plateau, couleurADetruire, 0, positionCouleurADetruire)
    if numLigne+1 < len(plateau):
        nombreCouleurADetruire += VerificationDestructionBas(numLigne+1, numColonne, plateau, couleurADetruire, 0, positionCouleurADetruire)
    if numLigne-1 >= 0:
        nombreCouleurADetruire += VerificationDestructionHaut(numLigne-1, numColonne, plateau, couleurADetruire, 0, positionCouleurADetruire)
    
    if nombreCouleurADetruire >= 3:
        destructionOK = True
    
    print("Case(s) détruite(s) : " + str(nombreCouleurADetruire))
    
    if destructionOK == True:
        print("Destruction autorisée")
    else:
        print("Destruction non autorisée")