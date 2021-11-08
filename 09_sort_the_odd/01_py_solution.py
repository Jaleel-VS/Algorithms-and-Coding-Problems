original_list = [5, 8, 6, 3, 4]

odd_numbers = sorted([x for x in original_list if x % 2 != 0])
odd_iter = iter(odd_numbers)

new_list = []

for y in original_list:
    if y % 2 == 0:
        new_list.append(y)
    else:
        new_list.append(next(odd_iter))


print(new_list)