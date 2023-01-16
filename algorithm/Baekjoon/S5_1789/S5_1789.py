n = int(input())

cnt = 0
result = 0
for i in range(1, n + 1):
    cnt += 1
    result += i
    if result == n:
        break
    elif result > n:
        cnt -= 1
        break
print(cnt)