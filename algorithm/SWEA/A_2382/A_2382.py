for tc in range(1, 1 + int(input())):
    n, time, k = map(int, input().split())  # n: 셀의 한 변의 길이, time: 격리 시간, k: 군집의 개수
    arr = [[] for _ in range(time + 1)]
    dy = [0, -1, 1, 0, 0]   # 상: 1, 하: 2, 좌: 3, 우: 4
    dx = [0, 0, 0, -1, 1]
    for i in range(k):      # 초기 위치 설정
        y, x, m, d = map(int, input().split())  # 좌표(y, x), 미생물의 수, 이동방향
        arr[0].append([y, x, m, d])

    for i in range(1, time + 1):
        for v in arr[i - 1]:        # 이전 미생물의 값들을 가져온다.
            ny = v[0] + dy[v[3]]    # 좌표를 이동방향으로 움직인다.
            nx = v[1] + dx[v[3]]
            m, d, m_max = v[2], v[3], v[2]  # 미생물의 수, 이동방향, 최대 미생물의 수(여러 개가 겹칠 때 사용)
            if ny == 0 or ny == n - 1:      # 위, 아래 끝에 도달한 경우
                m //= 2
                d = 3 - d
            if nx == 0 or nx == n - 1:      # 양 옆 끝에 도달한 경우
                m //= 2
                d = 7 - d
            for j in range(len(arr[i])):       # 같은 위치에 있는 경우
                if arr[i][j][0] == ny and arr[i][j][1] == nx:
                    if arr[i][j][4] < m_max:    # 미생물의 수가 더 많으면
                        arr[i][j][4] = m_max    # 최대 미생물의 수를 업데이트
                        arr[i][j][3] = d        # 방향을 바꿔준다(최대 미생물의 수일 때 방향이다)
                    arr[i][j][2] += m           # 미생물을 더해준다(같은 위치면 다 더한다)
                    break
            else:                           # 같은 위치에 존재하는 것이 없는 경우
                arr[i].append([ny, nx, m, d, m_max])

    result = 0
    for v in arr[-1]:   # 미생물들의 개수를 다 더한다.
        result += v[2]
    print(f'#{tc} {result}')
