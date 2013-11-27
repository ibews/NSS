# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 13:05:00 2013

@author: ibews
"""



# Verwenden Sie in dieser Aufgabe Wörter aus der News-Kategorie des Brown-Korpus.
#
# a) Bilden Sie einen möglichst langen sinnvollen englischen Satz (alternativ:
#    einen sinnvollen Text aus mehreren Sätzen), der (möglichst) nur aus Wörtern
#    besteht, die im Brown-Korpus jeweils mit mindestens zwei unterschiedlichen
#    Tags auftreten.
# b) An welchen Stellen ist es besonders schwierig, nur mehrdeutige Wortformen
#    zu verwenden?
# c) Wenden Sie auf Ihren Satz bzw. Text einen Tagger an und analysieren Sie
#    das Ergebnis.

from nltk import DefaultTagger
from nltk import UnigramTagger
from nltk.corpus import brown
from collections import defaultdict

tagged = brown.tagged_words(categories='news', simplify_tags=True)

taggings = defaultdict(set)
for word,tag in tagged:
    taggings[word].add(tag)
    
multiple = [(word, tags) for word, tags in taggings.items() if len(tags)>1]
    
sentence = "The staff succeeded in delivering the license to Christian in the 1960's \
            After they missed the first date because Christian returned home earlier"
            
brown_tagged_sents = brown.tagged_sents(categories='news')
size = int(len(brown_tagged_sents) * 0.9)
train_sents = brown_tagged_sents[:size]

t0 = DefaultTagger('NN')
t1 = UnigramTagger(train_sents, backoff=t0)

# Als Pronomen und Artikel war es nicht möglich mehrdeutige Worte zu verwenden. Weiterhin sind Namen fast nie
# mehrdeutig. Christian bildet hier die Ausnahme, da es auch ein Adjektive für Christen ist.
# Weiterhin waren in der Liste mehrdeutiger Worte nahezu keine Substantive enthalten.
# Dafür jedoch eine hohe Zahl von Verben in der Vergangenheitsform, da diese sowohl als 

#[('The', 'AT'),
# ('staff', 'NN'),
# ('succeeded', 'VBN'),
# ('in', 'IN'),
# ('delivering', 'VBG'),
# ('the', 'AT'),
# ('license', 'NN'),
# ('to', 'TO'),
# ('Christian', 'JJ'),
# ('in', 'IN'),
# ('the', 'AT'),
# ("1960's", 'CD$'),
# ('After', 'IN'),
# ('they', 'PPSS'),
# ('missed', 'VBD'),
# ('the', 'AT'),
# ('first', 'OD'),
# ('date', 'NN'),
# ('because', 'CS'),
# ('Christian', 'JJ'),
# ('returned', 'VBD'),
# ('home', 'NN'),
# ('earlier', 'RBR')]

# Das meiste ist korrekt getaggt. Dem führenden "the" sollte dies nicht zuzuschreiben sein, da nur ein Unigramtagger
# verwendet wurde. Daher ist davon auszugehen, dass die Worte im Trainingstext hauptsächlich in den hier
# relevanten Kontexten verwendet wurden.