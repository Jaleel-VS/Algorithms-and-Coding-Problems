strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"] 
k = 2



def find_consec_words(listy, skippy):
    if len(listy) == 0 or skippy > len(listy) or skippy <= 0:
        return ""
    consec_words = []
    for i in range(len(listy) - skippy + 1):
        concat = ""
        for j in range(i, i + skippy):
            concat += listy[j]
        consec_words.append(concat)

    return find_first_longest(consec_words)

def find_first_longest(listy2):
    longest = ''
    biggest = -1
    for word in listy2:
        word_size = len(word)
        if word_size > biggest:
            biggest = word_size
            longest = word
    
    return longest



print(find_consec_words(strarr, k))
print(find_consec_words(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2))
print(find_consec_words(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3))
