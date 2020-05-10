from os import listdir #importation bibliothèque lecture fichier et répertoire
import os
import math
import indexe_inverse
# Charger les documents dans l'index
# La méthode doit parcourir les documents d'un répertoire passer en entrée.
# Charger tous les fichiers que le répertoire contient, quel que soit le mode d'encodage du fichier.
monRepertoire = "./pages_web/"

#***********************Valider par Amine Yahouni************************************ 
#Retourne le nombre de mots dans un document choisi, donc sa longueur
def longueurDoc(document):
    doc = open(document,'r') #ouverture et lecture du fichier choisi
    rd = file.read() #chargement du fichier dans une variable
    liste = rd.split(" ") #chaque token est chargé dans une liste
    nbtokendoc = len(liste)
    document.close() #fermeture du fichier
    return nbtokendoc


#***********************Valider par Amine Yahouni************************************ 
#Average Document Length,  la longueur moyenne des documents de la collection
def avgdl(monRepertoire):                                      #A FINIR
    fichiers = [f for f in listdir(monRepertoire)] # les fichiers du répertoire sont chargés
    # print(fichiers) #L'affichage est optionnel
    list = os.listdir(monRepertoire) # création d'une liste chargeant les fichiers du répertoire
    c = 0
    for l in list:
        c+=1
        file = open(l,'r').read() #ouverture et lecture du fichier choisi
        liste = file.split(" ") #chaque token est chargé dans une liste
        file.close() #fermeture du fichier
        adl+=len(liste)
        #print(" Fichier =",fichier)
    return adl/c

    #doc = open(document,'r') #ouverture et lecture du fichier choisi
    #rd = file.read() #chargement du fichier dans une variable
    #word = rd.split(" ")
    #average = sum(len(word) for word in words) / len(words)
    #return average
    

#***********************Valider par Amine Yahouni************************************ 
def ftd(mot, document):
    doc = open(document,'r') #ouverture et lecture du fichier choisi
    rd = file.read() #chargement du fichier dan sune variable
    liste = rd.split(" ") #chaque token est chargé dans une liste
    nbterme = liste.count(mot) #variable qui va stocker l'entier correspondant à l'équivalence FREQUENCE BRUTE
    document.close()
    return nbterme



#***********************Valider par Amine Yahouni************************************ 
def chargerIndex(monRepertoire):
    fichiers = [f for f in listdir(monRepertoire)] # les fichiers du répertoire sont chargés
    # print(fichiers) #L'affichage est optionnel
    list = os.listdir(monRepertoire) # création d'une liste chargeant les fichiers du répertoire
    number_files = len(list) # fonction len qui va retourner un entier qui sera la longueur de la liste
    return number_files #renvoie nombre de fichiers


#***********************Valider par Amine Yahouni************************************ 
#Les fonction capables de calculer les variantes d'un TF-IDF
#TERM FREQUENCY TF = nb(t∈d)/nb(d)
#terme="Lyon" #terme que nous voulons compter dans un fichier
def tf(mot, document, monRepertoire):
    doc = open(document,'r') #ouverture et lecture du fichier choisi
    rd = file.read() #chargement du fichier dansune variable
    liste = rd.split(" ") #chaque token est chargé dans une liste
    nbtokendoc = len(liste)
    nbterme = liste.count(mot) #variable qui va stocker l'entier correspondant à l'équivalence FREQUENCE BRUTE
    document.close() #fermeture du fichier
    TF = nbterme / nbtokendoc #ce qui nous mène à coder la formule associé à Term Frequency
    return TF


#***********************Valider par Amine Yahouni************************************ 
#INVERSE DOCUMENT FREQUENCY IDF; mot et une collection de documents
def idf(mot, document, monRepertoire):
    #doc = open(document,'r')
    #rd = file.read()
    #liste = rd.split(" ")
    #nbterme = liste.count(mot) #ft,d = nbterme FREQUENCE
    #document.close()
    #Fonction qui renvoie le nombre de termes. Puis vérification si valeur postive
    if ftd(mot, document) < 1: #Fonction qui renvoie le nombre de mot dans le document
        print("Le nombre de termes dans le document vaut 0") #Si négative
    else: #Sinon on applique la formule IDF
        val=chargerIndex(monRepertoire)/nbterme #Pour appliquer la formule IDF utilisant log
        IDF = math.log(val)
        return IDF #renvoie valeur de IDF

    

    
    
#***********************Valider par Amine Yahouni************************************ 
#Normalisation Logarithmique
def N_Log(mot, document):
    res = 1+math.log(ftd(mot, document))
    return res



#***********************Valider par Amine Yahouni************************************ 
#Normalisation par le max
def N_Max(mot, document,terme):
    sol=0.5+0.5*(ftd(mot, document)/max(ftd(terme, document)))
    return sol



#***********************Valider par Amine Yahouni************************************ 
#Formule TF-IDF
def TF_IDF(mot, document, monRepertoire):
    tfidf=tf(mot, document, monRepertoire)*idf(mot, document, monRepertoire)
    return tfidf



#***********************Valider par Amine Yahouni************************************ 
def BM_25(mot, document, monRepertoire,k1):
    b=0.75
    resultat = idf(mot, document, monRepertoire)*((ftd(mot, document)*(k1+1))/(ftd(mot, document)+(k1*(1-b+(b*longueurDoc(document)/avgdl(monRepertoire))))))

    

#***********************Valider par Amine Yahouni************************************ 
#une fonction recherche qui prend en entrée séquence de mots-clés et qui renvoie les 10 premières pages qui maximisent le score pour ces mots clés
def recherche(mots):
    c=0 #on initialise le compteur
    k1=2 #on initialise la valeur de K appartient à [1.2,2.0] pour la formule BM 25
    #tab=[]
    for f in listdir(monRepertoire): #parcourir chaque fichier du répertoire (notre collection)
        valeur=BM_25(mots, f, monRepertoire,k1) #on calcule le score
        tab[c] = [(valeur,f)] #le score obtenu est stocké dans un tableau, couple de valeur et page associé
        c+=1 #compteur qui sert d'indice pour notre tableau
    maximisation = tab.sort(reverse=True) #on tri dans l'ordre décroissant les valeurs du tableau avec sort + reverse = true, en fonction de la première colonne
    return maximisation[:10] #retourner les 10 premières cases du tableau représentant les 10 premières pages qui maximisent le score
