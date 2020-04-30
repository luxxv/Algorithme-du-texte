from os import listdir #importation bibliothèque lecture fichier et répertoire
import os
import math

monRepertoire = "./pages_web/"
fichiers = [f for f in listdir(monRepertoire)] # les fichiers du répertoire sont chargés
# print(fichiers) #L'affichage est optionnel
list = os.listdir(monRepertoire) # création d'une liste chargeant les fichiers du répertoire
c = 1
adl = 0
for l in list:
    path = monRepertoire+l
    c+=1
    file = open(path,'r',encoding="utf8") #ouverture et lecture du fichier choisi
    rd = file.read()
    liste = rd.split(" ") #chaque token est chargé dans une liste
    file.close() #fermeture du fichier
    adl+=len(liste)
    #print(" Fichier =",fichier)
avgdl = adl/c
print(" La longueur moyenne de cette collection est : ",avgdl)
print(" c =",c)

#test='./pages_web/lipn.fr_man-www2018_MAN%40WWW2018_Home.html'
#file = open(test,'r')
#rd = file.read()
#liste = rd.split(" ")
#file.close()
#print(liste)
#print(" Fichier =",test)
#number_files = len(list) # fonction len qui va retourner un entier qui sera la longueur de la liste
#print("vérif chargement",number_files) #affichage
