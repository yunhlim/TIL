# [Baekjoon] 9375. 패션왕 신해빈 [S3]

## 📚 문제 : [패션왕 신해빈](https://www.acmicpc.net/problem/9375)

## 📖 풀이

조합 문제이다. 

딕셔너리로 의상 종류의 개수를 담는다.

예를 들어 바지 3개, 상의 2개이면, 조합에 의해 (3 + 1) * (2 + 1) - 1 = 11이 답이 된다.

1씩 더하는 이유는 그 옷의 종류를 입지 않는 경우를 더하는 것이고 -1을 하는 건 아무 것도 입지 않은 경우를 빼기 위해서이다.

따라서 딕셔너리로 의상 종류의 개수만 담고, 각각 1을 더해 곱해주고 마지막에 1만 빼주면 답이 된다.

아무 의상도 고르지 않는 경우도 0이 출력되므로 엣지케이스는 따로 처리할 필요는 없다.

## 📒 코드

```python
t = int(input())
for _ in range(t):
    n = int(input())
    wear = {}
    for _ in range(n):
        name, kind = input().split()
        wear[kind] = wear.get(kind, 0) + 1

    result = 1
    for cnt in wear.values():
        result *= (cnt + 1)
    
    result -= 1
    print(result)
```

## 🔍 결과

![image-20220731230457105](README.assets/image-20220731230457105.png)