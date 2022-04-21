t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    dic = {}
    for i in range(n):
        dic[arr[i]] = dic.get(arr[i], 0) + 1
        if dic[arr[i]] == 3:
            print(arr[i])
            break
    else:
        print(-1)