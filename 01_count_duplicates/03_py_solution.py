from collections import Counter
def duplicate_count(text):
    # similar to solution 1 but with built-in method
    my_C = Counter(t.lower() for t in text).itervalues() # count the key-value pairs in an object
    return sum(1 for v in my_C if v > 1)