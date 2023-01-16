# [Baekjoon] 2577. 숫자의 개수 [B2]

## 📚 문제 : [숫자의 개수](https://www.acmicpc.net/problem/2577)

## 📖 풀이

A, B, C 세 수를 곱한 후 0부터 9까지 숫자가 몇 번 쓰였는지 카운팅 배열을 활용해 구한다.

이 때 숫자의 각 자리 수를 순회하기 위해 문자열로 바꿔 순회한 다음에 다시 정수형으로 바꿔 카운팅 배열의 인덱스 값으로 찾아준다.

## 📒 코드

```python
a = int(input())
b = int(input())
c = int(input())
result = a * b * c
cnt_arr = [0 for _ in range(10)]

for c in str(result):
    cnt_arr[int(c)] += 1

for i in range(10):
    print(cnt_arr[i])
```

## 🔍 결과

![image-20220729024000500](README.assets/image-20220729024000500.png)