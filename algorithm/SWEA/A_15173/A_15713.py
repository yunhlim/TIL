# 섞을 수 있는 경우의 수를 담는다.
def recur(cur, arr):   # left가 나올 수 있는 경우의 수들의 조합
    temp = arr[:]
    if cur == n - 1:    # 다 구했으니 종료
        return
    for i in range(n // 2):
        if i != n // 2 - 1:     # 마지막 수가 아닌 경우
            if temp[i + 1] - temp[i] > 1:       # 오른쪽 수가 하나 더 큰 지 확인
                temp[i] += 1
        else:                   # 마지막 수인 경우
            if cur < n // 2:
                temp[i] += 1
    orders.append(temp)
    recur(cur + 1, temp)


# 섞기
def shuffle(cur, arr):
    if arr == sorted(arr) or arr == sorted(arr, reverse=True):      # 오름차순이나 내림차순인 경우 횟수를 리턴
        return cur
    if cur == 5:        # 5번까지만 섞는다.
        return INF        # 나올 수 없는 큰 수
    left = arr[:n // 2]
    right = arr[n // 2:]
    ans = INF             # 5번 안에 나오지 않는 경우
    for order in orders:        # 섞을 수 있는 경우를 순회
        result = []
        index_l, index_r = 0, 0
        for i in range(n):
            if i in order:
                result.append(left[index_l])
                index_l += 1
            else:
                result.append(right[index_r])
                index_r += 1
        ans = min(ans, shuffle(cur + 1, result))
    return ans


t = int(input())
INF = 6             # 5번 안에 나오지 않는 경우
for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    visited = [0 for _ in range(n)]
    orders = []         # 섞는 경우 left가 나올 수 있는 경우의 수
    recur(0, list(i for i in range(n // 2)))
    result = shuffle(0, arr)
    # INF는 -1 출력
    print(f'#{tc} {result if result != INF else -1}')
