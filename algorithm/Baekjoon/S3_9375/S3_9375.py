t = int(input())
for _ in range(t):
    n = int(input())
    wear = {}
    for _ in range(n):
        name, kind = input().split()
        wear[kind] = wear.get(kind, 0) + 1

    result = 1
    for cnt in wear.values():
        result *= (cnt + 1)
    
    result -= 1
    print(result)