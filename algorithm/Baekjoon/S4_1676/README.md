# [Baekjoon] 1676. 팩토리얼 0의 개수 [S4]

## 📚 문제 : [팩토리얼 0의 개수](https://www.acmicpc.net/problem/1676)

## 📖 풀이

2의 배수의 개수는 항상 5의 배수의 개수보다 많으니 5의 배수의 개수만 구하면 된다.

25의 배수는 5가 2번 들어간다. 그리고 125의 배수는 5가 3번 들어간다.

n이 500이니 5의 3제곱인 125의 배수까지만 생각하면 된다.

5의 배수의 개수 + 25의 배수의 개수 + 125의 배수의 개수가 답이다.

## 📒 코드

```python
n = int(input())
print(n // 5 + n // (5 * 5) + n // (5 * 5 * 5))
```

## 🔍 결과

![image-20220516121813750](README.assets/image-20220516121813750.png)