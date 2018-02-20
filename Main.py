import VueJeu

import Generateur
import GameEngine

def AffichePlateau(plateau):
    tailleGrille = len(plateau)
    for i in range(0,tailleGrille):
        for j in range(0,tailleGrille):
            print(str(plateau[i][j]), end='', flush=True)
            if j < tailleGrille-1:
                print(" ",end='',flush=True)
        print("")

VueJeu
'''tailleGrille = 10
finJeu = False
nombreCouleurADetruire = 0
score  = 0
destructionSelection = False
plateau = Generateur.Generation(tailleGrille)

while finJeu == False:
    AffichePlateau(plateau)
    print("--")
    i = int(input("Numéro ligne = "))-1
    j = int(input("Numéro colonne = "))-1
    nombreCouleurADetruire = GameEngine.VerificationDestruction(i,j, plateau,True)
    destructionSelection = GameEngine.PeutOnDetruire(nombreCouleurADetruire)
    if destructionSelection == True:
        for i in range(tailleGrille):
            GameEngine.ReplacementDesCubes(plateau)
        finJeu = GameEngine.VerificationFinJeu(plateau)
        GameEngine.CalculScore()
    else:
        print("Impossible de détruire la sélection")
    
print("Votre score est de : " + str(score))'''