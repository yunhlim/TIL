# [Baekjoon] 2473. 세 용액 [G4]

## 📚 문제

https://www.acmicpc.net/problem/2473

---

## 📖 풀이

n은 5000개 이하로 주어져 있다. 5000개 중 하나를 고르고, 나머지 2개는 투포인터를 활용하여 구한다.

투포인터를 활용하기 위해 정렬한다.

하나를 고른 후 s는 0 e는 n-1로 둔다.

골랐던 값이 s와 같으면 s를 1 늘리고, e랑 같으면 e를 1 줄인다.

세 수의 합이 0보다 크면 e를 1 줄인다.

세 수의 합이 0보다 작으면 s를 1 늘린다.

세 수의 합이 0이 나오면 바로 그 세 수를 출력하고 종료한다.

## 📒 코드

```python
n = int(input())
arr = sorted(list(map(int, input().split())))
result = abs(arr[0] + arr[1] + arr[2])  # 비교하기 위한 값, 배열 앞에서 3개 선택하여 더한 후 절댓값을 넣는다.
result_arr = [arr[0], arr[1], arr[2]]   # 배열에 세 수를 담아준다.
for i in range(n):  # 하나를 우선 선택한다.
    a = arr[i]  # 하나 선택
    s = 0       # 투포인터
    e = n - 1
    while s < e:    # 같지 않을 때만 봐야 한다.
        if s == i:  # 선택한 값을 중복 선택하지 않기 위함
            s += 1
            continue
        if e == i:
            e -= 1
            continue
        if abs(a + arr[s] + arr[e]) < result:   # 이전에 구한 값보다 작은 경우만
            result = abs(a + arr[s] + arr[e])   # 세 수의 합의 절댓값을 초기화
            result_arr = [a, arr[s], arr[e]]    # 출력해야하니 배열에 담는다.
        if a + arr[s] + arr[e] == 0:
            print(*sorted([a, arr[s], arr[e]])) # 합이 0이면 바로 출력한다.
            exit()
        elif a + arr[s] + arr[e] > 0:           # 합이 0보다 큰 경우 큰 값을 줄인다.
            e -= 1
        else:                                   # 합이 0보다 작으면 작은 값을 키운다.
            s += 1

print(*sorted(result_arr))      # 세 수를 정렬해 작은 수부터 출력한다.
```

## 🔍 결과

![image-20220419145115863](README.assets/image-20220419145115863.png)