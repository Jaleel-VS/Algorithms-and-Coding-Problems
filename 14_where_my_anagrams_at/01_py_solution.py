# my solution

from collections import Counter
        
def anagrams(word, words):
    find_mc = lambda x: sorted(Counter(list(x)).most_common())
    most_common_letters = find_mc(word)
    return [x for x in words if most_common_letters == find_mc(x)]

