#Roig Lucas
#Test Applications
import applications
import permutation
import itertools
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

def determinant(m,j):
    #m : une matrice carree
    #j : la colonne selon laquelle calculer le determinant
    #R : le determinant de la matrice
    if len(m) == 1 :return m[0][0] 
    else :
        det = 0
        for i in range(len(m)):
            det += ((-1)**(i+j))*m[i][j]*determinant(mineure(m, i, j),0)
        return det

def mineure(m,i,j):
    #m : matrice n*p#m : matrice n*p
    #i : num ligne, 0<= i < len(m)
    #j : num colonne, 0<=j<len(m[0])
    #R : la matrice mineure i,j de m
    
    mat = [lig[:] for lig in m]
    mat.pop(i)
    for i in range (len(mat)):
        mat[i].pop(j)
    return mat

#Pour tester la fonction determinant_plu on compare ses resultats avec ceux de la 
#fonction calculant le determinant de maniere recursive
@test
def test_determinant_plu():
    nbErreur = 0
    # On utilise ici l'algorithme de calcul du determinant recursif
    # on doit donc se limiter a des matrices de petite taille
    for i in range(1, 5):
        mat = permutation.matrice_aleatoire(i)
        if determinant(mat, 0) != round(applications.determinant_plu(mat),0):
            nbErreur += 1
            print "Erreur lors du test de ", mat
            print ""
    #Test avec des matrices necessitants des permutations
    listMat =[]
    listMat.append([[2,4,2,0],[1,3,1,0],[1,2,1,3],[1,2,2,1]])
    listMat.append([[0,4,2,0],[1,3,1,0],[1,2,1,3],[1,2,2,1]])
    listMat.append([[0,3,1,0],[2,4,2,0],[1,2,1,3],[1,2,2,1]])
    for mat in listMat:
        if determinant(mat, 0) != round(applications.determinant_plu(mat),0):
            nbErreur += 1
            print "Erreur lors du test de ", mat
            print ""
    return nbErreur

def liste_egale(l1,l2):
    return len(l1) == len(l2) and all([round(l1[i],5) == round(l2[i],5) for i in range(len(l1))])
@test
def test_resolution_tri_sup_cramer():
    nbErreur = 0
    listeA = []
    listeB = []
    listeRes = []
    listeA.append([[1,2],[0,1]])
    listeB.append([1,3])
    listeRes.append([-5,3])
    listeA.append([[3,1,2],[0,2,4],[0,0,3]])
    listeB.append([4,5,2])
    listeRes.append([1/2.,7/6.,2/3.])
    listeA.append([[1,2,3,4],[0,1,2,3],[0,0,1,2],[0,0,0,1]])
    listeB.append([1,2,3,4])
    listeRes.append([0,0,-5,4])
    for i, A in enumerate(listeA):
        if not(liste_egale(applications.resolution_tri_sup_cramer(A, listeB[i]),listeRes[i])):
            nbErreur += 1
            print "erreur lors du test de :"
            print "A = ", A
            print "B = ", listeB[i]
            print "Le resultat attendu etait :", listeRes[i]
            print ""
    return nbErreur

@test
def test_resolution_tri_inf_cramer():
    nbErreur = 0
    listeA = []
    listeB = []
    listeRes = []
    listeA.append([[1,0],[2,1]])
    listeB.append([1,3])
    listeRes.append([1,1])
    listeA.append([[1,0,0],[2,3,0],[4,5,1]])
    listeB.append([2,3,1])
    listeRes.append([2,-1/3.,-16/3.])
    listeA.append([[1,0,0,0],[1,2,0,0],[1,2,3,0],[1,2,3,4]])
    listeB.append([4,3,2,1])
    listeRes.append([4,-1/2.,-1/3.,-1/4.])
    for i, A in enumerate(listeA):
        if not(liste_egale(applications.resolution_tri_inf_cramer(A, listeB[i]),listeRes[i])):
            nbErreur += 1
            print "erreur lors du test de :"
            print "A = ", A
            print "B = ", listeB[i]
            print "Le resultat attendu etait :", listeRes[i]
            print ""
    return nbErreur

@test
def test_resolution_cramer():
    nbErreur = 0
    for i in range (2, 20):
        A = permutation.matrice_aleatoire(i)
        while applications.determinant_plu(A) == 0:
            A = permutation.matrice_aleatoire(i)
        B = [random.randint(-10,10) for j in range(i)]
        res = applications.resolution_cramer(A, B)
        erreur = False
        for j in range(i):
            somme = 0
            for k in range(i):
                somme += A[j][k] * res[k]
            if round(somme,0) != B[j] :
                erreur = True
        if erreur:
            nbErreur += 1
            print "erreur lors du test de :"
            print "A = ", A
            print "B = ", B

    #On compare maintenant les resultats obtenus grace a notre algorithme
    #de decomposition a ceux obtenus avec les decompositions de sage
    listeSage=[]
    listeMatrice =[]
    listeB = []

    listeSage.append([[[0,1],[1,0]],[[1,0],[1/2.,1]],[[2,-2],[0,2]]])
    listeMatrice.append([[1,1],[2,-2]])
    listeB.append([1,3])

    listeSage.append([[[0,0,1],[1,0,0],[0,1,0]],[[1,0,0],[2/3.,1,0],[1/3.,0,1]], [[3,6,5],[0,-2,-4/3.],[0,0,-2/3.]]])
    listeMatrice.append([[1,2,1],[3,6,5],[2,2,2]])
    listeB.append([2,5,3])

    for i in range(len(listeSage)):
        P,L,U = listeSage[i]
        res1 = applications.resolution_cramer_avec_plu(P, L, U, listeB[i])
        res2 = applications.resolution_cramer(listeMatrice[i], listeB[i])

        if  not(liste_egale(res1,res2)) :
            nbErreur += 1
            print "erreur lors du test de :"
            print "mat : ",listeMatrice[i]
            print "B :", listeB[i]
            print "Le resultat varie selon la decomposition utilisee"
            print "Le resultat obtenu avec la decomposition de sage est"
            print res1
            print "Le resultat obtenu avec notre de composition est "
            print res2
    return nbErreur

