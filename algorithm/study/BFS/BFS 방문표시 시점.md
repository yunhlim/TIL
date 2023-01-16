# [Algorithm] BFS의 방문표시 시점 주의!

## 📖 DFS와 BFS의 차이

DFS는 stack이나 재귀로 구현한다.

DFS는 **후입 선출 방식**이라, stack에서 꺼낸 후 방문표시를 해도 상관없다. 왜냐면 넣을 때 방문표시 하든 뺄 때 하던 같은 값이 stack 쌓일 일이 없다. 방문표시만 해준다면 말이다.

그렇지만 BFS는 **선입 선출 방식**이다. 때문에 queue에 넣기 전에 방문표시를 꼭 해줘야 한다. 그렇지 않으면 **queue에 중복된 값이 쌓여** 시간 초과하거나 메모리 초과하는 일이 발생할 수 있다.

**포인트는 큐에 중복된 값이 쌓이지 않게 방문표시를 큐에 넣기 전에 해줘야 한다는 점이다!!**

## 📒 python BFS 코드로 확인

- 정상적인 코드 (큐에 넣을 때 방문 표시)

```python
# 올바른 코드
que.append(1)	# 1부터 큐에 넣고 시작
visited[1] = True				# 초기 값도 방문표시
while len(que) > 0:
    cur = que.popleft()

    for nxt in v[cur]:
        if visited[nxt]:
            continue

        que.append(nxt)
        visited[nxt] = True		# 큐에 넣을 때 방문표시
```

- 잘못된 코드 (큐에서 꺼낼 때 방문 표시)

```python
# 잘못된 코드
que.append(1)
while len(que) > 0:
    cur = que.popleft()
    visited[cur] = True		# 큐에서 꺼낼 때 방문표시

    for nxt in v[cur]:
        if visited[nxt]:
            continue

        que.append(nxt)
```

두 코드의 차이점은 방문표시를 큐에 넣을 때 하느냐, 큐에서 꺼낼 때 하느냐의 차이이다.

큐에서 꺼낼 때 하는 게 더 간단하지만 실제론 큐에 중복된 값이 들어가게 되니 큐에 넣을 때 작성해줘야 한다.

