# [Baekjoon] 1167. 트리의 지름 [G3]

## 📚 문제

https://www.acmicpc.net/problem/1167

---

전에 풀었던 1967. 트리의 지름 문제와 거의 유사하다.

차이점은 입력으로 들어오는 것이 부모와 자식 관계가 아닌 정점 두 사이의 연결이다.

양방향으로 다 입력이 들어오니 입력을 다 받아준 후 visited로 확인하여 한쪽 방향으로만 진행할 수 있도록 해준다.

재귀함수를 돌면서 입력받은 정점의 visited 인덱스를 1로 바꾼다.

그리고 자식 노드를 검사할 때 visited이 0인 자식노드가 없으면 리프 노드인 것이다.

이 과정만 전 문제에서 추가하면 된다.

나머지 풀이는 다음을 참고한다.



### 📌 1967. 트리의 지름 블로그 포스팅 참고

https://velog.io/@yunhlim/Baekjoon-1967.-%ED%8A%B8%EB%A6%AC%EC%9D%98-%EC%A7%80%EB%A6%84-G4



## 📒 코드

```python
def recur(n):
    global total_max
    visited[n] = 1          # 정점 방문 표시
    
    result = []
    for c, w in arr[n]:     # 자식 노드를 재귀호출하면서 가중치 값을 더해준다.
        if not visited[c]:  # 방문했던 노드는 부모 노드로 사용했으니 보지 않는다.
            result.append(w + recur(c))

    if result == []:        # 자식 노드가 없으면 0을 반환
        return 0

    result.sort()           # 노드에 연결된 길이들을 크기 순대로 정렬한다.
    result = result[::-1][0:2]      # 가장 긴 2개만 남긴다.
    total_max = max(total_max, sum(result))  # 2개를 합한 것이 현재 구한 최대 트리의 지름보다 큰지 확인

    return result[0]        # 노드에 연결된 선 중 가장 긴 길이를 리턴


n = int(input())
arr = [[] for _ in range(n + 1)]    # 부모 노드를 인덱스로 하는 리스트(자식노드와 가중치를 담는다.)
visited = [0 for _ in range(n + 1)]
temp = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    s = 0
    while temp[i][s] > 0:   # -1이면 종료
        if s == 0:          # 첫 번째 입력을 정점 v1
            v1 = temp[i][s]
            s += 1
        else:
            arr[v1].append([temp[i][s], temp[i][s + 1]])    # 두 번째 입력부터 정점 v2, w로 받아 arr에 넣어준다.
            s += 2
total_max = 0   # 가장 긴 트리의 지름

recur(1)
print(total_max)
```

## 🔍 결과

![image-20220318001323019](README.assets/image-20220318001323019.png)