a = int(input())
b = int(input())
c = int(input())
result = a * b * c
cnt_arr = [0 for _ in range(10)]

for c in str(result):
    cnt_arr[int(c)] += 1

for i in range(10):
    print(cnt_arr[i])