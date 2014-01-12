# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 22:44:38 2014

@author: ibews
"""

from nltk.corpus import wordnet as wn

def synonyms(word):
    """returns a set of synonyms for a given word"""
    return set([item for sublist in [s.lemma_names for s in wn.synsets(word)] for item in sublist])
    
#In [41]: synonyms("computer")
#Out[41]: 
#{'calculator',
# 'computer',
# 'computing_device',
# 'computing_machine',
# 'data_processor',
# 'electronic_computer',
# 'estimator',
# 'figurer',
# 'information_processing_system',
# 'reckoner'}
#
#In [42]: synonyms("blargh")
#Out[42]: set()