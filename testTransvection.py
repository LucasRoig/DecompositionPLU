#Lucas Roig
#Test Transvection
import permutation
import transvection
import decomposition
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

@test
def test_matrice_transvection():
    nbErreur = 0
    for i in range(2,20):
        lig = random.randint(0, i-1)
        col = random.randint(0, i-1)
        a = random.randint(1, 10)
        while col == lig :
            col = random.randint(0, i-1)
        mat = transvection.matrice_transvection(lig, a, col, i)
        resLig =[j for j in range(len(mat)) if mat[j].count(0) != len(mat)-1][0]
        resCol =[j for j in range(len(mat)) if mat[resLig][j] != 0 and j != resLig][0]
        resTaille = len(mat)
        resA = mat[resLig][resCol]
        if not all([resLig == lig, resCol == col, resTaille == i, resA == a]):
            nbErreur += 1
            print "Erreur lors du test de matrice_transvection(", lig, ",", a, ",", col, ",", i, ")"
    return nbErreur

@test
def test_transvection_associee():    
    nbErreur = 0
    for i in range(2, 20):
        lig = random.randint(0, i-1)
        col = random.randint(0, i-1)
        while col == lig :
            col = random.randint(0, i-1)
        a = random.randint(1, 10)
        mat = transvection.matrice_transvection(lig, a, col, i)
        upletT = transvection.transvection_associee(mat)
        if not all([upletT[0] == lig, upletT[1] == a, upletT[2] == col, upletT[3] == i]):
            nbErreur += 1
            print "Erreur lors du test de transvection_associee(", mat, ")"
    return nbErreur

@test
def test_est_transvection():
    nbErreur = 0
    for i in range(2, 20):
        lig = random.randint(0, i-1)
        col = random.randint(0, i-1)
        while col == lig :
            col = random.randint(0, i-1)
        a = random.randint(1, 10)
        mat = transvection.matrice_transvection(lig, a, col, i)
        if not transvection.est_transvection(mat):
            nbErreur += 1
            print "Erreur lors du test de est_transvection(", mat , ")"
    listeMatrice = []
    listeResultAttendu = []
    listeMatrice.append([[1,0,0],[0,1,0],[0,0,1]])
    listeResultAttendu.append(False)
    listeMatrice.append([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
    listeResultAttendu.append(False)
    listeMatrice.append([[0,0],[0,0]])
    listeResultAttendu.append(False)
    listeMatrice.append([[1,0],[1,0]])
    listeResultAttendu.append(False)
    listeMatrice.append([[1,1,1],[0,1,0],[0,0,1]])
    listeResultAttendu.append(False)
    listeMatrice.append([[1,1,0],[0,1,0],[0,0,0]])
    listeResultAttendu.append(False)
    for i, mat in enumerate(listeMatrice):
        if not transvection.est_transvection(mat) == listeResultAttendu[i]:
            nbErreur += 1
            print "Erreur lors du test de est_transvection(", mat , "). Le resutat attendu est", listeResultAttendu[i]
    return nbErreur

@test
def test_matrice_transvection_inverse():
    nbErreur = 0
    for i in range(2,20):
        mat = decomposition.matrice_identite(i)
        j = random.randint(0,i-1)
        k = random.randint(0,i-1)
        while (k==j):
            k = random.randint(0,i-1)
        c = random.randint(1,10)
        mat[j][k] = c
        mat2 = [lig[:] for lig in mat]
        mat2 = transvection.matrice_transvection_inverse(mat2)
        if (transvection.matrice_transvection_inverse(mat2) != mat):
            nbErreur += 1
            print "Erreur lors du test de ", mat
    return nbErreur
        
@test
def test_produit_transvection_g():
    nbErreur = 0
    for i in range(2,20):
        mat = permutation.matrice_aleatoire(i);
        matSave = [lig[:] for lig in mat]
        j = random.randint(0,i-1)
        k = random.randint(0,i-1)
        alpha = random.randint(-10, 10)
        while(k==j):
            k=random.randint(0,i-1)
        mTransvec = transvection.matrice_transvection(j, alpha, k, i)
        mat = transvection.produit_transvection_g(mTransvec, mat)
        if not(all([(mat[j][l] == matSave[j][l]+matSave[k][l]*alpha) for l in range(len(mat))])):
            print "erreur lors du test de :"
            print "mat = ", matSave
            print "i =", j
            print "j =", k
            print "alpha =", alpha
            print ""
            nbErreur +=1
    return nbErreur

@test
def test_produit_transvection_d():
    nbErreur = 0
    for i in range(2,20):
        mat = permutation.matrice_aleatoire(i);
        matSave = [lig[:] for lig in mat]
        j = random.randint(0,i-1)
        k = random.randint(0,i-1)
        alpha = random.randint(-10, 10)
        while(k==j):
            k=random.randint(0,i-1)
        mTransvec = transvection.matrice_transvection(j, alpha, k, i)
        mat = transvection.produit_transvection_d(mTransvec, mat)
        if not(all([(mat[l][j] == matSave[l][j]+matSave[l][k]*alpha) for l in range(len(mat))])):
            print "erreur lors du test de :"
            print "mat = ", matSave
            print "i =", j
            print "j =", k
            print "alpha =", alpha
            print "le resultat obtenu est :", mat
            print ""
            nbErreur +=1
    return nbErreur