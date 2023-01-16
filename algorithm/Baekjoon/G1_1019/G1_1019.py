def reduce(num, digit):          # 일의 자리가 9가 될 때까지 줄이면서 각 자리 개수를 구해준다.
    if num % 10 == 9 or not num:            # 9를 만들고 0이면 종료
        return num
         
    for c in str(num):                      # 수를 만들면서 나오는 자리 개수를 더해준다.
        visited[int(c)] += digit
    num = reduce(num - 1, digit)
    return num

def page(num, digit):       # 현재 구할 수와 자릿 수
    num = reduce(num, digit)
    if not num:             # 0이면 종료
        return
    num //= 10
    cnt = num + 1
    for i in range(10):
        if i == 0:          # page가 0일 때는 제외
            visited[i] -= digit
        visited[i] += digit * cnt
    page(num, digit * 10)


n = int(input())
visited = [0 for _ in range(10)]
page(n, 1)
print(*visited)