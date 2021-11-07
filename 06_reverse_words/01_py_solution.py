# my (bad) solution
def reverse_words(text):
    new_list = []
    word = ""
    for i in range(0, len(text)):
        if i == len(text) - 1:
            word += text[i]
            new_list.append(word[::-1])
        elif text[i] != " ":
            word += text[i]
        elif text[i] == " ":
            new_list.append(word[::-1])
            new_list.append(text[i])
            word = ""

    return ''.join(x for x in new_list)

#one liner
def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))
