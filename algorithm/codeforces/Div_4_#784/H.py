t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 0
    visited = [0 for _ in range(30)]
    # 비트를 visited에 넣어준다.
    # 비트마스킹
    for i in range(30):
        pass