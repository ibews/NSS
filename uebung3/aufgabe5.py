from nltk.stem.snowball import GermanStemmer

def rootform(verb):
    return GermanStemmer().stem(verb)

def inflect(stem):
    print 'ich {}e'.format(stem)
    print 'du {}st'.format(stem)
    print 'er/sie/es {}t'.format(stem)
    print 'wir {}en'.format(stem)
    print 'ihr {}t'.format(stem)
    print 'sie {}en'.format(stem)

# funktioniert zum Beispiel bei unregelmaessigen Verben nicht / nicht gut ("sein")
