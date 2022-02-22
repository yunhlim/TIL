# 괄호검사
T = int(input())
for tc in range(1, T + 1):
    s = input() # 입력받은 문자열
    stack = []  # 여는 괄호를 담을 stack
    result = 0  # 괄호 검사
    for c in s:
        if c in '{(':   # 여는 괄호는 stack에 넣는다.
            stack.append(c)
        elif c in '})': # 닫는 괄호를 stack 값과 확인
            # 여는 괄호가 있는지 1차 확인, 입력받은 문자와 stack의 top이랑 비교해서 괄호가 맞다면 제거
            if stack and ((stack[-1] == '{' and c == '}') or (stack[-1] == '(' and c == ')')):
                stack.pop()
            else:   # 괄호의 짝이 맞지 않거나, 여는 괄호가 없다면 break
                break
    else:
        if not stack:   # 여는 괄호가 다 닫혔는지 확인
            result = 1
    print(f'#{tc} {result}')