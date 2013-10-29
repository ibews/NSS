import nltk

# liste aller daten im korpus
nltk.corpus.gutenberg.fileids()

# length von einem text
poems = nltk.corpus.gutenberg.words(’blake-poems.txt’)
len(poems) #8354

from nltk.corpus import gutenberg
emmaT = nltk.Text(gutenberg.words('austen-emma.txt'))

emmaT.similar("happy")
# Building word-context index...
# much well good long ready so superior that agreeable before in little
# sure all as clever cold glad kind likely

emmaT.similar("sad")
# bad complete great happy much odd strong acceptable agreeable
# comfortably completely composedly could deficient delightful different
# disagreeable distant doing dreadful

# results for sad doesn't seem to bze reasonable
# sad similar to happy. Kann sein.
