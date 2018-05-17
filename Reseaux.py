'''
Created on 13 mai 2018

@author: hugo_
'''
from ivy.std_api import *
from ivy.ivy import *
from time import sleep
import re
import VueJeu
from VueJeu import *
from Calcul import Str2Plateau
'''
Fonction d info si la connection a ivy a changee
'''
def on_connection_change(agent,event):
    if event == IvyApplicationDisconnected :
        info("Ivy Application %r has disconected",agent)
    else:
        info("Ivy appliction % r has connected", agent)
    info("Ivy application currently on the bus %ss",','.join(IvyGetApplicationList()))
    if(len(IvyGetApplicationList())>2):
        FinConnection()
'''
fonction d info si le client ivy est invite a mourir
'''
def on_die(agent,id):
    info("Reveived the order to die from %r with id = %d",agent,id)
    IvyStop()
'''
fonction appele a la reception d un message ivy
les differents messages sont traites avec des expressions regulieres
'''
def on_msg(agent, *arg):
    info("Received from %r : %s",agent, arg and str(arg) or '<no args>')
    message = str(arg)
    message = message.replace("(","")
    message = message.replace(")","")
    message = message.replace("\'","")
    patternConnectionEtablie = re.compile("^\[Connection etablie\]")
    patternPartageFirstPlateau = re.compile("^\[Partage First Plateau\]")
    patternPartagePlateau = re.compile("^\[Partage Plateau\]")
    patternUnlock = re.compile("^\[Debloque Plateau\]")
    patternLock = re.compile("^\[Bloque Plateau\]")
    patternFinPartie = re.compile("^\[Fin Partie\]")
    patternFinPartieRetour = re.compile("^\[Fin Partie Retour\]")
    patternDejaClique = re.compile("^\[Deja Clique\]")
    print(message)
    if patternConnectionEtablie.match(message):
        print("adversaire trouve")
        VueJeu.TrouveAdversaire()
    if patternPartageFirstPlateau.match(message):
        print("Plateau recut")
        VueJeu.MajPlateau(message.replace("[Partage First Plateau] : ",""))
        VueJeu.ModifRecPlat(True)
    if patternPartagePlateau.match(message):
        print("Plateau recut")
        VueJeu.MajPlateau(message.replace("[Partage Plateau] : ",""))
        VueJeu.AfficheCouleurDistant()
        EnvoieMessage("[Debloque Plateau]")
        sleep(0.1)
        VueJeu.ChangeCanPlay(True)
    if patternFinPartie.match(message):
        VueJeu.setScoreAd(int(message.replace("[Fin Partie] : ","").replace(",","")))
        VueJeu.EnvoieScoreIvy();
        VueJeu.AfficheFinJeuDistant();
        #VueJeu.RenvoieScore()
    if patternFinPartieRetour.match(message):
        VueJeu.setScoreAd(int(message.replace("[Fin Partie Retour] : ","").replace(",","")))
        VueJeu.AfficheFinJeuDistant();
        #VueJeu.RenvoieScore(int(message.replace("[Fin Partie] : ","").replace(",","")))
    if patternDejaClique.match(message):
        VueJeu.DejaClique()
    if patternUnlock.match(message):
        VueJeu.ChangeCanPlay(True)
    if patternLock.match(message):
        VueJeu.ChangeCanPlay(False)
        
'''
fonction d'envoie de message Ivy
'''
def EnvoieMessage(msg):
    IvySendMsg(msg)
'''
Initialisation de connection Ivy
'''
def NouvelleConnection(ip,pseudo):
    IvyInit(pseudo,"[Connection etablie] : "+pseudo,0,on_connection_change,on_die)
    #starting the bus
    print("l'ip est : "+ip)
    connection=ip+":2010"
    IvyStart(connection)
    IvyBindMsg(on_msg,  '(.*)')
    sleep(1)
'''
Fermeture de connection Ivy
'''
def FinConnection():
    IvyStop()