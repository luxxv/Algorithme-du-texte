from os import listdir #importation bibliothèque lecture fichier et répertoire
import os
import math
#import indexe_inverse # je ne vois pas l'utilité de cet import ??
import re
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

#****************Block modifié pour cause de dysfonctionnement de la méthode employée************************ 
#liste = rd.split(" ") #chaque token est chargé dans une liste
#print(liste) #affichage pour vérifier
#print(liste.count(terme)) #affichage du nombre de termes equivalent à celui entré en paramètre
#nbterme = liste.count(terme) #variable qui va stocker l'entier correspondant à l'équivalence
#nbtokendoc = len(liste)
#print("LONGUEUR DOCUMENT :",nbtokendoc) #affichage

#***************Block proposer par Amine Yahouni*********************

def isprefixe(texte,mot,i):
        """Vérifie si mot a une occurrence dans texte en position i"""
        B = True
        j = 0
        while (j < len(mot)) and B:
            if texte[i+j] != mot[j]:
                B = False
            j +=1
        return B
    
def cherche_occurrences(texte, mot):
        """Donne la liste de toutes les occurrences de mot dans texte"""
        occ = [] # liste des occurrences
        for i in range(len(texte)-len(mot)+1):
            if isprefixe(texte,mot,i):
                occ.append(i)
        return occ
    

#Par la suite l'idée est de rechercher les occurence d'un mot donné 
nbterme=len(cherche_occureences(rd,terme)) #variable qui va stocker l'entier correspondant à l'équivalence
print("Occurence du terme :'",terme,"' dans notre Texte est :",nbterme)#Affichage

#pour les nbtokendoc nous allons utlisé regex pour compter le nombre de mot avec findall
nbtokendoc = len(re.findall(r'\w+', rd)) #le nombre total des mots de notre fichier
print("LONGUEUR DOCUMENT :",nbtokendoc) #affichage

#on peut aussi afficher la liste des mots si nécessaire 
#print(re.findall(r'\w+', rd))

#*******************************Fin du block proposer par Amine Yahouni**********************************




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
