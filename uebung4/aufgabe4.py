# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 17:11:33 2013

@author: ibews
"""

import nltk
from nltk.corpus import brown

brown_tagged_sents = brown.tagged_sents(categories='news')
size = int(len(brown_tagged_sents) * 0.9)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]

t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1)
t3 = nltk.TrigramTagger(train_sents, backoff=t2)

print t3.evaluate(test_sents)
# 0.8423203428685339
