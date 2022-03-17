def recur(v):   # 후위 순회를 이용해 계산
    if arr[int(v)][0] not in '+-*/':    # 연산자가 아닌 경우
        return int(arr[int(v)][0])
    else:                               # 연산자인 경우
        a = recur(arr[int(v)][1])
        b = recur(arr[int(v)][2])

        if arr[int(v)][0] == '+':
            return a + b
        elif arr[int(v)][0] == '-':
            return a - b
        elif arr[int(v)][0] == '*':
            return a * b
        elif arr[int(v)][0] == '/':
            return a / b


for tc in range(1, 11):
    n = int(input())    # 정점의 수
    arr = [[0, 0, 0] for _ in range(n + 1)]     # 정점의 value, 자식 노드들
    temp = [input().split() for _ in range(n)]

    for i in range(n):
        if len(temp[i]) == 2:   # 리프 노드일 때, 숫자인 경우
            p, v = temp[i]
            arr[int(p)][0] = v
        else:                   # 연산자인 경우
            p, v, c1, c2 = temp[i]
            arr[int(p)] = [v, c1, c2]

    print(f'#{tc} {int(recur(1))}')     # 정수형으로 변환하여 출력