n = int(input())
arr = ['  *  ', ' * * ', '*****']
while n > len(arr):
    nxt_arr = []
    for s in arr:
        nxt_arr.append(' ' * ((len(s) + 1) // 2) + s + ' ' * ((len(s) + 1) // 2))
    for s in arr:
        nxt_arr.append(s + ' ' + s)
    arr = nxt_arr[:]
for i in range(n):
    print(arr[i])