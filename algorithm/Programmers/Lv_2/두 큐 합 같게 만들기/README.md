# [Programmers] 두 큐 합 같게 만들기 [Lv 2]

## 📚 문제 : [두 큐 합 같게 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/118667)

## 📖 풀이

두 큐가 입력으로 주어진다. 시간초과가 발생하지 않게 큐를 활용하기 위해 **deque**를 import해서 사용한다.

작업은 2가지가 있다.

- 첫번째 작업 : 첫번째 큐에서 popleft()한 후 두번째 큐에 append()

- 두번쨰 작업 : 두번째 큐에서 popleft()한 후 첫번째 큐에 append()

먼저 총 원소의 합을 구한다.

첫번째 큐의 합이 총 원소의 합보다 크면 위에 적은 첫번째 작업을 시행하고 작으면 두번째 작업을 시행한다.

deque의 popleft와 append의 시간복잡도는 O(1)이니 사용해도 상관없다. 그리고 그 때의 합을 매번 구하는 작업이 O(n)이니 처음에 각각의 합을 구하고 거기에서 append하면 더해주고, popleft를 하면 빼준다.

같은 값이 나오면 그 때 작업 횟수를 출력하면 된다.

### 만들 수 없는 경우

만들 수 없는 경우는 두 큐의 모든 원소를 조회하는 경우이다.

따라서 각 큐를 바꿔준 횟수를 트래킹해도 되는데, 나는 큐의 길이의 3배만큼을 확인했는데 나오지 않으면 이미 두 큐를 확인했다고 짐작이 되어 큐 하나의 길이의 3배보다 더 많이 작업한 경우는 -1를 리턴하게 하여 마무리했다.

## 📒 코드

```python
def solution(queue1, queue2):
    from collections import deque
    que_1 = deque(queue1)       # 덱으로 변경(큐의 시간복잡도를 줄이기 위해)
    que_2 = deque(queue2)
    length = len(que_1)         # 큐 하나의 길이
    sum_1 = sum(que_1)          # 큐 1의 합
    sum_2 = sum(que_2)          # 큐 2의 합
    half = (sum_1 + sum_2) // 2         # 모든 원소의 합의 절반

    cnt = 0                     # 작업 횟수 초기화
    while sum_1 != half:
        cnt += 1                # 작업 횟수 + 1
        if cnt > length * 3:
            return -1
        if sum_1 < half:        # 큐 1의 합이 더 클 때
            x = que_2.popleft()
            que_1.append(x)
            sum_1 += x
            sum_2 -= x
        else:                   # 큐 2의 합이 더 클 때
            x = que_1.popleft()
            que_2.append(x)
            sum_2 += x
            sum_1 -= x
    
    return cnt
```

