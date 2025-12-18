from random import*
from fltk import *


taille_fenetre = 13*47
taille_case = taille_fenetre/13

def pixel_vers_case(x,y,taille_casex,taille_casey):
    """
    traduction pixel vers case, transforme des coordonnée en pixel en coordonée de case
    paramètre:
    x: str, coordonée sur l'axe x
    y: str, coordonée sur l'axe y
    taille_casex: str, largeur de chaque case
    taille_caset: str: hauteur de chaque case
    exemple:
    >>> pixel_vers_case(156.5,40.3,20,20)
    (7.0, 2.0)
    >>> pixel_vers_case(16.5,60.3,50,20)
    (0.0, 3.0)
    >>> pixel_vers_case(56.2,264.6,30,20)
    (1.0, 13.0)
    >>> pixel_vers_case(523.5,75.3,20,40)
    (26.0, 1.0)
    >>> pixel_vers_case(69.5,42.3,50,70)
    (1.0, 0.0)
    >>> pixel_vers_case(86.5,35.3,29,10)
    (2.0, 3.0)
    """
    x1=(x//taille_casex)
    y1=(y//taille_casey)
    #print (x1,y1)
    return (x1,y1)

"""
print(pixel_vers_case(156.5,40.3,20,20))
print(pixel_vers_case(16.5,60.3,50,20))
print(pixel_vers_case(56.2,264.6,30,20))
print(pixel_vers_case(523.5,75.3,20,40))
print(pixel_vers_case(69.5,42.3,50,70))
print(pixel_vers_case(86.5,35.3,29,10))
"""

def case_vers_pixel(case):
    """
    Reçoit les coordonnées d'une case du plateau sous la forme d'un couple
    d'entiers (colonne, ligne) et renvoie les coordonnées du centre de cette
    case sous la forme d'un couple de flottants (abscisse, ordonnée). 
    
    Ce calcul prend en compte la taille de chaque case, donnée par la variable
    globale `taille_case`.
    
    >>> taille_case = 13*47/13
    >>> case_vers_pixel((4, 6))
    (211.5, 305.5)
    """
    i, j = case
    return (i + .5) * taille_case, (j + .5) * taille_case
#print (case_vers_pixel((4,6)))

def dessiner_plateau():
    """
    dessine un plateau/une grille vide
    """
    global taille_fenetre
    grillex= taille_fenetre//13
    grilley= taille_fenetre//13
    liste=[]
    ind=0 #indice pour dessiner le rectangle, le ind eme carré
    for i in range(13): #la longeure de plateau 
        for I in range(13):
            liste.append([I*grilley,i*grillex,(I+1)*grilley,(i+1)*grillex])
    for i in range(13): #la longeure de plateau 
        #print (plateau)
        for I in range(13):
                rectangle(liste[ind][0],liste[ind][1],liste[ind][2],liste[ind][3],"black","grey")
                #mise_a_jour()
                ind+=1

#dico={"orange":choice([False,True]), "blanc": choice([False,True]), "balle": {"j1":choice([False,True])}}
"""
[[' b', ' b', '1b', '1b', ' b', ' 0', '1o'],
 ['1b', ' o', ' b', '1o', ' b', '1b', ' o'],
 ['10', '1b', '1b', ' 0', ' o', ' o', '1b'],
 ['1b', ' b', ' o', ' o', '1b', '1b', '1b'],
 ['1o', ' 0', '1b', ' o', ' o', ' b', '1o'],
 ['1b', '1b', ' b', ' 0', ' 0', ' 0', ' o'],
 ['1o', ' b', '1b', ' 0', '1b', ' b', ' 0']]
"""

def dessine_jeu(plateau,tabgraph):
    """
    dessine graphiquement le plateau ainsi que tout ses éléments, hormis les tirettes a l'exterieur
    """
    for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            if "b" in plateau[i][j]:
                x,y = case_vers_pixel((i+3,j+3))
                cercle(x, y, 20,couleur='black', remplissage='white')
            if "o" in plateau[i][j]:
                x,y = case_vers_pixel((i+3,j+3))
                cercle(x, y, 20,couleur='black', remplissage='orange')
            if "0" in plateau[i][j]:
                x,y = case_vers_pixel((i+3,j+3))
                cercle(x, y, 20,couleur='black', remplissage='black')
            if "1" in plateau[i][j]:
                x,y = case_vers_pixel((i+3,j+3))
                if tabgraph[i][j]['balle']['j1']:
                    cercle(x, y, 10,couleur='black', remplissage='red')
                elif tabgraph[i][j]['balle']['j2']:
                    cercle(x, y, 10,couleur='black', remplissage='blue')
                elif tabgraph[i][j]['balle']['j3']:
                    cercle(x, y, 10,couleur='black', remplissage='yellow')
                elif tabgraph[i][j]['balle']['j4']:
                    cercle(x, y, 10,couleur='black', remplissage='green')
                else:
                    cercle(x, y, 10,couleur='black', remplissage='black')
#j1 = red, j2 = blue, j3 = yellow, j4 = green

def tableau():
    """
    renvoie une liste de liste de dictionaire qui represente le tableau
    "orange" et "blanc" representent les languettes oranges et blanches, True si il y a un trou, False sinon
    "balle" represente la présence d'une balle, True si il y en a une, False sinon
    "orange" et "blanc" sont aléatoire
    
    """
    
    plateau=[]
    for i in range(7):
        liste=[]
        for j in range(7):
            if i>1 and not plateau[i-1][j]['blanc'] and not plateau[i-2][j]['blanc']:
                blanc=True
            
            else:
                blanc=choice([False,True,False])
            if i>=6 and plateau[0][j]['blanc']==False:
                blanc=True
            if j>1 and (not(liste[j-1]['orange']) and not(liste[j-2]['orange'])):
                orange=True
            elif j==6  and not (liste[0]['orange']):
                orange=True
            else:
                orange=choice([False,True,False])
            """
            print("orange: ",orange)
            print("blanc: ",blanc)
            print("")
            """
            dico={"orange":orange, "blanc":blanc,
                "balle": {"j1":False,
                            "j2":False,
                            "j3":False,
                            "j4":False}}
            """
            dico={"orange":orange, "blanc":blanc,
                "balle": {"j1":choice([False,True,False,False,False,False,False,False,False,False]),
                            "j2":choice([False,True,False,False,False,False,False,False,False,False]),
                            "j3":choice([False,True,False,False,False,False,False,False,False,False]),
                            "j4":choice([False,True,False,False,False,False,False,False,False,False])}}
            """
            """
            dico={"orange":choice([False,True,False,True,True]), "blanc": choice([False,True,False,True,True]),
                  "balle": {"j1":choice([False,True,False,False,False,False,False,False,False,False]),
                            "j2":choice([False,True,False,False,False,False,False,False,False,False]),
                            "j3":choice([False,True,False,False,False,False,False,False,False,False]),
                            "j4":choice([False,True,False,False,False,False,False,False,False,False])}}
            """
            liste.append(dico)
        plateau.append(liste)
    """
    for I in range(7):
        for J in range(7):
            print(I,J)
            print(plateau[I][J])
    """
    return plateau


def je_veux_lire(plateau):
    """
    affiche le plateau sous forme de liste de liste de dico dans le terminal
    """
    for i in range(len(plateau)):
        print (plateau[i])
        print (" ")
        
def bille_tombe(grille):
    """
    Détecte si des des billes doivent tomber.
    Args:
    grille (list): Une liste de liste de dictionaire represenatant le plateau
    Returns:
    bool: True s'il reste des billes, False sinon.
    """
    billes_a_supprimer = []
    for j in range(7):
        for i in range(7):
            if (grille[i][j]['blanc'] and grille[i][j]['orange']) and bille_case(grille[i][j]['balle']) : 
                billes_a_supprimer.append((i, j))
    return billes_a_supprimer
#je_veux_lire(tableau())


def bille_case(dico):
    """
    recoit un dictionnaire et renvoie True si il existe un elément True dans le dictionnaire, renvoie False sinon
    paramètre:
    dico: un dictionnaire
    exemple:
    >>> bille_case({'j1': True})
    True
    >>> bille_case({'sfhgrd': False,'sfh': True})
    True
    >>> bille_case({'j1': False,'sfh': False})
    False
    >>> bille_case({'j1': False})
    False
    """
    for elt in dico:
        if dico[elt]==True:
            return True
    return False

def affiche_plateau(plateau):
    """
    recoit l'état du plateau sous forme de liste de liste de dictionnaire et
    renvoie une liste de liste representant le plateau tel qu'il est sensé être vu par les joueurs
    paramètre:
    plateau= liste de liste de dictionnaire
    renvoie:
    visu= la liste de liste finale
    """
    #0 si il y a un trou
    #X si les 2 languettes sont fermées
    #o si la languette orange est ouverte mais pas la blanche
    #b si la languette blache est ouverte mais pas la orange
    visu=[] #liste finale           pour la visualisation du plateau
    for i in range(len(plateau)):
        liste=[]
        for j in range(len(plateau[i])):
            case=""
            if bille_case(plateau[i][j]['balle']):
                case+="1"
            else:
                case+=" "
            if plateau[i][j]['orange'] and plateau[i][j]['blanc']:
                case+="0"
            elif not (plateau[i][j]['blanc']):
                case+="b"
            elif not(plateau[i][j]['orange']) and plateau[i][j]['blanc']:
                case+="o"
            #else:
            #    case+="t"
            liste.append(case)   
        visu.append(liste)
    return visu

#print (affiche_plateau(tableau()))
"""
def decale_gauche(liste):
    ""
    prends le 1er (indice=0) élément d'une liste, le met a la fin et décale tout les éléments vers la gauche
    paramètre:
    -liste: une liste
    return:
    renvoie la liste avec son 1er (indice=0) élément a la fin
    >>> decale_gauche([["a","b","c","d"],["1","2","3","4"],["z","y","x","w"]])
    [['1', '2', '3', '4'], ['z', 'y', 'x', 'w'], ['a', 'b', 'c', 'd']]
    >>> decale_gauche(["a","b","c","d"])
    ['b', 'c', 'd', 'a']
    >>> decale_gauche(["1","2","3","4"])
    ['2', '3', '4', '1']
    >>> decale_gauche(["z","y","x","w"])
    ['y', 'x', 'w', 'z']
    >>> decale_gauche(["9","8","7","6"])
    ['8', '7', '6', '9']
    ""
    liste.append(liste.pop(0))
    #b=liste[-1]+liste[:-1]
    return liste
"""
"""
def decale_droite(liste):
    ""
    prends le dernier élément d'une liste, le met au début (indice=0) et décale tout les éléments vers la droite
    paramètre:
    -liste: une liste
    return:
    renvoie la liste avec son dernier élément au debut (indice =0)
    
    >>> decale_droite([["a","b","c","d"],["1","2","3","4"],["z","y","x","w"],["9","8","7","6"]])
    [['9', '8', '7', '6'], ['a', 'b', 'c', 'd'], ['1', '2', '3', '4'], ['z', 'y', 'x', 'w']]
    >>> decale_droite(["9","8","7","6"])
    ['6', '9', '8', '7']
    >>> decale_droite(["a","b","c","d"])
    ['d', 'a', 'b', 'c']
    >>> decale_droite(["1","2","3","4"])
    ['4', '1', '2', '3']
    >>> decale_droite(["z","y","x","w"])
    ['w', 'z', 'y', 'x']
    ""
    liste.insert(0,liste.pop())
    #b=liste[-1]+liste[:-1]
    return liste
"""

def obtient_indice(dico,elem):
    """
    inutile nvm
    """
    i=0
    for elt in dico:
        if elem==elt:
            return i
        i+=1
    return i
"""
print (obtient_indice({"orange":1, "blanc": 2, "balle": {"j1":3}},'orange'))
print (obtient_indice({"orange":1, "blanc": 2, "balle": {"j1":3}},'blanc'))
print (obtient_indice({"orange":1, "blanc": 2, "balle": {"j1":3}},'balle'))
"""

def decale_gauche(liste,elem,x):
    """
    permet de "décaler" un élément vers la gauche d'un dictionnaire dans une liste de liste de dictionnaire
    paramètre:
    -liste: une liste de liste de dictionnaire
    -elem: la clé qui est a déplacer (type=str)
    -x: int qui pêrmet de choisir où déplacer, dans quelle liste
    return:
    renvoie la liste décallée
    """
    #liste.insert(0,liste.pop())
    temp=liste[x][0][elem]
    for j in range(len(liste[x])-1):
        liste[x][j][elem]=liste[x][j+1][elem]
    liste[x][-1][elem]=temp
    return liste

def decale_droite(liste,elem,x):
    """
    permet de "décaler" un élément vers la droite d'un dictionnaire dans une liste de liste de dictionnaire
    paramètre:
    -liste: une liste de liste de dictionnaire
    -elem: la clé qui est a déplacer (type=str)
    -x: int qui pêrmet de choisir où déplacer, dans quelle liste
    return:
    renvoie la liste décallée
    """
    for i in range(len(liste)-1):
        liste=decale_gauche(liste,elem,x)
    return liste

"""
#print (decale_droite([["a","b","c","d"],["1","2","3","4"],["z","y","x","w"]]))
dico={"orange":1, "blanc": 2, "balle": {"j1":3}}

testplat=[{'orange': "a", 'blanc': False, 'balle': {'j1': True}}, {'orange': "b", 'blanc': False, 'balle': {'j1': False}},{'orange': "c", 'blanc': False, 'balle': {'j1': True}}],[{'orange': "1", 'blanc': False, 'balle': {'j1': False}}, {'orange': "2", 'blanc': False, 'balle': {'j1': False}},{'orange': "3", 'blanc': False, 'balle': {'j1': True}}]

print (decale_droite(testplat,"orange",0))
print (decale_gauche(testplat,"orange",0))
"""

test=[["a","b","c","d"],
      ["1","2","3","4"],
      ["z","y","x","w"],
      ["9","8","7","6"]]

"""
def decale_haut(liste,y):
    ""
    recoit une liste de liste, prends le y eme (indice = y) élément de la 1ere (indice = 0) liste,
    le met au y eme element de la derniere liste, et décale tout les y eme éléments vers le haut
    paramètre:
    -liste: une liste de liste, (chaque liste dans la 1ere liste doit avoir autant d'éléments)
    -y: integer utilisé comme indice pour savoir quelles valeurs décaler (doit être plus petit que la taille de len(liste[0])
    
    >>> decale_haut([["a","b","c","d"],["1","2","3","4"],["z","y","x","w"],["9","8","7","6"]],0)
    [['1', 'b', 'c', 'd'], ['z', '2', '3', '4'], ['9', 'y', 'x', 'w'], ['a', '8', '7', '6']]
    >>> decale_haut([["a","b","c","d"],["1","2","3","4"],["z","y","x","w"],["9","8","7","6"]],1)
    [['a', '2', 'c', 'd'], ['1', 'y', '3', '4'], ['z', '8', 'x', 'w'], ['9', 'b', '7', '6']]
    >>> decale_haut([["a","b","c","d"],["1","2","3","4"],["z","y","x","w"],["9","8","7","6"]],2)
    [['a', 'b', '3', 'd'], ['1', '2', 'x', '4'], ['z', 'y', '7', 'w'], ['9', '8', 'c', '6']]
    >>> decale_haut([["a","b","c","d"],["1","2","3","4"],["z","y","x","w"],["9","8","7","6"]],3)
    [['a', 'b', 'c', '4'], ['1', '2', '3', 'w'], ['z', 'y', 'x', '6'], ['9', '8', '7', 'd']]
    >>> decale_haut([["a","b","c","d"],["1","2","3","4"],["9","8","7","6"]],3)
    [['a', 'b', 'c', '4'], ['1', '2', '3', '6'], ['9', '8', '7', 'd']]
    ""
    base= liste[0][y]
    for i in range(len(liste)-1):
        liste[i][y]=liste[i+1][y]
    liste[-1][y]=base
    return liste
"""

testplat=[{'orange': "a", 'blanc': "aa", 'balle': {'j1': True}},
          {'orange': "b", 'blanc': "bb", 'balle': {'j1': False}},
          {'orange': "c", 'blanc': "cc", 'balle': {'j1': True}}],[{'orange': "1", 'blanc': '11', 'balle': {'j1': False}},
         {'orange': "2", 'blanc':'22', 'balle': {'j1': False}},
         {'orange': "3", 'blanc': '33', 'balle': {'j1': True}}],[{'orange': "a1", 'blanc': 'a1a1', 'balle': {'j1': False}},
         {'orange': "a2", 'blanc':'a2a2', 'balle': {'j1': False}},
         {'orange': "a3", 'blanc': 'a3a3', 'balle': {'j1': True}}]

def decale_bas(liste,elem,y):
    """
    permet de "décaler" un élément vers le bas d'un dictionnaire dans une liste de liste de dictionnaire
    paramètre:
    -liste: une liste de liste de dictionnaire
    -elem: la clé qui est a déplacer (type=str)
    -y: int qui pêrmet de choisir où déplacer, dans quelle liste
    return:
    renvoie la liste décallée
    """
    base= liste[0][y][elem]
    for i in range(len(liste)-1):
        liste[i][y][elem]=liste[i+1][y][elem]
    liste[-1][y][elem]=base
    return liste

#je_veux_lire(decale_haut(testplat,"blanc",0))

"""
print (decale_droite(test))
print (decale_droite(test[0]))
print (decale_droite(test[1]))
print (decale_droite(test[2]))
print (decale_droite(test[3]))
#print (decale_haut(test,0))
"""



def decale_haut(liste,elem,y):
    """
    permet de "décaler" un élément vers le haut d'un dictionnaire dans une liste de liste de dictionnaire
    paramètre:
    -liste: une liste de liste de dictionnaire
    -elem: la clé qui est a déplacer (type=str)
    -y: int qui pêrmet de choisir où déplacer, dans quelle liste
    return:
    renvoie la liste décallée
    """
    for i in range(len(liste)-1):
        liste=decale_bas(liste,elem,y)
    return liste

#je_veux_lire(decale_haut(testplat,"blanc",0))

"""
print(decale_bas([["a","b","c","d"],["1","2","3","4"],["z","y","x","w"],["9","8","7","6"]],0))
    
print(decale_bas([["a","b","c","d"],["1","2","3","4"],["z","y","x","w"],["9","8","7","6"]],1))
    
print(decale_bas([["a","b","c","d"],["1","2","3","4"],["z","y","x","w"],["9","8","7","6"]],2))
    
print(decale_bas([["a","b","c","d"],["1","2","3","4"],["z","y","x","w"],["9","8","7","6"]],3))
    
print(decale_bas([["a","b","c","d"],["1","2","3","4"],["9","8","7","6"]],3))
#print (decale_bas(test,0))
#print (decale_haut(test,0))
"""


def bouge_tirette_terminal(plateau):
    """
    recoit une liste de liste represantant le plateau de jeu,
    demande a l'utilisateur sur le terminal quelle tirette il choisit,
    d'abord si c'est une tirette verticale ou horizontale (blanche ou orange)
    puis laquelle
    et enfin dans quel sens
    renvoit ensuite plateau modifié selon les actions de l'utilisateur
    paramètre:
    -plateau: une liste de liste (de dictionaire)
    return:
    -plateau: une liste de liste de dictionnaire
    -orientation: int (1 ou 0) représantant quelle type de tirette l'utilisateur a choisit
    -nbr_ligne: int (entre 1 et 7) représantant le numéro de la tirette choisie par l'utilisateur
    -sens: int (1 ou 0) représantant comment l'utilisateur a déplacé la tirette
    """
    orientation=2
    while orientation not in (0,1):
        orientation = int(input("Verticale ou horizontale ? [1 pour vertical, 0 pour horizontal] "))
    nbr_ligne=8
    while nbr_ligne not in range (1,8):
        nbr_ligne = int(input("quelle ligne ? (vous prendrez les languettes a droite ou en bas) (de haut en bas ou de gauche a droite, entre 1 et 7) "))
    nbr_ligne-=1
    sens=2
    while sens not in (0,1):
        sens = int(input("vers l'interieur ou l'exterieur ? (0 pour vers l'interieur, 1 pour vers l'exterieur) "))
    """
    for i in range(7):
        for j in range(7):
            grille[i] == grille[i+1] and grille[7] == grille[0]
    """
    if orientation==1:
        if sens == 0:
            plateau=decale_gauche(plateau,'orange',nbr_ligne)
        else:
            plateau=decale_droite(plateau,'orange',nbr_ligne)
    else:
        if sens == 0: # vers l'interieur
            plateau=decale_haut(plateau,'blanc',nbr_ligne)
        else:
            plateau=decale_bas(plateau,'blanc',nbr_ligne)
    
    return plateau,orientation,nbr_ligne,sens


def bouge_tirette(plateau,act,act1):
    
    """
    recoit une liste de liste represantant le plateau de jeu,
    ainsi que les 2 clicks de l'utilisateur qui representent normalement l'emplacement de la tête de la tirette et une case a coté
    la fonction va voir dans quel sens il faut déplacer la tirette,
    déplace les cases dans la liste de liste de dico
    renvoit ensuite plateau modifié selon les actions de l'utilisateur et comment les déplacement ont été fait
    paramètre:
    -plateau: une liste de liste (de dictionaire)
    return:
    -plateau: une liste de liste de dictionnaire
    -orientation: int (1 ou 0) représantant quelle type de tirette l'utilisateur a choisit
    -nbr_ligne: int (entre 1 et 7) représantant le numéro de la tirette choisie par l'utilisateur
    -sens: int (1 ou 0) représantant comment l'utilisateur a déplacé la tirette
    """
    global grillex, grilley
    sens = 5
    orientation=5
    nbr_ligne = 12
    #texte(1,1, ("veuillez choisir votre tirette"), taille=20,tag="temp")
    mise_a_jour()
    #orientation=2
    #ev=donne_ev()
    #act=pixel_vers_case(abscisse(ev),ordonnee(ev),grillex,grilley)
    if act[0] <3 or act[0] > 9:
        orientation=0
    else:
        orientation =1
    
    #while orientation not in (0,1):
        #orientation = int(input("Verticale ou horizontale ? [1 pour vertical, 0 pour horizontal] "))
        
    #nbr_ligne=8
    if orientation==0:
        if act[1] < 2:
            nbr_ligne=0
        elif act[1] > 8:
            nbr_ligne=6
        else:
            nbr_ligne=act[1]-3
    elif orientation==1:
        if act[0] < 2:
            nbr_ligne=0
        elif act[0] > 8:
            nbr_ligne=6
        else:
            nbr_ligne=act[0]-3
    efface("temp")
    mise_a_jour()
    texte(1,1, ("veuillez cliquer sur la nouvelle position de votre tirette"), taille=10)
    #ev1=attend_clic_gauche()
    #ev=donne_ev()
    #act1=pixel_vers_case(abscisse(ev1),ordonnee(ev1),grillex,grilley)
    if orientation == 0:
        if act[0] <4:
            if act[0] < act1[0]:
                sens=1
            else:
                sens=0
        elif act[0] >7:
            if act[0] < act1[0]:
                sens=1
            else:
                sens=0
    else:
        if act[1] <4:
            if act[1] < act1[1]:
                sens=1
            else:
                sens=0
        elif act[1] >7:
            if act[1] < act1[1]:
                sens=1
            else:
                sens=0
        
        
    """  
    ""
    while nbr_ligne not in range (1,8):
        nbr_ligne = int(input("quelle ligne ? (vous prendrez les languettes a droite ou en bas) (de haut en bas ou de gauche a droite, entre 1 et 7) "))
    nbr_ligne-=1
    ""
    sens=2
    while sens not in (0,1):
        sens = int(input("vers l'interieur ou l'exterieur ? (0 pour vers l'interieur, 1 pour vers l'exterieur) "))
    ""
    for i in range(7):
        for j in range(7):
            grille[i] == grille[i+1] and grille[7] == grille[0]
    ""
    """
    if orientation==1:
        if sens == 0:
            plateau=decale_gauche(plateau,'orange',int(nbr_ligne))
        else:
            plateau=decale_droite(plateau,'orange',int(nbr_ligne))
    else:
        if sens == 1: # vers l'interieur
            plateau=decale_haut(plateau,'blanc',int(nbr_ligne))
        else:
            plateau=decale_bas(plateau,'blanc',int(nbr_ligne))
    
    return plateau,orientation,int(nbr_ligne),sens

        

def supprime_bille(liste,sup):
    """
    supprime les billes qui sont tombées
    recoit une liste de liste de cio représantant le plateau et une liste de bille a supprimer
    arg:
    -liste:une liste de liste (de dictionaire)
    -sup:une liste de couple d'int
    return:
    -
    """
    for i in range(len(sup)):
        for elt in (liste[sup[i][0]][sup[i][1]]['balle']):
            #print (liste[sup[i][0]][sup[i][1]]['balle'][elt])
            liste[sup[i][0]][sup[i][1]]['balle'][elt]=False
            #print (liste[sup[i][0]][sup[i][1]]['balle'][elt])
            #print("")
    return liste

def reste_billes(plateau):
    """
    Détermine s'il reste des billes sur le plateau.

    Args:
    - plateau (list): Une liste de liste de dictionnaires représentant le plateau de jeu.

    Returns:
    - bool: True s'il reste des billes, False sinon.
    """
    for j in range(7):
        for i in range(7):
            #if (plateau[i][j]['blanc'] and plateau[i][j]['orange']) and bille_case(plateau[i][j]['balle']):
            if bille_case(plateau[i][j]['balle']):
                return True
    return False

def reste_joueur(plateau,joueur):
    """
    Détermine s'il reste des billes pour un joueur donné sur le plateau.

    Args:
    - plateau (list): Une liste de liste de dictionnaires représentant le plateau de jeu.
    - joueur : int, le joueur n°x

    Returns:
    - bool: True s'il reste des billes, False sinon.
    """
    for j in range(7):
        for i in range(7):
            #if (plateau[i][j]['blanc'] and plateau[i][j]['orange']) and bille_case(plateau[i][j]['balle']):
            if plateau[i][j]['balle']['j'+str(joueur)]:
                return True
    return False

"""
def dessiner_tirettes(plateau):
    ""
    Dessine les tirettes en fonction de l'état du plateau.

    Args:
    - plateau (list): Une liste de liste de dictionnaires représentant le plateau de jeu.
    ""
    for i in range(7):
        # Dessiner les tirettes horizontales (blanches)
        if not plateau[i][6]['blanc']:
            ligne = [case_vers_pixel((i + 3, j + 3)) for j in range(7)]
            ligne.append(case_vers_pixel((i + 3, 3)))
            polygone(ligne, couleur='black', remplissage='white')

    for j in range(7):
        # Dessiner les tirettes verticales (oranges)
        if not plateau[6][j]['orange']:
            colonne = [case_vers_pixel((i + 3, j + 3)) for i in range(7)]
            colonne.append(case_vers_pixel((3, j + 3)))
            polygone(colonne, couleur='black', remplissage='orange')
"""

def affiche_tirettes(etat):
    """
    dessine les tirettes selon leur état
    paramètre:
    -etat: un dictionnaire avec comme elements "o0" jusqu'a "06" et "b0" jusqu'a "b6", 1 = position neutre 
    """
    global taille_case
    for i in range(7):
        for j in range(7):
            rectangle( ((case_vers_pixel((i+2,etat["o"+str(i)])))[0]+(taille_case/2))+10,(case_vers_pixel(((7-j)-3,0+etat["o"+str(i)])))[1]+(0),
                       ((case_vers_pixel((i+4,etat["o"+str(i)])))[0]-(taille_case/2))-10,(case_vers_pixel(((7-j)+3,0+etat["o"+str(i)])))[1]+10*taille_case,
                       remplissage="orange")
            cercle((case_vers_pixel((i+3,etat["o"+str(i)])))[0],(case_vers_pixel(((7-j)-3,0+etat["o"+str(i)])))[1]+(0),20, remplissage="#e68a00")
            cercle((case_vers_pixel((i+3,etat["o"+str(i)])))[0],(case_vers_pixel(((7-j)+3,0+etat["o"+str(i)])))[1]+10*taille_case,20, remplissage="#e68a00")
            
    for j in range(7):
        for i in range(7):
            rectangle( (case_vers_pixel(((7-j)-3,0+etat["b"+str(i)])))[1]+(0),((case_vers_pixel((i+4,etat["b"+str(i)])))[0]-(taille_case/2))-10,
                       (case_vers_pixel(((7-j)+3,0+etat["b"+str(i)])))[1]+10*taille_case,((case_vers_pixel((i+2,etat["b"+str(i)])))[0]+(taille_case/2))+10,
                       remplissage="white")
            
            cercle((case_vers_pixel(((7-j)-3,0+etat["b"+str(i)])))[1]+(0),(case_vers_pixel((i+3,etat["b"+str(i)])))[0],20, remplissage="#f1f1f1")
            cercle((case_vers_pixel(((7-j)+3,0+etat["b"+str(i)])))[1]+10*taille_case,(case_vers_pixel((i+3,etat["b"+str(i)])))[0],20, remplissage="#f2f2f2")
            
            

#fltk.rectangle(ax: float, ay: float, bx: float, by: float, couleur: str = 'black', remplissage: str = '', epaisseur: float = 1, tag: str = '') 
#ax,ay,bx,by
#f2f2f2
"""
etat_tirette={'o0':1,
                  'o1':1,
                  'o2':1,
                  'o3':1,
                  'o4':1,
                  'o5':1,
                  'o6':1,
                  'b0':1,
                  'b1':1,
                  'b2':1,
                  'b3':1,
                  'b4':1,
                  'b5':1,
                  'b6':1,
                  }
cree_fenetre(taille_fenetre, taille_fenetre)
dessiner_plateau()
tab=tableau()
#affiche_tirettes(etat_tirette)
"""

def choisit_bille(nbr_joueurs,tabgraph, tab):
    """
    permet aux joueurs de choisir l'emplacement de leurs bille
    nbr_joueurs= un entier representant le nombre de joueurs
    renvoie:
    billesj1=liste de couple représantant les billes du j1
    billesj2=liste de couple représantant les billes du j2
    billesj3=liste de couple représantant les billes du j3
    billesj4=liste de couple représantant les billes du j4
    """
    billesj1=[]
    billesj2=[]
    billesj3=[]
    billesj4=[]
    #billes={'j1'=[] ,'j2'=[] ,'j3'=[] ,'j4'=[] }
    
    for i in range(5):
        for j in range(nbr_joueurs):
            texte(1,1,("le joueur " + str(j+1) + " choisit l'emplacement de sa bille n°" + str(i+1)), taille=15, tag="txtbille")
            ev1=(0,0)
            """
            rectangle(int(grillex)*3,int(grilley)*3,int(grillex)*10,int(grilley)*10, epaisseur=10)
            print (int(grillex)*3,int(grillex)*10)
            print (int(grilley)*3,int(grilley)*11)
            """
            while ev1[1] not in range(int(grillex)*3,int(grillex)*10) or ev1[0] not in range(int(grilley)*3,int(grilley)*10):
                ev1=attend_clic_gauche()
                #print(ev1)
            ev=pixel_vers_case(ev1[0],ev1[1],grillex,grilley)
            #print(ev)
            x,y=ev1
            if j == 0:
                billesj1.append(ev)
                cercle(x, y, 10,couleur='black', remplissage='red')
            elif j == 1:
                billesj2.append(ev)
                cercle(x, y, 10,couleur='black', remplissage='blue')
            elif j == 2:
                billesj3.append(ev)
                cercle(x, y, 10,couleur='black', remplissage='yellow')
            elif j == 3:
                billesj4.append(ev)
                cercle(x, y, 10,couleur='black', remplissage='green')
            else:
                print("wat")
            efface("txtbille")
            mise_a_jour()
    return billesj1, billesj2, billesj3, billesj4




def consignea():
    nbr_joueur = 0
    texte(170-50,80,"Comment jouer ?", couleur="black", taille=30)
    texte(90-50,150,"Chaque tirettes dispose de 3 états,", couleur="black", taille=20)
    texte(65-50,185,"pour en bouger une, vous devez cliquer", couleur="black", taille=20)
    texte(65-50,220,"sur le bout de la tirette, puis sur la case", couleur="black", taille=20)
    texte(110-50,255,"d'arrivée de la tirette souhaitée.", couleur="black", taille=20)
    texte(55-55, 310, "Combien de joueurs y a-t-il ?", couleur="black", taille=30)
    attente(1)
    rectangle(40, 420, 110, 520, couleur="red")
    texte(40, 400, "1", couleur="black", taille=100-20)
    attente(0.5)
    rectangle(190, 420, 260, 520, couleur="red")
    texte(190, 400, "2", couleur="black", taille=100-20)
    attente(0.5)
    rectangle(340, 420, 410, 520, couleur="red")
    texte(340, 400, "3", couleur="black", taille=100-20)
    attente(0.5)
    rectangle(490, 420, 560, 520, couleur="red")
    texte(490, 400, "4", couleur="black", taille=100-20)
    attente(0.5)
    
    while nbr_joueur == 0:
        ev = attend_clic_gauche()
        ev = pixel_vers_case(ev[0],ev[1],grillex,grilley)
        print(ev)
        """
        if ev in pixel_vers_case(40, 420, 60, 100):
            nbr_joueur = 1
        elif ev in pixel_vers_case(190, 420, 260, 520):
            nbr_joueur = 2
        elif ev in pixel_vers_case(340, 420, 410, 520):
            nbr_joueur = 3
        elif ev in pixel_vers_case(490, 420, 560, 520):
            nbr_joueur = 4
        """
        if (ev[0] ==1 or ev[0] ==2) and (ev[1] == 9 or ev[1] ==10) :
            nbr_joueur = 1
        elif (ev[0] ==4 or ev[0] ==5) and (ev[1] == 9 or ev[1] ==10) :
            nbr_joueur = 2
        elif (ev[0] ==7 or ev[0] ==8) and (ev[1] == 9 or ev[1] ==10) :
            nbr_joueur = 3
        elif (ev[0] ==10 or ev[0] ==11) and (ev[1] == 9 or ev[1] ==10) :
            nbr_joueur = 4
    return nbr_joueur

def consigne():
    nbr_joueur = 0
    texte(170-50,80,"Comment jouer ?", couleur="black", taille=30)
    texte(90-50,150,"Chaque tirettes dispose de 3 états,", couleur="black", taille=20)
    texte(65-50,185,"pour en bouger une, vous devez cliquer", couleur="black", taille=20)
    texte(65-50,220,"sur le bout de la tirette, puis sur la case", couleur="black", taille=20)
    texte(110-50,255,"d'arrivée de la tirette souhaitée.", couleur="black", taille=20)
    texte(55-55, 310, "Combien de joueurs y a-t-il ?", couleur="black", taille=30)
    attente(1)
    #rectangle(40, 420, 110, 520, couleur="red", tag="rec1")
    texte(40, 400, "1", couleur="black", taille=100, tag="n1")
    attente(0.5)
    #rectangle(190, 420, 260, 520, couleur="red", tag="rec2")
    texte(190, 400, "2", couleur="black", taille=100, tag="n2")
    attente(0.5)
    #rectangle(340, 420, 410, 520, couleur="red", tag="rec3")
    texte(340, 400, "3", couleur="black", taille=100, tag="n3")
    attente(0.5)
    #rectangle(490, 420, 560, 520, couleur="red", tag="rec4")
    texte(490, 400, "4", couleur="black", taille=100, tag="n4")
    attente(0.5)
    texte(40, 20, "j1", couleur="red", taille=40, tag="n1")
    texte(190, 20, "j2", couleur="blue", taille=40, tag="n2")
    texte(340, 20, "j3", couleur="yellow", taille=40, tag="n3")
    texte(490, 20, "j4", couleur="green", taille=40, tag="n4")
    
    #j1 = red, j2 = blue, j3 = yellow, j4 = green
    while nbr_joueur == 0:
        ev = donne_ev()
        tev = type_ev(ev)

        if tev == "ClicGauche":
            if abscisse(ev) in range(40, 111) and ordonnee(ev) in range(420, 521):
                nbr_joueur = 1
                print("D'accord, il y a donc", nbr_joueur,"joueur dans cette partie")

            if abscisse(ev) in range(190, 261) and ordonnee(ev) in range(420, 521):
                nbr_joueur = 2
                print("D'accord, il y a donc", nbr_joueur,"joueurs dans cette partie")

            if abscisse(ev) in range(340, 411) and ordonnee(ev) in range(420, 521):
                nbr_joueur = 3
                print("D'accord, il y a donc", nbr_joueur,"joueurs dans cette partie")

            if abscisse(ev) in range(490, 561) and ordonnee(ev) in range(420, 521):
                nbr_joueur = 4
                print("D'accord, il y a donc", nbr_joueur,"joueurs dans cette partie")
        
        mise_a_jour()
    texte(10, 550, ("D'accord, il y a donc "+ str(nbr_joueur)), couleur="black", taille=20)
    texte(10, 575, ( "joueur.s dans cette partie"), couleur="black", taille=20)
    attente(1)
    #efface("rec1")
    efface("n1")
    attente(0.5)
    #efface("rec2")
    efface("n2")
    attente(0.5)
    #efface("rec3")
    efface("n3")
    attente(0.5)
    #efface("rec4")
    efface("n4")
    attente(0.5)

    efface_tout()
    return nbr_joueur
"""
def consigne():
    nbr_joueur = 0
    texte(170,80,"Comment jouer ?", couleur="black", taille=30)
    texte(90,150,"Chaque tirettes dispose de 3 états,", couleur="black", taille=20)
    texte(65,185,"pour en bouger une, vous devez cliquer", couleur="black", taille=20)
    texte(65,220,"sur le bout de la tirette, puis sur la case", couleur="black", taille=20)
    texte(110,255,"d'arrivée de la tirette souhaitée.", couleur="black", taille=20)
    texte(55, 310, "Combien de joueurs y a-t-il ?", couleur="black", taille=30)
    attente(1)
    #rectangle(40, 420, 110, 520, couleur="red", tag="rec1")
    texte(40, 400, "1", couleur="black", taille=100, tag="n1")
    attente(0.5)
    #rectangle(190, 420, 260, 520, couleur="red", tag="rec2")
    texte(190, 400, "2", couleur="black", taille=100, tag="n2")
    attente(0.5)
    #rectangle(340, 420, 410, 520, couleur="red", tag="rec3")
    texte(340, 400, "3", couleur="black", taille=100, tag="n3")
    attente(0.5)
    #rectangle(490, 420, 560, 520, couleur="red", tag="rec4")
    texte(490, 400, "4", couleur="black", taille=100, tag="n4")
    attente(0.5)
    while nbr_joueur == 0:
        ev = donne_ev()
        tev = type_ev(ev)

        if tev == "ClicGauche":
            if abscisse(ev) in range(40, 111) and ordonnee(ev) in range(420, 521):
                nbr_joueur = 1
                print("D'accord, il y a donc", nbr_joueur,"joueur dans cette partie")

            if abscisse(ev) in range(190, 261) and ordonnee(ev) in range(420, 521):
                nbr_joueur = 2
                print("D'accord, il y a donc", nbr_joueur,"joueurs dans cette partie")

            if abscisse(ev) in range(340, 411) and ordonnee(ev) in range(420, 521):
                nbr_joueur = 3
                print("D'accord, il y a donc", nbr_joueur,"joueurs dans cette partie")

            if abscisse(ev) in range(490, 561) and ordonnee(ev) in range(420, 521):
                nbr_joueur = 4
                print("D'accord, il y a donc", nbr_joueur,"joueurs dans cette partie")

        mise_a_jour()

    attente(1)
    #efface("rec1")
    efface("n1")
    attente(0.5)
    #efface("rec2")
    efface("n2")
    attente(0.5)
    #efface("rec3")
    efface("n3")
    attente(0.5)
    #efface("rec4")
    efface("n4")
    attente(0.5)

    efface_tout()
"""

###########################################################################
if __name__ == '__main__':
    etat_tirette={'o0':1,
                  'o1':1,
                  'o2':1,
                  'o3':1,
                  'o4':1,
                  'o5':1,
                  'o6':1,
                  'b0':1,
                  'b1':1,
                  'b2':1,
                  'b3':1,
                  'b4':1,
                  'b5':1,
                  'b6':1,
                  }
    
    grillex=taille_fenetre/13
    grilley=taille_fenetre/13
    player=0
    joueur1=True
    joueur2=True
    joueur3=True
    joueur4=True
    
    #je_veux_lire(a)

    #je_veux_lire(b)

    #je_veux_lire(affiche_plateau(bouge_tirette(a)))

    tab=tableau()
    sup= bille_tombe(tab)
    #print (sup)
    #print (len(sup))



    tab=supprime_bille(tab,sup)
    

    tabgraph=affiche_plateau(tab)
    #print (tabgraph)
    cree_fenetre(taille_fenetre, taille_fenetre)
    nbr_joueurs=consigne()
    print (nbr_joueurs)
    if nbr_joueurs<4:
        joueur4 = False
    if nbr_joueurs<3:
        joueur3 = False
    if nbr_joueurs<2:
        joueur2 = False
    print (joueur1, joueur2, joueur3, joueur4)
    #dessiner_plateau()
    #dessine_jeu(tabgraph)
    
    #mise_a_jour()
    #hori = blanc / vert = orange
    sup= bille_tombe(tab)
    tab=supprime_bille(tab,sup)
    tabgraph=affiche_plateau(tab)
    dessiner_plateau()
    affiche_tirettes(etat_tirette)
    dessine_jeu(tabgraph,tab)
    lstbille=choisit_bille(nbr_joueurs,tabgraph,tab)
    #print(lstbille)
    for i in range(5):
        for j in range(nbr_joueurs):
            #(tab[lstbille[j][0]])([lstbille[j][1]])["j"+str(j+1)]=True
            tab[int(lstbille[j][i][0]-3)][int(lstbille[j][i][1]-3)]["balle"]["j"+str(j+1)]=True
    #print(tab)
    jouer = True
    while jouer:
        efface_tout()
        sup= bille_tombe(tab)
        tab=supprime_bille(tab,sup)
        tabgraph=affiche_plateau(tab)
        dessiner_plateau()
        affiche_tirettes(etat_tirette)
        dessine_jeu(tabgraph,tab)
        texte(1,1, ("veuillez choisir votre tirette"), taille=20,tag="temp")
        if player == 1:
            texte(1,13*44, ("C'est au tour du joueur 1"), taille=20,couleur='red')
        elif player == 2:
            texte(1,13*44, ("C'est au tour du joueur 2"), taille=20,couleur='blue')
        elif player == 3:
            texte(1,13*44, ("C'est au tour du joueur 3"), taille=20,couleur='yellow')
        elif player == 4:
            texte(1,13*44, ("C'est au tour du joueur 4"), taille=20,couleur='green')
        mise_a_jour()
        if not(reste_billes(tab)):
                jouer = not(jouer)
        if nbr_joueurs >1:
            v=0 #pour déterminer la victoire
            if joueur1:
                v+=1
            if joueur2:
                v+=1
            if joueur3:
                v+=1
            if joueur4:
                v+=1
            if v == 1:
                jouer = not(jouer)
        
        ev = donne_ev()
        ty = type_ev(ev)
        if ty == 'Quitte':
            ferme_fenetre()
            jouer = False
        elif ty == 'ClicGauche':
        #else:
            efface_tout()
            
            player+=1
            if player > nbr_joueurs:
                player=1
            if player == 1 and not joueur1:
                player+=1
            if player == 2 and not joueur2:
                player+=1
            if player == 3 and not joueur3:
                player+=1
            if player == 4 and not joueur4:
                player+=1
            if player > nbr_joueurs:
                player=1
            if player == 1 and not joueur1:
                player+=1
            print (player)
            rj=reste_joueur(tab,player) #rj = reste joueur
            print(rj)
            if player == 1:
                joueur1=rj
            elif player == 2:
                joueur2=rj
            elif player == 3:
                joueur3=rj
            elif player == 4:
                joueur4=rj
            print (joueur1, joueur2, joueur3, joueur4)
            dessiner_plateau()
            affiche_tirettes(etat_tirette)
            dessine_jeu(tabgraph,tab)
            efface("temp")
            mise_a_jour()
            texte(1,1, ("veuillez cliquer sur la nouvelle position de votre tirette"), taille=15)
            #print('Clic gauche :', abscisse(ev), ordonnee(ev))
            
            act=pixel_vers_case(abscisse(ev), ordonnee(ev),grillex,grilley) #action, la case touchée
            #print (act)
            ev1=attend_clic_gauche()
            
            #ev=donne_ev()
            act1=pixel_vers_case(ev1[0],ev1[1],grillex,grilley)
            nouvplat=bouge_tirette(tab,act,act1)
            tabgraph=affiche_plateau(nouvplat[0])
            dessine_jeu(tabgraph,nouvplat[0])
            #je_veux_lire(tabgraph)
            #print (nouvplat[1],nouvplat[2],nouvplat[3])
            #print(nouvplat[0])
            if nouvplat[1] == 1:
                if nouvplat[3] == 1:
                    etat_tirette["o"+str(nouvplat[2])]+=1
                else:
                    etat_tirette["o"+str(nouvplat[2])]-=1
            else:
                if nouvplat[3] == 1:
                    etat_tirette["b"+str(nouvplat[2])]+=1
                else:
                    etat_tirette["b"+str((nouvplat[2]))]-=1
            for elt in etat_tirette:
                if etat_tirette[elt] not in(0,1,2):
                    if nouvplat[1] == 1:
                        if nouvplat[3] == 1:
                            etat_tirette["o"+str(nouvplat[2])]-=1
                            tab=decale_gauche(nouvplat[0],'orange',nouvplat[2])
                        else:
                            etat_tirette["o"+str(nouvplat[2])]+=1
                            tab=decale_droite(nouvplat[0],'orange',nouvplat[2])
                    else:
                        if nouvplat[3] == 1:
                            etat_tirette["b"+str(nouvplat[2])]-=1
                            tab=decale_bas(nouvplat[0],'blanc',nouvplat[2])
                        else:
                            etat_tirette["b"+str((nouvplat[2]))]+=1
                            tab=decale_haut(nouvplat[0],'blanc',nouvplat[2])
                    print("vous ne pouver pas tirer/pouser plus loin")
                    
                    
                    
            #return plateau,orientation(1=vert),nbr_ligne,sens
    """
    efface_tout()
    dessiner_plateau()
    mise_a_jour()
    """
    #texte(1,taille_fenetre//3, ("GG"), taille=200)
    efface_tout()
    dessiner_plateau()
    attente(1)
    mise_a_jour()
    if nbr_joueurs ==1:
        texte(210,70, ("Fin"), taille=100)
        texte(225,210, ("de"), taille=100)
        texte(140, 350, ("partie"), taille=100)
        mise_a_jour()
        attente(4)
        ferme_fenetre()
    else:
        if joueur1:
            texte(210-150,70+30, ("Le Joueur 1"), taille=40)
            texte(225-150,210+30, ("a gagné"), taille=40)
        if joueur2:
            texte(210-150,70+30, ("Le Joueur 2"), taille=40)
            texte(225-150,210+30, ("a gagné"), taille=40)
        if joueur3:
            texte(210-150,70+30, ("Le Joueur 3"), taille=40)
            texte(225-150,210+30, ("a gagné"), taille=40)
        if joueur4:
            texte(210-150,70+30, ("Le Joueur 4"), taille=40)
            texte(225-150,210+30, ("a gagné"), taille=40)
    mise_a_jour()

    #import doctest
    #doctest.testmod()
