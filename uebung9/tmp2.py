# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 18:16:30 2013

@author: ibews
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-
import nltk

grammar = nltk.parse_fcfg(
"""
S -> NP[CASE=?c, GND=?g, NUM=?n, DET=?d]

NP[CASE=?c, GND=?g, NUM=?n, DET=?d] -> Det[CASE=?c, GND=?g, NUM=?n, DET=?d] N[CASE=?c, GND=?g, NUM=?n]
NP[CASE=?c, GND=?g, NUM=?n, DET=?d] -> Det[CASE=?c, GND=?g, NUM=?n, DET=?d] Adj[CASE=?c, GND=?g, NUM=?n, DET=?d] N[CASE=?c, GND=?g, NUM=?n]
NP[CASE=?c, GND=?g, NUM=pl, DET=?d] -> N[CASE=?c, GND=?g, NUM=pl]
NP[CASE=?c, GND=?g, NUM=pl, DET=?d] -> Adj[CASE=?c, GND=?g, NUM=pl, DET=?d] N[CASE=?c, GND=?g, NUM=pl]

Det[CASE=nom, GND=m, NUM=sg, DET=bes] -> 'der'
Det[CASE=gen, GND=m, NUM=sg, DET=bes] -> 'des'
Det[CASE=dat, GND=m, NUM=sg, DET=bes] -> 'dem'
Det[CASE=akk, GND=m, NUM=sg, DET=bes] -> 'den'

Det[CASE=nom, GND=m, NUM=sg, DET=unb] -> 'ein'
Det[CASE=gen, GND=m, NUM=sg, DET=unb] -> 'eines'
Det[CASE=dat, GND=m, NUM=sg, DET=unb] -> 'einem'
Det[CASE=akk, GND=m, NUM=sg, DET=unb] -> 'einen'

Det[CASE=nom, GND=w, NUM=sg, DET=bes] -> 'die'
Det[CASE=gen, GND=w, NUM=sg, DET=bes] -> 'der'
Det[CASE=dat, GND=w, NUM=sg, DET=bes] -> 'der'
Det[CASE=akk, GND=w, NUM=sg, DET=bes] -> 'die'

Det[CASE=nom, GND=w, NUM=sg, DET=unb] -> 'eine'
Det[CASE=gen, GND=w, NUM=sg, DET=unb] -> 'einer'
Det[CASE=dat, GND=w, NUM=sg, DET=unb] -> 'einer'
Det[CASE=akk, GND=w, NUM=sg, DET=unb] -> 'eine'

Det[CASE=nom, GND=n, NUM=sg, DET=bes] -> 'das'
Det[CASE=gen, GND=n, NUM=sg, DET=bes] -> 'des'
Det[CASE=dat, GND=n, NUM=sg, DET=bes] -> 'dem'
Det[CASE=akk, GND=n, NUM=sg, DET=bes] -> 'das'

Det[CASE=nom, GND=n, NUM=sg, DET=unb] -> 'ein'
Det[CASE=gen, GND=n, NUM=sg, DET=unb] -> 'eines'
Det[CASE=dat, GND=n, NUM=sg, DET=unb] -> 'einem'
Det[CASE=akk, GND=n, NUM=sg, DET=unb] -> 'ein'

Det[CASE=nom, NUM=pl] -> 'die'
Det[CASE=gen, NUM=pl] -> 'der'
Det[CASE=dat, NUM=pl] -> 'den'
Det[CASE=akk, NUM=pl] -> 'die'

N[CASE=nom, GND=m, NUM=sg] -> 'Baum'
N[CASE=gen, GND=m, NUM=sg] -> 'Baumes'
N[CASE=dat, GND=m, NUM=sg] -> 'Baum' | 'Baume'
N[CASE=akk, GND=m, NUM=sg] -> 'Baum'

N[CASE=nom, GND=m, NUM=pl] -> 'Bäume'
N[CASE=gen, GND=m, NUM=pl] -> 'Bäume'
N[CASE=dat, GND=m, NUM=pl] -> 'Bäumen'
N[CASE=akk, GND=m, NUM=pl] -> 'Bäume'

N[GND=w, NUM=sg] -> 'Kuh'

N[CASE=nom, GND=w, NUM=pl] -> 'Kühe'
N[CASE=gen, GND=w, NUM=pl] -> 'Kühe'
N[CASE=dat, GND=w, NUM=pl] -> 'Kühen'
N[CASE=akk, GND=w, NUM=pl] -> 'Kühe'

N[CASE=nom, GND=n, NUM=sg] -> 'Buch'
N[CASE=gen, GND=n, NUM=sg] -> 'Buches'
N[CASE=dat, GND=n, NUM=sg] -> 'Buch' | 'Buche'
N[CASE=akk, GND=n, NUM=sg] -> 'Buch'

N[CASE=nom, GND=n, NUM=pl] -> 'Bücher'
N[CASE=gen, GND=n, NUM=pl] -> 'Bücher'
N[CASE=dat, GND=n, NUM=pl] -> 'Büchern'
N[CASE=akk, GND=n, NUM=pl] -> 'Bücher'

Adj[CASE=nom, NUM=sg, DET=bes] -> 'alte'
Adj[CASE={gen,dat}, NUM=sg, DET=bes] -> 'alten'
Adj[CASE=akk, GND=m, NUM=sg, DET=bes] -> 'alten'
Adj[CASE=akk, GND=w, NUM=sg, DET=bes] -> 'alten'
Adj[NUM=pl, DET=bes] -> 'alten'

Adj[CASE=nom, GND=m, NUM=sg, DET=unb] -> 'alter'
Adj[CASE=gen, GND=m, NUM=sg, DET=unb] -> 'alten'

Adj[CASE={nom,akk}, GND=w, NUM=sg, DET=unb] -> 'alte'
Adj[CASE=gen, GND=w, NUM=sg, DET=unb] -> 'alten'

Adj[CASE={nom,akk}, GND=n, NUM=sg, DET=unb] -> 'altes'
Adj[CASE=gen, GND=n, NUM=sg, DET=unb] -> 'alten'

Adj[NUM=pl, DET=bes] -> 'alten'
""")

parser = nltk.FeatureChartParser(grammar, trace=10)

trees = parser.nbest_parse('einer alten Kuh'.split())

for tree in trees:
    print tree

"""
der Kuh
(S[]
(NP[CASE='gen', DET='bes', GND='w', NUM='sg']
(Det[CASE='gen', DET='bes', GND='w', NUM='sg'] der)
(N[GND='w', NUM='sg'] Kuh)))
(S[]
(NP[CASE='dat', DET='bes', GND='w', NUM='sg']
(Det[CASE='dat', DET='bes', GND='w', NUM='sg'] der)
(N[GND='w', NUM='sg'] Kuh)))

der Kühe
(S[]
(NP[CASE='gen', DET=?d, GND='w', NUM='pl']
(Det[CASE='gen', NUM='pl'] der)
(N[CASE='gen', GND='w', NUM='pl'] Kühe)))

der alten Kühe
(S[]
(NP[CASE='gen', DET='bes', GND='w', NUM='pl']
(Det[CASE='gen', NUM='pl'] der)
(Adj[DET='bes', NUM='pl'] alten)
(N[CASE='gen', GND='w', NUM='pl'] Kühe)))
"""