import sys
input = sys.stdin.readline

n = int(input())
arr = [0 for _ in range(10001)]

for i in range(n):
    arr[int(input())] += 1

for i in range(1, 10001):
    for _ in range(arr[i]):
        print(i)