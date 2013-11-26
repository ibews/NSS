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
S -> PN VP
VP -> V NP | V S
NP -> NAME | FW NAME
PN -> 'I'
A0 -> '100m'
N0 -> 'record'
FW -> 'that'
Det -> 'the'
V -> 'said' | 'reported' | 'broke' | 'thought'
NAME -> 'Andre' | 'Usain Bolt'
PROPER -> 'Jamaica Observer'
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