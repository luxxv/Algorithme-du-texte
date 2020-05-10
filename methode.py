#import indexe_inverse
# Charger les documents dans l'index
# La méthode doit parcourir les documents d'un répertoire passer en entrée.
# Charger tous les fichiers que le répertoire contient, quel que soit le mode d'encodage du fichier.
monRepertoire = "./pages_web/"


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
#Retourne le nombre de mots dans un document choisi, donc sa longueur
def longueurDoc(document):
    file = open(document,'r') #ouverture et lecture du fichier choisi
    rd = file.read() #chargement du fichier dans une variable
    liste = re.findall(r'\w+', rd) #chaque token est chargé dans une liste
    nbtokendoc = len(liste)
    file.close() #fermeture du fichier
    return nbtokendoc

#Average Document Length,  la longueur moyenne des documents de la collection
def avgdl(monRepertoire):                                      #A FINIR
    fichiers = [f for f in listdir(monRepertoire)] # les fichiers du répertoire sont chargés
    # print(fichiers) #L'affichage est optionnel
    list = os.listdir(monRepertoire) # création d'une liste chargeant les fichiers du répertoire
    c = 0
    adl=0
    for l in list:
        c=c+1
        tmp="pages_web/"+l
        file = open(tmp,'r')#ouverture et lecture du fichier choisi
        try :
            rd=file.read()
        except UnicodeDecodeError:
            continue
        #print(tmp)
        liste = re.findall(r'\w+', rd) #chaque token est chargé dans une liste
        file.close() #fermeture du fichier
        adl=adl+len(liste)
        #print(" Fichier =",fichier)
    print(adl/c)
    return adl/c

    #doc = open(document,'r') #ouverture et lecture du fichier choisi
    #rd = file.read() #chargement du fichier dans une variable
    #word = rd.split(" ")
    #average = sum(len(word) for word in words) / len(words)
    #return average

def ftd(mot, document):
    file = open(document,'r') #ouverture et lecture du fichier choisi
    rd = file.read() #chargement du fichier dan sune variable
    liste = re.findall(r'\w+', rd) #chaque token est chargé dans une liste
    nbterme = len(cherche_occurrences(rd,mot)) #variable qui va stocker l'entier correspondant à l'équivalence FREQUENCE BRUTE
    file.close()
    print("nombre de terme :",nbterme)
    return nbterme

def chargerIndex(monRepertoire):
    fichiers = [f for f in listdir(monRepertoire)] # les fichiers du répertoire sont chargés
    # print(fichiers) #L'affichage est optionnel
    list = os.listdir(monRepertoire) # création d'une liste chargeant les fichiers du répertoire
    number_files = len(list) # fonction len qui va retourner un entier qui sera la longueur de la liste
    return number_files #renvoie nombre de fichiers

#Les fonction capables de calculer les variantes d'un TF-IDF
#TERM FREQUENCY TF = nb(t∈d)/nb(d)
#terme="Lyon" #terme que nous voulons compter dans un fichier
def tf(mot, document, monRepertoire):
    doc = open(document,'r') #ouverture et lecture du fichier choisi
    rd = file.read() #chargement du fichier dansune variable
    liste = re.findall(r'\w+', file) #chaque token est chargé dans une liste
    nbtokendoc = len(liste)
    nbterme = len(cherche_occurrences(document,mot))#variable qui va stocker l'entier correspondant à l'équivalence FREQUENCE BRUTE
    document.close() #fermeture du fichier
    TF = nbterme / nbtokendoc #ce qui nous mène à coder la formule associé à Term Frequency
    return TF

#INVERSE DOCUMENT FREQUENCY IDF; mot et une collection de documents
def idf(mot, document, monRepertoire):
    doc = open(document,'r')
    try:
        rd = doc.read()
        liste = re.findall(r'\w+', rd) #chaque token est chargé dans une liste
        nbterme = len(cherche_occurrences(rd,mot))#variable qui va stocker l'entier correspondant à l'équivalence FREQUENCE 
        #liste = rd.split(" ")
        #nbterme = liste.count(mot) #ft,d = nbterme FREQUENCE
        #document.close()
        #Fonction qui renvoie le nombre de termes. Puis vérification si valeur postive
        if ftd(mot, document) < 1: #Fonction qui renvoie le nombre de mot dans le document
            print("Le nombre de termes dans le document :",document,"  vaut 0") #Si négative
            return 1
        else: #Sinon on applique la formule IDF
            val=chargerIndex(monRepertoire)/nbterme #Pour appliquer la formule IDF utilisant log
            IDF = math.log(val)
            print("i'm idf",IDF)
            return IDF #renvoie valeur de IDF
    except UnicodeDecodeError:
        print("Erreur de lecture du fichier ",document)
        return 1
#Normalisation Logarithmique
def N_Log(mot, document):
    res = 1+math.log(ftd(mot, document))
    return res

#Normalisation par le max
def N_Max(mot, document,terme):
    sol=0.5+0.5*(ftd(mot, document)/max(ftd(terme, document)))
    return sol

#Formule TF-IDF
def TF_IDF(mot, document, monRepertoire):
    tfidf=tf(mot, document, monRepertoire)*idf(mot, document, monRepertoire)
    return tfidf

def BM_25(mot, document, monRepertoire,k1):
    b=0.75
    resultat = idf(mot, document, monRepertoire)*((ftd(mot, document)*(k1+1))/(ftd(mot, document)+(k1*(1-b+(b*longueurDoc(document)/avgdl(monRepertoire))))))


#une fonction recherche qui prend en entrée séquence de mots-clés et qui renvoie les 10 premières pages qui maximisent le score pour ces mots clés
def recherche(mots):
    c=0 #on initialise le compteur
    k1=2 #on initialise la valeur de K appartient à [1.2,2.0] pour la formule BM 25
    tab=[]
    for f in listdir(monRepertoire): #parcourir chaque fichier du répertoire (notre collection)
        tmp="pages_web/"+f
        valeur=BM_25(mots, tmp , monRepertoire,k1) #on calcule le score
        tab.append([valeur,f]) #le score obtenu est stocké dans un tableau, couple de valeur et page associé
        c+=1 #compteur qui sert d'indice pour notre tableau
    maximisation = tab.sort(reverse=True) #on tri dans l'ordre décroissant les valeurs du tableau avec sort + reverse = true, en fonction de la première colonne
    return maximisation[:10] #retourner les 10 premières cases du tableau représentant les 10 premières pages qui maximisent le score

print(recherche("Lyon"))
