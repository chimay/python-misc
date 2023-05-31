#! /usr/bin/env python
# -*- coding: utf-8 -*-

# {{{ Importations

import outils.fonction

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ chevrons

def chevrons(fonction, N = 4) :

	def f(*a) :

		chaine = '<' * N + ' '
		chaine += fonction(*a)
		chaine += ' ' + '>' * N

		return chaine

	return f

# }}}

# ==============================================================================

# {{{ chevronsN

def chevronsN(N) :

	return outils.fonction.argumentConstant(chevrons, 'dernier', N)

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ Classe

class Classe(object) :

	"""
	Classe exemple
	"""

	# {{{ Variables de classe

	# Pour définir quelles créations d'attributs sont autorisées.
	# En l'absence de __slots__, tout est autorisé

	#__slots__ = ['a', 'b']

	compteur = 0

	# }}}

# ==============================================================================

	# {{{ Construction

	def __init__(self, L = []) :

		self.__class__.compteur += 1

		self.numero = self.__class__.compteur

		self.liste = L[:]

	def __del__(self) :

		Classe.compteur -= 1

		del self.liste, self.numero

	# }}}

# ==============================================================================

	# {{{ Représentation

	@chevronsN(4)
	def __str__(self) :

		chaine = '[' + ' : '.join([str(e) for e in self.liste]) + ']'

		return chaine

	def __repr__(self) :

		chaine = 'Instance de numéro ' + str(self.numero) + ' / ' + str(self.__class__.compteur) + ' '

		chaine += '[' + ' : '.join([str(e) for e in self.liste]) + ']'

		return chaine

	# }}}

# ==============================================================================

	# {{{ Propriété

	def getP(self) : return self.propriete

	def setP(self, val) : self.propriete = val

	def delP(self) : del self.propriete

	P = property(getP, setP, delP, 'Propriété P')

	# }}}

# ==============================================================================

	# {{{ Liste

	def __len__(self) : return len(self.liste)

	def __add__(self, autre) :

		l = self.liste + autre.liste

		return Classe(l)

	def __getitem__(self, indice) :

		ind = indice % len(self.liste)

		return self.liste[ind]

	def __setitem__(self, indice, elt) :

		ind = indice % len(self.liste)

		self.liste[ind] = elt

	def __getslice__(self, i, j) : return self.liste[i:j]

	def __setslice__(self, i, j, L) : self.liste[i:j] = L

	# }}}

# ==============================================================================

	# {{{ Appel comme une fonction

	def __call__(self, i) : return self[i]

	# }}}

# ==============================================================================

	# {{{ Copie

	def copie(self) : return self.__class__(self)

	# }}}

# ==============================================================================

	# {{{ Fonctions de classe

	def compte(cls) :

		print 'classmethod'

		return cls.compteur

	compte = classmethod(compte)

	# }}}

# ==============================================================================

	# {{{ Fonctions statiques

	def separateur() :

		print 'staticmethod'

		return '...'

	separateur = staticmethod(separateur)

	# }}}

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ Derivee

class Derivee(Classe) :

	"""
	Classe dérivée
	"""

	# {{{ Construction

	def __init__(self, L = []) :

		super(Derivee, self).__init__()

	# }}}

# ==============================================================================

	# {{{ Représentation

	def __str__(self) :

		chaine = super(Derivee, self).__str__()

		chaine += str(self.__class__.__mro__)

		return chaine

	# }}}

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ Fonction

def fonction(self, *a) :

	print a

Classe.fonction = fonction

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ main

if __name__ == '__main__' :

	try :
		import psyco
		psyco.full()
	except ImportError : pass

	print Classe.__doc__

	C = Classe(range(10))

	D = C

	E = Classe(range(10))

	print C.__class__.__dict__

	C.fonction('ijire', 'igjrtij')

	print repr(C)

	print str(C)

	print C is D, C is E

	C.propriete = 2
	print C.propriete, C.P

	print C.compte()
	print C.separateur()

	D = Derivee()

	print D

# }}}
