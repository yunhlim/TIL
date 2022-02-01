import sys
input = sys.stdin.readline

N = int(input())
deque = []

for _ in range(N):
    command = input().split()
    
    if command[0] == 'push_front':
        deque = [command[1]] + deque
    elif command[0] == 'push_back':
        deque = deque + [command[1]]
    elif command[0] == 'pop_front':
        if len(deque):
            print(deque[0])
            del deque[0]
        else: print(-1)
    elif command[0] == 'pop_back':
        if len(deque):
            print(deque[-1])
            del deque[-1]
        else: print(-1)
    elif command[0] == 'size':
        print(len(deque))
    elif command[0] == 'empty':
        if len(deque):
            print(0)
        else: print(1)
    elif command[0] == 'front':
        if len(deque):
            print(deque[0])
        else: print(-1)
    else:
        if len(deque):
            print(deque[-1])
        else: print(-1)