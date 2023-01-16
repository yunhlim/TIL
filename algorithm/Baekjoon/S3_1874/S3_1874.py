import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
stack = []

index = 1
result = []
for num in arr:
    if num == index:
        result.append('+')
        result.append('-')
        index += 1
    elif num > index:
        for i in range(index, num):
            stack.append(i)
            result.append('+')
        result.append('+')
        result.append('-')
        index = num + 1
    else:
        if stack.pop() == num:
            result.append('-')
        else:
            print('NO')
            break
else:
    for x in result:
        print(x)
