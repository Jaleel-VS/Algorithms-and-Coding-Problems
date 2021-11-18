def valid_parentheses(string):
    if len(string) == 0: return True
    stack = []
    for s in string:
        if s in ['(', ')']:
            if s == ')':
                if stack and stack[-1] == '(': stack.pop()
                else: return False
            else:
                stack.append(s)
        else:
            continue

    return not stack

# def isValid(s: str) -> bool:
#     stack = []
#     closeToOpen = {
#         ")" : "(",
#         "]" : "[",
#         "}" : "{",
#     }

#     for c in s:
#         if c in closeToOpen:
#             if stack and stack[-1] == closeToOpen[c]:
#                 stack.pop()

#             else: return False
        
#         else:
#             stack.append(c)

#     return not stack


# print(isValid("))"))
