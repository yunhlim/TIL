# 괄호가 정상인지 확인
def check():
    stack = []
    for c in string:
        if c in '[(':
            stack.append(c)
        elif c == ']':
            if not stack or stack.pop() != '[':
                return False
        elif c == ')':
            if not stack or stack.pop() != '(':
                return False
    if stack:
        return False
    else:
        return True


# 괄호 점수 세기
def score_counting():
    arr = string[:]
    while len(arr) != 1:
        stack = []
        for c in arr:
            if c == ['(', '[']:
                stack.append(c)
            elif c not in gwalho:   # 숫자가 나올 경우
                if not stack:
                    stack.append(c)
                elif stack[-1] not in gwalho:     # 숫자가 스택에 있으면 곱해준다.
                    stack.append(stack.pop() + int(c))
                else:
                    stack.append(c)
            else:
                if c == ']':
                    if stack[-1] == '[':
                        stack.pop()
                        stack.append(3)
                    elif (stack[-1] not in gwalho) and stack[-2] == '[':
                        num = stack.pop()
                        stack.pop()
                        stack.append(num * 3)
                    else:
                        stack.append(c)
                elif c == ')':
                    if stack[-1] == '(':
                        stack.pop()
                        stack.append(2)
                    elif (stack[-1] not in gwalho) and stack[-2] == '(':
                        num = stack.pop()
                        stack.pop()
                        stack.append(num * 2)
                    else:
                        stack.append(c)
                else:
                    stack.append(c)
        arr = stack[:]
    return arr[0]


gwalho = ['[', '(', ']', ')']
string = input()
if not check():
    print(0)
else:
    print(score_counting())
