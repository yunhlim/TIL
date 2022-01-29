N, K = map(int,input().split())    # 물품의 수(1<=N<=100), 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)
lst_WV = [(0,0)] # 무게와 가치를 튜플로 담는다.
for i in range(N):  # 물건의 무게 W(1 ≤ W ≤ 100,000), 물건의 가치 V(0 ≤ V ≤ 1,000)
    lst_WV.append(tuple(map(int,input().split())))
# 물건을 하나씩 넣고, 0 부터 1씩 증가하며 무게 대비 현재 최고의 가치를 적는 메모이제이션
memo = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):    # 첫번째 물건부터 검색한다
    weight = lst_WV[i][0]   # 선택된 물건의 무게
    value = lst_WV[i][1]    # 선택된 물건의 가치
    for j in range(1, K+1):    # 무게를 0부터 K까지 올려가며 무게대비 최선의 경우를 대입한다.
        if weight > j:    # 현재 무게보다 물건의 무게가 작으면 전 물건에서 사용했던 값을 사용
            memo[i][j] = memo[i-1][j]
        else:
            if value + memo[i-1][j-weight] > memo[i-1][j]:  # 가치가 더 높은 걸 선택
                # 현재 무게에서 물건의 무게를 뺀 가치에다가 현재물건을 더한 가치와 이전 가치를 비교
                memo[i][j] = value + memo[i-1][j-weight]
            else: memo[i][j] = memo[i-1][j] 

print(memo[N][K])