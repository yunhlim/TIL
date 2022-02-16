import sys
sys.stdin = open("input.txt")
T = 10
for tc in range(1, 1+T):
    V, E = map(int, input().split())

    arr = [[0 for _ in range(V+1)] for _ in range(V+1)]   # padding을 더한 2차원 배열
    visited = [0 for _ in range(V+1)]   # 등장한 간선인지 선택
    result = []
    in_lst = list(map(int,input().split()))
    for i in range(E):               # 배열에 담아준다.
        arr[in_lst[2*i]][in_lst[2*i+1]] = 1

    for i in range(1, V+1):
        for j in range(1, V+1):
            if arr[j][i]:  # 방향선이 꽂히는 정점은 break
                break
        else:
            visited[i] = 1
            result.append(i)
            nows = [i]       
            while nows != []:
                new_nows = []
                for now in nows:
                    for k in range(1, V+1):
                        if arr[now][k] and visited[k] == 0:   # 방향선을 받는 새로운 정점
                            visited[k] = 1
                            result.append(k)
                            new_nows.append(k)
                nows = new_nows[:]
        if len(result) == V:
            break
    print(f'#{tc} ', end='')
    print(*result)


            
