arr = list(input())
stack = []  # 연산자를 담을 stack
temp = []  # 후위 표기식으로 나타낸 걸 담을 리스트
for v in arr:  # 후위 표기식을 나타내기
    if v in '*/':
        while stack and stack[-1] in '*/':
            temp.append(stack.pop())
        stack.append(v)
    elif v in '+-':
        while stack and stack[-1] in '+-*/':
            temp.append(stack.pop())
        stack.append(v)
    elif v == '(':
        stack.append(v)
    elif v == ')':
        while stack[-1] != '(':
            temp.append(stack.pop())
        stack.pop()
    else:
        temp.append(v)
while stack:
    temp.append(stack.pop())
print(''.join(temp))