#! /usr/bin/env python
# -*- coding: utf-8 -*-

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ positif

def positif(x, strict = False) :
	if not strict : return x >= 0
	else : return x > 0

# }}}

# ========================================================================

# {{{ negatif

def negatif(x, strict = False) :
	if not strict : return x <= 0
	else : return x < 0

# }}}

# ========================================================================

def absolue(a) : return (a if a >=0 else -a)

# ========================================================================

def signe(a) : return (1 if a >= 0 else -1)

# ========================================================================

# {{{ signeTernaire

def signeTernaire(a) :
	if a > 0 : return 1
	if a < 0 : return -1
	if a == 0 : return 0

# }}}

# ========================================================================

def nonNul(a) : return (1 if a != 0 else 0)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def addition(a, b) : return a + b

# ========================================================================

def soustraction(a, b) : return a - b

# ========================================================================

def multiplication(a, b) : return a * b

# ========================================================================

def division(a, b) : return a / b

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ main

if __name__ == '__main__' :

	pass

# }}}
