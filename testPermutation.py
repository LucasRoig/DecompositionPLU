#Lucas Roig
#Tests Permutation
import permutation
import itertools

#Fonction gerant l'affichage du resultat des tests.
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

@test
def test_permutation_aleatoire():
    compte = 0
    for i in range (1,20):
        permut = permutation.permutation_aleatoire(i)
        if set(permut) != set(range(0,i)):
            print "Erreur lors du test de permutation (", i, ")"
            print "Le resultat est : ", permut, "\n"
            compte += 1
    return compte

@test
def test_est_carree():
    nbErreur = 0
    listeMatrice = []
    listeResultat = []
    listeMatrice.append([[1,1],[2,2]])
    listeResultat.append(True)
    listeMatrice.append([[1,1],[1,1],[1,1]])
    listeResultat.append(False)
    listeMatrice.append([[1,1]])
    listeResultat.append(False)
    listeMatrice.append([[1,1,1],[1,1]])
    listeResultat.append(False)
    listeMatrice.append([[1,1,1],[1,1,1],[1,1,1]])
    listeResultat.append(True)
    for i, x in enumerate(listeMatrice):
        if listeResultat[i] != permutation.est_carree(x):
            nbErreur += 1
            print("Erreur lors du test de est_carree(", x,") \n" )
    return nbErreur

@test
def test_matrice_permutation():
    compte = 0
    listeUplet =[]
    listeMatrice =[]
    listeUplet.append([0])
    listeMatrice.append([[1]])
    listeUplet.append([0,1,2])
    listeMatrice.append([[1,0,0],[0,1,0],[0,0,1]])
    listeUplet.append([2,0,1])
    listeMatrice.append([[0,1,0],[0,0,1],[1,0,0]])
    listeUplet.append([2,1,0,3])
    listeMatrice.append([[0,0,1,0],[0,1,0,0],[1,0,0,0],[0,0,0,1]])
    listeUplet.append([4,3,0,1,2])
    listeMatrice.append([[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1],[0,1,0,0,0],[1,0,0,0,0]])
    for i, x in enumerate(listeUplet):
        m = permutation.matrice_permutation(x)
        if (listeMatrice[i] != m) or not(permutation.est_carree(m)):
            compte += 1
            print "Erreur lors du test de matrice_permutation(", x, ") \n"
    return compte

@test
def test_permutation_associee():
    compte = 0
    for i in range(1,20) :
        permut = permutation.permutation_aleatoire(i)
        mat = permutation.matrice_permutation(permut)
        if (permutation.permutation_associee(mat) != permut):
            compte += 1
            print "Erreur lors du test de permutation_associee(", mat, ") \n"
    return compte

@test
def test_est_permutation():
    nbErreur = 0
    #Test avec des matrices de permutation :
    for i in range(1,20) :
        permut = permutation.permutation_aleatoire(i)
        mat = permutation.matrice_permutation(permut)
        if not permutation.est_permutation(mat):
            nbErreur += 1
            print "Erreur lors du test de est_permutation(", mat, ")"
    #Test avec des matrices n'etant pas des matrices de permutation
    listeMatrice = []
    listeMatrice.append([[1,1,1,1],[0,1,0,0],[0,0,1,0],[0,0,0,0]])
    listeMatrice.append([[1,0,0],[0,1,0],[1,0,0]])
    listeMatrice.append([[2,0],[0,1]])
    listeMatrice.append([[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,1,1,1]])
    listeMatrice.append([[-1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
    listeMatrice.append([[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0]])
    listeMatrice.append([[1,0,0],[1,1,0],[0,0,1]])
    listeMatrice.append([[1,0,0,0],[0,1,0],[0,0,1]])
    for mat in listeMatrice :
        if permutation.est_permutation(mat):
            nbErreur += 1
            print "Erreur lors du test de est_permutation(", mat, ")"
    return nbErreur

@test
def test_matrice_permutation_inverse():
    nbErreur = 0
    for i in range(1,20) :
        permut = permutation.permutation_aleatoire(i)
        mat = permutation.matrice_permutation(permut)
        if mat != permutation.matrice_permutation_inverse(permutation.matrice_permutation_inverse(mat)) or not(permutation.est_carree(permutation.matrice_permutation_inverse(mat))):
            nbErreur += 1
            print "Erreur lors du test de matrice_permutation_inverse(", mat, ")"
    return nbErreur

@test
def test_produit_permut_g():
    nbErreur = 0
    #teste avec des matrices aleatoires
    for i in range(1,20) :
        mat = permutation.matrice_aleatoire(i)
        permut = permutation.permutation_aleatoire(i)
        matPermutation = permutation.matrice_permutation(permut)
        result = permutation.produit_permut_g(matPermutation, mat)
        matInversePermut = permutation.matrice_permutation_inverse(matPermutation)
        if permutation.produit_permut_g(matInversePermut, result) != mat:
            nbErreur +=1
            print "Erreur lors du test de produit_permut_g(", matPermutation, ",", mat, ")"
    return nbErreur

@test
def test_produit_permut_d():
    nbErreur = 0
    #teste avec des matrices aleatoires
    for i in range(1,20) :
        mat = permutation.matrice_aleatoire(i)
        permut = permutation.permutation_aleatoire(i)
        matPermutation = permutation.matrice_permutation(permut)
        result = permutation.produit_permut_d(matPermutation,mat)
        matInversePermut = permutation.matrice_permutation_inverse(matPermutation)
        if permutation.produit_permut_d(matInversePermut,result) != mat:
            nbErreur +=1
            print "Erreur lors du test de produit_permut_d(", mat, ",", matPermutation, ")"
    return nbErreur
