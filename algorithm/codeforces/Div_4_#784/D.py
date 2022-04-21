t = int(input())
for _ in range(t):
    n = int(input())
    arr = input()
    store = set()
    for i in range(n):
        if arr[i] == 'W':
            if len(store) == 1:
                print('NO')
                break
            store = set()
        else:
            store.add(arr[i])
    else:
        if len(store) != 1:
            print('YES')
        else:
            print('NO')