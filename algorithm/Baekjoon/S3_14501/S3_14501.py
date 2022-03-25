def recur(day, p):
    global result
    if day > n:
        return
    if day == n:
        result = max(result, p)
        return
    recur(day + 1, p)
    recur(day + arr[day][0], p + arr[day][1])

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0
recur(0, 0)
print(result)