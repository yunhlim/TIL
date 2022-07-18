def page(digit, num):
    nameji = num % 10
    mok = num // 10
    
    if mok:
        page(digit + 1, mok)


n = int(input())
visited = [0 for _ in range(10)]

visited_sol = [0 for _ in range(10)]
for i in range(1, n + 1):
    for c in str(i):
        visited_sol[int(c)] += 1
print(*visited_sol)

digit = 1
