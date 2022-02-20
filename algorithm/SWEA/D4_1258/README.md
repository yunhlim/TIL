# [SWEA] 1258. [S/W 문제해결 응용] 7일차 - 행렬찾기 [D4]

## 📚 문제

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18LoAqItcCFAZN

---

0이 아닌 수를 찾으면 가로와 세로로 델타 탐색을 통해 어디까지 0이 아닌 수가 있는지 확인한다. 그리고 전부 0으로 바꿔 다시 탐색한 박스는 다시 탐색하지 않도록 한다.

함수를 통해 구현하여 행, 열, 크기를 반환값으로 반환한다.

tuple의 크기와 행으로 오름차순 정렬해야 하므로 `result.sort(key = lambda x: (x[2], x[1])) ` 도 사용할 수 있지만 버블정렬을 이용해 직접 구현해보았다.

## 📒 코드

```python
T = int(input())

def search(y, x, arr):
    ny, nx = y + 1, x + 1
    while arr[ny][x]:   # 행의 개수
        ny += 1
    while arr[y][nx]:   # 열의 개수
        nx += 1
    for i in range(y, ny):  # 확인했으니 행렬을 다 0으로 변경
        for j in range(x, nx):
                arr[i][j] = 0
    return ny - y, nx - x, (ny - y) * (nx - x)  # 행, 열, 크기

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N+1)] # 패딩으로 인덱스를 넘을 때 오류안나게
    result = []

    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                result.append(search(i, j, arr))

    #result.sort(key = lambda x: (x[2], x[1]))  
    for i in range(len(result)-1):  # 버블 정렬로 sort 구현, 크기 -> 행의 길이 순으로 정렬
        for j in range(len(result)-i-1):
            if result[j][2] > result[j+1][2]:
                result[j], result[j+1] = result[j+1], result[j]
            elif result[j][2] == result[j+1][2]:
                if result[j][0] > result[j+1][0]:
                    result[j], result[j+1] = result[j+1], result[j]
    

    print(f'#{tc} {len(result)}', end=' ')
    for i in range(len(result)):    # 행렬의 크기를 제외한 행과 열만 출력
        print(result[i][0], result[i][1], end=' ')
    print()
```

## 🔍 결과 : Pass



