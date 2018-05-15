'''
Created on 14 mai 2018

@author: hugo_
'''
#convertis un pleateau en string
from Generateur import Generation
def Plateau2Str(plateau):
    res=""
    for x in range(0, len(plateau)):
        for y in range(0, len(plateau[0])):
            res=res+str(plateau[x][y])
            if y != len(plateau[0])-1:
                res = res+":"
            
        res=res+"|"
    return res
#conversis un string en plateau
def Str2Plateau(chaine):
    plateau = chaine.split("|")
    for y in range(0, len(plateau)):
        plateau[y] = plateau[y].split(":")
    plateau2 = [[0 for j in range(len(plateau)-1)] for i in range(len(plateau)-1)]
    for x in range(0, len(plateau)-1):
        for y in range(0, len(plateau[0])):
            plateau2[x][y] = int(plateau[x][y])
    return plateau2