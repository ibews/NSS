#tag_ratio(brown.tagged_words(categories='news', simplify_tags=True), 'N')
def tag_ratio(tagged, tag):
    return 100.0*len(filter(lambda (_,t): t == tag,tagged))/len(tagged)

#In [3]: tag_ratio(brown.tagged_words(categories='news', simplify_tags=True), "N")
#Out[3]: 22.103546353203253
#In [4]: tag_ratio(brown.tagged_words(categories='news', simplify_tags=True), "DET")
#Out[4]: 11.538079042106729

