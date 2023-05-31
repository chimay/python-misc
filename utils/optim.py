#! /usr/bin/env python
# -*- coding: utf-8 -*-

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ indicesCondition

def indicesCondition(liste, condition) :

	return [
		i
		for i in range(len(liste))
		if condition(liste[i])
	]

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ argmin

def argmin(liste) : return liste.index(min(liste))

# }}}

# ========================================================================

# {{{ argmax

def argmax(liste) : return liste.index(max(liste))

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ argminlagrange

def argminlagrange(liste, indices = []) :
	if indices == [] : indices = range(len(liste))
	sousliste = [ liste[i] for i in indices ]
	minimum = min(sousliste)
	argumentSousListe = sousliste.index(minimum)
	argument = indices[argumentSousListe]
	return argument

# }}}

# ========================================================================

# {{{ argmaxlagrange

def argmaxlagrange(liste, indices = []) :
	if indices == [] : indices = range(len(liste))
	sousliste = [ liste[i] for i in indices ]
	maximum = max(sousliste)
	argumentSousListe = sousliste.index(maximum)
	argument = indices[argumentSousListe]
	return argument

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ argminCondition

def argminCondition(liste, condition) :
	indices = indicesCondition(liste, condition)
	return argminlagrange(liste, indices)

# }}}

# ========================================================================

# {{{ argmaxCondition

def argmaxCondition(liste, condition) :
	indices = indicesCondition(liste, condition)
	return argmaxlagrange(liste, indices)

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ main

if __name__ == '__main__' :

	pass

# }}}
