# Forth
import sys
sys.stdin = open("sample_input.txt")
T = int(input())
for tc in range(1, T + 1):
    arr = list(input().split())
    oper = '+-/*'   # 연산자들
    stack = []      # 숫자를 담을 stack
    for v in arr:   # 입력을 앞에서부터 하나씩 탐색
        if v == '.':
            if len(stack) == 1:     # .을 출력했는데 연산자가 2개이상 존재하면 안된다.
                print(f'#{tc} {stack.pop()}')
            else: print(f'#{tc} error')
            break
        elif v in oper:         # 연산자인 경우
            if len(stack) < 2:  # stack에 숫자가 2개 이상 들어있어야 한다.
                print(f'#{tc} error')
                break
            b = stack.pop()     # b와 a의 순서에 유의, 나중에 넣은 값이 연산할 때 뒤로 가게
            a = stack.pop()
            if v == '+':
                stack.append(a+b)
            elif v == '-':
                stack.append(a-b)
            elif v == '*':
                stack.append(a*b)
            else:
                stack.append(a//b)
        else:                   # 숫자인 경우 stack에 담는다.
            stack.append(int(v))
