# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 11:51:10 2013

@author: ibews
"""

# a Definieren Sie mit NLTK eine kontextfreie Grammatik, mit deren Hilfe der Satz
#   "I saw the man on the hill with a telescope" geparst werden kann (siehe
#   Grammatiken und Parsing in NLTK).
#
# b Parsen Sie den gegebenen Satz unter Verwendung Ihrer Grammatik und
#   vergleichen Sie die Ableitungsbäume, indem Sie für jeden Baum eine geeignete
#   deutsche Paraphrase angeben, die der jeweiligen Interpretation des Satzes
#   entspricht.
# 
# Hinweis: Sie können Begriffe wie 'Teleskopberg' (= Berg auf dem sich ein
# Teleskop befindet) verwenden, um Ihre Formulierungen kürzer und verständlicher
# zu gestalten, sofern Sie die Bedeutung dieser Begriffe angeben.

import nltk

grammar = nltk.parse_cfg("""
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP PP
Det -> 'a' | 'the'
P -> 'with' | 'on'
N -> 'hill' | 'telescope' | 'man'
V -> 'saw'
""")



# Parser auf Grundlage der Grammatik erzeugen
parser = nltk.ChartParser(grammar)

# Das zu parsende Wort
word = ["I", "saw", "the", "man", "on", "the", "hill", "with", "a", "telescope"]

# Parsen => Erzeugen der Syntaxbaeume
trees = parser.nbest_parse(word)

# Ausgabe der Syntaxbaeume
for tree in trees:
    print tree
    
# (S
#   (NP I)
#   (VP
#     (V saw)
#     (NP
#       (Det the)
#       (N man)
#       (PP
#         (P on)
#         (NP
#           (Det the)
#           (N hill)
#           (PP (P with) (NP (Det a) (N telescope))))))))
# Ich sah den Mann, der ein Teleskop (dabei) hat, auf dem Hügel.

# (S
#   (NP I)
#   (VP
#     (VP
#       (V saw)
#       (NP (Det the) (N man) (PP (P on) (NP (Det the) (N hill)))))
#     (PP (P with) (NP (Det a) (N telescope)))))
# Ich sah den Mann, der auf dem Hügel war, durch ein Teleskop

# (S
#   (NP I)
#   (VP
#     (VP (V saw) (NP (Det the) (N man)))
#     (PP
#       (P on)
#       (NP
#         (Det the)
#         (N hill)
#         (PP (P with) (NP (Det a) (N telescope)))))))
# Ich sah den Mann auf dem Hügel, auf dem ein Teleskop steht.

# (S
#   (NP I)
#   (VP
#     (VP
#       (VP (V saw) (NP (Det the) (N man)))
#       (PP (P on) (NP (Det the) (N hill))))
#     (PP (P with) (NP (Det a) (N telescope)))))
# Ich sah den Mann, als ich auf einem Hügel war, durch ein Teleskop