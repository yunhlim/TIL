def run_check(x, arr):  # run 체크
    if 0 < x < 9:
        if arr[x - 1] and arr[x + 1]:
            return True
    if 0 <= x < 8:
        if arr[x + 1] and arr[x + 2]:
            return True
    if 1 < x <= 9:
        if arr[x - 1] and arr[x - 2]:
            return True
    return False


t = int(input())
for tc in range(1, 1 + t):
    arr = list(map(int, input().split()))
    player = [[0 for _ in range(10)] for _ in range(2)]
    result = 0
    for i in range(12):
        p = i % 2       # 플레이어 선택
        player[p][arr[i]] += 1
        if player[p][arr[i]] == 3:  # triplet 체크
            result = p + 1
            break
        if i >= 5:
            if run_check(arr[i], player[p]):
                result = p + 1
                break
    print(f'#{tc} {result}')