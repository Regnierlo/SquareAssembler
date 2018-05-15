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

def on_connection_change(agent,event):
    if event == IvyApplicationDisconnected :
        info("Ivy Application %r has disconected",agent)
    else:
        info("Ivy appliction % r has connected", agent)
    info("Ivy application currently on the bus %ss",','.join(IvyGetApplicationList()))
def on_die(agent,id):
    info("Reveived the order to die from %r with id = %d",agent,id)
    IvyStop()
     
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
    print(message)
    if patternConnectionEtablie.match(message):
        print("adversaire trouve")
        VueJeu.TrouveAdversaire()
    if patternPartageFirstPlateau.match(message):
        print("Plateau recut")
        VueJeu.MajPlateau(Str2Plateau(message.replace("[Partage First Plateau] : ","")))
        VueJeu.ModifRecPlat(True)
    if patternPartagePlateau.match(message):
        print("Plateau recut")
        VueJeu.MajPlateau(Str2Plateau(message.replace("[Partage Plateau] : ","")))
        VueJeu.AfficheCouleurDistant()
        sleep(.01)
        EnvoieMessage("[Debloque Plateau\]")
        sleep(0.1)
        VueJeu.ChangeCanPlay(True)
    if  patternUnlock.match(message):
        VueJeu.ChangeCanPlay(True)
    if patternLock.match(message):
        VueJeu.ChangeCanPlay(False)
        
    
def EnvoieMessage(msg):
    IvySendMsg(msg)
def NouvelleConnection(ip,pseudo):
    IvyInit(pseudo,"[Connection etablie] : "+pseudo,0,on_connection_change,on_die)
    #starting the bus
    print("l'ip est : "+ip)
    connection=ip+":2010"
    IvyStart(connection)
    IvyBindMsg(on_msg,  '(.*)')
    sleep(1)
def FinConnection():
    IvyStop()