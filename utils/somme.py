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

# {{{ progressionArithmetique

def progressionArithmetique(n) : return n * (n + 1) / 2.0

# }}}

# ==============================================================================

# {{{ progressionQuadratique

def progressionQuadratique(n) : return (2 * n ** 2 + n) * (n + 1) / 6.0

# }}}

# ==============================================================================

# {{{ progressionGeometrique

def progressionGeometrique(a, n) : return ( 1.0 - a ** (n + 1) ) / (1 - a)

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
	print __file__
	N = 200
	print sum(range(1, N + 1)), progressionArithmetique(N)
	p2 = [ e * e for e in range(1, N + 1) ]
	print sum(p2), progressionQuadratique(N)
	N = 12
	a = 1.98
	g = [ a ** e for e in range(N + 1) ]
	print sum(g), progressionGeometrique(a, N)

# }}}
