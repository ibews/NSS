# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 17:29:13 2013

@author: ibews
"""
grammar = nltk.parse_fcfg("""
 # Grammar Productions
 S -> NP[CASE=nom, AGR=?a] VP[AGR=?a]
 NP[CASE=?c, AGR=?a] -> PRO[CASE=?c, AGR=?a]
 NP[CASE=?c, AGR=?a] -> PRO[CASE=?c, AGR=?a] NP[CASE=gen]
 NP[CASE=?c, AGR=?a] -> NP[CASE=?c, AGR=?a] NP[CASE=gen]
 NP[CASE=?c, AGR=?a] -> Det[CASE=?c, AGR=?a] N[CASE=?c, AGR=?a]
 NP[CASE=?c, AGR=?a] -> NP[CASE=?a, AGR=?a] NP[CASE=gen]
 VP[AGR=?a] -> IV[AGR=?a]
 VP[AGR=?a] -> TV[OBJCASE=?c, AGR=?a] NP[CASE=?c]
 # Lexical Productions
 # Singular determiners
 # masc
 Det[CASE=nom, AGR=[GND=masc,PER=3,NUM=sg]] -> 'der'
 Det[CASE=gen, AGR=[GND=masc,PER=3,NUM=sg]] -> 'des'
 Det[CASE=dat, AGR=[GND=masc,PER=3,NUM=sg]] -> 'dem'
 Det[CASE=acc, AGR=[GND=masc,PER=3,NUM=sg]] -> 'den'
 # fem
 Det[CASE=nom, AGR=[GND=fem,PER=3,NUM=sg]] -> 'die'
 Det[CASE=gen, AGR=[GND=fem,PER=3,NUM=sg]] -> 'der'
 Det[CASE=dat, AGR=[GND=fem,PER=3,NUM=sg]] -> 'der'
 Det[CASE=acc, AGR=[GND=fem,PER=3,NUM=sg]] -> 'die'
 # Plural determiners
 Det[CASE=nom, AGR=[PER=3,NUM=pl]] -> 'die'
 Det[CASE=gen, AGR=[PER=3,NUM=pl]] -> 'der'
 Det[CASE=dat, AGR=[PER=3,NUM=pl]] -> 'den'
 Det[CASE=acc, AGR=[PER=3,NUM=pl]] -> 'die'
 # Nouns
 N[AGR=[GND=masc,PER=3,NUM=sg]] -> 'Hund'
 N[AGR=[GND=fem,PER=3,NUM=sg]] -> 'Frau'
 N[CASE=gen, AGR=[GND=masc,PER=3,NUM=sg]] -> 'Diebstahls' | 'Buergermeisters'
 N[CASE=gen, AGR=[GND=fem,PER=3,NUM=pl]] -> 'Gelder'
 N[CASE=nom, AGR=[GND=masc,PER=3,NUM=pl]] -> 'Hunde'
 N[CASE=dat, AGR=[GND=masc,PER=3,NUM=pl]] -> 'Hunden'
 N[CASE=acc, AGR=[GND=masc,PER=3,NUM=pl]] -> 'Hunde'
 N[AGR=[GND=fem,PER=3,NUM=sg]] -> 'Katze'
 N[AGR=[GND=fem,PER=3,NUM=pl]] -> 'Katzen'
 # Pronouns
 PRO[CASE=nom, AGR=[PER=1,NUM=sg]] -> 'ich'
 PRO[CASE=acc, AGR=[PER=1,NUM=sg]] -> 'mich'
 PRO[CASE=dat, AGR=[PER=1,NUM=sg]] -> 'mir'
 PRO[CASE=nom, AGR=[PER=2,NUM=sg]] -> 'du'
 PRO[CASE=nom, AGR=[PER=3,NUM=sg]] -> 'er' | 'sie' | 'es'
 PRO[CASE=nom, AGR=[PER=1,NUM=pl]] -> 'wir'
 PRO[CASE=acc, AGR=[PER=1,NUM=pl]] -> 'uns'
 PRO[CASE=dat, AGR=[PER=1,NUM=pl]] -> 'uns'
 PRO[CASE=nom, AGR=[PER=2,NUM=pl]] -> 'ihr'
 PRO[CASE=nom, AGR=[PER=3,NUM=pl]] -> 'sie'
 # Verbs
 IV[AGR=[NUM=sg,PER=1]] -> 'komme'
 IV[AGR=[NUM=sg,PER=2]] -> 'kommst'
 IV[AGR=[NUM=sg,PER=3]] -> 'kommt'
 IV[AGR=[NUM=pl, PER=1]] -> 'kommen'
 IV[AGR=[NUM=pl, PER=2]] -> 'kommt'
 IV[AGR=[NUM=pl, PER=3]] -> 'kommen'
 TV[OBJCASE=acc, AGR=[NUM=sg,PER=1]] -> 'sehe' | 'mag' | 'bezichtige'
 TV[OBJCASE=acc, AGR=[NUM=sg,PER=2]] -> 'siehst' | 'magst' | 'bezichtigst'
 TV[OBJCASE=acc, AGR=[NUM=sg,PER=3]] -> 'sieht' | 'mag' | 'bezichtigt'
 TV[OBJCASE=dat, AGR=[NUM=sg,PER=1]] -> 'folge' | 'helfe'
 TV[OBJCASE=dat, AGR=[NUM=sg,PER=2]] -> 'folgst' | 'hilfst'
 TV[OBJCASE=dat, AGR=[NUM=sg,PER=3]] -> 'folgt' | 'hilft'
 TV[OBJCASE=acc, AGR=[NUM=pl,PER=1]] -> 'sehen' | 'moegen' | 'bezichtigen'
 TV[OBJCASE=acc, AGR=[NUM=pl,PER=2]] -> 'sieht' | 'moegt' | 'bezichtigst'
 TV[OBJCASE=acc, AGR=[NUM=pl,PER=3]] -> 'sehen' | 'moegen' | 'bezichtigen'
 TV[OBJCASE=dat, AGR=[NUM=pl,PER=1]] -> 'folgen' | 'helfen'
 TV[OBJCASE=dat, AGR=[NUM=pl,PER=2]] -> 'folgt' | 'helft'
 TV[OBJCASE=dat, AGR=[NUM=pl,PER=3]] -> 'folgen' | 'helfen'
 """)

tokens = 'er bezichtigt die Frau des Buergermeisters des Diebstahls der Gelder'.split()
parser = nltk.FeatureChartParser(grammar)
for tree in parser.nbest_parse(tokens):
    print tree
    
# er bezichtigt die Frau des Diebstahls der Gelder
#(S[]
#  (NP[AGR=[NUM='sg', PER=3], CASE='nom']
#    (PRO[AGR=[NUM='sg', PER=3], CASE='nom'] er))
#  (VP[AGR=[NUM='sg', PER=3]]
#    (TV[AGR=[NUM='sg', PER=3], OBJCASE='acc'] bezichtigt)
#    (NP[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc']
#      (NP[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc']
#        (NP[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc']
#          (Det[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc'] die)
#          (N[AGR=[GND='fem', NUM='sg', PER=3]] Frau))
#        (NP[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#          (Det[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen'] des)
#          (N[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#            Diebstahls)))
#      (NP[AGR=[GND='fem', NUM='pl', PER=3], CASE='gen']
#        (Det[AGR=[NUM='pl', PER=3], CASE='gen'] der)
#        (N[AGR=[GND='fem', NUM='pl', PER=3], CASE='gen'] Gelder)))))
#(S[]
#  (NP[AGR=[NUM='sg', PER=3], CASE='nom']
#    (PRO[AGR=[NUM='sg', PER=3], CASE='nom'] er))
#  (VP[AGR=[NUM='sg', PER=3]]
#    (TV[AGR=[NUM='sg', PER=3], OBJCASE='acc'] bezichtigt)
#    (NP[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc']
#      (NP[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc']
#        (Det[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc'] die)
#        (N[AGR=[GND='fem', NUM='sg', PER=3]] Frau))
#      (NP[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#        (NP[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#          (Det[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen'] des)
#          (N[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#            Diebstahls))
#        (NP[AGR=[GND='fem', NUM='pl', PER=3], CASE='gen']
#          (Det[AGR=[NUM='pl', PER=3], CASE='gen'] der)
#          (N[AGR=[GND='fem', NUM='pl', PER=3], CASE='gen'] Gelder))))))
#-----------------------------------------------------------------------------
# er bezichtigt die Frau des Buergermeisters des Diebstahls
#(S[]
#  (NP[AGR=[NUM='sg', PER=3], CASE='nom']
#    (PRO[AGR=[NUM='sg', PER=3], CASE='nom'] er))
#  (VP[AGR=[NUM='sg', PER=3]]
#    (TV[AGR=[NUM='sg', PER=3], OBJCASE='acc'] bezichtigt)
#    (NP[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc']
#      (NP[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc']
#        (NP[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc']
#          (Det[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc'] die)
#          (N[AGR=[GND='fem', NUM='sg', PER=3]] Frau))
#        (NP[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#          (Det[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen'] des)
#          (N[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#            Buergermeisters)))
#      (NP[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#        (Det[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen'] des)
#        (N[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen'] Diebstahls)))))
#(S[]
#  (NP[AGR=[NUM='sg', PER=3], CASE='nom']
#    (PRO[AGR=[NUM='sg', PER=3], CASE='nom'] er))
#  (VP[AGR=[NUM='sg', PER=3]]
#    (TV[AGR=[NUM='sg', PER=3], OBJCASE='acc'] bezichtigt)
#    (NP[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc']
#      (NP[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc']
#        (Det[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc'] die)
#        (N[AGR=[GND='fem', NUM='sg', PER=3]] Frau))
#      (NP[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#        (NP[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#          (Det[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen'] des)
#          (N[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#            Buergermeisters))
#        (NP[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#          (Det[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen'] des)
#          (N[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#            Diebstahls))))))
#-----------------------------------------------------------------------------
#er bezichtigt die Frau des Buergermeisters des Diebstahls der Gelder
#(S[]
#  (NP[AGR=[NUM='sg', PER=3], CASE='nom']
#    (PRO[AGR=[NUM='sg', PER=3], CASE='nom'] er))
#  (VP[AGR=[NUM='sg', PER=3]]
#    (TV[AGR=[NUM='sg', PER=3], OBJCASE='acc'] bezichtigt)
#    (NP[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc']
#      (NP[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc']
#        (Det[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc'] die)
#        (N[AGR=[GND='fem', NUM='sg', PER=3]] Frau))
#      (NP[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#        (NP[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#          (NP[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#            (Det[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen'] des)
#            (N[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#              Buergermeisters))
#          (NP[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#            (Det[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen'] des)
#            (N[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#              Diebstahls)))
#        (NP[AGR=[GND='fem', NUM='pl', PER=3], CASE='gen']
#          (Det[AGR=[NUM='pl', PER=3], CASE='gen'] der)
#          (N[AGR=[GND='fem', NUM='pl', PER=3], CASE='gen'] Gelder))))))
#(S[]
#  (NP[AGR=[NUM='sg', PER=3], CASE='nom']
#    (PRO[AGR=[NUM='sg', PER=3], CASE='nom'] er))
#  (VP[AGR=[NUM='sg', PER=3]]
#    (TV[AGR=[NUM='sg', PER=3], OBJCASE='acc'] bezichtigt)
#    (NP[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc']
#      (NP[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc']
#        (Det[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc'] die)
#        (N[AGR=[GND='fem', NUM='sg', PER=3]] Frau))
#      (NP[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#        (NP[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#          (Det[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen'] des)
#          (N[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#            Buergermeisters))
#        (NP[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#          (NP[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#            (Det[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen'] des)
#            (N[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#              Diebstahls))
#          (NP[AGR=[GND='fem', NUM='pl', PER=3], CASE='gen']
#            (Det[AGR=[NUM='pl', PER=3], CASE='gen'] der)
#            (N[AGR=[GND='fem', NUM='pl', PER=3], CASE='gen'] Gelder)))))))
#(S[]
#  (NP[AGR=[NUM='sg', PER=3], CASE='nom']
#    (PRO[AGR=[NUM='sg', PER=3], CASE='nom'] er))
#  (VP[AGR=[NUM='sg', PER=3]]
#    (TV[AGR=[NUM='sg', PER=3], OBJCASE='acc'] bezichtigt)
#    (NP[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc']
#      (NP[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc']
#        (NP[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc']
#          (NP[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc']
#            (Det[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc'] die)
#            (N[AGR=[GND='fem', NUM='sg', PER=3]] Frau))
#          (NP[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#            (Det[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen'] des)
#            (N[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#              Buergermeisters)))
#        (NP[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#          (Det[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen'] des)
#          (N[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#            Diebstahls)))
#      (NP[AGR=[GND='fem', NUM='pl', PER=3], CASE='gen']
#        (Det[AGR=[NUM='pl', PER=3], CASE='gen'] der)
#        (N[AGR=[GND='fem', NUM='pl', PER=3], CASE='gen'] Gelder)))))
#(S[]
#  (NP[AGR=[NUM='sg', PER=3], CASE='nom']
#    (PRO[AGR=[NUM='sg', PER=3], CASE='nom'] er))
#  (VP[AGR=[NUM='sg', PER=3]]
#    (TV[AGR=[NUM='sg', PER=3], OBJCASE='acc'] bezichtigt)
#    (NP[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc']
#      (NP[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc']
#        (NP[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc']
#          (Det[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc'] die)
#          (N[AGR=[GND='fem', NUM='sg', PER=3]] Frau))
#        (NP[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#          (NP[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#            (Det[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen'] des)
#            (N[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#              Buergermeisters))
#          (NP[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#            (Det[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen'] des)
#            (N[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#              Diebstahls))))
#      (NP[AGR=[GND='fem', NUM='pl', PER=3], CASE='gen']
#        (Det[AGR=[NUM='pl', PER=3], CASE='gen'] der)
#        (N[AGR=[GND='fem', NUM='pl', PER=3], CASE='gen'] Gelder)))))
#(S[]
#  (NP[AGR=[NUM='sg', PER=3], CASE='nom']
#    (PRO[AGR=[NUM='sg', PER=3], CASE='nom'] er))
#  (VP[AGR=[NUM='sg', PER=3]]
#    (TV[AGR=[NUM='sg', PER=3], OBJCASE='acc'] bezichtigt)
#    (NP[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc']
#      (NP[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc']
#        (NP[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc']
#          (Det[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc'] die)
#          (N[AGR=[GND='fem', NUM='sg', PER=3]] Frau))
#        (NP[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#          (Det[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen'] des)
#          (N[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#            Buergermeisters)))
#      (NP[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#        (NP[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#          (Det[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen'] des)
#          (N[AGR=[GND='masc', NUM='sg', PER=3], CASE='gen']
#            Diebstahls))
#        (NP[AGR=[GND='fem', NUM='pl', PER=3], CASE='gen']
#          (Det[AGR=[NUM='pl', PER=3], CASE='gen'] der)
#          (N[AGR=[GND='fem', NUM='pl', PER=3], CASE='gen'] Gelder))))))
