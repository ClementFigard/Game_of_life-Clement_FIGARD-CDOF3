# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:09:11 2025

@author: Clément
"""
import time



long = 21
larg = 21
next_mort = []
next_vivant = []

jeu = [ [ "-" for i in range(long) ] for i in range(larg)]
jeu[13][12]="#"
jeu[14][12]="#"
jeu[15][12]="#"
jeu[14][11]="#"
jeu[15][11]="#"
jeu[16][11]="#"

def Affichage(m):
    s=""
    for i in range(len(m)):
        for j in range(len(m[0])):
            s += str(m[i][j])+" "
        s += "\n"
    print(s)
    
def nbVoisin(l,c):
    nb=0
    if (jeu[(l-1)%larg][c]=="#") :
        nb+=1
    if (jeu[(l-1)%larg][(c+1)%long]=="#") :
        nb+=1    
    if (jeu[l][(c+1)%long]=="#") :
        nb+=1
    if (jeu[(l+1)%larg][(c+1)%long]=="#") :
        nb+=1
    if (jeu[(l+1)%larg][c]=="#") :
        nb+=1
    if (jeu[(l+1)%larg][(c-1)%long]=="#") :
        nb+=1
    if (jeu[(l)][(c-1)%long]=="#") :
        nb+=1        
    if (jeu[(l-1)%larg][(c-1)%long]=="#") :
        nb+=1
    return nb
        
def predict(jeu):
    for i in range(len(jeu)):
        for j in range(len(jeu[0])):
            if (jeu[i][j]=="-" and nbVoisin(i,j)==3) :
                next_vivant.append((i,j))
            if (jeu[i][j]=="#" and nbVoisin(i,j)!=2 and nbVoisin(i,j)!=3) :
                next_mort.append((i,j))

def nextEtat(jeu):
    for (i,j) in next_vivant :
        jeu[i][j]="#"
    for (i,j) in next_mort :
        jeu[i][j]="-"
    next_vivant.clear()
    next_mort.clear()
    

    

nb_tour = int(input("Veillez entrer le nombre de tour du jeu : "))
Affichage(jeu)
while(nb_tour>0):
    time.sleep(1)
    print('\n' * 50)
    predict(jeu)
    nextEtat(jeu)
    Affichage(jeu)
    nb_tour-=1
    
print("FIN DU JEU !!!")
      