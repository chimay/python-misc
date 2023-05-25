#! /usr/bin/env python
# -*- coding: utf-8 -*-

# {{{ Importations

import liste

# }}}

# ========================================================================

# {{{ Fonctions

estListeOuTuple = liste.estListeOuTuple

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ estFonction

def estFonction(f) :
	"""
	Fonction ou classe avec __call__
	"""
	return callable(f)

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ constante

def constante(*a) :
	if len(a) == 1 :
		def f(*x) : return a[0]
	else :
		def f(*x) : return a
	return f

# }}}

# ========================================================================

# {{{ identite

def identite(*a) :
	if len(a) == 1 : return a[0]
	else : return a

# }}}

# ========================================================================

# {{{ superieur

def superieur(a, strict = False) :
	if not strict :
		def f(x) : return x >= a
	else :
		def f(x) : return x > a
	return f

# }}}

# ========================================================================

# {{{ inferieur

def inferieur(a, strict = False) :
	if not strict :
		def f(x) : return x <= a
	else :
		def f(x) : return x < a
	return f

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ composee

def composee(f, g) :
	def h(*a) : return f(g(*a))
	return h

# }}}

# ========================================================================

# {{{ puissance

def puissance(fonction, puis) :
	if puis == 0 : return identite
	if puis == 1 : return fonction
	return composee(
		fonction,
		puissance(fonction, puis - 1)
	)

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ triArguments

def triArguments(*arguments) :
	L = list(arguments)
	Entiers = []
	Flottants = []
	Chaines = []
	Listes = []
	Tuples = []
	Dictionnaires = []
	Autres = []
	ListesEtTuples = []
	while len(L) > 0 :
		elt = L.pop(0)
		if isinstance(elt, int) : Entiers.append(elt)
		elif isinstance(elt, float) : Flottants.append(elt)
		elif isinstance(elt, str) : Chaines.append(elt)
		elif isinstance(elt, list) : Listes.append(elt)
		elif isinstance(elt, tuple) : Tuples.append(elt)
		elif isinstance(elt, dict) : Dictionnaires.append(elt)
		else : Autres.append(elt)
		if estListeOuTuple(elt) : ListesEtTuples.append(elt)
	dico = {}
	dico['Entiers'] = Entiers
	dico['Flottants'] = Flottants
	dico['Chaines'] = Chaines
	dico['Listes'] = Listes
	dico['Tuples'] = Tuples
	dico['Dictionnaires'] = Dictionnaires
	dico['Autres'] = Autres
	dico['ListesEtTuples'] = ListesEtTuples
	return dico

# }}}

# ========================================================================

# {{{ concatenee

def concatenee(*fonctions) :
	def f(*a) :
		r = []
		for fct in fonctions :
			val = fct(*a)
			if estListeOuTuple(val) : r.extend(list(val))
			else : r.append(val)
		return r
	return f

# }}}

# ========================================================================

# {{{ retourIndice

def retourIndice(indice, fonction) :
	if estListeOuTuple(indice) :
		def f(*a) :
			Fa = fonction(*a)
			return [ Fa[i] for i in indice ]
	else :
		def f(*a) : return fonction(*a)[indice]
	return f

# }}}

# ========================================================================

# {{{ argumentConstant

def argumentConstant(fonction, indice, constante) :
	if estListeOuTuple(indice) :
		def f(*a) :
			Nargs = len(a) + len(indice)
			args = [None] * Nargs
			for i in range(len(indice)) :
				args[ indice[i] ] = constante[i]

			var = list(a)
			for i in range(Nargs) :
				if args[i] == None : args[i] = var.pop(0)
			return fonction(*args)
	elif indice == 0 or indice == 'premier' :
		def f(*a) :
			args = [constante]
			args.extend(list(a))
			return fonction(*args)
	elif indice == -1 or indice == 'dernier' :
		def f(*a) :
			args = list(a)
			args.append(constante)
			return fonction(*args)
	else :
		def f(*a) :
			args = list(a[:indice])
			args.append(constante)
			args += a[indice:]
			return fonction(*args)
	return f

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ opUnaireSurListe

def opUnaireSurListe(operation) :
	def f(liste) : return [operation(e) for e in liste]
	return f

# }}}

# ========================================================================

# {{{ opBinaireSurListe

def opBinaireSurListe(operation) :
	def f(a, b) :
		listeA = estListeOuTuple(a)
		listeB = estListeOuTuple(b)
		if listeA and listeB :
			l = [ operation(a[i], b[i]) for i in range(len(a)) ]
		elif listeA :
			l = [operation(e, b) for e in a]
		elif listeB :
			l = [operation(a, e) for e in b]
		return l
	return f

# }}}

# ========================================================================

# {{{ opUnaireSurTableau

def opUnaireSurTableau(operation) :
	return opUnaireSurListe(opUnaireSurListe(operation))

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ periodique

def periodique(liste) :
	L = len(liste)
	def f(indice) :
		i = indice % L
		return liste[i]
	return f

# }}}

# ========================================================================

# {{{ liste2scalaire

def liste2scalaire(fonction) :
	def f(liste) :
		l = liste[:]
		x = 0
		while len(l) > 0 : x = fonction(x, l.pop())
		return x
	return f

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ testeArguments

def testeArguments() :
	def f(*a) :
		ch = ''
		for e in a :
			ch += e
			ch += ' '
		return ch
	g = argumentConstant(f, 0, 'constant')
	print g('toto', 'titi')
	print g('titi', 'toto')
	print ''
	g = argumentConstant(f, 'premier', 'constant')
	print g('toto', 'titi')
	print g('titi', 'toto')
	print ''
	g = argumentConstant(f, 1, 'constant')
	print g('toto', 'titi')
	print g('titi', 'toto')
	print ''
	g = argumentConstant(f, 2, 'constant')
	print g('toto', 'titi')
	print g('titi', 'toto')
	print ''
	g = argumentConstant(f, -1, 'constant')
	print g('toto', 'titi')
	print g('titi', 'toto')
	print ''
	g = argumentConstant(f, 'dernier', 'constant')
	print g('toto', 'titi')
	print g('titi', 'toto')
	print ''
	g = argumentConstant(f, [0, 1, 5, 3], ['Cst1', 'Cst2', 'Cst3', 'Cst4'])
	print g('toto', 'titi')
	print g('titi', 'toto')
	print ''

# }}}

# ========================================================================

# {{{ main

if __name__ == '__main__' :

	#print constante(1)(5, 7), constante(1, 2)(5, 7)
	#print identite(1), identite(1, 2)
	dico = triArguments(1, [1, 2], 3.0, [3, 4], 2, 4.0, {1 : 2, 3 : 4}, "coucou", 7, 'tutu', (7,8))
	print dico['Entiers']
	print dico['Flottants']
	print dico['Chaines']
	print dico['Listes']
	print dico['Tuples']
	print dico['Dictionnaires']
	print dico['Autres']
	print dico['ListesEtTuples']
	#testeArguments()
	pass

# }}}
