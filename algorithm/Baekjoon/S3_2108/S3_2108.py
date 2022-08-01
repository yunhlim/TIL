import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
cnt_dic = {}
total = 0
max_num = arr[0]
min_num = arr[0]

for i in range(n):
    cnt_dic[arr[i]] = cnt_dic.get(arr[i], 0) + 1
    total += arr[i]
    if max_num < arr[i]:
        max_num = arr[i]
    if min_num > arr[i]:
        min_num = arr[i]

print(total // n)

cnt_arr = []
for i in cnt_dic:
    pass


print(max_num - min_num)