# [SWEA] 2805. 농작물 수확하기 [D3]

## 📚 문제

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GLXqKAWYDFAXB

---

|      |      |  o   |      |      |
| :--: | :--: | :--: | :--: | :--: |
|      |  o   |  o   |  o   |      |
|  o   |  o   |  o   |  o   |  o   |
|      |  o   |  o   |  o   |      |
|      |      |  o   |      |      |

위의 표처럼 인덱스를 선택하게끔 범위를 설정해야 한다.

가운데에서 멀어지는 모양으로 선택하면 되니 절대값을 사용한다.

행의 범위는 0~N-1로 설정하고, 열의 범위는 abs(i - N//2) ~ N - abs(i - N//2) - 1로 설정한다.

## 📒 코드

```python
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    coin = 0
    for i in range(N):
        for j in range(abs(i - N//2), N - abs(i - N//2)):
            coin += arr[i][j]
    print(f'#{tc} {coin}')
```

## 🔍 결과 : Pass