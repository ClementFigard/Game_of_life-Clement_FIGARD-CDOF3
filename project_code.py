# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:09:11 2025

@author: Clément
"""

import time
import os

# Dimensions of the game grid
long = 21  # Number of columns
larg = 21  # Number of rows

# Lists to keep track of cells that will change state in the next generation
next_mort = []   # Cells that will die
next_vivant = [] # Cells that will become alive

# Initialize the game grid with "-" representing dead cells
jeu = [["-" for i in range(long)] for i in range(larg)]

# Define the initial pattern of live cells on the grid
jeu[13][12] = "#"
jeu[14][12] = "#"
jeu[15][12] = "#"
jeu[14][11] = "#"
jeu[15][11] = "#"
jeu[16][11] = "#"
jeu[0][7] = "#"
jeu[1][8] = "#"
jeu[2][8] = "#"
jeu[2][7] = "#"
jeu[2][6] = "#"

# Function to display the current state of the grid
def Affichage(m):
    s = ""
    for i in range(len(m)):
        for j in range(len(m[0])):
            s += str(m[i][j]) + " "
        s += "\n"
    print(s)

# Function to count the number of live neighbors for a given cell
def nbVoisin(l, c):
    nb = 0
    # Check all 8 neighboring cells (using modular arithmetic for wrapping)
    if jeu[(l-1) % larg][c] == "#":  # Top neighbor
        nb += 1
    if jeu[(l-1) % larg][(c+1) % long] == "#":  # Top-right neighbor
        nb += 1
    if jeu[l][(c+1) % long] == "#":  # Right neighbor
        nb += 1
    if jeu[(l+1) % larg][(c+1) % long] == "#":  # Bottom-right neighbor
        nb += 1
    if jeu[(l+1) % larg][c] == "#":  # Bottom neighbor
        nb += 1
    if jeu[(l+1) % larg][(c-1) % long] == "#":  # Bottom-left neighbor
        nb += 1
    if jeu[l][(c-1) % long] == "#":  # Left neighbor
        nb += 1
    if jeu[(l-1) % larg][(c-1) % long] == "#":  # Top-left neighbor
        nb += 1
    return nb

# Function to predict changes in the game grid based on the rules of the game
def predict(jeu):
    for i in range(len(jeu)):
        for j in range(len(jeu[0])):
            # Rule for a cell to become alive
            if jeu[i][j] == "-" and nbVoisin(i, j) == 3:
                next_vivant.append((i, j))
            # Rule for a live cell to die
            if jeu[i][j] == "#" and nbVoisin(i, j) not in (2, 3):
                next_mort.append((i, j))

# Function to apply the predicted changes and update the game grid
def nextEtat(jeu):
    for (i, j) in next_vivant:
        jeu[i][j] = "#"  # Cell becomes alive
    for (i, j) in next_mort:
        jeu[i][j] = "-"  # Cell dies
    next_vivant.clear()  # Clear the list for the next iteration
    next_mort.clear()

# Function to save the current state of the game grid to a file
def saveGame(jeu):
    save = input("Do you want to save the final state of the game? (yes/no): ").strip().lower()
    if save == "yes":
        # Determine the directory of the script or fallback to the current working directory
        script_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
        directory = os.path.join(script_dir, "SavedGames")

        # Create the "Saved Games" folder if it doesn't exist
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Ask for the file name
        filename = input("Enter the name of the save file (without extension): ").strip()
        if not filename:
            print("Invalid filename. Save aborted.")
            return

        try:
            # Write the game grid to the file
            filepath = os.path.join(directory, f"{filename}.txt")
            with open(filepath, "w", encoding="utf-8") as file:
                for row in jeu:
                    file.write(" ".join(row) + "\n")
            print(f"Game saved successfully to: {filepath}")
        except Exception as e:
            print(f"Error saving the game: {e}")

# Main game loop
nb_tour = -1  # Initialize with an invalid value
while nb_tour < 0:
    try:
        nb_tour = int(input("Veuillez entrer le nombre de tours du jeu (valeur positive) : "))  # Number of generations
        if nb_tour < 0:
            print("Le nombre de tours ne peut pas être négatif. Veuillez réessayer.")
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")

Affichage(jeu)  # Display the initial state of the grid
while nb_tour > 0:
    time.sleep(0.7)  # Pause for better visualization
    print('\n' * 50)  # Clear the console output
    predict(jeu)  # Predict the changes
    nextEtat(jeu)  # Apply the changes
    Affichage(jeu)  # Display the updated grid
    nb_tour -= 1

print("FIN DU JEU !!!")  # End of the game
saveGame(jeu)  # Prompt to save the final state of the game
