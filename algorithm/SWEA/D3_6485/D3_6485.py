T = int(input())

for tc in range(1, T+1):
    N = int(input())  # 버스의 개수
    bus_lst = [0 for _ in range(5000+1)] # 총 정류장 리스트
    for _ in range(N):
        A, B = map(int, input().split()) # 버스의 노선을 담는다.
        for i in range(A, B+1): # 버스가 지나가는 노선에 1씩 추가한다.
            bus_lst[i] += 1
    P = int(input())    # 출력할 정류장의 개수
    result_lst = [0 for _ in range(P)]
    for i in range(P):
        result_lst[i] = bus_lst[int(input())]

    print(f'#{tc} ', end='')
    print(*result_lst)