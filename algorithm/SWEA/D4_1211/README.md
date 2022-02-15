# [SWEA] 1211. [S/W 문제해결 기본] 2일차 - Ladder2 [D4]

## 📚 문제

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14BgD6AEECFAYh&categoryId=AV14BgD6AEECFAYh&categoryType=CODE&problemTitle=ladder&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

---

사다리타기를 수행할 때 **최단 거리**를 구하는 문제이다.

어차피 세로방향으로는 사다리타기 판의 세로 높이인 100만큼 똑같이 움직이니 **가로방향**으로 얼만큼 움직인지 판단하고 가장 적을 때의 시작점 인덱스를 찾아준다.

먼저 모든 시작점 인덱스를 찾아 리스트에 넣고 순회하며 하나씩 사다리 타기를 수행해준다.

가로로 움직이는 횟수를 파악하기 위해 변수를 0으로 초기화 하여 가로방향으로 움직일 때마다 1씩 더한다.

사다리 타기를 끝내면 가장 작은 횟수일 때로 업데이트 해 가장 적은 회수의 시작점을 출력한다.

## 📒 코드

```python
T = 10

for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    X_lst = []  # 시작점 배열
    min_row_move = 10000    # 가로방향으로 움직이는 횟수를 센다
    min_X = 0   # 최단 경로 X
    for i in range(100):    # 아래 2를 찾고 거기서부터 올라간다!
        if ladder[0][i] == 1:
            X_lst.append(i)

    for X in X_lst:
        dir = (1, 0)  # 처음에는 내려간다.  # 아래쪽 di = 1, dj = 0
        current = (0, X)   # 시작 인덱스
        cnt_row_move = 0 # 가로방향으로 움직이는 횟수
        while current[0] != 99:  # 맨 아래로 내려가면 끝(0번째 인덱스)
            ni, nj = current
            if dir != (1, 0):   # 움직이던 방향이 가로 방향인 경우
                if not(0 <= nj+dir[1] < 100 and ladder[ni][nj+dir[1]]): # 가던 방향으로 움직일 수 있는지 판단
                    dir = (1, 0)   # 못가면 아래로  # 아래쪽 di = 1, dj = 0
            else:           # 움직이던 방향이 아래 방향인 경우
                if 0 <= nj-1 < 100 and ladder[ni][nj-1]:    # 왼쪽으로 움직일 수 있는지 판단
                    dir = (0, -1)   # 왼쪽 di = 0, dj = -1
                if 0 <= nj+1 < 100 and ladder[ni][nj+1]:    # 오른쪽으로 움직일 수 있는지 판단
                    dir = (0, 1)    # 오른쪽 di = 0, dj = 1

            if dir != (1, 0):
                cnt_row_move += 1
            current = (ni+dir[0], nj+dir[1])    # 이동시킨다.

        if min_row_move >= cnt_row_move:    # 가로로 제일 조금 움직이는지 확인
            min_X = X
            min_row_move = cnt_row_move

    print(f'#{tc} {min_X}')
```

## 🔍 결과 : Pass