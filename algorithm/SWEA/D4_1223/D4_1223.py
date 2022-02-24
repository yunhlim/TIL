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