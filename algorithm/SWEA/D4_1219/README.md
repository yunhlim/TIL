# [SWEA] 1219. [S/W 문제해결 기본] 4일차 - 길찾기 [D4]

## 📚 문제

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14geLqABQCFAYD&categoryId=AV14geLqABQCFAYD&categoryType=CODE&problemTitle=1219&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

---

저번 그래프 경로 문제와 유사하다.

어떤 임의의 도착점에 도착하는지 확인하는 문제는 DFS를 이용하는 것이 BFS를 이용하는 것보다 빠르다.

따라서 DFS를 활용해 도착점에 도착하면 탐색을 종료하도록 코드를 짜보았다.

저번엔 set 자료형을 써서 인접되어있는 정점들을 나타냈는데 이번엔 인접 리스트 형태로 나타냈다.

## 📒 코드

```python
for _ in range(10):
    tc, N = map(int, input().split())   # 테스트케이스 개수, 길의 총 개수
    temp = list(map(int, input().split()))  # 입력받은 정점들의 관계
    arr = [[] for _ in range(100)]      # 0~99까지 인접 리스트
    
    for i in range(N):     # 입력받은 정점들의 관계를 인접 리스트에 담는다.
        arr[temp[2*i]].append(temp[2*i+1])  # 단방향

    visited = [0 for _ in range(100)]   # 방문한 정점 확인
    stack = [0]                         # 시작점은 0

    while stack and (not visited[99]):  # 원하는 경로에 도착하거나 더이상 진행할게 없으면 종료
        v = stack.pop()                 # stack에서 정점을 하나 뺀다.
        if not visited[v]:              # 방문하지 않은 정점일 때만 확인
            visited[v] = 1              # 방문시켜주고
            for i in arr[v]:            # 연결된 정점을 확인해 stack에 더해준다.
                if not visited[i]:      # 없으면 안 더해준다.
                    stack.append(i)

    if visited[99]:                     # 원하는 도착점에 도착했는지 확인
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
```

## 🔍 결과 : Pass