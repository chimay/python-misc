#! /usr/bin/env python
# -*- coding: utf-8 -*-

# moonphase.py - Calculate Lunar Phase
# Author: Sean B. Palmer, inamidst.com
# Cf. http://en.wikipedia.org/wiki/Lunar_phase#Lunar_phase_calculation

# {{{ Importations

import math, datetime

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ position

def position(now = None):

   if now is None:
      now = datetime.datetime.now()

   diff = now - datetime.datetime(2001, 1, 1)
   days = float(diff.days) + (float(diff.seconds) / float(86400))

   invDuree = 1.0 / 27.3217 - 1.0 / 365.25696
   lunations = 0.20439731 + (days * invDuree)

   return lunations % float(1)

# }}}

# =====================================================================

# {{{ phase

def phase(pos):

   index = (pos * float(8)) + 0.5
   index = math.floor(index)

   return {
      0: "New Moon",
      1: "Waxing Crescent",
      2: "First Quarter",
      3: "Waxing Gibbous",
      4: "Full Moon",
      5: "Waning Gibbous",
      6: "Last Quarter",
      7: "Waning Crescent"
   }[int(index) & 7]

# }}}

# =====================================================================

# {{{ jourDeLunaison

def jourDeLunaison(pos) :

	duree = 1.0 / ( 1.0 / 27.3217 - 1.0 / 365.25696 )

	return int(math.floor(pos * float(duree)))

# }}}

# =====================================================================

# {{{ main

if __name__=="__main__":

	pos = position()
	phasename = phase(pos)
	jour = jourDeLunaison(pos)
	roundedpos = round(float(pos) * 100, 1)
	print "%s jour %d position %s" % (phasename, jour, roundedpos)

# }}}
