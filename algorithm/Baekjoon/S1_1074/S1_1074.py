def recur(n, y, x):
    if n == 1:  # 더 이상 쪼개지지 않을 때 0을 return
        return 0
    
    n //= 2     # 작은 정사각형의 변의 길이는 원래 사각형의 절반이다.
    # 4 구역 중 y, x의 어디에 위치하는지 i, j에 담아준다.
    i = y // n  
    j = x // n
    # 작은 사각형에서 시작부분의 값 + recur(작은사각형의 변의 길이, 새로운 좌표)
    return (n * n) * (2 * i + j) + recur(n, y - n * i, x - n * j)

n, r, c = map(int, input().split())
print(recur(2 ** n, r, c))