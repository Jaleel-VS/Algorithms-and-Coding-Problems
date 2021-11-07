# my solution

# # b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]

# # new_b = list(map(lambda x: int(x**0.5), b))

# print(new_b)

def comp(array1, array2):
    if array1 == None or array2 == None:
        return False

    return sorted(array1) == sorted(list(map(lambda x: x**0.5, array2)))

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

c = [121, 144, 19, 161, 19, 144, 19, 11]  
d = [132, 14641, 20736, 361, 25921, 361, 20736, 361]

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]

e = []
f = []

print(comp(a, b))
print(comp(c, d))
print(comp(a1, a2))
print(comp(e, f))
