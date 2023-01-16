while True:
    string = input()
    if string[0] == '.':
        break
    stack = []
    result = 'yes'
    for c in string:
        if c in '([':
            stack.append(c)
        if c == ')':
            if not stack or stack.pop() != '(':
                result = 'no'
        if c == ']':
            if not stack or stack.pop() != '[':
                result = 'no'
    if stack:
        result = 'no'
    print(result)