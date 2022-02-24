# [SWEA] 1223. [S/W 문제해결 기본] 6일차 - 계산기2 [D4]

## 📚 문제

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14nnAaAFACFAYD&categoryId=AV14nnAaAFACFAYD&categoryType=CODE&problemTitle=1223&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

---

입력받은 문자열을 후위 표기식으로 표현한 후 연산하는 문제이다.

`+, *` 연산자와 숫자만 존재한다.

`+`의 우선순위가 `*`의 우선순위보다 낮다.

위처럼 간단한 연산자를 후위 표기식으로 표현할 때에는 연산자를 stack에 담는다.

> 1. 숫자는 후위 표기식의 리스트에 담는다.
> 2. 연산자는 stack에 우선순위가 자기랑 같거나 더 높은 것들을 다 pop하고난 후 우선 순위가 더 낮은 연산자를 만나면 push한다. `+`연산자는 stack에 있는 모든 연산자를 꺼내고 stack에 push하고, `*`연산자는 stack에 있는 `*`연산자를 모두 꺼내고 stack에 push한다.
> 3. 모든 문자열을 다 꺼냈으면 stack에서 꺼내 차례대로 후위 표기식에 append한다.

후위 표기식이 끝났으면 연산한다.

>1. 숫자가 나오는 경우는 stack에 담는다.
>2. 연산자가 나오는 경우에는 stack에 있는 숫자를 2개 꺼내어 연산한다.
>3. 최종적으로 마지막에 남은 수를 출력한다.

## 📒 코드

```python
for tc in range(1, 11):
    N = int(input())
    arr = list(input())
    stack = []
    temp = []   # 후위 표기식으로 나타낸 걸 담을 리스트
    for v in arr:   # 후위 표기식을 나타내기
        if v.isdigit():
            temp.append(v)
        elif v == '*':
            while stack and stack[-1] == '*':
                temp.append(stack.pop())
            stack.append(v)
        elif v == '+':
            while stack:
                temp.append(stack.pop())
            stack.append(v)
    while stack:
        temp.append(stack.pop())
    
    for v in temp:  # 후위 표기식을 연산하기
        if v in '+*':  # 연산자인 경우
            b = stack.pop()  # b와 a의 순서에 유의, 나중에 넣은 값이 연산할 때 뒤로 가게
            a = stack.pop()
            if v == '+':
                stack.append(a + b)
            else:
                stack.append(a * b)
        else:  # 숫자인 경우 stack에 담는다.
            stack.append(int(v))

    print(f'#{tc} {stack.pop()}')   # 마지막에 하나 남은 수 출력
```

## 🔍 결과 : Pass