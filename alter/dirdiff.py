#! /usr/bin/env python
# -*- coding: utf-8 -*-

# {{{ Importations

import os, sys

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ impression

def impression(fichiers, sortie) :
	fichierSortie = open(sortie, 'w')
	for f in fichiers : fichierSortie.write(f + '\n')

# }}}

# ==============================================================================

# {{{ principal

def principal(arguments) :
	depart = arguments[1]
	arrivee = arguments[2]
	os.chdir(depart)
	fichiersDepart = []
	for chemin, rep, fich in os.walk('.') :
		for elt in fich : fichiersDepart.append(chemin + '/' + elt)
	os.chdir(arrivee)
	fichiersArrivee = []
	for chemin, rep, fich in os.walk('.') :
		for elt in fich : fichiersArrivee.append(chemin + '/' + elt)
	differenceUn = set(fichiersDepart) - set(fichiersArrivee)
	differenceDeux = set(fichiersArrivee) - set(fichiersDepart)
	differenceUn = list(differenceUn)
	differenceDeux = list(differenceDeux)
	for f in differenceUn : print f
	print ''
	print ''
	print ''
	for f in differenceDeux : print f

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ main

if __name__ == '__main__' :
	print __file__
	try :
		import psyco
		psyco.full()
	except ImportError : pass
	arguments = sys.argv
	principal(arguments)

# }}}
