# [SWEA] 1954. 달팽이 숫자[D2]

## 📚 문제

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PobmqAPoDFAUq&categoryId=AV5PobmqAPoDFAUq&categoryType=CODE&problemTitle=%EB%8B%AC%ED%8C%BD%EC%9D%B4&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

---

델타를 이용한 2차 배열의 탐색을 활용해 해결했다.

현재 위치에서 이동하며 그 위치에 숫자를 채워준다.

이동을 못했을 때 이동방향을 정해진 규칙대로 바꿔준다.

> 오른쪽으로 이동할 곳이 없으면 아래로 방향 전환
>
> 아래로 이동할 곳이 없으면 왼쪽으로 뱡향 전환
>
> 왼쪽으로 이동할 곳이 없으면 위쪽으로 방향 전환
>
> 위로 이동할 곳이 없으면 오른쪽으로 방향 전환

이동을 못할 때는 정해진 범위를 넘어설 때와 이미 숫자가 채워졌을 때로 기준을 잡는다.

숫자가 채워졌을 때로 하기 위해서 처음에 0으로 초기화하여 해결한다.

## 📒 코드

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)] # N x N 배열
    ni, nj, di, dj = 0, 0, 0, 1   # 현재 위치(0, 0)와 움직이는 방향(우)

    arr[0][0] = 1
    for i in range(2, N * N + 1):
        if dj == 1:
            if nj == N-1 or arr[ni][nj+1] != 0:  # 오른쪽으로 움직일 곳이 없거나 이미 채워진 자리인 경우
                di, dj = 1, 0   # 아래쪽으로 경로 변경
        if dj == -1:
            if nj == 0 or arr[ni][nj-1] != 0:  # 왼쪽으로 움직일 곳이 없거나 이미 채워진 자리인 경우
                di, dj = -1, 0   # 위쪽으로 경로 변경
        if di == 1:
            if ni == N-1 or arr[ni+1][nj] != 0:  # 아래쪽으로 움직일 곳이 없거나 이미 채워진 자리인 경우
                di, dj = 0, -1   # 왼쪽으로 경로 변경
        if di == -1:
            if ni == 0 or arr[ni-1][nj] != 0:  # 위쪽으로 움직일 곳이 없거나 이미 채워진 자리인 경우
                di, dj = 0, 1   # 오른쪽으로 경로 변경
        ni += di
        nj += dj
        arr[ni][nj] = i  # 현재 위치에 정수를 적는다.
    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])
```

## 🔍 결과

![image-20220215011602525](README.assets/image-20220215011602525.png)

D2 난이도라 쉽게 봤지만 생각보다 오래 걸렸다.