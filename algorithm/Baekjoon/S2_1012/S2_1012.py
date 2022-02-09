T = int(input()) # T는 테스트 케이스 수

for _ in range(T):
    M, N, K = map(int,input().split()) # M은 가로길이, N은 세로길이, K는 배추 위치의 개수

    lst = [[0 for _ in range(M+2)] for _ in range(N+2)] # 배추밭을 2차원 lst로 초기화
    # 테두리를 추가해 인덱스 초과 error를 없앤다.

    for i in range(K):
        X, Y = map(int, input().split())    # X,Y는 배추의 좌표
        lst[Y+1][X+1] = 1   # 배추를 배추밭에 1로 표기

    result = 0  # 애벌레 개수
    
    dir = [(1,0), (-1,0), (0,1), (0,-1)] # 네 방향 인덱스

    for i in range(1, N+1):
        for j in range(1, M+1):
            if lst[i][j] == 1:  # 1을 만났을 때
                result += 1 # 애벌레를 하나 더한다.
                lst[i][j] = 0   # 1을 만나면 다 0으로 바꾼다.
                node = []   # 1을 만났을 때 주위 네 방향을 담을 리스트
                for y, x in dir:    # 현재 인덱스 중심으로 네 방향으로 움직인 인덱스를 node에 담는다.
                    node.append((i+y, j+x))
                while len(node) > 0:    # 비교할 노드가 있으면 계속한다.
                    node2 = []
                    for k in range(0,len(node)):                   
                        y1, x1 = node[k]
                        if lst[y1][x1] == 1:
                            lst[y1][x1] = 0
                            for y2,x2 in dir:   # 현재 인덱스 기준 다시 네 뱡향으로 조사한다.
                                node2.append((y1+y2, x1+x2))
                    node = node2[:] # 리스트를 복사할 때 슬라이싱을 활용한다.

    print(result)
