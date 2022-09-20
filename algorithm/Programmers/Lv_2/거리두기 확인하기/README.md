# [Programmers] Lv 2. 거리두기 확인하기 [2021 카카오 채용연계형 인턴십]

## 📚 문제 : [거리두기 확인하기](https://school.programmers.co.kr/learn/courses/30/lessons/81302)

## 📖 풀이

**BFS**로 2칸 이하로 움직이며 사람이 있는지 확인하여 해결했다.

맨해튼 거리가 2이하이니, 네가지 방향을 생각하면 된다.

모든 사람을 찾아 그 사람부터 BFS로 2칸 이하로 움직일 수 있는 모든 방향을 탐색한다.

토마토 문제를 풀 듯, depth를 기록하며 BFS를 돌면 된다.

2칸 이하에 사람이 있으면 거리두기를 실패했으니 0을 넣어주고, 아니면 1을 넣어준다.

## 📒 코드

```python
def solution(places):
    from collections import deque

    def in_range(x, y):
        return 0 <= x < 5 and 0 <= y < 5
    
    
    def bfs(place, x, y):
        visited = [[0] * 5 for _ in range(5)]
        que = deque()
        que.append([x, y])
        visited[x][y] = 1
        d = 0
        while que:
            if d > 1:
                break
            for _ in range(len(que)):
                x, y = que.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if not in_range(nx, ny) or visited[nx][ny]:
                        continue
                    if place[nx][ny] == 'P':
                        return False
                    elif place[nx][ny] == 'O':
                        que.append([nx, ny])
                        visited[nx][ny] = 1
                d += 1
        return True
        
    
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    answer = []
    
    for place in places:
        flag = 1
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if not bfs(place, i, j):
                        flag = 0
                        break
            if not flag:
                break
        answer.append(flag)
        
    return answer
```

