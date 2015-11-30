#Lucas Roig
#-------Transvection---------
import permutation
import operator
import itertools

def matrice_transvection(i,a,j,taille):
    """Prend en parametre une transvection (i, a, j) correspondant a l'operation
    Li <- Li + aLj avec i != j et renvoie la matrice correspondant a cette
    transvection c'est a dire Id + a E(i,j) de la taille specifiee"""
    mat = permutation.matrice_nulle(taille)
    for lig in range(taille):
        mat[lig][lig] = 1
    mat[i][j] = a
    return mat

def transvection_associee(mTransvec):
    """mTransvec : matrice de transvection
    retourne la transvection associee sous forme (i,a,j,taille)"""
    taille = len(mTransvec)
    try :
        lig = [i for i in range(taille) if mTransvec[i].count(0) != taille-1][0]
        col = [i for i in range(taille) if mTransvec[lig][i] != 0 and i != lig][0]
    except :
        #si on ne trouve rien, la matrice est la matrice identite
        return [0,0,1,taille]
    return [lig, mTransvec[lig][col], col, taille]

def est_transvection(mat):
    """renvoie true si mat est une matrice de transvection false sinon"""
    taille = len(mat)
    if len(mat)!=len(mat[0]):
        return False
    if set([mat[i][i] for i in range(taille)]) != set([1]):
        return False
    return sum([mat[i].count(0) for i in range(taille)]) == taille*(taille-1)-1

def matrice_transvection_inverse(mat):
    """mat : une matrice de transvection
    renvoie l'inverse de mat"""
    taille = len(mat)
    try :
        lig = [i for i in range(taille) if mat[i].count(0) != taille-1][0]
        col = [i for i in range(taille) if mat[lig][i] != 0 and i != lig][0]
    except :
        #Si on ne trouve rien la matrice est la matrice identite
        return mat
    inverse = [mat[i][:] for i in range(taille)]
    inverse[lig][col] *= -1
    return inverse

def produit_transvection_g_uplet(transvection, mat):
    """transvection : un n-uplet de transvection
    mat : une matrice
    renvoie le resultat de matrice_transvection(transvection) * mat"""
    lig1, coef, lig2, taille = transvection
    res = [lig[:] for lig in mat]
    res[lig1] = map(operator.add, res[lig1],map(operator.mul, itertools.repeat(coef,taille), res[lig2]))
    return res

def produit_transvection_g(matTransvection, mat):
    """matTransvection : une matrice de transvection
    mat : une matrice
    renvoie le resultat de mTransvection * mat"""
    upletT = transvection_associee(matTransvection)
    return produit_transvection_g_uplet(upletT, mat)

def produit_transvection_g_iteratif(lig, col, pivot, mat):
    """lig : l'indice d'une ligne
    col : l'indice d'une colonne
    pivot : le pivot
    realise en place les transvection des lignes de lig+1 a len(mat)
    en recalculant le coefficient alpha en fonction de pivot de maniere
    a annuler mat[i][lig] pour i de lig+1 a n-1
    NE DOIT ETRE UTILISEE QUE DANS DECOMPOSITION PLU"""
    n = len(mat)
    for i in range(lig+1, n):
        coef = float(-mat[i][col])/pivot
        mat[i][lig] = 0 #Evite des erreurs d'arrondis
        mat[i][lig+1:] = map(operator.add,mat[i][lig+1:],map(operator.mul, itertools.repeat(coef, n-lig-1),mat[lig][lig+1:]))

def produit_transvection_d(mTransvection, mat):
    """mTransvection : une matrice de transvection
    mat : une matrice
    renvoie le resultat de mat * mTransvection """
    resultat = produit_transvection_g(mTransvection, [list(i) for i in zip(*mat)])
    return [list(i) for i in zip(*resultat)]