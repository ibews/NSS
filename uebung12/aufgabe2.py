# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 21:16:40 2014

@author: ibews
"""

import nltk

lp = nltk.LogicParser()

e1 = lp.parse(r'\x exists y.(love(x, y))')
e2 = lp.parse('pat')
e3 = nltk.sem.logic.ApplicationExpression(e1, e2)
print e3.simplify()
#exists y.love(pat,y)
#exists y.love(pat, y)

e1 = lp.parse(r'\x exists y.(love(x,y) | love(y,x))')
e2 = lp.parse('pat')
e3 = nltk.sem.logic.ApplicationExpression(e1, e2)
print e3.simplify()
#exists y.(love(pat,y) | love(y,pat))
#exists y.(love(pat,y) | love(y,pat))

e1 = lp.parse(r'\x .walk(x)')
e2 = lp.parse('fido')
e3 = nltk.sem.logic.ApplicationExpression(e1, e2)
print e3.simplify()
#walk(fido)
#walk(fido)