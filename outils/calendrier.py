#! /usr/bin/env python
# -*- coding: utf-8 -*-

# ==============================================================================

# {{{ Importations

import opera, fonction, lune

import time
import datetime

# }}}

# ==============================================================================

# {{{ Variables

separateur = ' @ '

deltaListe = fonction.opBinaireSurListe(opera.soustraction)

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ chaine2temps

def chaine2temps(chaine, format = '%Y-%m-%d' + separateur + '%H:%M:%S') :

	try :
		return datetime.datetime(*time.strptime(chaine, format)[0:6])
	except ValueError :
		return None
	except :
		print '!!!', chaine, '!!!'

# }}}

# ==============================================================================

# {{{ chaine2date

def chaine2date(chaine, format = '%Y-%m-%d') :

	return chaine2temps(chaine, format)

# }}}

# ==============================================================================

# {{{ chaine2heure

def chaine2heure(chaine, format = '%H:%M:%S') :

	return chaine2temps(chaine, format)

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ representeUnTemps

def representeUnTemps(chaine, format = '%Y-%m-%d' + separateur + '%H:%M:%S') :

	return (chaine2temps(chaine, format) != None)

# }}}

# ==============================================================================

# {{{ representeUneDate

def representeUneDate(chaine, format = '%Y-%m-%d') :

	return (chaine2temps(chaine, format) != None)

# }}}

# ==============================================================================

# {{{ representeUneHeure

def representeUneHeure(chaine, format = '%H:%M:%S') :

	return (chaine2temps(chaine, format) != None)

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ temps2chaine

def temps2chaine(temps, format = '%Y-%m-%d' + separateur + '%H:%M:%S') :

	return temps.strftime(format)

# }}}

# ==============================================================================

# {{{ date2chaine

def date2chaine(date, format = '%Y-%m-%d') :

	return temps2chaine(date, format)

# }}}

# ==============================================================================

# {{{ heure2chaine

def heure2chaine(date, format = '%H:%M:%S') :

	return temps2chaine(date, format)

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def maintenant() : return datetime.datetime.now()

# ==============================================================================

# {{{ aujourdhui

def aujourdhui() :

	return chaine2date(date2chaine(maintenant()))

# }}}

# ==============================================================================

# {{{ horloge

def horloge() :

	return chaine2heure(heure2chaine(maintenant()))

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ jourDeLaSemaine

def jourDeLaSemaine(temps, numero = True) :

	if numero : return int(temps2chaine(temps, '%w'))
	else : return temps2chaine(temps, '%A')

# }}}

# ==============================================================================

def jourDuMois(temps) : return int(temps2chaine(temps, '%d'))

# ==============================================================================

def jourDeLunaison(temps) : return lune.jourDeLunaison(lune.position(temps))

# ==============================================================================

def jourDeLAnnee(temps) : return int(temps2chaine(temps, '%j'))

# ==============================================================================

def semaineDeLAnnee(temps) : return int(temps2chaine(temps, '%W'))

# ==============================================================================

# {{{ mois

def mois(temps, numero = True) :

	if numero : return int(temps2chaine(temps, '%m'))
	else : return temps2chaine(temps, '%B')

# }}}

# ==============================================================================

def annee(temps) : return temps.timetuple()[0]

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ differenceEnJours

def differenceEnJours(initial, final) :

	delta = (annee(final) - annee(initial)) * 365
	delta += jourDeLAnnee(final) - jourDeLAnnee(initial)

	return delta

# }}}

# ==============================================================================

# {{{ differenceEnAnnees

def differenceEnAnnees(initial, final) :

	delta = annee(final) - annee(initial)
	delta += (jourDeLAnnee(final) - jourDeLAnnee(initial)) / 365.0

	return delta

# }}}

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# {{{ testeTout

def testeTout() :

	t = maintenant()
	t = chaine2temps(temps2chaine(t))

	chaine = temps2chaine(t)
	print chaine
	print representeUnTemps(chaine)
	print representeUneDate(chaine)
	print representeUneHeure(chaine)
	print 'date', date2chaine(t)
	print 'heure', heure2chaine(t)
	print 'jour semaine', jourDeLaSemaine(t)
	print 'jour semaine', jourDeLaSemaine(t, numero = False)
	print 'jour mois', jourDuMois(t)
	print 'jour lunaison', jourDeLunaison(t)
	print 'jour annee', jourDeLAnnee(t)
	print 'mois', mois(t)
	print 'mois', mois(t, numero = False)

	print '------------------------------------------------------'

	t = aujourdhui()
	t = chaine2date(date2chaine(t))

	chaine = date2chaine(t)
	print chaine
	print representeUnTemps(chaine)
	print representeUneDate(chaine)
	print representeUneHeure(chaine)
	print 'date', date2chaine(t)
	print 'heure', heure2chaine(t)
	print 'jour semaine', jourDeLaSemaine(t)
	print 'jour semaine', jourDeLaSemaine(t, numero = False)
	print 'jour mois', jourDuMois(t)
	print 'jour lunaison', jourDeLunaison(t)
	print 'jour annee', jourDeLAnnee(t)
	print 'mois', mois(t)
	print 'mois', mois(t, numero = False)

	print '------------------------------------------------------'

	t = horloge()
	t = chaine2heure(heure2chaine(t))

	chaine = heure2chaine(t)
	print chaine
	print representeUnTemps(chaine)
	print representeUneDate(chaine)
	print representeUneHeure(chaine)
	print 'date', date2chaine(t)
	print 'heure', heure2chaine(t)
	print 'jour semaine', jourDeLaSemaine(t)
	print 'jour semaine', jourDeLaSemaine(t, numero = False)
	print 'jour mois', jourDuMois(t)
	print 'jour lunaison', jourDeLunaison(t)
	print 'jour annee', jourDeLAnnee(t)
	print 'mois', mois(t)
	print 'mois', mois(t, numero = False)

	print '------------------------------------------------------'

	initial = chaine2date('1905-5-12')
	final = chaine2date('1907-8-1')
	print differenceEnJours(initial, final)
	print differenceEnAnnees(initial, final)

# }}}

# ==============================================================================

# {{{ teste

def teste() :

	testeTout()

# }}}

# ==============================================================================

# {{{ main

if __name__ == '__main__' :

	import sys
	args = sys.argv
	if len(args) > 1 : journalier = args[1]
	else : journalier = "journalier.txt"

	teste()

# }}}
