# [SWEA] 1224. [S/W 문제해결 기본] 6일차 - 계산기3 [D4]

## 📚 문제

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14tDX6AFgCFAYD&categoryId=AV14tDX6AFgCFAYD&categoryType=CODE&problemTitle=1224&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&

---

계산기2 문제와 다르게 ()가 포함된 문제이다.

후위 표기식으로 표현할 때 달라진다.

`(`를 만나면 무조건 stack에 push한다.

stack 맨 위에 `(`가 있으면 연산자들은 그 위로 쌓는다.

`)`를 만나면 `(`를 만날 때까지 stack에서 꺼내어 후위표기식에  넣는다.

나머지 연산자들의 관계는 동일하다.

## 📒 코드

```python
for tc in range(1, 11):
    N = int(input())
    arr = list(input())
    stack = []
    temp = []  # 후위 표기식으로 나타낸 걸 담을 리스트
    for v in arr:  # 후위 표기식을 나타내기
        if v.isdigit():
            temp.append(v)
        elif v == '*':
            while stack and stack[-1] == '*':
                temp.append(stack.pop())
            stack.append(v)
        elif v == '+':
            while stack and stack[-1] in '+*':
                temp.append(stack.pop())
            stack.append(v)
        elif v == '(':
            stack.append(v)
        elif v == ')':
            while stack[-1] != '(':
                temp.append(stack.pop())
            stack.pop()
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

    print(f'#{tc} {stack.pop()}')  # 마지막에 하나 남은 수 출력
```

## 🔍 결과 : Pass