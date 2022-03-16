# [SWEA] 1238. [S/W 문제해결 기본] 10일차 - Contact [D4]

## 📚 문제

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15B1cKAKwCFAYD

---

그래프, BFS 문제

먼저 그래프는 방향이 있는 그래프로 배열의 인덱스가 가리키는 정점에서 향하는 정점들을 모두 담는다.

이 때 중복으로 값이 들어올 수 있으니 **set** 연산자를 활용해서 값을 받아준다. 

연락받게 되는 사람 중 번호가 가장 큰 사람을 구하는 줄 알고 한참 헤맸다.😢😢😢

가장 나중에 연락을 받은 사람 중 번호가 가장 큰 사람을 구하는 문제이다.

따라서 BFS를 이용하는데 visited에 들리는 순서를 적어줘야한다. 큐에서 값을 꺼내 연결되어 있는 정점들 중 확인하지 않는 정점들을 꺼낸 정점의 순서에 +1을 하여 visited에 표시하고 큐에 담아준다.

위 과정을 반복 후 나온 visited 리스트의 값이 큰 수를 뽑는데 중복된 경우 뒤에 나온 리스트 인덱스 값을 출력한다.

## 📒 코드

```python
from collections import deque


for tc in range(1, 11):
    n, s = map(int, input().split())
    arr = [set() for _ in range(101)]   # 번호 : 1~100, 연결상태 표시, 중복된 값이 들어오니 set로 없애준다.
    visited = [0 for _ in range(101)]   # 연락 순서로 적어준다. 연락이 없으면 0

    temp = list(map(int, input().split()))
    for i in range(n // 2):     # 방향성이 있는 그래프
        arr[temp[i * 2]].add(temp[i * 2 + 1])
    queue = deque()
    queue.append(s)
    visited[s] = 1
    while queue:        # 연락이 끝날 때까지 시행
        v = queue.popleft()
        for v2 in arr[v]:
            if visited[v2] == 0:    # 연결된 정점들 중 아직 등장하지 않는 정점만 고른다.
                visited[v2] = visited[v] + 1    # 연락 순서를 +1 한다.
                queue.append(v2)        # 큐에 담아 다음 연락을 이어간다.
    v_max = 0
    for i in range(101):    # 연락순서가 가장 나중인 visited의 값이 큰 것 중 인덱스가 가장 큰 값을 고른다.
        if visited[i] >= visited[v_max]:
            v_max = i
    print(f'#{tc} {v_max}')
```

## 🔍 결과 : Pass