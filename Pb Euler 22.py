# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 15:35:08 2018

@author: moreau123u
"""

def extraction(nomdefichier):
    """ Return the clear list of names"""
    fichier = open(nomdefichier+'.txt','r')
    Lignes = []
    for ligne in fichier:
        Lignes.append(ligne)
    NomsBis=Lignes[0].split(',')
    Noms =[]
    for nom in NomsBis:
        Noms.append(nom[1:len(nom)-1])
        Noms.sort()
    return Noms



def score(nom):
    """ Return the score of one single name"""
    
    alphabet = []
    for letter in range(65, 91):
        alphabet.append(chr(letter))
    worth=0
    for c in nom:
        worth+=alphabet.index(c)+1
    return worth*(Noms.index(nom)+1)




def solve(nomfichier):
    """Solve the 22th EUler problem
        Return th sum of all names scores"""
    Noms = extraction(nomfichier)
    somme=0
    for nom in Noms:
        somme+=score(nom)
    return somme


Noms=extraction('p022_names')
assert(score('COLIN')==49714)

print(solve('p022_names'))
