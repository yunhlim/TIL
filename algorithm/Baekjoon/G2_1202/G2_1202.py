import heapq
import sys
input = sys.stdin.readline


n, k = map(int, input().split())
jams = sorted([list(map(int, input().split())) for _ in range(n)])  # 무게 순으로 정렬
bags = sorted([int(input()) for _ in range(k)])     # 무게 순으로 정렬

heap = []   # 가치가 큰 것부터 담을 최대 힙
s = 0
total = 0
for bag in bags:        # 무게가 작은 가방부터 순회
    while s < len(jams) and bag >= jams[s][0]:  # 현재 가방보다 무게가 작거나 같은 보석들을 순회
        heapq.heappush(heap, -jams[s][1])       # heap에 보석의 가치를 큰 순서대로 담는다.
        s += 1
    if heap:    # 힙에 가치가 가장 큰 것부터 가방 하나당 하나씩 꺼낸다.
        total += -heapq.heappop(heap)
print(total)