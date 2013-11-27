# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 12:48:17 2013

@author: ibews
"""



# Write a CFG that can generate the sentence
#
# I thought Andre said the Jamaica Observer reported that Usain Bolt broke the 100m record
#
# and similar ones. Test parsing the sentence using NLTK.

import nltk

grammar = nltk.parse_cfg("""
S -> NP VP
NP -> F NP | N | 'I' | N N
VP -> V NP | V F S | V NP VP
N -> 'Andre' | 'Jamaica Observer' | 'Usain Bolt' | '100m' | 'record'
V -> 'reported' | 'said' | 'thought' | 'said'
F -> 'the' | 'that'
""")

# Parser auf Grundlage der Grammatik erzeugen
parser = nltk.ChartParser(grammar)

# Das zu parsende Wort
word = ["I","thought","Andre","said","the","Jamaica Observer","reported",
        "that","Usain Bolt","broke","the","100m","record"]

# Parsen => Erzeugen der Syntaxbaeume
trees = parser.nbest_parse(word)

# Ausgabe der Syntaxbaeume
for tree in trees:
    print tree
    
#(S
#  (NP I)
#  (VP
#    (V thought)
#    (NP (N Andre))
#    (VP
#      (V said)
#      (NP (F the) (NP (N Jamaica Observer)))
#      (VP
#        (V reported)
#        (NP (F that) (NP (N Usain Bolt)))
#        (VP (V broke) (NP (F the) (NP (N 100m) (N record))))))))