# [SWEA] 4874. [파이썬 S/W 문제해결 기본] 5일차 - Forth [D2]

## 📚 문제

> Forth라는 컴퓨터 언어는 스택 연산을 기반으로 하고 있어 후위 표기법을 사용한다. 예를 들어 3+4는 다음과 같이 표기한다.
>  
>
> 3 4 + .
>  
>
> Forth에서는 동작은 다음과 같다.
>  
>
> 숫자는 스택에 넣는다.
>
> 연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.
>
> ‘.’은 스택에서 숫자를 꺼내 출력한다.
>
>  
>
> Forth 코드의 연산 결과를 출력하는 프로그램을 만드시오. 만약 형식이 잘못되어 연산이 불가능한 경우 ‘error’를 출력한다.

후위 표기법으로 이루어져 있는 문자열을 입력으로 받아 연산결과를 출력하는 문제이다.

1. `.`이 나오면 하나를 출력하는데, 이 때 stack에 값이 2개 이상 있으면 error를 출력한다.
2. `+-/*` 연산자가 나오면 stack에서 두개를 꺼내 연산하여 다시 stack에 push한다. 값이 없거나 하나 있으면 error를 출력한다.
3. 숫자가 나오면 int로 형변환 후 stack에 push한다.

## 📒 코드

```python
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
```

## 🔍 결과 : Pass