# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 17:20:00 2013

@author: ibews
"""

from nltk import RegexpTagger
from nltk.corpus import brown

# Frank's talk was the best talk of the conference he visited in 2009.
# He could apply most of the proposed ways for getting involved in 
# political actions. 

text = "Frank's talk was the best talk of the conference he visited in 2009 . \
        He could apply most of the proposed ways for getting involved in \
        political actions . Since then he watches the local news more attentive"

patterns = [
        (r'.*ing$', 'VBG'),               # gerunds
        (r'.*ed$', 'VBD'),                # simple past
        (r'.*es$', 'VBZ'),                # 3rd singular present
        (r'.*ould$', 'MD'),               # modals
        (r'.*\'s$', 'NN$'),               # possessive nouns
        (r'.*s$', 'NNS'),                 # plural nouns
        (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
        (r'.*', 'NN')                     # nouns (default)
    ]
    

additions = [
        (r'[.?;!:]', '.'),
        ('\\($', '('),
        (r'.*ly$', 'ADV'),
        ('n[o\']t$', '*'),
        (r'^,$', ',')
    ]

ret = RegexpTagger(patterns)
print ret.evaluate(brown.tagged_sents(categories='news'))
    
for pattern in additions:
    patterns.insert(-1, pattern)
    print "added pattern {}".format(pattern)
    ret = RegexpTagger(patterns)
    print ret.evaluate(brown.tagged_sents(categories='news'))
    
# 0.203263917895
# added pattern ('[.?;!:]', '.')
# 0.247538635957
# added pattern ('\\($', '(')
# 0.24901048193
# added pattern ('.*ly$', 'ADV')
# 0.248314338564
# added pattern ("n[o']t$", '*')
# 0.250830399586
# added pattern ('^,$', ',')
# 0.301877598106
