# [SWEA] 1226. 미로1 [D4]

## 📚 문제

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14vXUqAGMCFAYD&categoryId=AV14vXUqAGMCFAYD&categoryType=CODE&problemTitle=%EB%AF%B8%EB%A1%9C1&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

---

미로의 시작점은 2, 도착점은 3이다.

갈 수 있는지 판단해야하니 **델타 탐색 + DFS 문제**이다.

현재 위치를 stack에 담는다.

stack에서 하나씩 꺼내어 네 방향으로 확인 후 3(도착점)이 있으면 1(도착)을 리턴하고, 길이 있으면 스택에 담는다.

지나간 길을 확인하지 않기 위해 stack에서 값을 꺼내면 입력을 벽인 1로 바꾸어준다.

stack에 값이 없는데 3에 도달하지 못했으면 0(도착하지 못함)을 리턴한다.

## 📒 문제

```python
def miro():     # 미로 결과 가능 여부 판별
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:  # 시작점 확인
                s = (i, j)
    stack = [s]

    while stack:
        v = stack.pop()
        y, x = v[0], v[1]
        arr[y][x] = 1   # 가지치기를 위해 현재 위치를 벽으로 만든다.
        for i in range(4):      # 네 방향으로 확인
            ny = y + dy[i]
            nx = x + dx[i]
            if arr[ny][nx] == 0:    # 길인지 확인하고 길이면 stack에 담는다.
                stack.append((ny, nx))
            elif arr[ny][nx] == 3:  # 도착점에 도달하는지 확인
                return 1
    return 0        # 도달하지 않는 경우


for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    dy = [0, 1, 0, -1]  # 우 하 좌 상
    dx = [1, 0, -1, 0]
    
    print(f'#{tc} {miro()}')
```

## 🔍 결과 : Pass