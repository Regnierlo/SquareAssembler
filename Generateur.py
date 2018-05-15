import random

import array

'''
    Retourne le nombre de couleurs présent sur le plateau
    
    @param plateau: Plateau qui va subir l'opération
    
    @return: Retourne le nombre de couleur présent sur le plateau
'''
def GetQuantiteCouleur(plateau):
    return NombreCouleur(len(plateau))

'''
    Définit la quantité de cube de couleur selon le nombre de couleur
    
    @param nbCouleur: Nombre de couleur présent sur le plateau
    
    @return: Retourne la quantité de cube par couleur
'''
def QuantiteCouleur(nbCouleur):
    if nbCouleur == 4:
        quantiteCouleur = 25
    else:#nbCouleur == 8
        quantiteCouleur = 50
    
    return quantiteCouleur

'''
    Définit le nombre de couleurs différentes selon la taille du plateau
    
    @param n: Taille du plateau (n*n)
    
    @return: Retourne le nombre de couleurs différentes
'''
def NombreCouleur(n):
    if n == 10:
        nbCouleur = 4
    else:#n == 20
        nbCouleur = 8
    
    return nbCouleur

'''
    Etablie une liste de tous les cubes des différentes couleurs à placer
    
    @param nbCouleur: Nombre de couleur différente
    @param quantiteCouleur: Quantité de cube voulu par couleur
    
    @return: Retourne la liste des cubes de couleurs
'''
def NumerotationCouleur(nbCouleur,quantiteCouleur):
    numCouleur = [quantiteCouleur]*nbCouleur #initialisation du tableau de taille "nbCouleur" à 0
    return numCouleur
    
'''
    Génère le plateau
    
    @param tailleGrille: Taille de la grille voulu (n*n)
    
    @return: Retourne le plateau généré
'''
def Generation(tailleGrille):
    nbCouleur = NombreCouleur(tailleGrille)#combien de couleurs differentes(+1 pour le 0 qui sera une zone vide
    quantiteCouleur = NumerotationCouleur(nbCouleur,QuantiteCouleur(nbCouleur))
    
    fineRandomColor =  False
    
    plateau = [[0 for j in range(tailleGrille)] for i in range(tailleGrille)]
    
    for i in range(0,tailleGrille):
        for j in range(0,tailleGrille):
            fineRandomColor = False
            
            while fineRandomColor == False:
                numCouleur = random.randint(1,nbCouleur)
                if  quantiteCouleur[numCouleur-1] > 0:#s'il reste cette couleur a placer
                    fineRandomColor = True
                    quantiteCouleur[numCouleur-1] -= 1
            
            plateau[i][j] = numCouleur
    
    return plateau