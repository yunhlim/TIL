import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [input().split() for _ in range(n)]
dic = {}
for i in range(n):
    num = int(arr[i][1])
    dic[num] = 0

mmax = 0
for i in range(n):
    GL, num = arr[i]
    num = int(num)
    if GL == 'G':
        for k in dic:
            if k >= num:
                dic[k] += 1
                mmax = max(mmax, dic[k])
    else:
        for k in dic:
            if k <= num:
                dic[k] += 1
                mmax = max(mmax, dic[k])
print(n - mmax)