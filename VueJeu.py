#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import * 
import tkinter as Tk 
from tkinter import messagebox, Toplevel
import Generateur
from Main import AffichePlateau
import GameEngine

  
def GenerationGrille(tailleGrille,fenetre):
    global plateau 
    plateau = Generateur.Generation(tailleGrille)
    fenetre.quit()
    fenetre.destroy()
  
def NouvelleFenetre():
    #rep = messagebox.askquestion("Nouveau jeu", "Voulez-vous créez un jeu de 10x10 ? (Si non, alors un jeu de 20x20 sera crée")
    fenetre = Toplevel()
    
    label = Label(fenetre,text="Taille de la grille")
    label.pack()
    
    button10 = Tk.Button(fenetre,text="10x10",command=lambda:GenerationGrille(10,fenetre))
    button10.pack(side = LEFT)
    
    button20 = Button(fenetre,text="20x20",command=lambda:GenerationGrille(20,fenetre))
    button20.pack(side = RIGHT)
    
    fenetre.mainloop()
    
    
def Nouveau(root):
    NouvelleFenetre()
    size = len(plateau[0])
    
    # dimensions du canevas
    can_width = 50*size
    can_height = 50*size
     
    # création canevas
    global can
    can = Tk.Canvas(root, width=can_width, height=can_height)
    can.grid()
    can.bind("<Button-1>", joue)
    
    AfficheCouleur(plateau,tailleCase)
    
def joue(evt):
    pos_y = int(evt.x / tailleCase)
    pos_x = int(evt.y / tailleCase)
    
    nombreCouleurADetruire = GameEngine.VerificationDestruction(pos_x, pos_y, plateau, True)
    destructionSelection = GameEngine.PeutOnDetruire(nombreCouleurADetruire)
    if destructionSelection == True:
        tailleGrille = len(plateau)
        for i in range(tailleGrille):
            GameEngine.ReplacementDesCubes(plateau)
        finJeu = GameEngine.VerificationFinJeu(plateau)
        GameEngine.CalculScore()
    else:
        print("Impossible de détruire la sélection")
    
    AffichePlateau(plateau)
    AfficheCouleur(plateau, tailleCase)

def AfficheCouleur(plateau, tailleCase):
    
    nbCouleur = Generateur.GetQuantiteCouleur(plateau)
    listeCouleur = GenerationCouleur(nbCouleur)
    size = len(plateau[0])
    
    for i in range(size):
        for j in range(size):
            can.create_rectangle(j*tailleCase, i*tailleCase,
                                 j*tailleCase+tailleCase, i*tailleCase+tailleCase,
                                fill = listeCouleur[plateau[i][j]])
    
    AffichePlateau(plateau)



def GenerationCouleur(nbCouleur):
    listeTotaleCouleur = ['White','Red','Blue','Green','Pink','Orange','Yellow','Purple','Brown']
    listeCouleur = listeTotaleCouleur[0:nbCouleur+1]
    return listeCouleur

root = Tk.Tk()   ## Fenêtre principale 

# taille d'une "case"
tailleCase = 50

finJeu = False

mainmenu = Tk.Menu(root)   

menuNouveau = Tk.Menu(mainmenu)  
menuNouveau.add_command(label="Nouveau", command=lambda:Nouveau(root))  ## Ajout d'une option au menu fils menuFile 
menuNouveau.add_command(label="Quitter", command=root.quit) 
  
menuAProposDe = Tk.Menu(mainmenu) 
menuAProposDe.add_command(label="17820048")
menuAProposDe.add_command(label="17820037") 
  
mainmenu.add_cascade(label = "Nouveau", menu=menuNouveau) 
mainmenu.add_cascade(label = "A propos de", menu=menuAProposDe) 
  
root.config(menu = mainmenu) 

root.mainloop()