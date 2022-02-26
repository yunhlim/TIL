def f_cnt(num, k):  # num!에 곱해진 소수 k의 개수
    num //= k
    cnt = num
    while num >= k:
        num //= k
        cnt += num
    return cnt

n , m = map(int, input().split())
arr = [[n, n-m, m], [0, 0, 0], [0, 0, 0]]   # n, n-m, m 일 때 각 팩토리얼의 2의 개수와 5의 개수

for i in range(3):
    arr[1][i] = f_cnt(arr[0][i], 2)         # n, n-m, m의 2의 개수
    arr[2][i] = f_cnt(arr[0][i], 5)         # n, n-m, m의 5의 개수
two = arr[1][0] - arr[1][1] - arr[1][2]     # n의 2의 개수에서 나머지를 빼준다.
five = arr[2][0] - arr[2][1] - arr[2][2]    # n의 5의 개수에서 나머지를 빼준다.

print(min(two, five))       # 2와 5 중 최소의 개수를 출력