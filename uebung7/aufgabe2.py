# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:24:19 2013

@author: ibews
"""

import nltk
import random

grammar = nltk.parse_cfg("""
S   -> NP VP
VP  -> V NP | V NP PP
PP  -> P NP
V   -> 'saw' | 'ate' | 'walked'
NP  -> 'John' | 'Mary' | 'Bob' | Det N | Det N PP
Det -> 'a' | 'an' | 'the' | 'my'
N   -> 'man' | 'dog' | 'cat' | 'telescope' | 'park'
P   -> 'in' | 'on' | 'by' | 'with'
""")

def fromsymbol(g, symbol):
    if type(symbol) == str:
        return [symbol]
    else:
        rules = []
        prod = g.productions(symbol)
        for p in prod:
            rules.append(p.rhs())
        rule = random.choice(prod)
        result = []
        for r in rule.rhs():
            result.extend(fromsymbol(g, r))
        return result

def sentgen(g):
    return fromsymbol(g, g.start())


sents = []
for i in range(5): sents.append(sentgen(grammar))
    
parser = nltk.ChartParser(grammar)

for sent in sents:
    trees = parser.nbest_parse(sent)
    
    for tree in trees:
        print tree
    print "------------------------------------"
    
#(S (NP (Det a) (N cat)) (VP (V saw) (NP John) (PP (P by) (NP Bob))))
#------------------------------------
#(S
#  (NP Bob)
#  (VP (V saw) (NP (Det the) (N cat)) (PP (P by) (NP John))))
#(S
#  (NP Bob)
#  (VP (V saw) (NP (Det the) (N cat) (PP (P by) (NP John)))))
#------------------------------------
#(S
#  (NP (Det my) (N dog))
#  (VP (V ate) (NP (Det my) (N cat) (PP (P in) (NP Bob)))))
#(S
#  (NP (Det my) (N dog))
#  (VP (V ate) (NP (Det my) (N cat)) (PP (P in) (NP Bob))))
#------------------------------------
#(S (NP Mary) (VP (V walked) (NP Mary) (PP (P on) (NP Bob))))
#------------------------------------
#(S (NP Mary) (VP (V saw) (NP Bob)))
#------------------------------------