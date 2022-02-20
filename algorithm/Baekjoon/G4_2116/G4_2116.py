N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_cnt = 3 * N     # 6(+1)이나 5, 6(+2)이 나올 때 cnt 세기
for t in range(1, 7):   # 맨 처음 주사위 바닥면 정하기
    cnt = 0
    for i in range(N):
        for j in range(6):
            if arr[i][j] == t:  # 전 주사위의 top과 현재 주사위의 bottom이 같을 때
                b = arr[i][j]
                if j == 0 or j == 5:    # 현재 주사위의 bottom으로 top 구하기
                    t = arr[i][5 - j]
                elif j == 1 or j == 3:
                    t = arr[i][4 - j]
                else:
                    t = arr[i][6 - j]
                if b == 6 or t == 6:    # 주사위의 top과 bottom 중 6이상이 있는지 확인
                    if b == 5 or t == 5:    # 5와 6 둘 다 있는지 확인
                        cnt += 1
                    cnt += 1
                break
    if min_cnt > cnt:   # 6이나 5,6이 젤 조금 나오는 값 선택
        min_cnt = cnt
    
print(6 * N - min_cnt)  # 6이나 5, 6이 안나왔을 경우에서 나오는 경우를 빼줘서 구한다.