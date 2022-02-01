import sys
input = sys.stdin.readline

N = int(input())
stack = []

for i in range(N):
    command = input().split()
    if command[0] == 'push':
        stack += [int(command[1])]
    elif command[0] == 'pop':
        if len(stack):
            print(stack[-1])
            del stack[-1]
        else: print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack):
            print(0)
        else: print(1)
    else:
        if len(stack):
            print(stack[-1])
        else: print(-1)