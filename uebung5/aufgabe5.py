# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 18:38:20 2013

@author: ibews
"""

# Definieren Sie mit NLTK eine Grammatik g_pal der formalen Sprache Lpal, die 
# alle Palindrome über dem Alphabet {a,b} enthält. Ein Palindrom ist ein Wort,
# das sowohl vorwärts als auch rückwärts mit dem gleichen Ergebnis gelesen werden
# kann (wie bspw. 'Reliefpfeiler', bzw. über dem gegebenen Alphabet 'abba' oder
# 'aba').


# Das leere Wort (Lambda) wird in dieser Grammatik definiert als L

import nltk

grammar = nltk.parse_cfg("""
S -> X | L
X -> 'a' X 'a' | L
X -> 'b' X 'b' | L
X -> 'a' | 'b'
L ->
""")

# Parser auf Grundlage der Grammatik erzeugen
parser = nltk.ChartParser(grammar)

# Das zu parsende Wort
word = "baabbab"

# Parsen => Erzeugen der Syntaxbaeume
trees = parser.nbest_parse(word)

# Ausgabe der Syntaxbaeume
for tree in trees:
    print tree
