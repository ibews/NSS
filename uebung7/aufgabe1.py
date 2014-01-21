# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 11:21:55 2013

@author: ibews
"""



# Gegeben sei der folgende (auf rekursiven Strukturen basierende) Satz:
# die die die die die die ihn nicht kannten kannten nicht kannten kannten ihn 
# nicht
# 
#     Setzen Sie im gegebenen Satz die fehlenden Kommas und taggen Sie ihn unter
#     Verwendung folgender Tags:
#         - ADV (Adverb), FV (finites Verb), TB (transitives Verb),
#         - PPro (Personal-), DemPro (Demonstrativ-), RelPro (Relativpronomen)
#     Definieren Sie mit NLTK eine kontextfreie Grammatik, mit deren Hilfe Sätze
#     wie der obige (ohne Kommas) geparst werden können. Testen Sie ihre Grammatik
#     mit geeigneten Sätzen wie bspw. (* kennzeichnet ungrammatische Sätze):
#        - die kannten ihn nicht
#        - die die die die ihn kannten kannten kannten ihn nicht
#        - *die die ihn nicht kannten (ungrammatisch, da Satz unvollständig)
#        - *die die ihn kannten nicht kannten
#        - *die die ihn kannten ihn kannten kannten ihn
#        - *die die kannten ihn kannten ihn
#     Ersetzen Sie im gegebenen Satz alle Vorkommen von 'die' durch die geeignete 
#     Verwendung von 'jene' oder 'welche'.
#     Erweitern Sie ausschließlich die lexikalischen Regeln (d.h. Regeln der
#     Form Nichtterminal -> Terminal) ihrer Grammatik, indem Sie sie um die 
#     Einträge "jene" und "welche" ergänzen und überprüfen Sie, ob Ihre 
#     Satzvariation aus (c) von Ihrer erweiterten Grammatik geparst werden kann.
#
#     Erläutern Sie ggf. warum das Parsing scheitert und welche Veränderungen 
#     an Ihrer Grammatik vorgenommen werden müssen, um den Fehler zu beseitigen.

#die, die    die,   die    die,    die   ihn  nicht kannten, kannten, nicht kannten, kannten ihn
#PPro RelPro DemPro RelPro DemPro RelPro PPro (     TV     ) FV       (     FV     ) FV      PPro

import nltk

grammar = nltk.parse_cfg("""
S -> Pro O VP Pro
O -> Pro Pro O VP |
VP -> V | Neg V
V -> "kannten" 
Neg -> "nicht"
Pro -> "die" | "ihn"
""")

parser = nltk.ChartParser(grammar)

#word = "die die die die die die ihn nicht kannten kannten nicht kannten kannten ihn".split()
word = "die die die die ihn kannten kannten kannten ihn nicht".split()
#die die ihn nicht kannten (ungrammatisch, da Satz unvollständig)
#die die ihn kannten nicht kannten
#die die ihn kannten ihn kannten kannten ihn
#die die kannten ihn kannten ihn


trees = parser.nbest_parse(word)

for tree in trees:
    print tree