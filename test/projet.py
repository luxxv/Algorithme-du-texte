from os import listdir #importation bibliothèque lecture fichier et répertoire
import os
import math
import indexe_inverse
# Charger les documents dans l'index
# La méthode doit parcourir les documents d'un répertoire passer en entrée.
# Charger tous les fichiers que le répertoire contient, quel que soit le mode d'encodage du fichier.
monRepertoire = "./pages_web/"
fichiers = [f for f in listdir(monRepertoire)] # les fichiers du répertoire sont chargés
# print(fichiers) #L'affichage est optionnel
list = os.listdir(monRepertoire) # création d'une liste chargeant les fichiers du répertoire
number_files = len(list) # fonction len qui va retourner un entier qui sera la longueur de la liste
print("vérif chargement",number_files) #affichage

#Les fonction capables de calculer les variantes d'un TF-IDF
#TERM FREQUENCY TF = nb(t∈d)/nb(d)
terme="Lyon" #terme que nous voulons compter dans un fichier
file = open('./pages_web/lipn.fr_man-www2018_MAN%40WWW2018_Home.html','r') #ouverture et lecture du fichier choisi
rd = file.read() #chargement du fichier dansune variable
liste = rd.split(" ") #chaque token est chargé dans une liste
print(liste) #affichage pour vérifier
print(liste.count(terme)) #affichage du nombre de termes equivalent à celui entré en paramètre
nbtokendoc = len(liste)
print("LONGUEUR DOCUMENT :",nbtokendoc) #affichage
nbterme = liste.count(terme) #variable qui va stocker l'entier correspondant à l'équivalence
#average = sum(len(liste) for liste in words) / len(liste)
#print("AVERAGE =", average)
#print(rd)
file.close() #fermeture du fichier
TF = nbterme / nbtokendoc #ce qui nous mène à coder la formule associé à Term Frequency
print("TF =",TF) #affichage pour vérifier

#INVERSE DOCUMENT FREQUENCY IDF = (d)
#a=1
if nbterme < 1:
    print("Le nombre de termes dans le document vaut 0")
else:
    val=number_files/nbterme
    IDF = math.log(val)
    print(IDF)
