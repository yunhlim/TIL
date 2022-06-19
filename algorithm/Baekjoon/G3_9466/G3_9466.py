import sys
sys.setrecursionlimit(100005)


def dfs(x):     # cycle 확인
    global cnt
    visited[x] = 1
    cycle.append(x)
    if visited[arr[x]]:      # 다른 cycle에 연결되는 건 X
        if arr[x] in cycle:       # 방문했던 정점을 또 방문한 경우 cycle O
            for cycle_num in cycle[::-1]:
                cnt += 1                    # cycle이 형성된 개수만큼 cnt 증가
                if arr[x] == cycle_num:     # cycle이 끝나면 종료
                    break
        return
    return dfs(arr[x])


t = int(input())
for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))     # 1부터이니 앞에 padding으로 0 추가
    cnt = 0
    visited = [0 for _ in range(n + 1)]            # cycle이 완성된 수들은 제외
    for i in range(1, n + 1):
        if visited[i]:         # cycle이 완성됐던 수면 pass
            continue
        cycle = []       # cycle을 이루는지 dfs를 탐색하며 값을 담아준다.
        dfs(i)

    print(n - cnt)