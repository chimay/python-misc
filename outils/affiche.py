#! /usr/bin/env python
# -*- coding: utf-8 -*-

# {{{ Importations

import sys

# }}}

# ==============================================================================

# {{{ Variables

sortieInfo = sys.stderr
sortieDonnees = sys.stdout
#sortie = open('fichier', 'w')

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ information

def information(chaine, **dictionnaire) :

	niveau = 0
	sortie = sortieInfo

	cles = dictionnaire.keys()

	if 'niveau' in cles : niveau = dictionnaire['niveau']
	if 'sortie' in cles : sortie = dictionnaire['sortie']

	debut = '++++ ' + '       ' * niveau + '--> '

	sortie.write(debut)
	sortie.write(chaine)
	sortie.write('\n')

# }}}

# ==============================================================================

# {{{ titre

def titre(chaine, **dictionnaire) :

	car = '#'

	Nligne = 84
	Nlim = 12
	Nesp = 7
	sortie = sortieDonnees

	cles = dictionnaire.keys()

	if 'car' in cles : car = dictionnaire['car']
	if 'Nligne' in cles : Nligne = dictionnaire['Nligne']
	if 'Nlim' in cles : Nlim = dictionnaire['Nlim']
	if 'Nesp' in cles : Nesp = dictionnaire['Nesp']
	if 'sortie' in cles : sortie = dictionnaire['sortie']

	esp = ' '

	ligne = car * Nligne + '\n'

	debut = car * Nlim + esp * Nesp

	Nrestant = Nligne - 2 * len(debut) - len(chaine)

	restant = ' ' * Nrestant

	fin = esp * Nesp + car * Nlim + '\n'

	sortie.write(ligne)
	sortie.write(debut)
	sortie.write(chaine)
	sortie.write(restant)
	sortie.write(fin)
	sortie.write(ligne)
	sortie.write('\n')

# }}}

# ==============================================================================

# {{{ partie

def partie(chaine, **dictionnaire) :

	titre(chaine, car = '#', Nligne = 84, **dictionnaire)

# }}}

# ==============================================================================

# {{{ chapitre

def chapitre(chaine, **dictionnaire) :

	titre(chaine, car = '=', Nligne = 84, **dictionnaire)

# }}}

# ==============================================================================

# {{{ section

def section(chaine, **dictionnaire) :

	car = '-'

	Nligne = 29
	Nesp = 4
	sortie = sortieDonnees

	cles = dictionnaire.keys()

	if 'car' in cles : car = dictionnaire['car']
	if 'Nligne' in cles : Nligne = dictionnaire['Nligne']
	if 'Nesp' in cles : Nesp = dictionnaire['Nesp']
	if 'sortie' in cles : sortie = dictionnaire['sortie']

	esp = ' '

	debut = esp * Nesp
	fin = '\n'
	ligne = car * Nligne + '\n'

	sortie.write(debut)
	sortie.write(chaine)
	sortie.write(fin)
	sortie.write(ligne)
	sortie.write('\n')

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ main

if __name__ == '__main__' :

	pass

# }}}
