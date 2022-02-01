T = int(input())

for _ in range(T):
    H, W, N = map(int,input().split())
    floor = ((N-1) % H) + 1 # 층이 낮은 것부터 채운다.
    ho = (N-1) // H + 1 # 호수가 작은 것부터 채운다.
    if ho // 10:
        print(f'{floor}{ho}')
    else:   # 호수가 10보다 작으면 0을 중간에 삽입한다.
        print(f'{floor}0{ho}')