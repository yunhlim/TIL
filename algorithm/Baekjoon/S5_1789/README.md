# [Baekjoon] 1789. 수들의 합 [S5]

## 📚 문제 : [수들의 합](https://www.acmicpc.net/problem/1789)

## 📖 풀이

1부터 1씩 증가하는 자연수들의 합을 구한다. 

합을 구하면서 더해주는 수들의 개수도 증가시킨다.

그 때 우리가 원하는 수보다 커지면 더해주던 수의 개수를 1 감소시키고 개수를 출력한다.

정확히 같아지면 그 때의 수를 출력한다.

## 📒 코드

```python
n = int(input())

cnt = 0
result = 0
for i in range(1, n + 1):
    cnt += 1
    result += i
    if result == n:
        break
    elif result > n:
        cnt -= 1
        break
print(cnt)
```

## 🔍 결과

![image-20220729012113668](README.assets/image-20220729012113668.png)