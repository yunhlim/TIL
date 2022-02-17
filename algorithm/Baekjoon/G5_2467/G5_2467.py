N = int(input())
arr = list(map(int, input().split()))

s = 0
e = N-1

x, y = arr[s], arr[e]
while e - s > 0:
    if abs(arr[s] + arr[e]) < abs(x + y):
        x, y = arr[s], arr[e]
    if arr[s] + arr[e] > 0:
        e -= 1
    else: s += 1
print(x, y)