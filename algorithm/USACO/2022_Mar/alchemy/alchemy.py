import sys
input = sys.stdin.readline

def recur(metal, cnt):   # 필요한 개수를 재귀로 구현
    if visited[metal] >= cnt:   # 개수가 충분한 경우
        visited[metal] -= cnt
        return True
    if not graph[metal]:    # 원하는 개수가 충족되지 않았는데 만들 조합이 없는 경우 종료
        return False

    plus_cnt = cnt - visited[metal] # 개수가 충분하지 않지만 만들 조합이 있는 경우 확인
    for u in graph[metal]:
        if not recur(u, plus_cnt):  # 만들 수 없는 경우
            return False
    visited[metal] = 0              # 다 만들 수 있으면 0으로 만든다.
    return True


n = int(input().rstrip())
unit_cnt = [0] + list(map(int, input().split()))
k = int(input().rstrip())
graph = [[] for _ in range(n + 1)]  # i(금속) -> j(재료)

for _ in range(k):
    temp = list(map(int, input().split()))
    metal = temp[0]
    for material in temp[2:]:
        graph[metal].append(material)

s, e = 0, 10000000
ans = 0
while s <= e:   # 이진 탐색
    visited = unit_cnt[:]   # 입력된 개수를 복사
    mid = (s + e) // 2
    if recur(n, mid):
        ans = mid
        s = mid + 1
    else:
        e = mid - 1
print(ans)