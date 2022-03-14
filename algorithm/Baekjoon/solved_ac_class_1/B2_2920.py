arr = list(map(int, input().split()))
asc = [i + 1 for i in range(8)]
desc = asc[::-1]
if arr == asc:
    print('ascending')
elif arr == desc:
    print('descending')
else:
    print('mixed')