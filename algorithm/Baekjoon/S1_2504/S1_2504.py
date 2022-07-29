string = input()
stack = []
calc = []
result = 0
tmp = 1
prv = -1         # 이전 값이 닫는 괄호였으면 0, 여는 괄호였으면 1
for c in string:
    if c in '([':
        stack.append(c)
    elif c in ')]':
        if not stack:       # 닫는 괄호가 나왔는데 stack에 여는 괄호가 없다면 0 출력
            result = 0
            break
        x = stack.pop()
        if c == ')':
            if not prv:     # 닫는 괄호였을 경우
                pass
        if c == ']':
            pass