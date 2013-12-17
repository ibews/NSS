# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 11:43:57 2013

@author: ibews
"""



# Konzipieren, implementieren und testen Sie mit NLTK eine merkmalsbasierte
# Grammatik für einfache deutsche Nominalphrasen im Singular in den verschiedenen
# Fällen (Kasus), die aus Artikel und Nomen bestehen.

# Sie sollten als Artikel die Formen des definiten Artikels (der, die, das, ...)
# und des indefiniten Artikels (ein, eine, ...) korrekt behandeln und ihr Lexikon
# sollte für jedes grammatische Geschlecht  mind. ein Beispielnomen beinhalten.

# Testen Sie Ihre Lösung mit geeigneten Beispielen.

import nltk

grammar = nltk.parse_fcfg("""
% start S
 # Grammar Productions
 S -> NP[CASE=?c, AGR=?a]
 NP[CASE=?c, AGR=?a] -> Det[CASE=?c, AGR=?a] N[CASE=?c, AGR=?a]
 # Lexical Productions
 # masc
 Det[CASE=nom, AGR=[GND=masc,NUM=sg]] -> 'der' | 'ein'
 Det[CASE=gen, AGR=[GND=masc,NUM=sg]] -> 'des' | 'eines'
 Det[CASE=dat, AGR=[GND=masc,NUM=sg]] -> 'dem' | 'einem'
 Det[CASE=acc, AGR=[GND=masc,NUM=sg]] -> 'den' | 'einen'
 # fem
 Det[CASE=nom, AGR=[GND=fem,NUM=sg]] -> 'die' | 'eine'
 Det[CASE=gen, AGR=[GND=fem,NUM=sg]] -> 'der' | 'einer'
 Det[CASE=dat, AGR=[GND=fem,NUM=sg]] -> 'der' | 'einer'
 Det[CASE=acc, AGR=[GND=fem,NUM=sg]] -> 'die' | 'eine'
 # neu
 Det[CASE=nom, AGR=[GND=neu,NUM=sg]] -> 'das' | 'ein'
 Det[CASE=gen, AGR=[GND=neu,NUM=sg]] -> 'des' | 'eines'
 Det[CASE=dat, AGR=[GND=neu,NUM=sg]] -> 'dem' | 'einem'
 Det[CASE=acc, AGR=[GND=neu,NUM=sg]] -> 'das' | 'ein'
 # Nouns
 N[CASE=gen, AGR=[GND=masc,NUM=sg]] -> 'Hundes'
 N[CASE=nom, AGR=[GND=masc,NUM=sg]] -> 'Hund'
 
 N[AGR=[GND=fem,NUM=sg]] -> 'Katze'
 
 N[CASE=gen, AGR=[GND=masc,NUM=sg]] -> 'Kindes'
 N[AGR=[GND=neu,NUM=sg]] -> 'Kind'
""")

tokens = 'Katze'.split()
parser = nltk.FeatureChartParser(grammar)
for tree in parser.nbest_parse(tokens):
    print tree