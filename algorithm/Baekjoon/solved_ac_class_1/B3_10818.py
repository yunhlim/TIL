n = int(input())
arr = list(map(int, input().split()))
small = arr[0]
big = arr[0]
for num in arr:
    if num > big:
        big = num
    elif num < small:
        small = num
print(small, big)