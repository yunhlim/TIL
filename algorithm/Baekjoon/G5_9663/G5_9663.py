N = int(input())    # N개의 퀸
visited = []        # queen의 위치
cnt = 0             # N개를 놓는 경우의 수

def queens(cur):
    global cnt
    if cur == N:    # 퀸을 N개 다 놓으면 cnt 1 증가
        cnt += 1
        return
    for i in range(N):          # 퀸의 위치 선택
        if i not in visited:    # 퀸이 원하는 열에 등장하지 않았는지 확인
            for j in range(cur):
                if abs(visited[j] - i) == cur - j:       # 대각선에 등장하지 않아야 함.
                    break
            else:
                visited.append(i)   # 퀸을 위치에 둔다.
                queens(cur + 1)     # 다음 행으로 이동~
                visited.pop()       # 퀸을 위치에서 제거
queens(0)              
print(cnt)