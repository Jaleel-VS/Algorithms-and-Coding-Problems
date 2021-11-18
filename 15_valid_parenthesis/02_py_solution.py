def valid_parentheses(string):
    open = 0
    for i in range(len(string)):
        if string[i] == "(":
            open+=1
        elif string[i] == ")":
            open-=1
            if open < 0:
                return False
                
    return open == 0


