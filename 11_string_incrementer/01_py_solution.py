def increment_string(strng):
    if len(strng) == 0 or not strng[-1].isdigit():
        return strng + "1"
        
    num = "" 
    prenum = "" #string before number
    for i in range(len(strng)-1, -1, -1):
        if strng[i].isdigit():
            num = strng[i] + num
        else:
            prenum = strng[0: i + 1]
            break
    
    if num[0] == '0':
        count_num_len = len(num)
        sum_one = int(num) + 1
        count_sum_one_len = len(str(sum_one))
        leading_zeros = '0' * (count_num_len - count_sum_one_len)
        return prenum + leading_zeros + str(sum_one)
    else:
        return prenum + str(int(num) + 1)

print(increment_string("1"))