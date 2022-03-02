# [Baekjoon] 2606. 바이러스 [S3]

## 📚 문제

https://www.acmicpc.net/problem/2606

---

1번 컴퓨터에서 연결된 총 컴퓨터의 개수를 구하라는 문제이다. 컴퓨터 수는 100개 이하이다. 그래프 문제로 간선 연결의 방향성이 없다.

큐를 활용한 **BFS**문제로 푼다. 간선들의 방향이 존재하지 않으니 입력받은 걸 정점의 양방향 연결관계로 두 번 넣어주어야 한다.

deque의 자료구조를 활용해 처음에 1을 큐에 넣고 BFS 탐색을 한다. 큐에 값이 있으면 왼쪽부터 하나씩 꺼내 확인한다. 

전염된 컴퓨터가 이미 나온 컴퓨터인지 확인하기 위해 visited 리스트를 만들어서 사용한다. visited에 추가하면서 cnt를 1씩 더해준다. 1 컴퓨터의 개수는 제외하고 걸린 컴퓨터의 수를 출력해야 하니 cnt에서 1을 빼서 출력한다.

## 📒 코드

```python
from collections import deque


n = int(input())    # 컴퓨터 수
e = int(input())    # 간선의 수
arr = [[] for _ in range(n + 1)]   # 정점들의 연결관계

for i in range(e):
    a, b = map(int, input().split())    # 연결된 컴퓨터의 숫자 a, b
    arr[a].append(b)
    arr[b].append(a)    # 방향이 없는 그래프니 반대방향도 넣어준다.

visited = [0] * (n + 1) # 방문 했는지 확인
queue = deque()
queue.append(1)         # 바이러스의 시작점 1을 큐에 담는다.

cnt = 0
while queue:                # 큐에 값이 있으면 반복문을 돈다.
    v = queue.popleft()     # 정점을 하나씩 꺼낸다.
    if visited[v] == 0:     # 정점이 아직 나오지 않았으면 확인
        cnt += 1            # 바이러스가 퍼진 컴퓨터의 개수를 하나 더한다.
        visited[v] = 1      # 확인했음을 표시
        for v2 in arr[v]:   # 연결되어있는 컴퓨터를 큐에 담아준다.
            queue.append(v2)

print(cnt - 1)      # 바이러스가 전염된 컴퓨터의 개수를 출력
```

## 🔍 결과

![image-20220302135500477](README.assets/image-20220302135500477.png)