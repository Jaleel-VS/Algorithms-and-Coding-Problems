def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]

def anagrams_3(word, words):
    return list(filter(lambda x: sorted(word) == sorted(x), words))

