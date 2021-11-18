def comp(a1, a2):
    return None not in (a1,a2) and [i*i for i in sorted(a1)]==sorted(a2)

def comp(a1, a2):
    return None not in (a1, a2) and all(x**2 == y for x, y in zip(sorted(a1), sorted(a2)))
    # all checks if all values are True in an iterable
