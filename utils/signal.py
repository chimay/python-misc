#! /usr/bin/env python
# -*- coding: utf-8 -*-

# {{{ Importations

import opera

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ filtreEchantillonnage

def filtreEchantillonnage(sensDuree, Ndonnees) :
	sens = opera.signe(sensDuree)
	duree = abs(sensDuree)
	if sens == 1 :
		indices = range(1, Ndonnees, duree)

	else :
		indices = range(Ndonnees - 1, -1, -duree)
		indices.reverse()
	return indices

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ main

if __name__ == '__main__' :
	pass

# }}}
