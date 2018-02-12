import random
from test.sortperf import flush

def QuantiteCouleur(nbCouleur):
    if nbCouleur == 4:
        quantiteCouleur = 25
    else:#nbCouleur == 8
        quantiteCouleur = 50
    
    return quantiteCouleur

def NombreCouleur(n):
    if n == 10:
        nbCouleur = 4
    else:#n == 20
        nbCouleur = 8
    
    return nbCouleur

def NumerotationCouleur(nbCouleur,quantiteCouleur):
    numCouleur = [quantiteCouleur]*nbCouleur #initialisation du tableau de taille "nbCouleur" à 0
    return numCouleur
    
def Generation(tailleGrille):
    nbCouleur = NombreCouleur(tailleGrille)+1#combien de couleurs differentes(+1 pour le 0 qui sera une zone vide
    quantiteCouleur = NumerotationCouleur(nbCouleur,QuantiteCouleur(nbCouleur))
    
    fineRandomColor =  False
    
    for i in range(0,tailleGrille):
        for j in range(0,tailleGrille):
            fineRandomColor = False
            
            while fineRandomColor == False:
                numCouleur = random.randint(1,nbCouleur-1)
                if  quantiteCouleur[numCouleur] > 0:#s'il reste cette couleur a placer
                    fineRandomColor = True
                    quantiteCouleur[numCouleur] -= 1
            
            print(str(numCouleur), end='', flush=True)
            if j < tailleGrille-1:
                print(" ",end='',flush=True)
        print("")
    
    