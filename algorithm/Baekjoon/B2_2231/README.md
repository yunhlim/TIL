# [Baekjoon] 2231. 분해합 [B2]

## 📚 문제 : [분해합](https://www.acmicpc.net/problem/2231)

## 📖 풀이

1일 때부터 분해합을 구해 해당되는 값의 분해합이 n일 때를 찾는다.

생성자가 분해합보다 큰 경우는 없으니 최대 n일 때까지 봐도 충분하다.

n일 때까지 분해합을 찾을 수 없었다면 0을 출력한다.

## 📒 코드

```python
n = int(input())

for i in range(1, n + 1):
    total = i
    for c in str(i):
        total += int(c)
    
    if total == n:
        print(i)
        break
else:
    print(0)
```

## 🔍 결과

![image-20220729015002847](README.assets/image-20220729015002847.png)
