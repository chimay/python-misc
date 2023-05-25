#! /usr/bin/env python
# -*- coding: utf-8 -*-

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ pgcd

def pgcd(*arguments):

	"""
	Plus Grand Commun Diviseur
	"""

	if len(arguments) == 2 :

		a, b = arguments

		while b != 0 : a, b = b, a % b

		return a

	else :

		p = pgcd(arguments[0], arguments[1])

		for x in arguments[2:] : p = pgcd(p, x)

		return p

# }}}

# ========================================================================

# {{{ pgcdBezout

def pgcdBezout(a, b):

	"""
	Plus Grand Commun Diviseur
	et coefficients de Bézout u, v entiers tels que :

	a * u + b * v = pgcd(a, b)
	"""

	Pa, Ua, Va = a, 1, 0
	Pb, Ub, Vb = b, 0, 1

	while Pb != 0 :

		q = Pa // Pb

		Pc, Uc, Vc = Pa, Ua, Va
		Pa, Ua, Va = Pb, Ub, Vb

		Pb = Pc - q * Pb
		Ub = Uc - q * Ub
		Vb = Vc - q * Vb

	return Pa, Ua, Va

# }}}

# ========================================================================

# {{{ ppcm

def ppcm(*arguments):

	"""
	Plus Petit Commun Multiple
	"""

	if len(arguments) == 2 :

		a, b = arguments

		if a == 0 or b == 0 : return 0
		else : return (a * b) // pgcd(a, b)

	else :

		a, b = arguments[:2]

		p = abs(a * b) // pgcd(a, b)

		for x in arguments[2:] : p = abs(p * x) // pgcd(p, x)

		return p

# }}}

# ========================================================================

# {{{ restesChinois

def restesChinois(*arguments):

	"""
	Restes chinois

	Trouver x entier tel que :

	x mod m1 = a1
	x mod m2 = a2
	...      ...
	x mod mi = ai
	...      ...
	x mod mn = an

	Avec m1, m2, ..., mn entiers quelconques (> 0 ou < 0) mais <> 0

	Arguments = liste de n couples :

	arguments = [ [a1,m1], [a2,m2], ..., [an,mn] ]

	Condition d'existence de solution:

	(ai,aj) % pgcd(mi,mj)==0 (i<>j)

	Retour de x accompagné de son modulo
	"""

	a1, m1 = arguments[0]

	for a2, m2 in arguments[1:]:

		# r = pgcd; y1 et y2 = coef de Bézout de m2 et m1

		r, y1, y2 = pgcdBezout(m2, m1)

		# il n'y a pas de solution => on renvoie None

		if (a1 - a2) % r != 0: return None, None

		a1 = ( (a1 * m2 * y1 + a2 * m1 * y2) % (m1*m2) ) // r
		m1 = ppcm(m1, m2)

	# renvoi de x et de son modulo

	return a1 % m1, m1

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ puissanceEntiere

# Adaptation d'une fonction trouvée sur la page :
#
# http://python.jpvweb.com/mesrecettespython/tri_rapide
#
# Merci à l'auteur :)

def puissanceEntiere(x, y) :

	puissance = 1

	while y != 0 :

		# y impair

		if y & 1 == 1 :

			puissance *= x
			y -= 1

		# y pair

		else :

			x *= x
			y >>= 1

	return puissance

# }}}

# ========================================================================

# {{{ puissanceModulaire

# Adaptation d'une fonction trouvée sur la page :
#
# http://python.jpvweb.com/mesrecettespython/tri_rapide
#
# Merci à l'auteur :)

def puissanceModulaire(x, y, n) :

	"""
	(x ** y) % n
	"""

	puissance = 1

	while y > 0 :

		if y & 1 > 0 : puissance = (puissance * x) % n

		y >>= 1
		x = (x * x) % n

	return puissance

# }}}

# ========================================================================

# {{{ racineEntiere

def racineEntiere(x, n = 2):

	"""
	Racine entiere n_ieme d'un nombre entier x
	"""

	# traitement des cas particuliers x < 1

	if x > 0 : s = 1
	else:
		if x == 0 : return 0
		if n % 2 == 0 :
			raise ValueError ("erreur lrac(x,n=2): avec n pair, x ne peut pas etre negatif")
		s, x = -1, -x

	# calcul des r1 et r2 qui encadrent de plus pres la valeur cherchee de la racine

	r1 = 10 ** ( (len(str(x)) - 1) // n )
	r2 = r1 * 10 ** n

	# calcul par dichotomie de la racine entiere r de x, qui se trouve entre r1 et r2

	while r1 != r2:

		r = (r1+r2)>>1
		rn = r**n

		if rn > x: r2 = r
		else: r1 = r+1

	if x-rn < 0: r -= 1

	# retour de la racine avec le bon signe

	if s > 0 : return r

	return -r

# }}}

# ========================================================================

# {{{ factorielle

def factorielle(n):

	if n < 2 : return 1
	else : return n * factorielle(n - 1)

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ facteursPremiers

def facteursPremiers(n):

	"""
	Décomposition d'un nombre entier n en facteurs premiers
	"""

	F = []

	if n == 1 : return F

	# recherche de tous les facteurs 2 s'il y en a

	while n >= 2 :

		x, r = divmod(n, 2)

		if r != 0 : break

		F.append(2)

		n = x

	# recherche des facteurs 1er > 2

	i = 3

	rn = racineEntiere(n) + 1

	while i <= n :

		if i>rn:
			F.append(n)
			break

		x,r = divmod(n,i)

		if r==0:
			F.append(i)
			n=x
			rn = racineEntiere(n) + 1
		else: i += 2

	return F

# }}}

# ========================================================================

# {{{ estPremier

def estPremier(n):

	if n < 7:

		if n in (2,3,5) : return True
		else: return False

	# si n est pair et > 2 (= 2 : cas traité ci-dessus), il ne peut pas être premier

	if n & 1 == 0: return False

	# autres cas

	k = 3
	r = racineEntiere(n) + 1

	while k <= r:

		if n % k == 0: return False

		k += 2

	return True

# }}}

# ========================================================================

# {{{ nombresPremiers

def nombresPremiers(n, methode = 'eratosthene'):

	"""
	Nombres premiers inférieurs à n
	"""

	if methode == 'eratosthene' :

		L = range(0, n + 1)

		L[1] = 0

		k = 2

		while k * k <= n:

			L[k * 2 :: k] = [0] * len(L[k * 2 :: k])
			k += 1

		return [x for x in L if x]

	elif methode == 'divisions' :

		p = [2, 3, 5]

		k = p[-1] + 2

		if n < k : return [x for x in p if x<=n]

		while k <= n :

			i = 0

			while i < len(p):

				if p[i] * p[i] > k :

					p.append(k)
					break

				if (k % p[i]) == 0 : break

				i += 1

			k += 2

		return p

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ main

if __name__ == '__main__' :

	# 3, 2

	print pgcd(12, 9), pgcd(16, 12, 6)

	# 1, -9, 47

	print pgcdBezout(120, 23)

	# 770

	print ppcm(70, 154)


	# 256

	print puissanceEntiere(2, 8)

	# 6

	print puissanceModulaire(2, 8, 10)


	# 3, 3

	print racineEntiere(9), racineEntiere(27, 3)

	# 24

	print factorielle(4)


	# [2, 2, 5, 5], [3, 3, 3607, 3803]

	print facteursPremiers(100), facteursPremiers(123456789)

	# True, False

	print estPremier(29), estPremier(27)

	# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
	# 31, 37, 41, 43, 47, 53, 59, 61, 67,
	# 71, 73, 79, 83, 89, 97

	print nombresPremiers(100)
	print nombresPremiers(100, methode = 'divisions')

	# 1000

	arg = [
		[6, 7],
		[10, 11],
		[12, 13]
	]

	print restesChinois(*arg)

	pass

# }}}
