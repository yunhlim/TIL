n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

min_cost = 1_000_000_000    # 현재까지의 최소 값을 저장한다.(초기화는 나올 수 있는 가장 큰 수로 초기화)

result = 0
for i in range(n - 1):
    if cost[i] < min_cost:
        min_cost = cost[i]
    result += dist[i] * min_cost

print(result)