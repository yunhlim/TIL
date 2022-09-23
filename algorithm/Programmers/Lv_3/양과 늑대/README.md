# [Programmers] Lv 3. 양과 늑대 [2022 KAKAO BLIND RECRUITMENT]

## 📚 문제 : [양과 늑대](https://school.programmers.co.kr/learn/courses/30/lessons/92343)

## 📖 풀이

완전 탐색 문제이다.

순서가 있으니 그냥 완전 탐색을 돌리면 2 ^ 17로 시간 안에 돌기 어렵다. 비트마스킹을 써도 되지만, 트리로 되어있고 늑대가 다 잡아먹을 경우를 배제한 가지치기를 접목한 백트래킹으로 해결할 수 있다.

DFS로 해결하면 되는데 이 때, 그냥 자식으로 내려가며 해결하려고하면 답을 구할 수 없다.

왜냐하면 되돌아와 다른 부분으로 퍼지지 않기 때문이다.

따라서 해결 방법이 **2가지** 정도 있다.

1. 현재 위치부터 순서대로 연결된 정보를 다 담아가며 **비트마스킹 DP**로 해결하는 방법이 있다.

그렇지만 나는 트리의 성질을 이용하며 말단으로 퍼져나가기만 하니, **매번 움직일 수 있는 모든 말단의 노드로 퍼져나가는 방법**을 생각했다.

따라서 현재 방문한 모든 노드에서 연결되어 있는 방문하지 않는 노드들을 다 순회하여 해결한다.

## 📒 코드

```python
def solution(info, edges):
    def dfs(cur, sheep, wolf):
        if info[cur] == 0:      # 양이 나왔을 때
            sheep += 1
        else:                   # 늑대가 나왔을 때
            wolf += 1
            if wolf >= sheep:   # 늑대가 더 많은 경우는 보지 않는다.
                return sheep
            
        visited[cur] = True
        ans = sheep
        for i in range(len(info)):  
            if visited[i]:      # 방문한 노드들 순회
                for nxt in child_arr[i]:        # 방문한 노드들에 연결되어 있는 방문하지 않은 모든 노드들 순회
                    if not visited[nxt]:
                        ans = max(ans, dfs(nxt, sheep, wolf))
        visited[cur] = False
        return ans
    
    child_arr = [[] for _ in range(len(info))]
    visited = [False for _ in range(len(info))]

    for par, child in edges:
        child_arr[par].append(child)

    return dfs(0, 0, 0)
```

