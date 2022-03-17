# [SWEA] 5178. [파이썬 S/W 문제해결 기본] 8일차 - 노드의 합 [D3]

## 📚 문제

https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVJ-_6qfsDFAWg

---

빈 노드들을 채워 줄 때 후위 순회를 활용해 안쪽으로 더해준다.

완전 이진 트리이다. 따라서 배열을 1차원으로 선언한다.

주어진 리프 노드들을 트리에 노드의 번호에 맞게 집어 넣어준다.

재귀를 활용해 리프부터 순회하며 자식 노드의 합이 부모 노드의 합이 되도록 작성한다.

그리고 출력하고 싶은 노드 번호를 출력한다.

## 📒 코드

```python
def recur(v):  # 빈 노드들을 채워준다.(후위 순회)
    if v <= n:
        if tree[v] == 0:    # 노드에 값이 없는 경우
            tree[v] = recur(v*2) + recur(v*2+1)
        return tree[v]      # 노드에 값이 있는 경우
    else:       # 노드의 범위를 넘어간 경우 0
        return 0


t = int(input())
for tc in range(1, t + 1):
    # n: 노드 수 m: 리프 노드 수 l: 출력할 노드 번호
    n, m, node = map(int, input().split())
    tree = [0 for _ in range(n + 1)]

    for i in range(m):  # 리프 노드를 채워준다.
        p, c = map(int, input().split())
        tree[p] = c
        
    recur(1)    # 모든 노드들 다 채우기
    print(f'#{tc} {tree[node]}')

```

## 🔍 결과 : Pass