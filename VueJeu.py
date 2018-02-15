#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import * 
import tkinter as Tk 
from tkinter import messagebox, Toplevel
import Generateur
from Main import AffichePlateau

  
def GenerationGrille(tailleGrille):
    global plateautmp
    plateautmp = Generateur.Generation(tailleGrille)
    AffichePlateau(plateautmp)
    return plateautmp
  

  
def Nouveau():
    #rep = messagebox.askquestion("Nouveau jeu", "Voulez-vous créez un jeu de 10x10 ? (Si non, alors un jeu de 20x20 sera crée")
    fenetre = Toplevel()
    
    label = Label(fenetre,text="Taille de la grille")
    label.pack()
    
    button10 = Tk.Button(fenetre,text="10x10",command=lambda:GenerationGrille(10))
    button10.pack(side = LEFT)
    
    button20 = Button(fenetre,text="20x20",command=lambda:GenerationGrille(20))
    button20.pack(side = RIGHT)
    
    fenetre.mainloop()
    
    plateau = plateautmp
    AffichePlateau(plateau)
    
  







root = Tk.Tk()   ## Fenêtre principale 

mainmenu = Tk.Menu(root)   

menuNouveau = Tk.Menu(mainmenu)  
menuNouveau.add_command(label="Nouveau", command=Nouveau)  ## Ajout d'une option au menu fils menuFile 
menuNouveau.add_command(label="Quitter", command=root.quit) 
  
menuAProposDe = Tk.Menu(mainmenu) 
menuAProposDe.add_command(label="17820048")
menuAProposDe.add_command(label="17820037") 
  
mainmenu.add_cascade(label = "Nouveau", menu=menuNouveau) 
mainmenu.add_cascade(label = "A propos de", menu=menuAProposDe) 
  
root.config(menu = mainmenu) 
  
root.mainloop()