#! /usr/bin/env python
# -*- coding: utf-8 -*-

# {{{ Importations

import optim

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ estListeOuTuple

def estListeOuTuple(x) : return isinstance(x, (list, tuple))

# }}}

# ========================================================================

# {{{ estImbrique

def estImbrique(x) :

	if not isinstance(x, (list, tuple)) : return False

	return isinstance(x[0], (list, tuple))

# }}}

# ========================================================================

# {{{ profondeur

def profondeur(x) :

	"""
	Profondeur d'après la première entrée
	"""

	if not isinstance(x, (list, tuple)) : return 0
	else : return 1 + profondeur(x[0])

# }}}

# ========================================================================

# {{{ profondeurMax

def profondeurMax(x) :

	"""
	Profondeur maximale
	"""

	if not isinstance(x, (list, tuple)) : return 0
	else :
		Prof = [ profondeurMax(elt) for elt in x ]
		return 1 + max(Prof)

# }}}

# ========================================================================

# {{{ profondeurMin

def profondeurMin(x) :

	"""
	Profondeur minimale
	"""

	if not isinstance(x, (list, tuple)) : return 0
	else :
		Prof = [ profondeurMin(elt) for elt in x ]
		return 1 + min(Prof)

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ etend

def etend(longueur, liste, valeur, sens = 1) :

	if longueur > len(liste) :

		diff = longueur - len(liste)
		extension = [valeur] * diff

		L = liste[:]

		if sens > 0 : L.extend(extension)
		else :
			extension.extend(L)
			L = extension

	return L

# }}}

# ========================================================================

# {{{ enleve

def enleve(delai, donnees, sens = 1) :

	if not estListeOuTuple(donnees[0]) :

		if sens >= 0 : return donnees[delai:]
		else : return donnees[:-delai]

	if isinstance(donnees, tuple) : D = list(donnees)
	else : D = donnees

	for i in range(len(D)) :
		if isinstance(D[i], tuple) : D[i] = list(D[i])

	if sens >= 0 :
		for i in range(len(D)) : D[i] = D[i][delai:]
	else :
		for i in range(len(D)) : D[i] = D[i][:-delai]

	return D

# }}}

# ========================================================================

# {{{ tronque

def tronque(Ndonnees, donnees, sens = 1) :

	if not estImbrique(donnees) :

		if sens >= 0 : return donnees[:Ndonnees]
		else : return donnees[-Ndonnees:]

	if isinstance(donnees, tuple) : D = list(donnees)
	else : D = donnees

	for i in range(len(D)) :
		if isinstance(D[i], tuple) : D[i] = list(D[i])

	if sens >= 0 :
		for i in range(len(D)) : D[i] = D[i][:Ndonnees]
	else :
		for i in range(len(D)) : D[i] = D[i][-Ndonnees:]

	return D

# }}}

# ========================================================================

# {{{ ajusteLongueurs

def ajusteLongueurs(listes, sens = 1) :

	if len(listes) == 1 : return listes

	elif len(listes) == 2 :

		l1 = listes[0][:]
		l2 = listes[1][:]

		N1 = len(l1)
		N2 = len(l2)
		decalage = abs(N1 - N2)

		if sens >= 0 :

			if N1 > N2 : l1 = l1[decalage:]
			elif N1 < N2 : l2 = l2[decalage:]

		elif sens < 0 :

			if N1 > N2 : l1 = l1[:-decalage]
			elif N1 < N2 : l2 = l2[:-decalage]

		return l1, l2

	else :

		longueurs = [len(l) for l in listes]

		indice = optim.argmin(longueurs)

		ListeMin = listes[indice]

		l = []

		for i in range(len(listes)) :

			l.append(
				ajusteLongueurs([listes[i], ListeMin], sens)[0]
			)

		return l

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ produitScalaire

def produitScalaire(l, m) :

	a = 0.0

	for i in range(len(l)) : a += l[i] * m[i]

	return a

# }}}

# ========================================================================

# {{{ norme2

def norme2(l) :

	a = 0.0

	for i in range(len(l)) : a += l[i] * l[i]

	return a ** 0.5

# }}}

# ========================================================================

# {{{ moyenne2

def moyenne2(l) :

	a = 0.0

	longueur = len(l)

	for i in range(longueur) : a += l[i] * l[i]

	return (a / longueur) ** 0.5

# }}}

# ========================================================================

# {{{ produitTensoriel

def produitTensoriel(l, m) :

	return [(x,y) for x in l for y in m]

# }}}

# ==============================================================================

# {{{ intervalles

def intervalles(liste) :

	N = len(liste)

	return [ liste[i] - liste[i - 1] for i in range(1, N) ]

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ transposee

def transposee(matrice) :

	return [ [ liste[i] for liste in matrice ] for i in range(len(matrice[0])) ]

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ sommesPartielles

def sommesPartielles(liste) :

	l = []
	somme = 0.0

	for i in range(len(liste)) :

		somme = somme + liste[i]
		l.append(somme)

	return l

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ main

if __name__ == '__main__' :

	print estImbrique(1)
	print estImbrique([1, 2])
	print estImbrique([range(2), range(2)])
	print estImbrique([ [range(2), range(2)] , [range(2), range(2)] ])

	print profondeur(1)
	print profondeur([1, 2])
	print profondeur([range(2), range(2)])
	print profondeur([ [range(2), range(2)] , [range(2), range(2)] ])
	print ''
	print profondeur([ [range(2), range(2)] , 2 ])
	print profondeur([ 2 , [range(2), range(2)] ])
	print ''
	print profondeurMax([ [range(2), range(2)] , 2 ])
	print profondeurMax([ 2 , [range(2), range(2)] ])
	print ''
	print profondeurMin([ [range(2), range(2)] , 2 ])
	print profondeurMin([ 2 , [range(2), range(2)] ])

	print ''
	print ''

	print etend(10, range(5), 3)
	print etend(10, range(5), 3, 1)
	print etend(10, range(5), 3, -1)

	pass

# }}}
