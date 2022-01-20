N = int(input())

def jinsu2(num):
    if num == 1:
        return 1
    else:
        return num % 2 + 10 * jinsu2(num//2) 

print(jinsu2(N))