#! /usr/bin/env python
# -*- coding: utf-8 -*-

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ puis2

def puis2(n) :
	e = 1
	while e <= n :
		yield e
		e *= 2

# }}}

# ========================================================================

# {{{ combinaison

def combinaison(*arguments) :
	if len(arguments) == 1 :
		for e in arguments[0] :
			yield [e]
	else :
		for e in arguments[0] :
			for f in combinaison(*arguments[1:]) :
				liste = [e]
				liste.extend(f)
				yield liste

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ main

if __name__ == '__main__' :
	for e in combinaison(range(2), range(1, 4), range(2, 4), range(3, 5)) :
		print e

	pass

# }}}
