# [SWEA]  4836. [파이썬 S/W 문제해결 기본] 2일차 - 색칠하기 [D2]

## 📚 문제

https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

---

색칠하는데 중첩해서 색칠되지가 않는다. 따라서 영역을 탐색하고 색칠되어있지 않으면 색칠하고, 색칠되어있으면 보라색으로 색칠하는 것이니 1을 더해준다.

## 📒 코드

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 칠할 영역의 개수
    arr = [[0]*10 for _ in range(10)]   # 10X10 배경
    purple = 0
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split()) # r1,c1, r2,c2 인덱스와 color
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if arr[i][j] == 0:   # 판에 안 칠해져있으면 0이니 color로 칠한다.
                    arr[i][j] = color
                else:   # 칠해져 있는 판에 덧칠하면 보라색으로 바뀐다.
                    purple += 1
    print(f'#{tc} {purple}')
```

---

똑같은 색을 덧칠할 수 있다고 생각하고 코드를 풀어본다.

그러면 판에 안 칠해져있으면 color(1, 2)로 칠하고, 다른 컬러가 칠해진 경우만 보라색으로 바꾼다(3으로 적어준다).

그리고 다 색칠한 이후에 보라색인 3의 색을 2차원 배열에서 세서 출력한다.

## 📒 코드

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 칠할 영역의 개수
    arr = [[0]*10 for _ in range(10)]   # 10X10 배경
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split()) # r1,c1, r2,c2 인덱스와 color
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if arr[i][j] == 0:   # 판에 안 칠해져있으면 0이니 color로 칠한다.
                    arr[i][j] = color
                elif arr[i][j] != color:    # 서로 다른 색이면 3으로 바꾼다, 3이어도 3으로 바꾸니 상관없다.
                    arr[i][j] = 3   # 보라색은 3으로 바꾼다.
    purple = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                purple += 1
    print(f'#{tc} {purple}')
```

## 🔍 결과 : PASS