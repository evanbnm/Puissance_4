"""
interface.py
------------
Classe pour gérer l'interface graphique du jeu Puissance 4 avec Tkinter.

Auteur : ChatGPT
Date : 2024-12-13
"""

import tkinter as tk
from Grille import Grille

class Interface:
    """
    Classe pour l'interface graphique du jeu Puissance 4.
    """
    def __init__(self):
        """
        Initialise la fenêtre Tkinter et la grille de jeu.
        """
        self.fenetre = tk.Tk()
        self.fenetre.title("Puissance 4")
        
        self.grille = Grille()
        self.joueur_actuel = 1

        # Créer la grille d'affichage
        self.boutons = []
        for col in range(self.grille.colonnes):
            bouton = tk.Button(self.fenetre, text=f"↓", command=lambda c=col: self.jouer(c))
            bouton.grid(row=0, column=col)
            self.boutons.append(bouton)
        
        self.cases = []
        for ligne in range(self.grille.lignes):
            ligne_cases = []
            for col in range(self.grille.colonnes):
                label = tk.Label(self.fenetre, text=" ", width=5, height=2, bg="white", relief="ridge")
                label.grid(row=ligne + 1, column=col)
                ligne_cases.append(label)
            self.cases.append(ligne_cases)

        self.message = tk.Label(self.fenetre, text="Joueur 1 à vous de jouer", font=("Arial", 12))
        self.message.grid(row=self.grille.lignes + 1, column=0, columnspan=self.grille.colonnes)

    def jouer(self, colonne: int):
        """
        Gère le clic sur une colonne pour insérer un jeton.
        
        :param colonne: Index de la colonne cliquée.
        """
        if self.grille.ajouter_jeton(colonne, self.joueur_actuel):
            self.mettre_a_jour_grille()
            if self.grille.verifier_victoire(self.joueur_actuel):
                self.message.config(text=f"Joueur {self.joueur_actuel} a gagné !")
                self.desactiver_boutons()
            elif self.grille.est_pleine():
                self.message.config(text="Match nul !")
                self.desactiver_boutons()
            else:
                self.joueur_actuel = 3 - self.joueur_actuel
                self.message.config(text=f"Joueur {self.joueur_actuel}, à vous de jouer.")
        else:
            self.message.config(text=f"Colonne {colonne + 1} pleine. Choisissez une autre colonne.")

    def mettre_a_jour_grille(self):
        """
        Met à jour l'affichage de la grille.
        """
        for ligne in range(self.grille.lignes):
            for col in range(self.grille.colonnes):
                valeur = self.grille.grille[ligne][col]
                couleur = "white"
                if valeur == 1:
                    couleur = "red"
                elif valeur == 2:
                    couleur = "yellow"
                self.cases[ligne][col].config(bg=couleur)

    def desactiver_boutons(self):
        """
        Désactive tous les boutons de la grille.
        """
        for bouton in self.boutons:
            bouton.config(state="disabled")

    def demarrer(self):
        """
        Lance la boucle principale de Tkinter.
        """
        self.fenetre.mainloop()