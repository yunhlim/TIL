# [SWEA] 1210. [S/W 문제해결 기본] 2일차 - Ladder1 [D4]

## 📚 문제

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14ABYKADACFAYh&categoryId=AV14ABYKADACFAYh&categoryType=CODE&problemTitle=ladder&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

---

사다리 타기 중 2로 적혀있는 도착점으로 갈 수 있는 시작점의 인덱스를 찾는 문제이다.

시작점에서 여러번 출발하기 보다는 도착점에서 역으로 올라가는 방법이 빠르다.

맨 아래에 2를 찾아 거기서 출발을 한다. 목적지인 맨 위에 도착하면 break로 반복문을 탈출한다.

>1. 위쪽으로 움직인 경우 그 다음에 왼쪽이나 오른쪽을 먼저 탐색해 움직일 수 있으면 움직인다.
>2. 왼쪽이나 오른쪽으로 움직인 경우, 전에 움직였던 곳 말고 움직이던 방향으로 먼저 확인하고 움직일 수 없으면 위로 올라간다.
>3. 이를 반복한다.

## 📒 코드

```python
T = 10

for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    dir = (-1, 0)    # 처음에는 올라간다.

    for i in range(100):    # 아래 2를 찾고 거기서부터 올라간다!
        if ladder[99][i] == 2:
            X = i
            break
    current = (98, X)   # 99번째 줄에서 시작
    while current[0] != 0:  # 맨 위로 올라오면 끝(0번째 인덱스)
        ni, nj = current
        if dir != (-1, 0):   # 움직이던 방향이 가로 방향인 경우
            if not(0 <= nj+dir[1] < 100 and ladder[ni][nj+dir[1]]): # 가던 방향으로 움직일 수 있는지 판단
                dir = (-1, 0)     # 못가면 위로, 위쪽 di = -1, dj = 0 
        else:           # 움직이던 방향이 위 방향인 경우
            if 0 <= nj-1 < 100 and ladder[ni][nj-1]:    # 왼쪽으로 움직일 수 있는지 판단
                dir = (0, -1)  # 왼쪽 di = 0, dj = -1
            if 0 <= nj+1 < 100 and ladder[ni][nj+1]:    # 오른쪽으로 움직일 수 있는지 판단
                dir = (0, 1)  # 오른쪽 di = 0, dj = 1
        current = (ni+dir[0], nj+dir[1])    # 이동시킨다.
    print(f'#{tc} {current[1]}')
```

## 🔍 결과 : Pass

---

좀 더 깔끔하게 풀어본다.

가로 방향으로 움직이는지 판단하는데 움직이는 방향을 기억하기보다는 가로 방향으로 움직였을 때 그 전 위치를 지워버린다.

## 📒 더 개선한 코드

```python
for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    y = 99
    for i in range(100):    # 아래 2를 찾고 거기서부터 올라간다!
        if ladder[y][i] == 2:
            x = i
            break
    
    dx = [-1, 1] # 좌우만 검색

    while y > 0:    
        for i in range(2):
            nx = x + dx[i]
            if 0 <= nx < 100 and ladder[y][nx]:
                ladder[y][x] = 0    # 행으로 움직이면 그 전 위치를 0으로 지워버리면 쉽다.
                x = nx
                break
        else:
            y -= 1
    print(f'#{tc} {x}')
```

## 🔍 결과 : Pass