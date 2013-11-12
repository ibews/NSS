# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:32:07 2013

@author: ibews
"""
from nltk import pos_tag as pt

t = ['Dies', 'ist', 'eine', 'Beispiel', 'bGame', '.']

a = [len(x) for x in t if "a" in x]

# Was ist mit types der Länge 4 gemeint?
# Ist eine Liste der Types von „Worten mit einer Länge == 4“ gefordert?
b = sorted(list(set(x[1] for x in pt(t) if len(x[0])==4)))