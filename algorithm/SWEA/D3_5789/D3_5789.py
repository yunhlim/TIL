T = int(input())
for tc in range(1, T+1):
    N, Q = map(int,input().split()) # N: 정수의 개수, Q: 변경 횟수
    num_lst = [0 for _ in range(N+1)] # 0번 상자를 추가해준다. 쓰진 않는다.
    for i in range(1, Q+1):
        L, R = map(int,input().split())
        for j in range(L,R+1):  # L번부터 R번 상자 순회
            num_lst[j] = i  # 상자들에 i를 담는다.

    print(f'#{tc} ', end='')
    print(*num_lst[1:])