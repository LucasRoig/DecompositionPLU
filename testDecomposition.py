#Lucas Roig
#Test Decomposition
import permutation
import itertools
import decomposition
import random

def test(fun) :
    nom = ''.join(itertools.dropwhile(lambda x : x != "_",fun.__name__))[1:]
    print "----- Debut du test de", nom, "----- \n"
    nbErreur = fun()
    print "Test de", nom, "termine :"
    if nbErreur == 0 :
        print "Aucune erreur rencontree \n \n"
    elif nbErreur == 1 :
        print "1 erreur rencontree \n \n"
    else :
        print nbErreur, "erreurs rencontrees \n \n"

#Fonction utilisee pour verifier les resultats de decomposition PLU
def produit(m1,m2):
    #m1 une matrice
    #m2 une matrice
    #R : M1*M2
    mat = permutation.matrice_nulle(len(m1))
    for ligne in range(len(mat)) :
        for colonne in range(len(mat[0])) :
            somme = 0 
            for i in range(len(m1[0])) :
                somme += m1[ligne][i] * m2[i][colonne] 
            mat[ligne][colonne] = somme
    return mat

def matrices_egales(m1, m2):
    return all([all([round(m1[j][i],0) == round(m2[j][i],0) for i in range(len(m1[0]))]) for j in range(len(m1))])

@test
def test_decomposition_plu():
    nbErreur = 0
    #Tests avec des matrices aleatoires
    for i in range(2,20):
        mat = permutation.matrice_aleatoire(i)
        PLU = decomposition.decomposition_plu(mat)
        temp = produit(PLU[0], PLU[1])
        res = produit(temp, PLU[2])
        if not(matrices_egales(res,mat)):
            nbErreur += 1
            print "erreur lors du produit de trois matrices", mat
        if not(decomposition.triangulaire_inf(PLU[1])):
            nbErreur += 1
            print "erreur", mat, "L n'est pas triangulaire inferieure"
        if not(decomposition.triangulaire_sup(PLU[2])):
            nbErreur += 1
            print "erreur", mat, "U n'est pas triangulaire superieure"
        if not(permutation.est_carree(PLU[0])):
            nbErreur += 1
            print "erreur", mat, "P n'est pas carree"
        if not(permutation.est_carree(PLU[1])):
            nbErreur += 1
            print "erreur", mat, "L n'est pas carree"
        if not(permutation.est_carree(PLU[2])):
            nbErreur += 1
            print "erreur", mat, "U n'est pas carree"

    #Tests avec des matrices necessitants des permutations:
    for i in range(2, 20):
        mat = permutation.matrice_aleatoire(i)
        lig = random.randint(0, i-2)
        for j in range(i-1):
            mat[lig][j] = 0
        PLU = decomposition.decomposition_plu(mat)
        temp = produit(PLU[0], PLU[1])
        res = produit(temp, PLU[2])
        if not(matrices_egales(res,mat)):
            nbErreur += 1
            print "erreur lors du produit de trois matrices", mat
        if not(decomposition.triangulaire_inf(PLU[1])):
            nbErreur += 1
            print "erreur", mat, "L n'est pas triangulaire inferieure"
        if not(decomposition.triangulaire_sup(PLU[2])):
            nbErreur += 1
            print "erreur", mat, "U n'est pas triangulaire superieure"
        if not(permutation.est_carree(PLU[0])):
            nbErreur += 1
            print "erreur", mat, "P n'est pas carree"
        if not(permutation.est_carree(PLU[1])):
            nbErreur += 1
            print "erreur", mat, "L n'est pas carree"
        if not(permutation.est_carree(PLU[2])):
            nbErreur += 1
            print "erreur", mat, "U n'est pas carree"

    #Test avec des matrices ayant des colonnes nulles
    for i in range(10,20):
        mat = permutation.matrice_aleatoire(i)
        for j in range(0,i):
            mat[j][1] = mat[j][0]
            mat[j][3] = mat[j][2]
            mat[j][5] = mat[j][4]
            mat[0][j] = 0
        PLU = decomposition.decomposition_plu(mat)
        temp = produit(PLU[0], PLU[1])
        res = produit(temp, PLU[2])
        if not(matrices_egales(res,mat)):
            nbErreur += 1
            print "erreur lors du produit de trois matrices", mat
        if not(decomposition.triangulaire_inf(PLU[1])):
            nbErreur += 1
            print "erreur", mat, "L n'est pas triangulaire inferieure"
        if not(decomposition.triangulaire_sup(PLU[2])):
            nbErreur += 1
            print "erreur", mat, "U n'est pas triangulaire superieure"
        if not(permutation.est_carree(PLU[0])):
            nbErreur += 1
            print "erreur", mat, "P n'est pas carree"
        if not(permutation.est_carree(PLU[1])):
            nbErreur += 1
            print "erreur", mat, "L n'est pas carree"
        if not(permutation.est_carree(PLU[2])):
            nbErreur += 1
            print "erreur", mat, "U n'est pas carree"

    #Tests avec des matrices choisies
    listeMatrice = []
    listeMatrice.append([[1,2,1],[3,6,5],[2,2,2]])
    listeMatrice.append([[1,2,1,1],[3,6,5,4],[2,2,2,1],[2,3,4,1]])
    listeMatrice.append([[1,2,1,1],[3,6,3,4],[2,2,2,1],[2,3,4,1]])
    listeMatrice.append([[1,2,1,1],[3,6,3,4],[4,2,4,1],[2,3,4,1]])
    listeMatrice.append([[1,1,1,1,1,1,1,1,1,1],[2,2,2,2,2,2,2,2,2,8],[1,2,4,3,4,4,8,6,2,1],[6,1,2,4,3,7,6,5,3,1],[1,2,4,1,0,0,0,1,4,2],[12,4,3,8,6,1,-3,1,8,8],[8,4,6,3,4,5,2,1,1,1],[-12,3,4,5,0,0,1,3,2,1],[7,7,5,2,1,4,9,6,3,4],[-3,-7,1,2,0,0,8,4,6,7]])
    for mat in listeMatrice :
        PLU = decomposition.decomposition_plu(mat)
        temp = produit(PLU[0], PLU[1])
        res = produit(temp, PLU[2])
        if not(matrices_egales(res,mat)):
            nbErreur += 1
            print "erreur lors du produit de trois matrices", mat
        if not(decomposition.triangulaire_inf(PLU[1])):
            nbErreur += 1
            print "erreur", mat, "L n'est pas triangulaire inferieure"
        if not(decomposition.triangulaire_sup(PLU[2])):
            nbErreur += 1
            print "erreur", mat, "U n'est pas triangulaire superieure"
        if not(permutation.est_carree(PLU[0])):
            nbErreur += 1
            print "erreur", mat, "P n'est pas carree"
        if not(permutation.est_carree(PLU[1])):
            nbErreur += 1
            print "erreur", mat, "L n'est pas carree"
        if not(permutation.est_carree(PLU[2])):
            nbErreur += 1
            print "erreur", mat, "U n'est pas carree"
    return nbErreur

@test
def test_triangulaire_sup():
    nbErreur = 0
    #Genere des matrices triangulaires superieures
    for i in range(2,20):
        mat = permutation.matrice_aleatoire(i)
        for j in range(1,i):
            for k in range(j):
                mat[j][k] = 0
        if not(decomposition.triangulaire_sup(mat)):
            nbErreur += 1
            print "erreur lors du test de", mat
            print "Le resultat attendu etait True"
    #Genere des matrices n'etant pas triangulaires superieures
    for i in range(2,20):
        mat = permutation.matrice_aleatoire(i)
        j = random.randint(1,i-1)
        k = random.randint(0,j-1)
        mat[j][k] = 1
        if decomposition.triangulaire_sup(mat):
            nbErreur += 1
            print "erreur lors du test de", mat
            print "le resultat attendu etait False"
    return nbErreur

@test
def test_triangulaire_inf():
    nbErreur = 0
    #Genere des matrices triangulaires superieures
    for i in range(2,20):
        mat = permutation.matrice_aleatoire(i)
        for j in range(0,i-1):
            for k in range(j+1,i):
                mat[j][k] = 0
        if not(decomposition.triangulaire_inf(mat)):
            nbErreur += 1
            print "erreur lors du test de", mat
            print "Le resultat attendu etait True"
    #Genere des matrices n'etant pas triangulaires superieures
    for i in range(2,20):
        mat = permutation.matrice_aleatoire(i)
        j = random.randint(0,i-2)
        k = random.randint(j+1,i-1)
        mat[j][k] = 1
        if decomposition.triangulaire_inf(mat):
            nbErreur += 1
            print "erreur lors du test de", mat
            print "le resultat attendu etait False"
    return nbErreur


