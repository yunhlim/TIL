n = int(input())

for i in range(1, n + 1):
    total = i
    for c in str(i):
        total += int(c)
    
    if total == n:
        print(i)
        break
else:
    print(0)