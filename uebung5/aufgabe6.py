# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 19:00:05 2013

@author: ibews
"""

# Definieren Sie mit NLTK eine kontextfreie Grammatik g_odd für die formale
# Sprache Lodd, die alle Zahlen (auch jene mit führenden Nullen) enthält, deren
# Quersumme ungerade ist:

#

import nltk

grammar = nltk.parse_cfg("""
S -> U Y | G S
Y -> U X U X | U X U X Y | L
X -> G X | L
U -> "1" | "3" | "5" | "7" | "9"
G -> "0" | "2" | "4" | "6" | "8"
L ->
""")

# Parser auf Grundlage der Grammatik erzeugen
parser = nltk.ChartParser(grammar)

# Das zu parsende Wort
word = "011112112111011"

# Parsen => Erzeugen der Syntaxbaeume
trees = parser.nbest_parse(word)

# Ausgabe der Syntaxbaeume
for tree in trees:
    print tree
