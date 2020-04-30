from os import listdir #importation bibliothèque lecture fichier et répertoire
import os
import math

#creer la classe indexe inversée
class IndexInverse:
    """constructeur de la classe index_inverse"""                   #méthode documenté >>>> utiliser help(NomClasse)
    #séquence de mots et nombre d'url où apparait les mots
    def __init__(self, mot, nbUrl, page): #Notre méthode constructeur     #index = IndexInverse("lipn",6,"cheminpage")
        self.m = mot                                                      #index.mot >>> 'lipn'
        self.nbU = nbUrl                                                  #index.nbUrl >>> 6
        self.page = page
