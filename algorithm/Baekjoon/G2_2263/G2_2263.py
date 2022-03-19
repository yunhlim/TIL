from collections import deque


n = int(input())
in_order = [0] + list(map(int, input().split()))    # 입력받은 in order
post_order = [0] + list(map(int, input().split()))  # 입력받은 post order

in_order_arr = [0 for _ in range(n + 1)]    # 노드가 인오더에서 어디 위치해있는지 배열에 담아준다.
for i in range(1, n + 1):
    in_order_arr[in_order[i]] = i           # 배열의 인덱스는 노드번호, 값은 인오더에서의 위치이다.

stack = deque()                 # pop의 시간복잡도를 줄인다.
stack.append((n, 0))            # 루트는 post order의 마지막에 나온다.
visited = [1] + [0 for _ in range(n)]       # 방문 처리
result = []

while stack:
    v, minus = stack.pop()  # stack에 넣는 값은 포스트오더의 인덱스 값과 오른쪽 자식노드를 거치는 횟수이다.
                            # 오른쪽 자식노드를 거칠 때마다 인오더에서 자식노드를 루트로 하는 서브트리가
                            # 한 칸씩 밀리므로 그 때마다 처리해준다.
    if visited[v]:          # 아직 나오지 않은 노드일 경우만 본다.
        continue
    visited[v] = 1
    result.append(post_order[v])    # 정점을 출력해준다.

    if v != in_order_arr[post_order[v]] - minus:   # 자식이 둘인 경우
        stack.append((v - 1, minus + 1))           # 오른쪽 자식 노드 선택, 선택한 노드의 바로 왼쪽 노드다.
    stack.append((in_order_arr[post_order[v]] - 1 - minus, minus))  # 왼쪽 자식 노드 선택, 인오더에서 위치한 인덱스 - 1에 위치해있다.
    
print(*result)