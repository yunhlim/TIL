import sys
input = sys.stdin.readline

N = int(input())
cue = []

for _ in range(N):
    command = input().split()
    if command[0] == 'push':
        cue += [command[1]]
    elif command[0] == 'pop':
        if len(cue):
            print(cue[0])
            del cue[0]
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(cue))
    elif command[0] == 'empty':
        if len(cue):
            print(0)
        else: print(1)
    elif command[0] == 'front':
        if len(cue):
            print(cue[0])
        else: print(-1)
    else:
        if len(cue):
            print(cue[-1])
        else: print(-1)