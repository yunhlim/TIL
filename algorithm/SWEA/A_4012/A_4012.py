def taste():    # 맛 차이의 절댓값
    global min_result
    result = 0
    for i in range(n):
        for j in range(n):
            if visited[i] and visited[j]:   # 고른 걸 더해주고
                result += arr[i][j]
            elif visited[i] == 0 and visited[j] == 0:   # 안 고른 걸 빼준다.
                result -= arr[i][j]
    min_result = min(min_result, abs(result))   # 최솟값으로 초기화
    return


def recur(cur, num):
    if num > n // 2:        # 절반을 넘게 고르는 경우는 종료
        return
                            # 0011 1100처럼 대칭되면 같으므로 가장 큰 자릿수가 0일 때만 뽑는다.
    if cur == n - 1:        # 절반을 고르면 taste()를 돌고 종료, 아니면 그냥 종료
        if num == n // 2:   # 절반을 고르는 경우만
            taste()
        return

    recur(cur + 1, num)     # 선택하지 않는 경우

    visited[cur] = 1
    recur(cur + 1, num + 1)     # 선택하는 경우
    visited[cur] = 0


t = int(input())
for tc in range(1, 1 + t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0 for _ in range(n)]
    min_result = 10000000
    recur(0, 0)
    print(f'#{tc} {min_result}')