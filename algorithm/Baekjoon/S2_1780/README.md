# [Baekjoon] 1780. 종이의 개수 [S2]

## 📚 문제 : [종이의 개수](https://www.acmicpc.net/problem/1780)

## 📖 풀이

똑같은 크기로 줄여나가는 거라 재귀를 사용하면 된다.

9개로 자르니 가로는 3 세로는 3으로 나누며 나아간다. 똑같이 나누면서 나가니 분할정복 문제다.

먼저 현재 종이의 시작 부분의 숫자 값을 기억하고, 모든 위치의 값이 같으면 그 숫자의 개수를 1 늘려준다.

다르면 9개로 쪼개며 반복한다.

## 📒 코드

```python
def recur(x, y, size):
    start = arr[x][y]
    same = True
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != start:
                same = False
                break

    if same == True:
        result[start] += 1
    else:
        size //= 3
        for i in range(3):
            for j in range(3):
                recur(x + size * i, y + size * j, size)


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = {-1: 0, 0: 0, 1: 0}
recur(0, 0, n)
print(result[-1])
print(result[0])
print(result[1])

```

## 🔍 결과

![image-20220813003706689](README.assets/image-20220813003706689.png)