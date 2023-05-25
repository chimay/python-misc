#! /usr/bin/env python
# -*- coding: utf-8 -*-

# {{{ Importations

#import numpy as np
#import scipy as sp

import pylab as pl

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def date2nombre(date) : return pl.date2num(date)

# ==============================================================================

def chaineDate2nombre(date) : return pl.datestr2num(date)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ moyenne

def moyenne(echantillon) :
	return pl.mean(echantillon)

# }}}

# ==============================================================================

# {{{ variance

def variance(echantillon) :
	return pl.var(echantillon)

# }}}

# ==============================================================================

# {{{ ecartType

def ecartType(echantillon) :
	return pl.sqrt(pl.var(echantillon))

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ transposee

def transposee(matrice) :
	return pl.array.transpose(matrice)

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ inverse

def inverse(matrice) :
	return pl.inv(matrice)

# }}}

# ==============================================================================

# {{{ determinant

def determinant(matrice) :
	return pl.det(matrice)

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ valeursPropres

def valeursPropres(matrice) :
	return pl.eig(matrice)

# }}}

# ==============================================================================

# {{{ valeursSingulieres

def valeursSingulieres(matrice) :
	return pl.svd(matrice)

# }}}

# ==============================================================================

# {{{ pseudoInverse

def pseudoInverse(matrice) :
	return pl.pinv(matrice)

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ solution

def solution(matrice, vecteur) :
	return pl.solve(matrice, vecteur)

# }}}

# ==============================================================================

# {{{ moindresCarres

def moindresCarres(matrice, vecteur) :
	return pl.lstsq(matrice, vecteur)

# }}}

# ==============================================================================

# {{{ regressionPolynomiale

def regressionPolynomiale(x, y, degre) :
	return pl.polyfit(x, y, degre)

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ main

if __name__ == '__main__' :

	print '################# Module science.matrice ###############################'

	a = pl.arange(0,2.4,0.1)
	print a
	a.shape = (2,4,3)
	print a
	a.shape = 4,6
	print a

	print pl.eye(10)
	print pl.ones((4,2,3))
	print pl.zeros((2,3,4))

	A = pl.mat(a)
	print A
	print A.A
	print A.T
	print (2 * pl.mat(pl.eye(2))).I

	b = pl.linspace(0,2,4)
	x = moindresCarres(A, b)[0]
	print pl.dot(A, x)

# }}}
