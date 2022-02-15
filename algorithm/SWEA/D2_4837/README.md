# [SWEA] 4839. [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합 [D3]

## 📚 문제

https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

---

**부분 집합**을 구하기 위해 `<<` **비트 연산자**를 활용한다. (1 << n) == 2<sup>n</sup> 을 활용하여 문제를 풀어준다.

그리고` i & (1 << j)` 이진법의 각각의 자리 수에 1이 있는지 확인하여 부분집합의 값을 넣어준다.

부분 집합의 출현을 2진법으로 인코딩하여 기계가 이해하기 쉽게 바꾸고 계산하기 쉽게 바꾼다고 생각하면 쉽다.

2<sup>n</sup>으로 하나씩 표현하는 게 인코딩이고 `i & (1 << j)`로 하나씩 부분 집합의 인수와 연결시켜 추상화 시키는 것이 디코딩이다.

## 📒 코드

```python
T = int(input())
A = list(range(1, 13))    # A: [1,2,...,12]
for tc in range(1, T+1):
    N, K = map(int, input().split())    # N:부분집합 원소의 수, K:부분 집합의 합
    result_sum = 0 # 만족시키는 부분집합 개수
    for i in range(1 << 12): # 모든 부분집합 탐색
        cnt = 0
        sum_num = 0
        for j in range(12):
            if i & (1 << j):
                sum_num += A[j]
                cnt += 1
        if cnt == N and sum_num == K:
            result_sum += 1 # 만족시키는 경우 + 1

    print(f'#{tc} {result_sum}')
```

## 🔍 결과 : Pass

부분집합을 재귀나 중첩 for문으로 나타내는 것보다 훨씬 빠르고 간단하니 비트 연산자를 활용하여 해결하는 걸 알아두자!