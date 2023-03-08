# n이하의 자연수 중 k-세준수를 찾아라
n = int(input())
k = int(input())
# 현재 k이하의 소수 담기!
# 에라토스테네스의 체로 소수를 구한다.
sosu = []
temp = [0 for _ in range(k + 1)]
for i in range(2, k + 1):
    if temp[i] == 0:
        sosu.append(i)
        for j in range(i, k + 1, i):
            temp[j] = 1
# print(sosu)   # 소수의 집합

visited = [False for _ in range(n + 1)]
visited[1] = True   # 1을 넣어준다.
for i in sosu:
    for j in range(1, n + 1):
        # 이미 조합된(확인한) 수인지 보고 방문표시 해준다.
        if (j // i) > 0 and j % i == 0 and visited[j // i] is True:
            visited[j] = True

print(sum(visited))
