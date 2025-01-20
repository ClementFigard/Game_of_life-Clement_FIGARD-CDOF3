# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:09:11 2025

@author: Clément
"""
import time
import os

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
jeu[0][7]="#"
jeu[1][8]="#"
jeu[2][8]="#"
jeu[2][7]="#"
jeu[2][6]="#"

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
        nb+=13
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

def saveGame(jeu):
    save = input("Do you want to save the final state of the game? (yes/no): ").strip().lower()
    if save == "yes":
        # Determine the directory of the script or fallback to the current working directory
        script_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
        directory = os.path.join(script_dir, "SavedGames")

        # Create the "Saved Games" folder if it doesn't exist
        if not os.path.exists(directory):
            os.makedirs(directory)  # Create the folder if it doesn't exist

        # Ask for the file name
        filename = input("Enter the name of the save file (without extension): ").strip()
        if not filename:
            print("Invalid filename. Save aborted.")
            return

        try:
            # Construct the full path to the save file
            filepath = os.path.join(directory, f"{filename}.txt")
            with open(filepath, "w", encoding="utf-8") as file:
                for row in jeu:
                    file.write(" ".join(row) + "\n")
            print(f"Game saved successfully to: {filepath}")
        except Exception as e:
            print(f"Error saving the game: {e}")



nb_tour = int(input("Veillez entrer le nombre de tour du jeu : "))
Affichage(jeu)
while(nb_tour>0):
    time.sleep(0.7)
    print('\n' * 50)
    predict(jeu)
    nextEtat(jeu)
    Affichage(jeu)
    nb_tour-=1

print("FIN DU JEU !!!")
saveGame(jeu)
