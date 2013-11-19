# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 23:02:08 2013

@author: ibews
"""

from nltk import RegexpTagger
import nltk

text = u"""Langsam erhob sich der Brahmane, Siddhartha stand stumm mit gekreuzten 
Armen. Worauf wartest du? fragte der Vater. Sprach Siddhartha: Du weißt es. Unwillig 
ging der Vater aus der Kammer, unwillig suchte er sein Lager auf und legte sich nieder. 
Nach einer Stunde, da kein Schlaf in seine Augen kam, stand der Brahmane von neuem auf, 
tat Schritte hin und her, trat vor das Haus, sah den Mond aufgegangen. Durch das Fenster 
der Kammer blickte er hinein, da stand Siddhartha, unverrückt, mit gekreuzten Armen, an 
seinen bloßen Schienbeinen spiegelte das Mondlicht. Besorgnis im Herzen, suchte der Vater 
sein Lager auf. """


words = [(u'Langsam', 'ADJ'), (u'erhob', None), (u'sich', None), (u'der', None), 
         (u'Brahmane', 'NN'), (u',', None), (u'Siddhartha', None), (u'stand', None), 
         (u'stumm', 'ADJ'), (u'mit', None), (u'gekreuzten', 'ADJ'), (u'Armen.', None), 
         (u'Worauf', None), (u'wartest', None), (u'du', None), (u'?', None), 
         (u'fragte', None), (u'der', None), (u'Vater.', 'NN'), (u'Sprach', None), 
         (u'Siddhartha', None), (u':', None), (u'Du', None), (u'weißt', None), 
         (u'es.', None), (u'Unwillig', 'ADJ'), (u'ging', None), (u'der', None), 
         (u'Vater', 'NN'), (u'aus', None), (u'der', None), (u'Kammer', 'NN'), 
         (u',', None), (u'unwillig', 'ADJ'), (u'suchte', None), (u'er', None), 
         (u'sein', None), (u'Lager', 'NN'), (u'auf', None), (u'und', None), 
         (u'legte', None), (u'sich', None), (u'nieder.', None), (u'Nach', None), 
         (u'einer', None), (u'Stunde', 'NN'), (u',', None), (u'da', None), 
         (u'kein', None), (u'Schlaf', 'NN'), (u'in', None), (u'seine', None), 
         (u'Augen', 'NN'), (u'kam', None), (u',', None), (u'stand', None), 
         (u'der', None), (u'Brahmane', 'NN'), (u'von', None), (u'neuem', None), 
         (u'auf', None), (u',', None), (u'tat', None), (u'Schritte', 'NN'), 
         (u'hin', None), (u'und', None), (u'her', None), (u',', None), (u'trat', None), 
         (u'vor', None), (u'das', None), (u'Haus', 'NN'), (u',', None), (u'sah', None), 
         (u'den', None), (u'Mond', 'NN'), (u'aufgegangen.', None), (u'Durch', None), 
         (u'das', None), (u'Fenster', 'NN'), (u'der', None), (u'Kammer', 'NN'), 
         (u'blickte', None), (u'er', None), (u'hinein', None), (u',', None), 
         (u'da', None), (u'stand', None), (u'Siddhartha', None), (u',', None), 
         (u'unverrückt', 'ADJ'), (u',', None), (u'mit', None), (u'gekreuzten', 'ADJ'), 
         (u'Armen', 'NN'), (u',', None), (u'an', None), (u'seinen', None), 
         (u'bloßen', 'ADJ'), (u'Schienbeinen', 'NN'), (u'spiegelte', None), (u'das', None), 
         (u'Mondlicht.', 'NN'), (u'Besorgnis', 'NN'), (u'im', None), (u'Herzen', 'NN'), 
         (u',', None), (u'suchte', None), (u'der', None), (u'Vater', 'NN'), (u'sein', None), 
         (u'Lager', 'NN'), (u'auf', None), (u'.', None)]

patterns = [
        (ur'.*ung$', 'NN'),
        (ur'.*keit$', 'NN'),
        (ur'.*heit$', 'NN'),
        (ur'.*nis$', 'NN'),
        (ur'.*schaft$', 'NN'),
        (ur'.*mus$', 'NN'),
        (ur'.*er$', 'NN'),
        (ur'.*chen$', 'NN'),
        (ur'.*lein$', 'NN'),
        (ur'.*lich$', 'ADJ'),
        (ur'.*ig$', 'ADJ'),
        (ur'.*isch$', 'ADJ'),
        (ur'.*haft$', 'ADJ'),
        (ur'.*bar$', 'ADJ'),
        (ur'.*los$', 'ADJ'),
        (ur'.*sam$', 'ADJ'),
        (ur'.*', None)
    ]
    
ret = RegexpTagger(patterns)
tokens = nltk.word_tokenize(text)
tagged = ret.tag(tokens)

diff = [(w, lt, rt)
        for ((w, lt),(_, rt)) in zip(tagged, words)
        if lt != rt
        ]

print diff
# [(u'der', 'NN', None), (u'Brahmane', None, 'NN'), (u'stumm', None, 'ADJ'),
# (u'gekreuzten', None, 'ADJ'), (u'der', 'NN', None), (u'Vater.', None, 'NN'),
# (u'der', 'NN', None), (u'der', 'NN', None), (u'er', 'NN', None), (u'einer', 'NN', None),
# (u'Stunde', None, 'NN'), (u'Schlaf', None, 'NN'), (u'Augen', None, 'NN'),
# (u'der', 'NN', None), (u'Brahmane', None, 'NN'), (u'Schritte', None, 'NN'),
# (u'her', 'NN', None), (u'Haus', None, 'NN'), (u'Mond', None, 'NN'), (u'der', 'NN', None),
# (u'er', 'NN', None), (u'unverr\xfcckt', None, 'ADJ'), (u'gekreuzten', None, 'ADJ'),
# (u'Armen', None, 'NN'), (u'blo\xdfen', None, 'ADJ'), (u'Schienbeinen', None, 'NN'),
# (u'Mondlicht.', None, 'NN'), (u'Herzen', None, 'NN'), (u'der', 'NN', None)]


# Sehr schlechte Performance, da wenig Worte mit den durch den Tagger angenommenen Endungen im Text enthalten sind.
# Weiterhin wurden Worte wie „der“ falsch getaggt, da nicht auf die Groß- und Kleinschreibung geachtet wurde.