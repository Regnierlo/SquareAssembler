#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import * 
import tkinter as Tk 
from tkinter import Toplevel,messagebox
import Generateur
from Main import AffichePlateau
from Reseaux import NouvelleConnection
from Reseaux import EnvoieMessage
import GameEngine
import socket
from Calcul import Plateau2Str
import Reseaux
from time import sleep
import Calcul
import queue

def FermetureFenetre(fenetre):
    fenetre.quit()
    fenetre.destroy() 
def GenerationGrille(tailleGrille,fenetre):
    global plateau 
    plateau = Generateur.Generation(tailleGrille)
    fenetre.quit()
    fenetre.destroy()
  
def NouvelleFenetre(multi,oldFenetre):
    fenetre = Toplevel()
    label = Label(fenetre,text="Taille de la grille")
    label.pack()
    if (multi):#multi a true donc hebergement partie multijoueur
        FermetureFenetre(oldFenetre)
        button10 = Tk.Button(fenetre,text="10x10",command=lambda:WaitConnection(10,fenetre))
        button10.pack(side = LEFT)
        button20 = Button(fenetre,text="20x20",command=lambda:WaitConnection(20,fenetre))
        button20.pack(side = RIGHT)
    else:#multi a false donc partie solo
        button10 = Tk.Button(fenetre,text="10x10",command=lambda:GenerationGrille(10,fenetre))
        button10.pack(side = LEFT)
        button20 = Button(fenetre,text="20x20",command=lambda:GenerationGrille(20,fenetre))
        button20.pack(side = RIGHT)
    
    fenetre.mainloop()
    
    
def WaitConnection(taille,oldFenetre):
    FermetureFenetre(oldFenetre)
    fenetre = Toplevel()
    
    label = Label(fenetre,text="En attente d'un adversaire")
    label.pack()
    buttonCancel = Tk.Button(fenetre,text="Cancel", command=lambda:FermetureFenetre(fenetre))
    buttonCancel.pack()
    #on recupere l'adresse ip locale
    ipLocal = socket.gethostbyname(socket.gethostname())
    #on creer une connection sur l'ip locale
    NouvelleConnection(ipLocal, pseudo)
    while adversaireTrouve == False:
        fenetre.update_idletasks()
        fenetre.update()
    GenerationGrille(taille,fenetre)
    EnvoieMessage("[Partage First Plateau] : "+Plateau2Str(plateau))
    ChangeCanPlay(False)
    global multiplayer
    multiplayer = True
    LancementJeuMulti();
    #fenetre.quit()
    #fenetre.destroy()
def ChangeCanPlay(bol):
    global canPlay
    canPlay=bol
def TrouveAdversaire():
    global adversaireTrouve
    adversaireTrouve = True
    print("advairesaire trouvé et changé")
def MajPlateau(nouvPlateau):
    global plateau
    plateau = nouvPlateau

def FenetreMulti():
    fenetre = Toplevel()
    label = Label(fenetre,text="Choix de action")
    label.pack()
    buttonHeb = Tk.Button(fenetre,text="Héberger",command=lambda:NouvelleFenetre(True,fenetre))
    buttonHeb.pack(side = LEFT)
    
    buttonRej = Button(fenetre,text="Rejoindre",command=lambda:fenetreReseaux(fenetre))
    buttonRej.pack(side = RIGHT)
    
    fenetre.mainloop()
    
def fenetreReseaux(oldFenetre):
    FermetureFenetre(oldFenetre)
    fenetre = Toplevel()
    label = Label(fenetre,text="Entrez l'IP de l'hebergeur")
    label.pack()
    textAreaIP = Text(fenetre, height=1, width=15)
    textAreaIP.pack()
    textAreaIP.insert(END, "IP")
    buttonRej = Button(fenetre,text="Rejoindre",command=lambda:NouvelleConnection(textAreaIP.get("1.0",END),pseudo))
    buttonRej.pack()
    ChangeCanPlay(False)
    global multiplayer
    multiplayer = True
    while plateauRecut == False:
        fenetre.update_idletasks()
        fenetre.update()
    LancementJeuMulti();
def Pseudo():
    fenetre = Toplevel()
    label = Label(fenetre,text="Entrez votre pseudo")
    label.pack()
    textAreaPseudo = Text(fenetre, height=1, width=15)
    textAreaPseudo.pack()
    textAreaPseudo.insert(END, "pseudo")
    buttonRej = Button(fenetre,text="Accepter",command=lambda:ModifierPseudo(textAreaPseudo.get("1.0",END), fenetre))
    buttonRej.pack()
    fenetre.mainloop()
    
def ModifRecPlat(bol):
    global plateauRecut
    plateauRecut = bol
    Reseaux.EnvoieMessage("[Debloque Plateau]"+pseudo)
    sleep(0.1)
    ChangeCanPlay(True)
    
def ModifierPseudo(nouvPseudo,oldFenetre):
    global pseudo
    pseudo=nouvPseudo
    oldFenetre.quit()
    oldFenetre.destroy()
    
def Nouveau(root):
    NouvelleFenetre(False,None)
    global canPlay
    canPlay=True
    global multiplayer
    multiplayer = False
    size = len(plateau[0])
    
    # dimensions du canevas
    can_width = 50*size
    can_height = 50*size
     
    # création canevas
    global can
    global score
    
    can = Tk.Canvas(root, width=can_width, height=can_height)
    can.grid(row=0,column=0)
    
    if nbClic >= 2:
        can.destroy()
    
    score = 0
    can.grid()
    can.bind("<Button-1>", joue)
    
    scoreMessage = Label(root,text="0")
    scoreMessage.config(font=('courier', 15, 'bold'))
    scoreMessage.grid(row=0,column=1)
    
    AfficheCouleur(plateau,tailleCase)

def NouveauMulti(root):
    if pseudo == "":
        Pseudo()
    
    FenetreMulti()
   
def LancementJeuMulti():
    size = len(plateau[0])
    # dimensions du canevas
    can_width = 50*size
    can_height = 50*size
     
    # création canevas
    global can
    global score
    
    can = Tk.Canvas(root, width=can_width, height=can_height)
    can.grid(row=0,column=0)
    
    if nbClic >= 2:
        can.destroy()
    
    score = 0
    can.grid()
    can.bind("<Button-1>", joue)
    
    scoreMessage = Label(root,text="0")
    scoreMessage.config(font=('courier', 15, 'bold'))
    scoreMessage.grid(row=0,column=1)
    periodicCall()
    AfficheCouleur(plateau,tailleCase)

def Rejouer():
    can.delete(ALL)
    
def joue(evt):
    if canPlay == True:
        global score
        pos_y = int(evt.x / tailleCase)
        pos_x = int(evt.y / tailleCase)
        
        finJeu = True
        
        nombreCouleurADetruire = GameEngine.VerificationDestruction(pos_x, pos_y, plateau, True)
        destructionSelection = GameEngine.PeutOnDetruire(nombreCouleurADetruire)
        if destructionSelection == True:
            #Si on est on mode multiplayer, les deux joueur ont le plateau bloqué
            if multiplayer == True:
                ChangeCanPlay(False)
                Reseaux.EnvoieMessage("[Bloque Plateau] : "+pseudo)
            tailleGrille = len(plateau)
            for i in range(tailleGrille):
                GameEngine.ReplacementDesCubes(plateau)
            for i in range(tailleGrille):
                GameEngine.ReplacementDesCubesHorizontal(plateau)
            score = GameEngine.CalculScore(score,nombreCouleurADetruire)
            #Changement dynamique du score --------------------------------------------------------
            scoreMessage = Label(root,text=score)
            scoreMessage.config(font=('courier', 15, 'bold'))
            scoreMessage.grid(row=0,column=1)
            finJeu = GameEngine.VerificationFinJeu(plateau)
            
    
        else:
            print("Impossible de détruire la sélection")
            print("i = " + str(pos_x))
            print("j = " + str(pos_y))
        
        AffichePlateau(plateau)
        print("------")
        AfficheCouleur(plateau, tailleCase)
        
        if finJeu == True:
            finJeu = GameEngine.VerificationFinJeu(plateau)
            if finJeu == True:
                FinDuJeu(score)
        Reseaux.EnvoieMessage("[Partage Plateau] : "+Plateau2Str(plateau))
                
def FinDuJeu(score):
        reponse = messagebox.askokcancel("Fin du jeu !","Votre score est de " + str(score) + ".\nVoulez-vous recommencer ?")
        Rejouer()
def AfficheCouleurDistant():
    listeAttente.put("affiche")
    AffichePlateau(plateau)
    #http://code.activestate.com/recipes/82965/
def processIncoming():
    """
    Handle all the messages currently in the queue (if any).
    """
    print("incoming")
    while listeAttente.qsize():
        print("incoming")
        try:
            msg = listeAttente.get(0)
            if msg == "affiche":
                AfficheCouleur(plateau, tailleCase)
        except listeAttente.Empty:
            pass
def periodicCall():
        """
        Check every 100 ms if there is something new in the queue.
        """
        print("on passe")
        processIncoming()
        #sleep(1)
        #periodicCall()
        root.after(1000, periodicCall)
def AfficheCouleur(plateau, tailleCase):
    
    nbCouleur = Generateur.GetQuantiteCouleur(plateau)
    listeCouleur = GenerationCouleur(nbCouleur)
    size = len(plateau[0])
    
    for i in range(size):
        for j in range(size):
            can.create_rectangle(j*tailleCase, i*tailleCase,
                                 j*tailleCase+tailleCase, i*tailleCase+tailleCase,
                                fill = listeCouleur[plateau[i][j]])



def GenerationCouleur(nbCouleur):
    listeTotaleCouleur = ['White','Red','Blue','Green','Orange','Pink','Yellow','Purple','Brown']
    listeCouleur = listeTotaleCouleur[0:nbCouleur+1]
    return listeCouleur

def Cliquer():
    global nbClic
    nbClic += 1

root = Tk.Tk()   ## Fenêtre principale 

# taille d'une "case"
tailleCase = 50

nbClic = 0

mainmenu = Tk.Menu(root)   

menuNouveau = Tk.Menu(mainmenu)  
menuNouveau.add_command(label="Nouveau", command=lambda:Nouveau(root))  # Ajout d'une option au menu fils menuFile 
menuNouveau.add_command(label="Multijoueur", command=lambda:NouveauMulti(root)) 
menuNouveau.add_command(label="Quitter", command=root.quit) 
  
menuAProposDe = Tk.Menu(mainmenu) 
menuAProposDe.add_command(label="17820048")
menuAProposDe.add_command(label="17820037")
menuAProposDe.add_command(label="17820028")

  
mainmenu.add_cascade(label = "Nouveau", menu=menuNouveau) 
mainmenu.add_cascade(label = "A propos de", menu=menuAProposDe) 
  
root.config(menu = mainmenu) 
pseudo = ""
adversaireTrouve = False
plateauRecut = False
canPlay = False
multiplayer = False
listeAttente = queue.Queue()
root.mainloop()