import nltk
from nltk.corpus import brown

text = brown.words(categories='reviews')
fdist = nltk.FreqDist([w.lower() for w in text])
wh = ["what", "which", "when", "where", "who", "why" ]
for w in wh:
  print w + ':', fdist[w],

# what: 56 which: 124 when: 60 where: 29 who: 130 why: 9
