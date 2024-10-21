###JOB1
"""
def draw_rectangle(width, height):
    # Dessiner la première ligne
    print("|" + "-" * (width-2) + "|")

    # Dessiner les lignes du milieu
    for _ in range(height-2):
        print("|" + "*" * (width-2) + "|")

    # Dessiner la dernière ligne
    print("|" + "-" * (width-2) + "|")

# Exemple d'utilisation
draw_rectangle(10, 3)
"""

###JOB2
"""

def draw_triangle(height):
    for i in range(height-1):
        
        print("*" * (height - i - 1) + "/" + " " * (2 * i) + "\\")

   
    print("/" + "_" * (2 * (height - 1)) + "\\")


hauteur = int(input("Entrez la hauteur du triangle : "))  
draw_triangle(hauteur)
"""
###JOB3et4???
###JOB5
"""
Un gardien de phare va aux toilettes cinq fois par jour. Or les WC
sont au rez-de-chaussée...
Écrire une fonction qui reçoit en paramètres, le nombre de marches
du phare et la hauteur de chaque marche (en cm), cette fonction
doit calculer combien de mètre le gardien effectué par semaine

pour aller aux toilettes. La sortie du code doit être :
Pour x marches de y cm, le gardien parcourt z.zz m par semaine.
On n'oubliera pas :
➔ Qu’une semaine comporte 7 jours ;
➔ Qu’une fois en bas, le gardien doit remonter ;
➔ Que le résultat est à exprimer en m.
"""
"""
nbr_marches=int(input("nombres de marches : "))
ht_marches=float(input("hauteurs des marches en cm :"))

print("pour",nbr_marches, "marches de" ,ht_marches, "cm le gardien parcourt",((nbr_marches*2) * (ht_marches)*7)*0.01, "m par semaine.")

"""

###Job06
"""
Luke Skywalker, un professeur de Math, fait passer un test et décide de noter
ses élèves sur une échelle allant de 0 à 100 inclus.
Si un étudiant obtient moins de 40 sur 100, il échoue au test.
S'il a plus de 40, il réussit le test. Luke est un professeur fort sympathique et
décide donc d’arrondir à la hausse les notes des étudiants ayant réussi le
test. Mais Luke n’est quand même pas trop gentil. Cet arrondi à la hausse ne
bénéficiera qu’aux étudiants remplissant certains critères, car tout de même,
il ne faut pas exagérer, sans blague.

Le critère est simple : Si un étudiant a eu une note de moins de strictement 3
points de son prochain multiple de 5, alors sa note est arrondie à ce multiple
de 5. Par exemple, un 83 sera arrondi à 85 alors qu’un 82 restera un 82.
Pour simplifier le travail de Luke, écrivez une fonction qui prend en paramètre
une liste de notes et qui renvoie une liste de notes, arrondies comme il se doit,
quand cela est nécessaire.
"""

def arrondir_notes(liste_notes):
    notes_arrondies = []  # Liste pour stocker les notes arrondies

    # Parcourir chaque note dans la liste
    for note in liste_notes:
        if note < 40:
            print("à échoué : ",note)
        else:
            # Calculer le prochain multiple de 5
            prochain_multiple_de_5 = (note // 5 + 1) * 5
            
            # Vérifier si la différence avec le prochain multiple de 5 est inférieure à 3
            if prochain_multiple_de_5 - note < 3:
                # Si c'est le cas, on arrondit
                notes_arrondies.append(prochain_multiple_de_5)
            else:
                # Sinon, on garde la note telle quelle
                notes_arrondies.append(note)
    
    return notes_arrondies

# Exemple d'utilisation
notes = [83, 82, 38, 29, 67, 40, 39]
resultat = arrondir_notes(notes)

print("Notes arrondies :", resultat)


