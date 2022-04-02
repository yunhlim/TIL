t = int(input())
for _ in range(t):
    string = input()
    visited = []
    cnt = 0
    for i in string:
        if i in visited:
            cnt += len(visited) - 1
            visited = []
        else:
            visited.append(i)
    print(cnt + len(visited))