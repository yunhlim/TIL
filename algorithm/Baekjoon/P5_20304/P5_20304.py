from collections import deque

N = int(input())    # 비밀번호 최댓값 정수 N
M = int(input())    # 시도한 비밀번호 개수
queue = deque(map(int, input().split()))
visited = [-1 for _ in range(N+1)]      # visited에 bit의 차이만큼 적어준다.

temp = N        # bit의 자릿 수를 구하기 위해 따로 만들어준다.
cnt = 0         # N까지의 bit 수
while temp:
    temp //= 2  # 2로 나누며 bit 수를 찾아준다.
    cnt += 1

for i in queue:     # queue에 담으면서 visited에 0으로 적는다.
    visited[i] = 0  # bit의 차이가 없으므로

while queue:        # queue에 존재할 때 반복
    v = queue.popleft()     
    for i in range(cnt):    # 자릿수마다 bit를 바꿔준다.
        nv = v ^ (1 << i)   # bit를 하나 바꾼다. bit 차이는 1 더한다.
        if nv <= N and (visited[nv] == -1): # 아직 나오지 않은 것만 확인
            visited[nv] = visited[v] + 1    # queue에 담을 때 bit가 달라졌음을 적어준다.
            queue.append(nv)

if N:               # N이 0이 아닌 수 제거
    print(max(visited))
else: print(0)      # 0이 들어오면 0뿐이다.