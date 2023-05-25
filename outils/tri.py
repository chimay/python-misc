#! /usr/bin/env python
# -*- coding: utf-8 -*-

# {{{ Importations

#import outils.liste as outiliste

#import historique

#import pstats, cProfile

# }}}

# ==============================================================================

# {{{ Raccourcis

#outiliste = historique.outiliste

# }}}

# ==============================================================================

# {{{ Fonctions

#estListeOuTuple = outiliste.estListeOuTuple

# }}}

# ==============================================================================

# {{{ Variables

precision = 4

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ triage

def triage(liste) :

	couples = [(elt, ind) for ind, elt in enumerate(liste)]
	couples.sort()

	return [ind for (elt, ind) in couples], [elt for (elt, ind) in couples]

# }}}

# ========================================================================

# {{{ trirapide

# Adaptation d'une fonction trouvée sur la page :
#
# http://python.jpvweb.com/mesrecettespython/tri_rapide
#
# Merci à l'auteur :)

def trirapide(liste, **dictionnaire) :

	"""
	Tri rapide (quicksort)
	"""

	# Fonction récursive

	def crible(liste, gauche, droite) :

		centre = (gauche + droite) // 2

		pivot = liste[centre]

		i = gauche
		j = droite

		while True:

			while liste[i] < pivot : i += 1

			while liste[j] > pivot : j -= 1

			if i > j : break

			if i < j :
				liste[i], liste[j] = liste[j], liste[i]
				if indices : coordonnees[i], coordonnees[j] = coordonnees[j], coordonnees[i]

			i += 1
			j -= 1

		if gauche < j : crible(liste, gauche, j)
		if i < droite : crible(liste, i, droite)

	# Fonction récursive inverse

	def cribleInverse(liste, gauche, droite) :

		centre = (gauche + droite) // 2

		pivot = liste[centre]

		i = gauche
		j = droite

		while True:

			while liste[i] > pivot : i += 1

			while liste[j] < pivot : j -= 1

			if i > j : break

			if i < j :
				liste[i], liste[j] = liste[j], liste[i]
				if indices : coordonnees[i], coordonnees[j] = coordonnees[j], coordonnees[i]

			i += 1
			j -= 1

		if gauche < j : cribleInverse(liste, gauche, j)
		if i < droite : cribleInverse(liste, i, droite)

	# Arguments

	copie = True
	indices = True
	sens = 1

	cles = dictionnaire.keys()

	if 'copie' in cles : copie = dictionnaire['copie']
	if 'indices' in cles : indices = dictionnaire['indices']
	if 'sens' in cles : sens = dictionnaire['sens']

	# Code

	if copie : L = list(liste)
	else : L = liste

	gauche = 0
	droite = len(L) - 1

	if indices : coordonnees = range(len(liste))

	if sens > 0 : crible(L, gauche, droite)
	else : cribleInverse(L, gauche, droite)

	if indices : return coordonnees, L
	else : return L

# }}}

# ========================================================================

# {{{ dichotomie

# Adaptation d'une fonction trouvée sur la page :
#
# http://python.jpvweb.com/mesrecettespython/tri_rapide
#
# Merci à l'auteur :)

def dichotomie(valeur, liste, comparaison = cmp, cle = lambda c : c) :

	i, j = 0, len(liste) -1

	while i < j :

		k = (i + j) // 2

		if comparaison( valeur, cle(liste[k]) ) <= 0 : j = k
		else : i = k + 1

	return i

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ Par défaut

#retracements = retracementsFibonacci

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{  profil

def profil(dictionnaire) :

	journalier = dictionnaire['journalier']

	cProfile.run('fonction(...)', 'profil')

	p = pstats.Stats('profil')

	#p.sort_stats('time').print_stats()
	p.sort_stats('cumulative').print_stats()

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ main

if __name__ == '__main__' :

	import pylab

	liste = range(29)
	pylab.shuffle(liste)

	indices, listeTriee = trirapide(liste, sens = 1, indices = True, copie = True)

	print 'Liste : ', liste
	print 'Liste triée : ', listeTriee
	print 'Indices : ', indices
	print 'Liste[Indices] : ', [liste[e] for e in indices]

	import random

	valeur = random.randint(0, 28)
	liste = range(29)

	print 'Dichotomie : '
	print liste
	print valeur, dichotomie(valeur, liste)

	pass

# }}}
