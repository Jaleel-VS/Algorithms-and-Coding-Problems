def high_and_low(numbers):
    int_list = list(map(int, numbers.split()))
    return f"{max(int_list)} {min(int_list)}"

# YOU CAN LOOP OVER FUNCTIONS!!!
def high_and_low(numbers):
    valy = []
    for function in (max, min):
        my_val = function(numbers.split(), key=int)
        valy.append(my_val)

