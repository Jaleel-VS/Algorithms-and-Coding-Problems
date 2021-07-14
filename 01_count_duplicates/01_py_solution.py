def duplicate_count(text):
    letters = {}
    # add each letter to the dictionary. Each duplicate letter's value will be incremented
    for letter in text.lower():
        letters[letter] += 1

    # Loop through dictionary, add 1 to a list if value is greater than 1
    return sum([ 1 for k,v in letters.items() if v > 1])
