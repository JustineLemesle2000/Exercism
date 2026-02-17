from collections import Counter
def find_anagrams(word, candidates):
    res = []
    for mot in candidates : 
        if mot.lower() == word.lower() :
            continue
        if Counter(mot.lower()) == Counter(word.lower()) :
            res.append(mot)
    return res


        
