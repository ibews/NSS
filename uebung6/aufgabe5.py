# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 12:56:36 2013

@author: ibews
"""



# Modify the grammar
# 
# S -> NP VP
# PP -> P NP
# NP -> Det N | Det N PP | 'I'
# VP -> V NP | VP PP
# Det -> 'an' | 'my'
# N -> 'elephant' | 'pajamas'
# V -> 'shot'
# P -> 'in'
# 
# (cf. lecture Grammatiken und Parsing in NLTK (slide 6)) to parse the sentence
# 
# I saw John shooting an elephant in my pajamas in a cage.
# 
# How many interpretations and how many parsing trees are possible?

import nltk

grammar = nltk.parse_cfg("""
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP PP | V N VG NP
Det -> 'an' | 'my' | 'a'
N -> 'John' | 'elephant' | 'pajamas' | 'cage'
V -> 'shot' | 'saw'
VG -> 'shooting'
P -> 'in'
""")

# Parser auf Grundlage der Grammatik erzeugen
parser = nltk.ChartParser(grammar)

# Das zu parsende Wort
word = "I saw John shooting an elephant in my pajamas in a cage".split()

# Parsen => Erzeugen der Syntaxbaeume
trees = parser.nbest_parse(word)

# Ausgabe der Syntaxbaeume
for tree in trees:
    print tree
    
print len(trees)
# 4
# possible interpretations:
# 3/4?