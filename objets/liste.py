#! /usr/bin/env python
# -*- coding: utf-8 -*-

# ==============================================================================

class Liste :

	"""
	Liste generique
	"""

	# ------------------------------------------------------------------------

	def __init__(self, objet = '', fichier = False) :

		"""
		Creation de l'objet
		"""

		self.elements = []

	def __repr__(self) :
		elts = [str(e) for e in self.elements]
		chaine = ' '.join(elts)
		return chaine

	# ------------------------------------------------------------------------

	def __len__(self) :

		"""
		Renvoie le nombre d'element de l'objet
		"""

		return len(self.elements)

	def __getitem__(self, i) :

		"""
		Renvoie le ieme element de la liste que contient l'objet,
		ou l'objet lui-meme
		"""

		return self.elements[i]

	def __setitem__(self, i, elt) :

		"""
		Modifie en elt le ieme element de la liste que contient l'objet,
		ou l'objet lui-meme
		"""

		self.elements[i] = elt

	def __getslice__(self, i, j) :

		"""
		Renvoie la tranche de i à j de la liste que contient l'objet,
		ou l'objet lui-meme
		"""

		return self.elements[i:j]

	def __setslice__(self, i, j, liste) :

		"""
		Modifie la tranche de i à j de la liste que contient l'objet,
		ou l'objet lui-meme
		"""

		self.elements[i:j] = liste

	# ------------------------------------------------------------------------

	def copie(self) :
		liste = Liste()
		liste[:] = self[:]

		return liste

	# ------------------------------------------------------------------------

	def ajoute(self, elt) :

		"""
		Ajoute un element a l'objet, ou ne fait rien si l'objet
		ne contient pas de liste d'element
		"""

		self.elements.append(elt)

	def poupeeRusse(self) :

		"""
		Enleve les extrémités de la liste
		"""

		self.elements.pop(0) ; self.elements.pop()

	def enrobe(self, a, b) :

		"""
		Ajoute a et b aux extrémités de la liste
		"""

		self.elements.insert(0, a) ; self.elements.append(b)

	def renverse(self) : self.elements.reverse()

# ==============================================================================

if __name__ == '__main__' :

	"""
	Tous les tests du module
	"""

	print Liste.__doc__
	pass
