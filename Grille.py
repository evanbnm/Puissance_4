"""
grille.py
---------
Classe pour gérer la logique du plateau de jeu Puissance 4.

Auteur : ChatGPT
Date : 2024-12-13
"""
class Grille:
    """
    Représente la grille du jeu Puissance 4.
    Permet de gérer les ajouts de jetons et de vérifier les conditions de victoire.
    """
    def __init__(self, lignes: int = 6, colonnes: int = 7):
        """
        Initialise une grille vide.
        
        :param lignes: Nombre de lignes de la grille.
        :param colonnes: Nombre de colonnes de la grille.
        """
        self.lignes = lignes
        self.colonnes = colonnes
        self.grille = [[0 for _ in range(colonnes)] for _ in range(lignes)]

    def ajouter_jeton(self, colonne: int, joueur: int) -> bool:
        """
        Ajoute un jeton dans une colonne donnée pour un joueur.

        :param colonne: Index de la colonne (0 à colonnes-1).
        :param joueur: Identifiant du joueur (1 ou 2).
        :return: True si le jeton a été ajouté, False si la colonne est pleine.
        """
        for ligne in range(self.lignes - 1, -1, -1):
            if self.grille[ligne][colonne] == 0:
                self.grille[ligne][colonne] = joueur
                return True
        return False

    def verifier_victoire(self, joueur: int) -> bool:
        """
        Vérifie si un joueur a gagné.

        :param joueur: Identifiant du joueur (1 ou 2).
        :return: True si le joueur a gagné, False sinon.
        """
        # Vérification horizontale
        for ligne in range(self.lignes):
            for col in range(self.colonnes - 3):
                if all(self.grille[ligne][col + i] == joueur for i in range(4)):
                    return True

        # Vérification verticale
        for col in range(self.colonnes):
            for ligne in range(self.lignes - 3):
                if all(self.grille[ligne + i][col] == joueur for i in range(4)):
                    return True

        # Vérification diagonale (haut-gauche vers bas-droit)
        for ligne in range(self.lignes - 3):
            for col in range(self.colonnes - 3):
                if all(self.grille[ligne + i][col + i] == joueur for i in range(4)):
                    return True

        # Vérification diagonale (haut-droit vers bas-gauche)
        for ligne in range(self.lignes - 3):
            for col in range(3, self.colonnes):
                if all(self.grille[ligne + i][col - i] == joueur for i in range(4)):
                    return True

        return False

    def est_pleine(self) -> bool:
        """
        Vérifie si la grille est pleine.

        :return: True si la grille est pleine, False sinon.
        """
        return all(self.grille[0][col] != 0 for col in range(self.colonnes))