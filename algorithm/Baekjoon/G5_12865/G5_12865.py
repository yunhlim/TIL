N, K = input().split()    # 물품의 수(1<=N<=100), 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)
N = int(N)
lst_WV = [] # 무게와 가치를 튜플로 담는다.
for i in range(N):  # 물건의 무게 W(1 ≤ W ≤ 100,000), 물건의 가치 V(0 ≤ V ≤ 1,000)
    lst_WV.append(tuple(input().split()))
weight = 0  # 현재 무게
value = 0 # 현재 가치
value_max = 0 # 가장 큰 가치
index_lst = [0 for _ in range(N)]   # 등장한 물품은 1로 표시(중복을 제거하기 위해)


def recur(cur):
    global weight, value, value_max
    if cur == N:
        return
    for i in range(N):  
        if (not index_lst[i]) and (weight + int(lst_WV[i][0])) <= int(K): 
            weight += int(lst_WV[i][0])
            value += int(lst_WV[i][1])
            index_lst[i] = 1
            recur(cur+1)
            weight -= int(lst_WV[i][0])
            value -= int(lst_WV[i][1])
            index_lst[i] = 0

    if value_max < value:
        value_max = value


recur(0)
print(value_max)