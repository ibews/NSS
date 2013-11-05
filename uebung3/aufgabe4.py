from nltk import FreqDist
from nltk.corpus import brown

categories = ["news", "government", "lore"]

for cat in categories:
    tagged = brown.tagged_words(categories=cat, simplify_tags=True)
    tag_fd = FreqDist(tag for (word, tag) in tagged)
    print len(tagged)    
    print tag_fd
    for tag in tag_fd.items():
        print tag, 
    #tag_fd.plot()
    #tag_fd.plot(cumulative=True)

# news:
# ('N', 22226) ('DET', 11602) ('P', 10845) ('NP', 8336) ('V', 6392) ('ADJ', 5435) 
# (',', 5188) ('.', 4472) ('CNJ', 4227) ('PRO', 3408) ('ADV', 2770) ('VD', 2531) 
# ('NUM', 2508) ('VN', 2410) ('VG', 1425) ('TO', 1244) ('WH', 1101) ('MOD', 1082) 
# ('``', 732) ("''", 702) ('VBZ', 558) ('', 300) ('*', 257) (')', 171) ('(', 168) 
# ('EX', 163) (':', 149) ('FW', 92) ("'", 46) ('UH', 13) ('VB+PPO', 1)
#
# gov: 
# ('N', 17509) ('P', 9046) ('DET', 8172) ('ADJ', 4923) ('V', 4576) ('CNJ', 3735) 
# (',', 3408) ('.', 3005) ('VN', 2397) ('NP', 1930) ('PRO', 1888) ('ADV', 1745) 
# ('NUM', 1733) ('VG', 1058) ('MOD', 1012) ('TO', 935) ('WH', 654) ('VBZ', 424) 
# ('VD', 405) (')', 345) ('(', 342) ('*', 208) ('', 139) ('``', 125) ("''", 122) 
# (':', 105) ('EX', 96) ('NIL', 40) ('FW', 33) ("'", 7)
#
# lore:
# ('N', 22606) ('DET', 13612) ('P', 12225) ('V', 8209) ('ADJ', 7289) ('CNJ', 5973) 
# (',', 5519) ('PRO', 5260) ('.', 5231) ('ADV', 4143) ('NP', 3918) ('VN', 2880) 
# ('VD', 2273) ('VG', 1706) ('TO', 1550) ('NUM', 1506) ('WH', 1438) ('MOD', 1124) 
# ('VBZ', 775) ('``', 727) ("''", 717) ('*', 420) ('', 395) ('EX', 194) (')', 169) 
# ('(', 164) (':', 146) ('FW', 97) ('UH', 23) ("'", 5) ('VB+PPO', 4) ('VB+RP', 1)
#
# news:
#     N DET P NP V 60%
#   + ADJ , . CNJ PRO 82%
#
# government:
#     N P DET ADJ V 63%
#   + CNJ , . VN NP 84%
#
# lore:
#     N DET P V ADJ 58%
#   + CNJ , PRO . ADV 82%
# --> Die verteilungen Unterscheiden sich in der Häufigkeit der einzelnen Tags, jedoch nur unwesentlich in der Form
#     N P DET sind in alle 3 Fällen die 3 häufigsten Tags
