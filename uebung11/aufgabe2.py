# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 22:21:02 2014

@author: ibews
"""

from nltk.corpus import wordnet as wn

def get_synsets(word):
    #return string: 
    #synset <number>: {<lemma_names>}
    #   def: <definition>
    #   examples: <example 1>
    #   examples: <example 2>
    #   ...
    #
    result = ""
    count = 0
    senses = wn.synsets(word)
    if len(senses) == 0:
        return "no synsets"
    
    for sense, count in zip((senses), range(len(senses))):
        result += "synset {}: {{{}}}\n\tdef: {}\n".format(count+1, sense.lemma_names, sense.definition)
        examples = sense.examples
        if len(examples) == 0:
            result += "\tno examples\n\n"
        else:
            for ex in examples:
                result+= "\texample: {}\n".format(ex)
        result += "\n"
    
    return result.strip()
    
# print get_synsets("dog")
# synset 1: {['dog', 'domestic_dog', 'Canis_familiaris']}
#         def: a member of the genus Canis (probably descended from the common wolf) that has been domesticated by man since prehistoric times; occurs in many breeds
#         example: the dog barked all night
#
# synset 2: {['frump', 'dog']}
#         def: a dull unattractive unpleasant girl or woman
#         example: she got a reputation as a frump
#         example: she's a real dog
#
# print get_synsets("blargh")
# no synsets