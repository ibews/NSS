# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 16:25:17 2013

@author: ibews
"""
import codecs
from nltk import RegexpTagger

f = codecs.open("./staedte.txt", "r", encoding="utf8")
names = [line.strip() for line in f.readlines()]

# https://de.wikipedia.org/wiki/Liste_der_St%C3%A4dte_in_Deutschland
# grab url
# parse html
# find all links of tho form:
#   <dd><a href="/wiki/.*" title=".*">$1</a>.*</dd>
# combing all $1 into a list.

# look through tho complete list of cities looking for similarities
# compile similaritiesinto patterns
# apply

patterns = [
    (ur'.+(Hall|bach|b[eu]rg|dorf|feld|hausen|heim|leben|r[ao]de|st[ae]dt|tah?l)$', 'city'),
    (ur'^Bad .+', 'city'),
    (ur'^Burg', 'city'),
    (ur'^.*$', 'DEFAULT')
]

ret = RegexpTagger(patterns)
tagged = ret.tag(names)

print len(filter(lambda (_, tag): tag == 'city', tagged))*100.0/len(names)