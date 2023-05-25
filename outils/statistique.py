#! /usr/bin/env python
# -*- coding: utf-8 -*-

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ ecartTypePositif

def ecartTypePositif(signal) :

	n = 0
	et = 0

	for i in range(len(signal) - 1) :

		delta = signal[i + 1] - signal[i]

		if delta > 0 :
			n += 1
			et += delta * delta

	et = (et / n) ** 0.5

	return et

# }}}

# ========================================================================

# {{{ ecartTypeNegatif

def ecartTypeNegatif(signal) :

	n = 0
	et = 0

	for i in range(len(signal) - 1) :

		delta = signal[i + 1] - signal[i]

		if delta < 0 :
			n += 1
			et += delta * delta

	et = (et / n) ** 0.5

	return et

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ main

if __name__ == '__main__' :

	print ecartTypePositif([1, 4, 0])
	print ecartTypeNegatif([10, 12, 4])

	pass

# }}}
