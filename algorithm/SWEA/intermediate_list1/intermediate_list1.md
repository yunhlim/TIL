# [SWEA] 파이썬 SW문제해결 기본 - List 1

## 4828. [파이썬 S/W 문제해결 기본] 1일차 - min max [D2]

### 📚 문제 

https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

---

max와 min 값을 주어진 수의 첫번째 수로 초기화 시키고 for문에 넣어 if elif로 처리한다.

### 📒 코드

```python
T = int(input()) 

for tc in range(1, T+1):
    N = int(input())    # 양수의 개수
    num_lst = list(map(int, input().split()))
    max_num = num_lst[0]
    min_num = num_lst[0]

    for i in range(N):
        if max_num < num_lst[i]:
            max_num = num_lst[i]
        elif min_num > num_lst[i]:    # 이미 최댓값이면 최솟값인지 확인 안해도되니 elif로 
            min_num = num_lst[i]
    print(f'#{tc} {max_num - min_num}')
```

### 🔍 결과: **Pass**

---

---

## 4831. [파이썬 S/W 문제해결 기본] 1일차 - 전기버스 [D3]

### 📚 문제

https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

---

정류장을 0이 담긴 리스트로 초기화하고 충전기가 있는 index에 1을 추가한다.

현재 정류장에서 움직일 수 있는 구간에서 가장 멀리 있는 충전기로 이동하는 걸 반복한다.

가장 멀리 있는 충전기로 이동할 때 cnt를 증가시켜 종점에 닿았을 때 cnt를 출력한다.

이동할 충전기가 없으면 0을 출력한다.

### 📒 코드

```python
T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    M_lst = list(map(int, input().split())) # 충전기 설치된 정류장
    station = [0 for _ in range(N+1)]   # 정류장 0으로 초기화

    for num in M_lst:   # 충전기가 설치되면 정류장을 1로 변경
        station[num] = 1

    now = 0 # 현재 위치
    cnt = 0 # 충전 횟수
    while now + K < N:  # 현재 충전없이 종점에 도착할 수 있는 위치에 있는지 확인
        move = 0 # 충전기 설치 구간이 있는지 확인
        for location in range(now + 1, now + K + 1):    # 최대 이동 구간
            # 최대한 멀리 있는 충전기로 이동
            if station[location] == 1:
                now = location  # 충전기로 이동
                move = 1    # 충전기 설치 구간으로 움직임 표시
        if move == 0: # 충전기 설치 구간으로 움직이지 못하는 경우
            cnt = 0 # 종점에 도착하지 못하니 0으로 출력
            break
        else: cnt += 1  # 충전했으니 cnt 증가
    print(f'#{tc} {cnt}')
```

### 🔍 결과 : **Pass**

---

---

## 4834. [파이썬 S/W 문제해결 기본] 1일차 - 숫자 카드 [D2]

### 📚 문제

https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

---

count 배열을 만들어 0으로 초기화한다.  0 ~ 9 까지의 index 중 나오는 카드마다 1을 올려준다.

### 📒 코드

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 카드 수
    card_lst = list(map(int, input()))
    count = [0 for _ in range(10)]

    many_card_num = 0   # 가장 많은 카드에 적힌 숫자
    many_card_cnt = 0   # 위 숫자가 적힌 카드의 개수
    for i in card_lst:
        count[i] += 1

    for i in range(10):
        # 같을 때에 index는 나중에 나온 걸로 선택하라고 했으니 <=로 써준다.
        if many_card_cnt <= count[i]:         
            many_card_num = i
            many_card_cnt = count[i]

    print(f'#{tc} {many_card_num} {many_card_cnt}')
```

### 🔍 결과: **Pass**

---

---

## 4835. [파이썬 S/W 문제해결 기본] 1일차 - 구간합 [D2]

### 📚 문제

https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

---

M개를 먼저 앞에서부터 더한다. queue를 응용해 앞에 하나씩 더하고 뒤를 하나씩 빼준다. 

이렇게 해주기 위해서 처음에 M개만큼 더해 그걸 최대 최소로 설정한다.

그리고 for문을 돌며 하나 더하고 하나 빼주는 걸 반복하며 max와 min을 바꾸어준다.

### 📒 코드

```python
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())    # N: 정수의 개수, M: 구간의 개수
    num_lst = list(map(int, input().split()))   # 정수 리스트
    num_sum = 0
    for i in range(M):  # 처음 M개의 합을 구한다
        num_sum += i
    min_sum = num_sum   # 합의 최소, 처음 M개의 합으로 초기화
    max_sum = num_sum   # 합의 최대, 처음 M개의 합으로 초기화

    for i in range(1, N-M+1):   # N개 안에서 M개의 배열을 이동시킬 수 있는 경우의 수

        # 이전 M개의 합에서 오른쪽 하나를 더하고 왼쪽 하나를 뺀다.
        num_sum = num_sum - num_lst[i-1] + num_lst[i+M-1]

        if num_sum < min_sum:
            min_sum = num_sum
        elif num_sum > max_sum:
            max_sum = num_sum

    print(f'#{tc} {max_sum - min_sum}')
```

### 🔍 결과: **Pass**