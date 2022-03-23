n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))
prefix_cnt = {}                 # 딕셔너리 활용

for i in range(1, n + 1):       # 누적합
    arr[i] += arr[i - 1]

ans = 0
for i in range(n + 1):          
    ans += prefix_cnt.get(arr[i] - k, 0)        # 이전에 나온 값들 중 차이가 k인 것의 개수를 ans에 더한다.
    prefix_cnt[arr[i]] = prefix_cnt.get(arr[i], 0) + 1     # 딕셔너리에 현재 값의 개수를 하나 늘린다.

print(ans)