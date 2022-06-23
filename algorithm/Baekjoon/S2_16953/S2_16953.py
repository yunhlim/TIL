from collections import deque

def bfs():
    que = deque()
    que.append(a)
    dic[a] = 1  # 최소 연산 횟수에 1을 더하라 했으므로 시작값은 1이다.
    while que:
        v = que.popleft()
        if v == b:          # b가 나온 경우
            return dic[b]
        if v * 2 <= b and not dic.get(v * 2):     # 나오지 않은 값인 경우
            dic[v * 2] = dic[v] + 1
            que.append(v * 2)                   # que에 담아준다.
        if v * 10 + 1 <= b and not dic.get(v * 10 + 1):    # 1을 붙인 수의 연산횟수가 더 작아지면 변경
            dic[v * 10 + 1] = dic[v] + 1
            que.append(v * 10 + 1)
    return -1

a, b = map(int, input().split())
dic = {}
print(bfs())