string = input()
stack = []
calc = []
result = 0

for c in string:
    if c == '(':
        stack.append(c)
    if c == ')':
        x = stack.pop()
        if 