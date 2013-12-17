# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 16:46:56 2013

@author: ibews
"""


grammar = nltk.parse_fcfg("""
% start S
 # Grammar Productions
 S -> NP[CASE=?c, AGR=?a]
 NP[CASE=?c, AGR=?a] -> N[CASE=?c, AGR=?a]
 NP[CASE=?c, AGR=?a] -> ADJ[CASE=?c, D=?d, AGR=?a] N[CASE=?c, AGR=?a]
 NP[CASE=?c, AGR=?a] -> Det[CASE=?c, AGR=?a] N[CASE=?c, AGR=?a]
 NP[CASE=?c, AGR=?a] -> Det[CASE=?c, AGR=?a] ADJ[CASE=?c, D=?d, AGR=?a] N[CASE=?c, AGR=?a]
 # Lexical Productions
 # masc
 Det[CASE=nom, D=def, AGR=[GND=masc,NUM=sg]] -> 'der'
 Det[CASE=gen, D=def, AGR=[GND=masc,NUM=sg]] -> 'des'
 Det[CASE=dat, D=def, AGR=[GND=masc,NUM=sg]] -> 'dem'
 Det[CASE=acc, D=def, AGR=[GND=masc,NUM=sg]] -> 'den'
 Det[CASE=nom, D=indef, AGR=[GND=masc,NUM=sg]] -> 'ein'
 Det[CASE=gen, D=indef, AGR=[GND=masc,NUM=sg]] -> 'eines'
 Det[CASE=dat, D=indef, AGR=[GND=masc,NUM=sg]] -> 'einem'
 Det[CASE=acc, D=indef, AGR=[GND=masc,NUM=sg]] -> 'einen'
 # fem
 Det[CASE=nom, D=def, AGR=[GND=fem,NUM=sg]] -> 'die'
 Det[CASE=gen, D=def, AGR=[GND=fem,NUM=sg]] -> 'der'
 Det[CASE=dat, D=def, AGR=[GND=fem,NUM=sg]] -> 'der'
 Det[CASE=acc, D=def, AGR=[GND=fem,NUM=sg]] -> 'die'
 Det[CASE=nom, D=indef, AGR=[GND=fem,NUM=sg]] -> 'eine'
 Det[CASE=gen, D=indef, AGR=[GND=fem,NUM=sg]] -> 'einer'
 Det[CASE=dat, D=indef, AGR=[GND=fem,NUM=sg]] -> 'einer'
 Det[CASE=acc, D=indef, AGR=[GND=fem,NUM=sg]] -> 'eine'
 # neu
 Det[CASE=nom, D=def, AGR=[GND=neu,NUM=sg]] -> 'das'
 Det[CASE=gen, D=def, AGR=[GND=neu,NUM=sg]] -> 'des'
 Det[CASE=dat, D=def, AGR=[GND=neu,NUM=sg]] -> 'dem'
 Det[CASE=acc, D=def, AGR=[GND=neu,NUM=sg]] -> 'das'
 Det[CASE=nom, D=indef, AGR=[GND=neu,NUM=sg]] -> 'ein'
 Det[CASE=gen, D=indef, AGR=[GND=neu,NUM=sg]] -> 'eines'
 Det[CASE=dat, D=indef, AGR=[GND=neu,NUM=sg]] -> 'einem'
 Det[CASE=acc, D=indef, AGR=[GND=neu,NUM=sg]] -> 'ein'
 # Plural determiners
 Det[CASE=nom, AGR=[NUM=pl]] -> 'die'
 Det[CASE=gen, AGR=[NUM=pl]] -> 'der'
 Det[CASE=dat, AGR=[NUM=pl]] -> 'den'
 Det[CASE=acc, AGR=[NUM=pl]] -> 'die'
 
 # Nouns
 N[CASE=gen, AGR=[GND=masc,NUM=sg]] -> 'Hundes'
 N[CASE=nom, AGR=[GND=masc,NUM=sg]] -> 'Hund'
 N[AGR=[GND=masc,NUM=pl]] -> 'Hunde'
 N[CASE=dat, AGR=[GND=masc,NUM=pl]] -> 'Hunden'
 
 N[AGR=[GND=fem,NUM=sg]] -> 'Katze'
 N[AGR=[GND=fem,NUM=pl]] -> 'Katzen' 
 
 N[CASE=gen, AGR=[GND=masc,NUM=sg]] -> 'Kindes'
 N[AGR=[GND=neu,NUM=sg]] -> 'Kind'
 N[CASE=dat, AGR=[GND=masc,NUM=pl]] -> 'Kindern'
 N[AGR=[GND=masc,NUM=pl]] -> 'Kinder'
 
 #Adjectives
 #sg
 #masc
 ADJ[CASE=nom, D=def, AGR=[GND=masc, NUM=sg]] -> 'junge'
 ADJ[CASE=nom, D=indef, AGR=[GND=masc, NUM=sg]] -> 'junger'
 ADJ[CASE=gen, AGR=[GND=masc, NUM=sg]] -> 'jungen'
 ADJ[CASE=dat, AGR=[GND=masc, NUM=sg]] -> 'jungen'
 ADJ[CASE=acc, AGR=[GND=masc, NUM=sg]] -> 'jungen'
 #fem
 ADJ[CASE=nom, D=def, AGR=[GND=fem, NUM=sg]] -> 'junge'
 ADJ[CASE=gen, AGR=[GND=fem, NUM=sg]] -> 'jungen'
 ADJ[CASE=dat, AGR=[GND=fem, NUM=sg]] -> 'jungen'
 ADJ[CASE=acc, AGR=[GND=fem, NUM=sg]] -> 'junge'
 #neu
 ADJ[CASE=nom, D=def, AGR=[GND=neu, NUM=sg]] -> 'junge'
 ADJ[CASE=nom, D=indef, AGR=[GND=neu, NUM=sg]] -> 'junges'
 ADJ[CASE=gen, AGR=[GND=neu, NUM=sg]] -> 'jungen'
 ADJ[CASE=dat, AGR=[GND=neu, NUM=sg]] -> 'jungen'
 ADJ[CASE=acc, D=def, AGR=[GND=neu, NUM=sg]] -> 'junge'
 ADJ[CASE=acc, D=indef, AGR=[GND=neu, NUM=sg]] -> 'junges'
 
 #pl
 ADJ[AGR=[NUM=pl]] -> 'jungen'
""")

tokens = 'ein junges Kind'.split()
parser = nltk.FeatureChartParser(grammar)
for tree in parser.nbest_parse(tokens):
    print tree