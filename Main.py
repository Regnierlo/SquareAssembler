'''import VueJeu
VueJeu'''
import Generateur
import GameEngine

def AffichePlateau(plateau):
    for i in range(0,tailleGrille):
        for j in range(0,tailleGrille):
            print(str(plateau[i][j]), end='', flush=True)
            if j < tailleGrille-1:
                print(" ",end='',flush=True)
        print("")

tailleGrille = 10
plateau = Generateur.Generation(tailleGrille)
AffichePlateau(plateau)
print("--")
i = int(input("Numéro ligne = "))-1
j = int(input("Numéro colonne = "))-1
GameEngine.VerificationDestruction(i,j, plateau)
