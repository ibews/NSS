# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 22:57:23 2014

@author: ibews
"""

from nltk.corpus import wordnet as wn
from aufgabe3 import synonyms
from random import choice

def hyper(word):
    hyper = [item for sublist in [s.hypernyms() for s in wn.synsets(word)] for item in sublist]
    return set([item for sublist in hyper for item in sublist.lemma_names])
    
def hypo(word):
    hypo = [item for sublist in [s.hyponyms() for s in wn.synsets(word)] for item in sublist]
    return set([item for sublist in hypo for item in sublist.lemma_names])

def rephrase(sent, mode="syno"):
    if not mode in ["syno", "hyper", "hypo"]:
        raise ValueError("mode must be either \"syno\", \"hyper\" or \"hypo\".")
    result = []
    
    for word in sent:
        if "syno" == mode:
            words = list(synonyms(word))
        elif "hyper" == mode:
            words = list(hyper(word))
        else:
            words = list(hypo(word))
    
        if 0 < len(words):
            result.append(choice(words))
        else:
            result.append(word)
    return result;

# In [65]: rephrase(["i", "saw", "a", "computer"])
# Out[65]: ['ace', 'interpret', 'axerophthol', 'computing_device']
# In [92]: rephrase(["i", "saw", "a", "race"], "hyper")
# Out[92]: ['chemical_element', 'watch', 'base', 'canal']
# In [106]: rephrase(["Bycycles", "are", "not", "cars"])
# Out[106]: ['Bycycles', 'follow', 'non', 'machine']
# In [107]: rephrase(["Bycycles", "are", "not", "cars"], mode="hypo")
# Out[107]: ['Bycycles', 'coexist', 'not', 'electric_automobile']
# In [108]: rephrase(["Bycycles", "are", "not", "cars"], mode="hyper")
# Out[108]: ['Bycycles', 'rest', 'not', 'automotive_vehicle']

# None of the test sentences was easier to understand since a random replacement word from
# the list constructed from the hyponyms, hypernyms or synonyms is chosen.
# simple words like "I" or "a" or "no" are often recognized as chemical elements.