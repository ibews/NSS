# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:19:28 2014

@author: ibews
"""

from nltk.corpus import wordnet as wn

def get_antonyms(lemma):
    results = [l.lemma_names for sublists in lemma.antonyms() for l in sublists]
    results.extend(
        [w.name for sim in lemma.synset.similar_tos() 
                  for lems in sim.lemmas 
                  for w in lems.antonyms()])
    return results