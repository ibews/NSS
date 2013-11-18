# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 23:02:08 2013

@author: ibews
"""

from nltk import RegexpTagger

patterns = [
        (r'.*ung$', 'NN'),
        (r'.*keit$', 'NN'),
        (r'.*heit$', 'NN'),
        (r'.*nis$', 'NN'),
        (r'.*schaft$', 'NN'),
        (r'.*mus$', 'NN'),
        (r'.*er$', 'NN'),
        (r'.*chen$', 'NN'),
        (r'.*lein$', 'NN'),
        (r'.*lich$', 'ADJ'),
        (r'.*ig$', 'ADJ'),
        (r'.*isch$', 'ADJ'),
        (r'.*haft$', 'ADJ'),
        (r'.*bar$', 'ADJ'),
        (r'.*los$', 'ADJ'),
        (r'.*sam$', 'ADJ'),
        (r'.*', 'NONE')
    ]
    
ret = RegexpTagger(patterns)