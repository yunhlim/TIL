arr = [0] + [int(input()) for _ in range(9)]
max_cnt = 0
for i in range(1, 10):
    if arr[i] > arr[max_cnt]:
        max_cnt = i
print(arr[max_cnt], max_cnt)