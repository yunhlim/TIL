n = int(input())

dist = 1
cnt = 1
for i in range(1, n):
    if n <= cnt:
        break
    cnt += i * 6
    dist += 1
print(dist)