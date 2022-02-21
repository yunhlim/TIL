T = int(input())
memo = [[1], [1, 1]] # 파스칼 삼각형의 위부터 순차적으로 채운다.
for tc in range(1, T + 1):
    N = int(input())    # 출력시킬 줄의 수
    while len(memo) < N: # 준비된 줄보다 출력시킬 줄이 많으면 반복문을 수행
        l = len(memo)    # 현재 출력가능한 줄의 수
        # 다음 출력시킬 줄을 추가할 배열
        small_arr = [1]   # 왼쪽은 1을 붙인다.
        for i in range(0, l - 1):
            # 전 줄을 이용해 다음 줄을 추가한다.
            small_arr.append(memo[l - 1][i] + memo[l - 1][i + 1])
        small_arr.append(1)     # 오른쪽에도 1을 붙인다.
        memo.append(small_arr)   # 배열에 추가해준다.
    print(f'#{tc}')
    for i in range(N):  # 원하는 줄의 개수를 출력한다.
        print(*memo[i])