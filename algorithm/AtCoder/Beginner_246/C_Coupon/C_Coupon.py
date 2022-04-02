def coupon():
    global k
    if k == 0:  # 할인 횟수가 0이면 종료
        return
    for i in range(n):
        if arr[i] >= x:     # x보다 클 때, 할인해준다.
            if k < arr[i] // x:     # 남은 할인을 다 쓸 수 있을 때
                arr[i] = arr[i] - k * x
                k = 0
                return
            k -= arr[i] // x    # 할인하고 남은 할인 횟수
            arr[i] %= x     # 할인하고 남은 금액으로 변경
            if k == 0:          # 할인 횟수가 0이면 종료
                return


n, k, x = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True)     # 오름차순 정렬
coupon()
arr.sort(reverse=True)      # 남은 것들 재정렬
total = 0
for i in range(k, n):       # 할인하면 0이 되니까 큰 것부터 횟수만큼 제외하고 나머지를 더한다.
    total += arr[i]
print(total)