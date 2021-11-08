from collections import Counter

def find_uniq(arr):
    # most common returns a list of tuples, 
    # in descending order of the most common to least common values (number, count)
    return Counter(arr).most_common()[-1][0]

def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
