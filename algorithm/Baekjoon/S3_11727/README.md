# [Baekjoon] 11727. 2xn 타일링 2 [S3]

## 📚 문제 : [2xn 타일링 2](https://www.acmicpc.net/problem/11727)

## 📖 풀이

DP로 시간을 줄여 해결해야하는 문제이다.

세로로 하나 세워 완성하는 경우와 가로 2개, 2x2 정사각형 하나로 만드는 경우의 수 2개를 활용해서 해결한다.

점화식으로 보면, `dp[cur] = recur(cur - 2) * 2 + recur(cur - 1)` 와 같이 나온다.

## 📒 코드

```python
def recur(cur):
    if cur == 1:
        return 1
    elif cur == 2:
        return 3

    if dp[cur]:
        return dp[cur]
    dp[cur] = recur(cur - 2) * 2 + recur(cur - 1)
    dp[cur] %= 10007
    return dp[cur]


n = int(input())
dp = [0 for _ in range(n + 5)]
print(recur(n))
```

##  🔍 결과

![image-20220530225520323](README.assets/image-20220530225520323.png)