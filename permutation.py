#Lucas Roig
#-------Permutation---------
from random import shuffle
from random import randint
import itertools
import operator

def matrice_aleatoire(taille):
	"""renvoie une matrice aleatoire de la taille specifiee"""
	mat = []
	for i in range(taille) :
		lig = []
		for j in range(taille) :
			lig.append(randint(-100,100))
		mat.append(lig)
	return mat

def est_carree(mat):
	"""mat : une matrice
	Sortie : un booleen, True si la matrice est carree, false sinon"""
	n = len(mat)
	return all([len(lig) == n for lig in mat])
	
def transpose(mat):
	"""renvoie la transposee de mat"""
	return [list(col) for col in zip(*mat)]

def afficher_matrice(mat):
	"""affiche la matrice mat"""
	for lig in mat : print lig

def matrice_nulle(taille):
	"""Renvoie une matrice carree de taille (taille) dont tous les termes sont nuls"""
	return [[0]*taille for i in range(taille)]

def permutation_aleatoire(taille):
	"""Renvoie une liste de longueur taille contenant les entiers de 1 a taille
	dans un ordre aleatoire. La liste represante une permution ecrite
	sous forme de n-uplet"""
	permut = range(0,taille)
	shuffle(permut)
	return permut

def matrice_permutation(permut):
	"""retourne la matrice associee a permut
	permut : une permutation sous forme de n-uplet"""
	mat = matrice_nulle(len(permut))
	for i, x in enumerate(permut):
		mat[x][i] = 1
	return mat

def permutation_associee(mat):
	"""retourne le n-uplet associee a la matrice de permutation mat"""
	return list(zip(*sorted([(lig.index(1),i) for i,lig in enumerate(mat)]))[1])

def est_permutation(mat):
	"""mat : une matrice
	Sortie : un booleen True si mat est une matrice de permutation false sinon"""
	return len(mat) == len(mat[0]) and \
		   all([x.count(0) == len(x)-1 and x.count(1) == 1 for x in mat]) and \
		   set([lig.index(1) for lig in mat]) == set(range(len(mat)))

def matrice_permutation_inverse(mat):
	"""Retourne l'inverse (c'est a dire la transposee) de mat.
	Mat doit etre une matrice de permutation"""
	res = [lig[:] for lig in mat]
	return transpose(res)

def produit_permut_g(matPermut, mat):
	"""matPermut : une matrice de permutation
	mat : une matrice
	matPermut et mat doivent avoir la meme taille
	renvoie le produit matPermut*mat"""
	permut = permutation_associee(matPermut)
	return produit_permut_g_uplet(permut, mat)

def produit_permut_g_uplet(upletPermut, mat):
	"""upletPermut : le n-uplet d'une permutation
	mat : une matrice
	Sortie : Le produit de la matrice correspondant au n-uplet par mat"""
	upletPermut = zip(*sorted([(x,i) for i,x in enumerate(upletPermut)]))[1]
	result = [mat[i][:] for i in upletPermut]
	return result

def produit_permut_d(matPermut, mat):
	"""matPermut : une matrice de permutation
	mat : une matrice
	matPermut et mat doivent avoir la meme taille
	renvoie le produit mat*matPermut"""
	permut = permutation_associee(matPermut)
	return produit_permut_d_uplet(permut, mat)

def produit_permut_d_uplet(upletPermut, mat):
	"""upletPermut : le n-uplet d'une permutation
	mat : une matrice
	Sortie : Le produit de par mat par la matrice correspondant au n-uplet """
	tr = [lig[:] for lig in mat]
	tr = transpose(tr)
	result = [tr[i] for i in upletPermut]
	result = transpose(result)
	return result

def permutation_colonne(col1, col2, mat):
	"""col1 : l'indice d'une colonne de mat
	col2 : l'indice d'une colonne de mat 
	mat : une matrice carree
	Permutte les colonnes col1 et col 2 dans mat
	Utilisee dans decomposition_plu"""
	for i in range(len(mat)):
		aux = mat[i][col1]
		mat[i][col1] = mat[i][col2]
		mat[i][col2] = aux
	return mat

def permutation_ligne(lig1,lig2,mat):
	"""lig1 : l'indice d'une ligne de mat
	lig2 : l'indice d'une ligne de mat
	mat : une matrice carree
	Permutte les lignes lig1 et lig2 dans mat
	Utilisee dans decomposition_plu"""
	aux = mat[lig1]
	mat[lig1] = mat[lig2]
	mat[lig2] = aux
	return mat