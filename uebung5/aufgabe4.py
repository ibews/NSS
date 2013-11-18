# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 22:25:57 2013

@author: ibews
"""

Given is the following grammar:

S -> NP VP
VP -> V
VP -> V NP
NP -> N2
NP -> Det N2
N2 -> Adj N2
N2 -> N

(1) John eats the beautiful red apple.
(2) He loves a smart woman.

a Create a suitable lexicon for these sentences (e.g., N -> apple).
b List five more sentences which can be generated from this grammar using this lexicon.


(S (NP (N2 (N John))) (VP (V eats) (NP (Det the) (N2 (Adj beautiful) (N2 (Adj red) (N2 (N apple)))))))
(S (NP (N He)) (VP (V loves) (NP (Det a) (N2 (Adj smart) (N2 (N woman))))))

a:
N -> John, apple, He, woman
V -> eats, loves
Adj -> smart, red, beautiful
Det -> the, a

b:
(S (NP (N Woman)) (VP (V eats)))
(S (NP (N He)) (VP (V eats)))
(S (NP (N John)) (VP (V eats)))
(S (NP (N apple)) (VP (V eats)))
(S (NP (N Woman)) (VP (V eats) (NP (Det the) (N2 (N John)))))