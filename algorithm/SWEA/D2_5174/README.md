# [SWEA] 5174. [파이썬 S/W 문제해결 기본] 8일차 - subtree [D2]

## 📚 문제

https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVJ-_6qfsDFAWg

---

**이진 트리** 문제이다.

부모와 자식관계를 배열에 담아준다.

이 때 이진트리이니 자식은 값이 2개인 리스트를 2차원으로 만들어 안에 넣어준다.

트리 순회로 노드의 개수를 알아낼 수 있지만 어차피 루트에서 연결된 모든 서브 트리의 노드 개수를 구하는 것이므로 BFS 탐색으로 푼다.

## 📒 코드

```python
from collections import deque

t = int(input())
for tc in range(1, t + 1):
    e, par = map(int, input().split())    # e: 간선의 개수, par: 확인할 서브 트리의 루트 노드
    temp = list(map(int, input().split()))  # 입력받은 부모 자식 노드 쌍
    arr = [[0, 0] for _ in range(e + 2)]    # 부모 자식 관계

    for i in range(e):  # 부모와 자식 노드 관계를 arr 배열에 담는다.
        p, c = temp[i * 2], temp[i * 2 + 1]
        if arr[p][0] == 0:
            arr[p][0] = c
        else:
            arr[p][1] = c

    queue = deque()
    queue.append(par)
    cnt = 0

    while queue:    # BFS로 탐색하며 개수를 센다.
        v = queue.popleft()
        cnt += 1    # 연결된 노드들의 개수 + 1
        for i in range(2):  # 연결됐는지 확인
            if arr[v][i] == 0:
                break
            queue.append(arr[v][i])
        arr[v] = [0, 0]     # 방문했으면 다시 탐색하지 않도록 초기화
    print(f'#{tc} {cnt}')
```

## 🔍 결과 : Pass