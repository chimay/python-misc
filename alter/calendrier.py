#! /usr/bin/env python
# -*- coding: utf-8 -*-

# {{{ Importations

#import outils.liste as outiliste

#import historique

#import pstats, cProfile

# }}}

# ==============================================================================

# {{{ Raccourcis

#outiliste = historique.outils.liste

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

# {{{ testeTout

def testeTout(dictionnaire) :

	journalierLineaire = dictionnaire['journalierLineaire']
	journalier = dictionnaire['journalier']
	hebdomadaire = dictionnaire['hebdomadaire']
	mensuel = dictionnaire['mensuel']
	trimestriel = dictionnaire['trimestriel']
	annuel = dictionnaire['annuel']

# }}}

# ==============================================================================

# {{{ teste

def teste(dictionnaire) :

	#profil(dictionnaire)

	testeTout(dictionnaire)

# }}}

# ==============================================================================

# {{{ main

if __name__ == '__main__' :

	import os, sys

	arguments = sys.argv

	if len(arguments) > 3 :
		repertoire = arguments[1]
		logarithme = arguments[2]
		actif = arguments[3]
		fichier = arguments[4]
	else :
		repertoire = 'cours/'
		logarithme = 'log-'
		actif = os.getcwd().split('/')[-1] + '-'
		fichier = 'journalier.txt'

	# Linéaire

	journalierLineaire = repertoire + actif + fichier

	# Logarithmique

	journalier = repertoire + logarithme + actif + 'journalier.txt'
	hebdomadaire = repertoire + logarithme + actif + 'hebdomadaire.txt'
	mensuel = repertoire + logarithme + actif + 'mensuel.txt'
	trimestriel = repertoire + logarithme + actif + 'trimestriel.txt'
	annuel = repertoire + logarithme + actif + 'annuel.txt'

	dictionnaire = {
		'journalierLineaire' : journalierLineaire,
		'journalier' : journalier,
		'hebdomadaire' : hebdomadaire,
		'mensuel' : mensuel,
		'trimestriel' : trimestriel,
		'annuel' : annuel
	}

	print 'Traitement', journalierLineaire

	teste(dictionnaire)

# }}}
