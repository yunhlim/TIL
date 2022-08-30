t = int(input())
name = 'Timur'
for _ in range(t):
    n = int(input())
    string = input()
    if n != 5:
        print('NO')
        continue
    visited = set()
    for c in string:
        if c in visited or c not in name:
            print('NO')
            break
        visited.add(c)
    else:
        print('YES')
