# [Baekjoon] 2698. 인접한 비트의 개수 [G4]

## 📚 문제 : [인접한 비트의 개수](https://www.acmicpc.net/problem/2698)

## 📖 풀이

dp문제이다. dp 테이블을 3차원으로 두고 탑다운으로 해결한다.

dp 테이블의 각 행은 비트의 개수, 각 열은 인접한 비트의 개수이다.

끝이 0, 1인 경우 두 가지로 값을 담아준다. 즉 3차원으로 dp테이블에 담는다.

1. 끝이 0으로 끝나는 경우

   > `dp[x, y, 0] = dp[x-1, y, 0] + dp[x-1, y, 1]`

   길이가 1 작고 인접한 비트의 개수가 같고 0이나 1로 끝나는 경우의 수를 합친다.

2. 끝이 1로 끝나는 경우

   > `dp[x, y, 1] = dp[x-1, y, 0] + dp[x-1, y - 1, 1]`

   길이가 1 작고 인접한 비트의 개수가 같으며 0으로 끝나는 경우의 수에 길이가 1 작고 인접한 비트의 개수가 1로 끝나는 경우의 수를 합친다.

   이 경우에는 1로 끝나는 경우 뒤에 1을 붙이면 인접합 비트의 개수가 1 증가한다.

위와 같은 점화식을 이용해서 탑다운 방식으로 해결한다.

점화식의 기저조건을 적어주고, 예외 값을 처리해준다.

- 길이가 0이면 0을 return 한다.
- 인접한 비트의 개수가 0보다 작아지면 0을 return 한다.
- 인접한 비트의 개수가 수의 길이보다 크면 나올 수 없으므로 0을 return 한다.

## 📒 코드

```python
def recur(cur, cnt, prv):
    if cur == 0 or cnt < 0 or cur <= cnt:
        return 0
    if dp[cur][cnt][prv] != -1:
        return dp[cur][cnt][prv]
    if prv == 1:
        ret = recur(cur - 1, cnt, 0) + recur(cur - 1, cnt - 1, 1)
    else:
        ret = recur(cur - 1, cnt, 0) + recur(cur - 1, cnt, 1)
    dp[cur][cnt][prv] = ret
    return ret

t = int(input())
dp = [[[-1, -1] for _ in range(101)] for _ in range(101)]

dp[1][0][1] = 1
dp[1][0][0] = 1

for _ in range(t):
    n, k = map(int, input().split())
    print(recur(n, k, 0) + recur(n, k, 1))
```

## 🔍 결과

![image-20220514215408654](README.assets/image-20220514215408654.png)
