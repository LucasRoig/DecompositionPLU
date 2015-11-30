#Lucas Roig
#Applications
import decomposition
import operator
import permutation
import random
import time

def determinant_plu(m):
    """m : une matrice carree
    sortie : le determinant de m"""
    
    P, L, U = decomposition.decomposition_plu(m)
    #multiplication des diagonales
    det = reduce(operator.mul, [L[i][i] for i in range(len(L))])
    det *= reduce(operator.mul, [U[i][i] for i in range(len(U))])
    #calcul du nombre de permutation necessaires pour retrouver la matrice identite
    perm = permutation.permutation_associee(P)
    alpha = 0
    i = 0
    while (perm != range(len(P))):
        if perm[i] != i:
            perm[perm.index(i)] = perm[i]
            perm[i] = i
            alpha += 1
        i += 1
    if alpha % 2 != 0 :
        det *= -1
    return det

def resolution_tri_sup_cramer(a,b):
    """a : une matrice triangulaire superieure
    b : une matrice de dimension 1,n
    Le systeme A*X=B doit etre de Cramer
    sortie : la solution de A*X=B"""

    X = []
    i = len(a) - 1
    while i>=0 :
        S = sum(map(operator.mul,[a[i][j] for j in range(i+1, len(a))], X))
        X.insert(0,(b[i] - S)/float(a[i][i]))
        i -= 1
    return X

def resolution_tri_inf_cramer(a,b):
    """a : une matrice triangulaire inferieure
    b : une matrice de dimension 1,n
    Le systeme A*X=B doit etre de Cramer
    sortie : la solution de A*X=B"""

    X = []
    for i in range(len(a)):
        S = sum(map(operator.mul,X,[a[i][j] for j in range(0,i)]))
        X.append((b[i] - S)/float(a[i][i]))
        i -= 1
    return X

def resolution_cramer(a,b):
    """a : une matrice
    b : une liste correspondant au vecteur B dans l'equation AX = B
    Le systeme A*X=B doit etre de Cramer
    sortie : la solution de A*X=B"""

    P, L, U = decomposition.decomposition_plu(a)
    P = permutation.matrice_permutation_inverse(P)
    b = [[b[i]]for i in range(len(b))]
    b = permutation.produit_permut_g(permutation.transpose(P), b)
    b = [b[i][0] for i in range(len(b))]
    Y = resolution_tri_inf_cramer(L, b)
    X = resolution_tri_sup_cramer(U, Y)
    return X
    
#Cette fonction sera utilisee pour comparer les resultats obtenus avec differentes decompositions
def resolution_cramer_avec_plu(P,L,U,b):
    """P : une matrice de permutation
    L : une matrice triangulaire inferieure
    U : une matrice triangulaire superieure
    b : une liste correspondant au vecteur B dans l'equation PLUX = B
    PLUX = B doit etre un systeme de cramer"""

    b = [[b[i]]for i in range(len(b))]
    b = permutation.produit_permut_g(permutation.transpose(P), b)
    b = [b[i][0] for i in range(len(b))]
    Y = resolution_tri_inf_cramer(L, b)
    X = resolution_tri_sup_cramer(U, Y)
    return X