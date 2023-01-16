# 택배

n, c = map(int, input().split())        # n은 동네 수, c는 트럭 최대 적재량
m = int(input())                        # m은 택배 개수
parcels = [[] for _ in range(n + 1)]    # 각 마을에서 보낼 택배 리스트
for i in range(m):
    s, e, cnt = map(int, input().split())       # 출발, 도착, 택배 개수
    parcels[s].append([e, cnt])

last_cap = -1                           # 싣은 택배 중 가장 마지막에 받을 택배
receive_parcels = {}                    # 각 마을에서 받을 택배
cap = 0                                 # 현재 싣고 있는 택배 무게

for i in range(1, n + 1):
    if receive_parcels.get(i):                      # 현재 도착한 택배 조회
        cap -= receive_parcels[i]                   # 도착한 택배 무게를 뺀다.
    for arrive, cnt in sorted(parcels[i]):
        if last_cap <= arrive and cap == c:         # 꽉 찼는데 더 멀리가야하는 경우 종료
            break

        receive_parcels[arrive] = receive_parcels.get(arrive, 0) + cnt
        cap += cnt

        if cap <= c:                                # 새로 넣어도 택배 무게를 넘치지 않는다.
            continue

        receive_parcels_item = sorted(receive_parcels.items())      # 택배 정렬
        while cap > c:                                              # 택배가 더 적어질 때까지 멀리 갈 택배 제거
            arrive, cnt = receive_parcels_item.pop()
            del receive_parcels[arrive]
            cap -= cnt
            if cap < c:                                             # 택배가 더 적어진 경우
                receive_parcels[arrive] = c - cap                   # 택배 무게만큼 다시 채워준다.
                receive_parcels_item.append([arrive, c - cap])
                cap = c
        last_cap = receive_parcels_item[-1][0]         # 담겨있는 택배 중 가장 멀리 갈 택배 마을 번호를 담는다.

print(sum(receive_parcels.values()))