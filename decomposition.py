#Lucas Roig
#Decomposition

import transvection
import permutation
import operator
import itertools
import time

def matrice_identite(n):
    """n : un entier
    renvoie la matrice identite de taille n"""
    mat = permutation.matrice_nulle(n)
    for i in range(n):
        mat[i][i] = 1
    return mat

def triangulaire_sup(mat):
    """retourne True si mat est une matrice triangulaire superieure
    false sinon"""
    return all([lig[:i].count(0) == i for i,lig in enumerate(mat)])

def triangulaire_inf(mat):
    """retourne True si mat est une matrice triangulaire superieure
    false sinon"""
    return all([lig[i+1:].count(0) == len(mat)-i-1 for i,lig in enumerate(mat)])

def decomposition_plu(mat):
    """mat : une matrice carree
    retourne une liste de trois matrices [P,L,U]
    P, L et U sont solutions du probleme de decomposition en PLU"""
    n = len(mat)
    lig = 0
    col = 0
    P = matrice_identite(n)
    L = matrice_identite(n)
    U = [ligne[:] for ligne in mat]
    listePermutation = []
    while (lig < n) and (col < n):
        pivot = U[lig][col]
        if pivot == 0 :
            try : 
                lp = [i for i, ligne in enumerate(U) if (ligne[col] != 0) and i >= lig][0]
            except :
                col += 1
                lig += 1
                continue
            if lp != lig:
                #conserve chaque permutation effectuee
                listePermutation.append([lig,lp])

                permutation.permutation_ligne(lig, lp, U)
                permutation.permutation_colonne(lig,lp,P)
                pivot = U[lig][col]
        for i in range(lig+1, n):
            L[i][col] = float(U[i][col])/pivot
        transvection.produit_transvection_g_iteratif(lig, col, pivot, U)
        col += 1
        lig += 1
    #permutte les elements de L selon les permutations effectuees precedemment
    for per in listePermutation:
        for i in range(per[0]):
            aux = L[per[0]][i]
            L[per[0]][i] = L[per[1]][i]
            L[per[1]][i] = aux
    return [P,L,U]

