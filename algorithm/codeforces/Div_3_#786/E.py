n = int(input())
arr = list(map(int, input().split()))
min_two = [100000000, 100000000]    # 따로 떨어진 벽의 파괴 횟수
result = 100000000
for i in range(n):
    # 두 벽이 붙어있는 경우
    if i < n - 1:
        x, y = arr[i], arr[i + 1]
        big, small = max(x, y), min(x, y)
        if big < small * 2:
            cnt = big - small       # 내구성이 같아질 때까지
            big -= cnt * 2
            small -= cnt
            cnt += (big + small) // 3 + (1 if (big + small) % 3 else 0) # 내구성이 같으면 3으로 나눈다.
            result = min(result, cnt)
        else:               # 큰 쪽이 작은 쪽 * 2보다 크거나 같을 때
            result = min(result, big // 2 + big % 2)
    # 따로 떨어진 벽을 깨는 경우(1칸 이상)
    min_two.append(arr[i] // 2 + arr[i] % 2)
    min_two = sorted(min_two)[0:2]      # 가장 작은 횟수 2개만 남긴다.

    # 1칸의 벽을 사이에 두고 떨어져있는 경우(두 벽의 내구성이 홀수인 경우만)
    if 0 < i < n - 1 and arr[i - 1] and arr[i + 1]:
        total = arr[i - 1] + arr[i + 1]
        cnt = total // 2 + total % 2
        result = min(result, cnt)

result = min(sum(min_two), result)      # 벽이 떨어져있는 경우를 결과값과 비교
print(result)